import ui
import player
import uiCommon
import uiToolTip
import changelook
import localeInfo
import mouseModule
import app
import item

class Window(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = 0
		self.PositionOut = 0
		self.PositionStartX = 0
		self.PositionStartY = 0
		self.dialog = None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
		self.titleBar = None
		self.titleName = None
		self.accept = None
		self.cancel = None
		self.slot = None
		self.passItemSlot = None
		self.cost = None
		self.PositionOut = 0
		self.PositionStartX = 0
		self.PositionStartY = 0
		self.dialog = None

	def LoadWindow(self):
		if self.isLoaded:
			return
		
		self.isLoaded = 1
		
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/changelookwindow.py")
			
		except:
			import exception
			exception.Abort("ChangeLookWindow.LoadDialog.LoadScript")
		
		try:
			self.titleBar = self.GetChild("TitleBar")
			self.titleName = self.GetChild("TitleName")
			self.accept = self.GetChild("AcceptButton")
			self.cancel = self.GetChild("CancelButton")
			self.cost = self.GetChild("Cost")
			self.slot = self.GetChild("ChangeLookSlot")
			self.passItemSlot = self.GetChild("ChangeLookSlot_PassYangItem")
		except:
			import exception
			exception.Abort("ChangeLookWindow.LoadDialog.BindObject")
		
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.OnClose))
		self.titleBar.InfoButton('show')
		self.titleBar.SetInfoToolTip(self.CreateInfoToolTip())
		self.titleName.SetText(localeInfo.CHANGE_LOOK_TITLE)
		self.cancel.SetEvent(ui.__mem_func__(self.OnClose))
		self.accept.SetEvent(ui.__mem_func__(self.OnPressAccept))
		self.cost.SetText(localeInfo.CHANGE_LOOK_COST % (localeInfo.AddPointToNumberString(changelook.GetCost())))
		
		self.slot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		self.slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		self.slot.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		self.slot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.slot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		
		self.passItemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlotFreepass))
		self.passItemSlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlotFreepass))
		self.passItemSlot.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlotFreepass))
		self.passItemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItemFreeYang))
		self.passItemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		
		self.tooltipItem = None

	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip
		
	def CreateInfoToolTip(self):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetTitle(localeInfo.CHANGE_TOOLTIP_TITLE)
		toolTip.AppendSpace(5)
		toolTip.AutoAppendTextLine(localeInfo.CHANGE_TOOLTIP_LINE1)
		toolTip.AutoAppendTextLine(localeInfo.CHANGE_TOOLTIP_LINE2)
		toolTip.AutoAppendTextLine(localeInfo.CHANGE_TOOLTIP_LINE3)
		toolTip.AutoAppendTextLine(localeInfo.CHANGE_TOOLTIP_LINE4)
		toolTip.AutoAppendTextLine(localeInfo.CHANGE_TOOLTIP_LINE5)
		toolTip.AutoAppendTextLine(localeInfo.CHANGE_TOOLTIP_LINE6)
		toolTip.AlignHorizonalCenter()
		return toolTip

	def IsOpened(self):
		if self.IsShow() and self.isLoaded:
			return True
		
		return False

	def Open(self):
		self.PositionOut = 0
		(self.PositionStartX, self.PositionStartY, z) = player.GetMainCharacterPosition()
		self.cost.SetText(localeInfo.CHANGE_LOOK_COST % (localeInfo.AddPointToNumberString(changelook.GetCost())))
		for i in xrange(changelook.WINDOW_MAX_MATERIALS):
			self.slot.ClearSlot(i)
			
		self.passItemSlot.ClearSlot(0)
		
		self.SetTop()
		self.Show()

	def Close(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
		
		self.OnCancelAccept()
		self.Hide()

	def OnClose(self):
		changelook.SendCloseRequest()

	def OnPressEscapeKey(self):
		self.OnClose()
		return True

	def OnPressAccept(self):
		(isHere, iCell) = changelook.GetAttachedItem(1)
		if not isHere:
			return
		
		dialog = uiCommon.QuestionDialog()
		dialog.SetText(localeInfo.CHANGE_LOOK_CHANGE_ITEM)
		dialog.SetAcceptEvent(ui.__mem_func__(self.OnAccept))
		dialog.SetCancelEvent(ui.__mem_func__(self.OnCancelAccept))
		dialog.Open()
		self.dialog = dialog

	def OnAccept(self):
		changelook.SendRefineRequest()
		self.OnCancelAccept()

	def OnCancelAccept(self):
		if self.dialog:
			self.dialog.Close()
		
		self.dialog = None
		return True

	def OnUpdate(self):
		LIMIT_RANGE = changelook.LIMIT_RANGE
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.PositionStartX) >= LIMIT_RANGE or abs(y - self.PositionStartY) >= LIMIT_RANGE:
			if not self.PositionOut:
				self.PositionOut += 1
				self.OnClose()

	def SelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if not isAttached:
			return
		
		attachedSlotType = mouseModule.mouseController.GetAttachedType()
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
		mouseModule.mouseController.DeattachObject()
		if attachedSlotType == player.SLOT_TYPE_INVENTORY and attachedInvenType == player.INVENTORY:
			changelook.Add(attachedInvenType, attachedSlotPos, selectedSlotPos)

	def UseItemSlot(self, selectedSlotPos):
		mouseModule.mouseController.DeattachObject()
		changelook.Remove(selectedSlotPos)

	def OverInItem(self, selectedSlotPos):
		if self.tooltipItem:
			(isHere, iCell) = changelook.GetAttachedItem(selectedSlotPos)
			if isHere:
				self.tooltipItem.SetInventoryItem(iCell)

	def OverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def Refresh(self):
		for i in xrange(changelook.WINDOW_MAX_MATERIALS):
			self.slot.ClearSlot(i)
			(isHere, iCell) = changelook.GetAttachedItem(i)
			if isHere:
				self.slot.SetItemSlot(i, player.GetItemIndex(iCell), 1)
		self.passItemSlot.ClearSlot(0)
		(isHere, iCell) = changelook.GetAttachedPassItem()
		if isHere:
			self.passItemSlot.SetItemSlot(0, player.GetItemIndex(iCell), 1)	
			
		self.cost.SetText(localeInfo.CHANGE_LOOK_COST % (localeInfo.AddPointToNumberString(changelook.GetCost())))
				
	def SelectEmptySlotFreepass(self):
		isAttached = mouseModule.mouseController.isAttached()
		if not isAttached:
			return
		
		attachedSlotType = mouseModule.mouseController.GetAttachedType()
		attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
		attachedInvenType = player.SlotTypeToInvenType(attachedSlotType)
		mouseModule.mouseController.DeattachObject()
		if attachedSlotType == player.SLOT_TYPE_INVENTORY and attachedInvenType == player.INVENTORY:
			changelook.AddPassItem(attachedInvenType, attachedSlotPos)

	def UseItemSlotFreepass(self):
		mouseModule.mouseController.DeattachObject()
		changelook.RemovePassItem()

	def OverInItemFreeYang(self):
		if self.tooltipItem:
			(isHere, iCell) = changelook.GetAttachedPassItem()
			if isHere:
				self.tooltipItem.SetInventoryItem(iCell)

