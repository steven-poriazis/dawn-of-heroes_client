import uiCommon, snd, chat, app, net, player, item, wndMgr, mouseModule, localeInfo, constInfo, ui

class GemShopWindow(ui.ScriptWindow):
	GEM_SHOP_ADD_ITEM_VNUM = 39064
	GEM_SHOP_REFRESH_ITEM_VNUM = 39063
	GEM_SHOP_SLOT_MAX = 9
	GEM_SHOP_WINDOW_LIMIT_RANGE = 500

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		
		self.tooltipItem = 0
		self.xGemShopStart = 0
		self.yGemShopStart = 0
		self.questionDialog = None
		self.lastUpdate = 0
		
		self.priceDict = {}
		
		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def __LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/gemshopwindow.py")
		except:
			import exception
			exception.Abort("GemShopWindow.__LoadWindow.LoadObject")

		try:
			self.titleBar = self.GetChild("TitleBar")
			self.itemSlot = self.GetChild("SellItemSlot")
			self.refreshTime = self.GetChild("BuyRefreshTime")
			self.refreshButton = self.GetChild("RefreshButton")
			for i in xrange(9):
				self.priceDict["slot_%d_price" % i] = self.GetChild("slot_%s_price" % str(i+1))
		except:
			import exception
			exception.Abort("GemShopWindow.__LoadWindow.BindObject")
			
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.refreshButton.SetEvent(ui.__mem_func__(self.SendRequestRefresh))
		
		self.itemSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
			
	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.ClearDictionary()
		
		self.questionDialog = None
		
	def Open(self):
		self.RefreshItemSlot()
	
		self.SetTop()
		self.Show()

		(self.xGemShopStart, self.yGemShopStart, z) = player.GetMainCharacterPosition()
		
		self.lastUpdate = app.GetGlobalTime() +	player.GetGemShopRefreshTime()*1000
		
	def TransformTime(self, seconds):
		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)
		
		return "%02d:%02d" % (h, m)
	
	def OnUpdate(self):
		(x, y, z) = player.GetMainCharacterPosition()
		if abs(x - self.xGemShopStart) > self.GEM_SHOP_WINDOW_LIMIT_RANGE or abs(y - self.yGemShopStart) > self.GEM_SHOP_WINDOW_LIMIT_RANGE:
			self.Close()
			
		if player.GetGemShopRefreshTime() > 0:
			self.refreshTime.SetText(self.TransformTime(int(self.lastUpdate - app.GetGlobalTime())/1000))
		else:
			self.refreshTime.SetText("00:00")
			
	def SetItemToolTip(self, tooltip):
		self.tooltipItem = tooltip
			
	def OverInItem(self, slotIndex):
		if mouseModule.mouseController.isAttached():
			return

		if 0 != self.tooltipItem:
			self.tooltipItem.SetItemToolTip(player.GetGemShopItemVnum(slotIndex))

	def OverOutItem(self):
		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()
						
	def UseItemSlot(self, slotIndex):
		ADD_ITEM_NEED_COUNT = [0, 0, 0, 1, 2, 4, 8, 8, 8]

		if player.GetGemShopItemStatus(slotIndex) == 1:
			haveCount = constInfo.COUNT_SPECIFY_ITEM(self.GEM_SHOP_ADD_ITEM_VNUM)
			needCount = ADD_ITEM_NEED_COUNT[slotIndex]
			item.SelectItem(self.GEM_SHOP_ADD_ITEM_VNUM)
			if haveCount < needCount:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_SYSTEM_NOT_ENOUGHT_ADDITEM % (str(item.GetItemName()), int(needCount - haveCount)))
			else:
				self.SlotAddQuestion(slotIndex, needCount, item.GetItemName())
		else:
			if player.GetGem() < player.GetGemShopItemPrice(slotIndex):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_SYSTEM_NOT_ENOUGH_HP_GEM)
			else:
				self.GemShopSlotBuy(slotIndex)
			
	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def RefreshGemShop(self):
		self.lastUpdate = app.GetGlobalTime() +	player.GetGemShopRefreshTime()*1000
		
		self.RefreshItemSlot()
		
	def RefreshItemSlot(self):
		for i in xrange(self.GEM_SHOP_SLOT_MAX):
			itemCount = player.GetGemShopItemCount(i)
			itemStatus = player.GetGemShopItemStatus(i)
			itemPrice = player.GetGemShopItemPrice(i)
			if itemCount <= 1:
				itemCount = 0
			
			self.itemSlot.SetItemSlot(i, player.GetGemShopItemVnum(i), itemCount)
			
			self.priceDict["slot_%d_price" % i].SetText(str(itemPrice))
			
			if itemStatus == 1:
				self.itemSlot.DisableSlot(i)
			else:
				self.itemSlot.EnableSlot(i)

		wndMgr.RefreshSlot(self.itemSlot.GetWindowHandle())
		
	def GemShopSlotAdd(self, slotIndex, enable):
		if enable == 1:
			self.itemSlot.DisableSlot(slotIndex)
		else:
			self.itemSlot.EnableSlot(slotIndex)

	def SlotAddQuestion(self, slotIndex, needCount, needName):
		questionDialog = uiCommon.QuestionDialog2()
		questionDialog.SetText1((localeInfo.GEM_SYSTEM_ADD_SLOT_0 % str(needName)), True)
		questionDialog.SetText2((localeInfo.GEM_SYSTEM_ADD_SLOT_1 % int(needCount)), True)
		questionDialog.SetAcceptEvent(lambda arg = int(slotIndex): ui.__mem_func__(self.SlotAddQuestionAccept)(arg))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.SlotAddQuestionCancel))
		questionDialog.AutoResize()
		questionDialog.Open()
		self.questionDialog = questionDialog
		
	def SlotAddQuestionAccept(self, slotIndex):
		self.SlotAddQuestionCancel()
		net.SendGemShopAdd(slotIndex)
		
	def SlotAddQuestionCancel(self):
		if self.questionDialog:
			self.questionDialog.Close()

		self.questionDialog = None
		
	def RefreshGemQuestion(self):
		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.GEM_SYSTEM_REFRESH_SHOP_ITEMS)
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.RefreshGemAccept))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.SlotAddQuestionCancel))
		questionDialog.Open()
		self.questionDialog = questionDialog
		
	def RefreshGemAccept(self):
		self.SlotAddQuestionCancel()
		net.SendGemShopRefresh()

	def SendRequestRefresh(self):
		haveCount = constInfo.COUNT_SPECIFY_ITEM(self.GEM_SHOP_REFRESH_ITEM_VNUM)
		if haveCount < 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GEM_SYSTEM_NOT_ENOUGHT_REFRESHITEM)
		else:
			self.RefreshGemQuestion()
			
	def GemShopSlotBuy(self, slotIndex):
		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.GEM_SYSTEM_BUY_ITEM)
		questionDialog.SetAcceptEvent(lambda arg = int(slotIndex): ui.__mem_func__(self.SendBuyAccept)(arg))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.SlotAddQuestionCancel))
		questionDialog.Open()
		self.questionDialog = questionDialog
		
	def SendBuyAccept(self, slotIndex):
		self.SlotAddQuestionCancel()
		net.SendGemShopBuy(slotIndex)
