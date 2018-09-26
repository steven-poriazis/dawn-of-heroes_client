import ui
import net
import mouseModule
import player
import item
import uiToolTip
import chat
import exchange
import wndMgr
import app
import localeInfo

class DiceDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.tooltipItem = 0
		self.time_end = 0
		self.close = FALSE
		self.closenotimer = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/dicesystem.py")
		except:
			import exception
			exception.Abort("DiceDialog.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild
			self.Owner_Slot = GetObject("Owner_Slot")
			self.Owner_Slot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectOwnerEmptySlot))
			self.Owner_Slot.SetOverInItemEvent(ui.__mem_func__(self.OverInOwnerItem))
			self.Owner_Slot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.Owner_Number_Text = GetObject("Owner_Number_Text")
			self.Owner_Accept_Light = GetObject("Owner_Accept_Light")
			self.Owner_Accept_Light.Disable()
			
			self.Target_Slot = GetObject("Target_Slot")
			self.Target_Slot.SetOverInItemEvent(ui.__mem_func__(self.OverInTargetItem))
			self.Target_Slot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			self.Target_Number_Text = GetObject("Target_Number_Text")
			self.Target_Accept_Light = GetObject("Target_Accept_Light")
			self.Target_Accept_Light.Disable()
			
			self.Owner_Number_Text.SetFontName("Tahoma:22")
			self.Target_Number_Text.SetFontName("Tahoma:22")

			self.TitleName = self.GetChild("TitleName")
			
			self.AcceptButton = self.GetChild("Owner_Accept_Button")
			self.AcceptButton.SetToggleDownEvent(ui.__mem_func__(self.AcceptExchange))
			self.GetChild("TitleBar").SetCloseEvent(net.SendExchangeExitPacket)
		except:
			import exception
			exception.Abort("dice.LoadDialog.BindObject")

		self.Show()

	def Destroy(self):
		self.ClearDictionary()
		self.tooltipItem = 0
		self.close = FALSE
		self.closenotimer = 0
		self.Owner_Slot = 0
		self.Owner_Number_Text = 0
		self.Owner_Accept_Light = 0
		self.Target_Slot = 0
		self.Target_Number_Text = 0
		self.Target_Accept_Light = 0
		self.TitleName = 0
		self.AcceptButton = 0

	def OverInOwnerItem(self, slotIndex):

		if 0 != self.tooltipItem:
			self.tooltipItem.SetExchangeOwnerItem(slotIndex)

	def OverInTargetItem(self, slotIndex):

		if 0 != self.tooltipItem:
			self.tooltipItem.SetExchangeTargetItem(slotIndex)

	def OverOutItem(self):

		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def AcceptExchange(self):
		net.SendExchangeAcceptPacket()
		self.AcceptButton.Disable()

	def SelectOwnerEmptySlot(self, SlotIndex):

		if FALSE == mouseModule.mouseController.isAttached():
			return

		if mouseModule.mouseController.IsAttachedMoney():
			net.SendExchangeElkAddPacket(mouseModule.mouseController.GetAttachedMoneyAmount())
		else:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			if (player.SLOT_TYPE_INVENTORY == attachedSlotType
				or player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedSlotType):

				attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)

				SrcSlotNumber = mouseModule.mouseController.GetAttachedSlotNumber()
				DstSlotNumber = SlotIndex

				itemID = player.GetItemIndex(attachedInvenType, SrcSlotNumber)
				item.SelectItem(itemID)

				if item.IsAntiFlag(item.ANTIFLAG_GIVE):
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE)
					mouseModule.mouseController.DeattachObject()
					return

				net.SendExchangeItemAddPacket(attachedInvenType, SrcSlotNumber, DstSlotNumber)

		mouseModule.mouseController.DeattachObject()
	def RefreshOwnerSlot(self):
		for i in xrange(exchange.EXCHANGE_ITEM_MAX_NUM):
			itemIndex = exchange.GetItemVnumFromSelf(i)
			itemCount = exchange.GetItemCountFromSelf(i)
			if 1 == itemCount:
				itemCount = 0
			self.Owner_Slot.SetItemSlot(i, itemIndex, itemCount)
		self.Owner_Slot.RefreshSlot()

	def RefreshTargetSlot(self):
		for i in xrange(exchange.EXCHANGE_ITEM_MAX_NUM):
			itemIndex = exchange.GetItemVnumFromTarget(i)
			itemCount = exchange.GetItemCountFromTarget(i)
			if 1 == itemCount:
				itemCount = 0
			self.Target_Slot.SetItemSlot(i, itemIndex, itemCount)
		self.Target_Slot.RefreshSlot()

	def Refresh(self):

		self.RefreshOwnerSlot()
		self.RefreshTargetSlot()

		if TRUE == exchange.GetAcceptFromSelf():
			self.Owner_Accept_Light.Down()
		else:
			self.AcceptButton.Enable()
			self.AcceptButton.SetUp()
			self.Owner_Accept_Light.SetUp()

		if TRUE == exchange.GetAcceptFromTarget():
			self.Target_Accept_Light.Down()
		else:
			self.Target_Accept_Light.SetUp()

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def OpenDialog(self):
		self.AcceptButton.Enable()
		self.AcceptButton.SetUp()
		self.closenotimer = 0
		self.close = FALSE
		self.TitleName.SetText(localeInfo.DICE_TITLE % (exchange.GetNameFromTarget()))
		self.Show()
		
	def DiceAddNumber(self, myNumber, targetNumber):
		self.Owner_Number_Text.SetText(str(myNumber))
		self.Target_Number_Text.SetText(str(targetNumber))
		self.closenotimer = 1

	def CloseDialog(self):
		wndMgr.OnceIgnoreMouseLeftButtonUpEvent()

		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()
		
		if self.closenotimer == 1:
			self.time_end = app.GetGlobalTimeStamp()
			self.close = TRUE
		else:
			self.close = FALSE
			self.Close()

	def Close(self):
		self.Owner_Number_Text.SetText("-")
		self.Target_Number_Text.SetText("-")
		self.Hide()

	def OnUpdate(self):
		seconds = app.GetGlobalTimeStamp() - self.time_end 
		if self.close and seconds > 4:
			self.close = FALSE
			self.Close()
