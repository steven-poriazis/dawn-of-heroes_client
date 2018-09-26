import ui
import localeInfo
import player
import chat
import net
import wndMgr
import app
import ui

class AchievementBoard(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.listBaseWidth = 0
		self.listMaxCount = 0
		self.selectWndBaseHeight = 0
		self.selectBtnBaseY = 0
		self.baseHeight = 0

		self.LoadWindow()
		self.Refresh()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/AchievementBoard.py")
		except:
			import exception
			exception.Abort("AchievementBoard.LoadWindow.LoadScript")

		try:
			GetObject=self.GetChild
			self.board = GetObject("Board")
			self.currentLine = GetObject("current_achievement")
			self.selectWnd = GetObject("achievement_selection_wnd")
			self.listBox = GetObject("selectionbox")
			self.scrollBar = GetObject("selectionscroll")
			self.selectBtn = GetObject("select_button")
			# self.itemBtn = GetObject("item_button")
		except:
			import exception
			exception.Abort("AchievementBoard.LoadWindow.BindObject")

		self.board.SetCloseEvent(self.Close)
		self.scrollBar.SetScrollEvent(self.OnScroll)
		self.selectBtn.SAFE_SetEvent(self.OnClickSelectAchievementButton)
		# self.itemBtn.SAFE_SetEvent(self.OnClickItemAchievementButton)

		self.listBaseWidth = self.listBox.GetWidth()
		self.listMaxCount = self.listBox.GetHeight() / 17
		self.selectWndBaseHeight = self.selectWnd.GetHeight() - self.listMaxCount * 17
		self.selectBtnBaseY = self.selectBtn.GetTop() - self.listMaxCount * 17
		self.baseHeight = self.GetHeight() - self.selectWnd.GetHeight()

	def Destroy(self):
		self.Close()

	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def Resize(self, newHeight):
		self.SetSize(self.GetWidth(), newHeight)
		self.board.SetSize(self.GetWidth(), newHeight)

	def Refresh(self):
		self.RefreshList()
		self.RefreshActive()

	def Update(self, index):
		self.RefreshList()

	def RefreshActive(self):
		index = player.GetCurrentAchievement()
		if index == -1:
			self.currentLine.SetFontColor(0.8549, 0.8549, 0.8549)
			self.currentLine.SetText(localeInfo.ACHIEVEMENT_CURRENT_TITLE_NONE)
		else:
			colorIndex = player.GetAchievementColor(index)
			name, r, g, b = player.GetAchievementInfo(index, colorIndex)
			self.currentLine.SetFontColor(r, g, b)
			self.currentLine.SetText(name)

	def RefreshList(self):
		self.listBox.ClearItem()

		self.listBox.InsertItem(0, localeInfo.ACHIEVEMENT_NO_TITLE)
		for i in xrange(player.ACHIEVEMENT_MAX_NUM):
			if player.HasAchievement(i):
				colorIndex = player.GetAchievementColor(i)
				name, r, g, b = player.GetAchievementInfo(i, colorIndex)

				self.listBox.InsertItem(i + 1, name, self.SetTextLineData, r, g, b)

		self.listBox.SetSize(self.listBox.GetWidth(), 17 * min(self.listMaxCount, self.listBox.GetItemCount()))
		self.selectWnd.SetSize(self.selectWnd.GetWidth(), self.selectWndBaseHeight + self.listBox.GetHeight())

		if self.listBox.GetItemCount() == 1:
			self.selectWnd.Hide()
			self.Resize(self.baseHeight - 10)
		else:
			if self.listBox.GetItemCount() <= self.listMaxCount:
				self.listBox.SetSize(self.listBaseWidth + self.scrollBar.GetWidth(), self.listBox.GetHeight())
				self.scrollBar.Hide()
			else:
				self.listBox.SetSize(self.listBaseWidth, self.listBox.GetHeight())
				self.scrollBar.SetMiddleBarSize(self.listBox.GetViewItemCount() / float(self.listBox.GetItemCount()))
				self.scrollBar.SetPos(0.0)
				self.scrollBar.Show()

			self.listBox.LocateItem()
			self.selectBtn.SetPosition(self.selectBtn.GetLeft(), self.selectBtnBaseY + self.listBox.GetHeight())
			# self.itemBtn.SetPosition(self.itemBtn.GetLeft(), self.selectBtnBaseY + self.listBox.GetHeight())

			self.Resize(self.baseHeight + self.selectWnd.GetHeight())

			self.selectWnd.Show()

	def SetTextLineData(self, textLine, r, g, b):
		textLine.SetOutline()
		textLine.SetFontColor(r, g, b)

	def OnScroll(self):
		pos = self.scrollBar.GetPos()
		basePos = int((self.listBox.GetItemCount() - self.listBox.GetViewItemCount()) * pos + 0.5)
		if basePos != self.listBox.GetBasePos():
			self.listBox.SetBasePos(basePos)

	def OnClickSelectAchievementButton(self):
		index = self.listBox.GetSelectedItem(-1) - 1
		if index < -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "You have to choose you title first a")
			return
		elif index == player.GetCurrentAchievement():
			chat.AppendChat(chat.CHAT_TYPE_INFO, "This title is already seleted.")
			return

		net.SendChatPacket("/set_achievement " + str(index))

	def OnClickItemAchievementButton(self):
		index = self.listBox.GetSelectedItem(-1) - 1
		if index <= -1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "You have to select an title first.")
			return

		net.SendAchievementToItemPacket(index)

class AchievementRewardShower():
	def __init__(self):
		# window: without a window with size = 0 x 0 you won't be able to click there if it's shown
		bgWindow = ui.Window()
		bgWindow.Hide()
		self.bgWindow = bgWindow
		showingImage = ui.ImageBox()
		showingImage.SetParent(self.bgWindow)
		showingImage.LoadImage("locale/%s/ui/game/achievement/reward_shower.tga" % (app.GetLocaleName()))
		showingImage.SetPosition(wndMgr.GetScreenWidth() / 2 - showingImage.GetWidth() / 2, wndMgr.GetScreenHeight() / 8 - showingImage.GetHeight() / 2)
		showingImage.Show()
		self.image = showingImage
		showingImageName = ui.ImageBox()
		showingImageName.SetParent(self.bgWindow)
		showingImageName.SetPosition(showingImage.GetLeft(), showingImage.GetTop() + showingImage.GetHeight() + 3)
		showingImageName.Show()
		self.imageName = showingImageName

		self.indexLeft = []

	def Open(self, index):
		if self.bgWindow.IsShow():
			self.indexLeft.append(index)
			return

		self.imageName.LoadImage("locale/%s/ui/game/achievement/names/%d.tga" % (app.GetLocaleName(),index))
		self.bgWindow.SetFadeFinishEvent(self.__HideImage)
		self.bgWindow.FadeIn(0.2, 0, TRUE)

	def Hide(self):
		self.bgWindow.Hide()

	def __HideImage(self):
		self.bgWindow.SetFadeFinishEvent(self.__OpenNext)
		self.bgWindow.FadeOut(1.0, 6.0)

	def __OpenNext(self):
		if len(self.indexLeft) == 0:
			return
			
		self.Open(self.indexLeft[0])
		del self.indexLeft[0]