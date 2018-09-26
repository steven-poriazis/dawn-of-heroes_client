import ui, app, wndMgr, grp, game, net, chat, uiCommon, uiGuild, time

BIOLOG_BINARY_LOADED = {
	"vnum"  : {
		0 : 0,
	},
	"time"  : {
		0 : 0,
	},
	"countActual"  : {
		0 : "",
	},
	"countNeed"  : {
		0 : "",
	},
	"checkIndex"  : {
		0 : 0,
	},
	"typeWindow"  : {
		0 : 0,
	},
	"coordonates"  : {
		0 : wndMgr.GetScreenHeight() - 50 + 900,
	},
}

def pTableTranslate(i): 
	translate = {
					1	:	"[i] Esti sigur ca vrei sa accepti aceasta rasplata?",
					2	:	"[i] Nu ai selectat rasplata!",
					3	:	"[i] Analiza Biologica",
					4	:	"[i] Timpul a expirat, acum poti trimite inca un item spre analizare!"
				}
	if translate.has_key(i):
		return translate[i]

class WaitingDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/biolog_time_expired.py")

		except:
			import exception
			exception.Abort("WaitingDialog.LoadDialog.BindObject")

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime
		self.Show()	

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)
		
	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return

	def OnPressExitKey(self):
		self.Close()
		return TRUE

class CreateWindow:
	def _AppendSlot(self, parent, text, x, y, width, height):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, height)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		textline = ui.TextLine()
		textline.SetParent(SlotBar)
		textline.SetPosition(5, 1)
		textline.SetText(text)
		textline.Show()
		return SlotBar, textline

	def _AppendTextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline
	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

class Biolog_SelectReward(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.dialogQuestion = uiCommon.QuestionDialog()
		self.createWindow = CreateWindow()
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/biolog_selectrewards.py")
		getObject = self.GetChild
		self.board = getObject("Board")
		self.board.SetCloseEvent(self.CloseSelectReward)

		self.acceptButton = getObject("AcceptButton")
		self.TextLine_1 = getObject("TextLine_1")
		self.TextLine_2 = getObject("TextLine_2")
		self.TextLine_3 = getObject("TextLine_3")

		self.checkBoxTable	=	{
									0	:	[uiGuild.CheckBox(self, 288, 40, lambda arg = 0: self.SetType(arg)), 0, 0],
									1	:	[uiGuild.CheckBox(self, 288, 70, lambda arg = 1: self.SetType(arg)), 0, 0],
									2	:	[uiGuild.CheckBox(self, 288, 100, lambda arg = 2: self.SetType(arg)), 0, 0]
								}
		if self.acceptButton:
			self.acceptButton.SetEvent(ui.__mem_func__(self.GetDialogQuestion))	

		self.bonusValue = {}
		count = 0
		pos = 1 + 43
		while count < 3:
			self.bonusValue[count] = self.createWindow._AppendTextLine(self.board, '', 235, pos, self.createWindow.RGB(185, 218, 143))
			count = count + 1
			pos = pos + 30

		BIOLOG_BINARY_LOADED["checkIndex"][0] = 0

	def CloseSelectReward(self):
		if self.dialogQuestion:
			self.dialogQuestion.Close()
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.Hide()
	def SetType(self, arg):
		if arg == 0:
			BIOLOG_BINARY_LOADED["checkIndex"][0] = 1
			self.checkBoxTable[2][0].SetCheck(0)
			self.checkBoxTable[1][0].SetCheck(0)
			self.checkBoxTable[0][0].SetCheck(1)
		elif arg == 1:
			BIOLOG_BINARY_LOADED["checkIndex"][0] = 2
			self.checkBoxTable[0][0].SetCheck(0)
			self.checkBoxTable[2][0].SetCheck(0)
			self.checkBoxTable[1][0].SetCheck(1)
		elif arg == 2:
			BIOLOG_BINARY_LOADED["checkIndex"][0] = 3
			self.checkBoxTable[0][0].SetCheck(0)
			self.checkBoxTable[1][0].SetCheck(0)
			self.checkBoxTable[2][0].SetCheck(1)

	def SetText(self, text, arg):
		if arg == 1:
			self.TextLine_1.SetText(text)
		elif arg == 2:
			self.TextLine_2.SetText(text)
		elif arg == 3:
			self.TextLine_3.SetText(text)
			
	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def Open_SelectRewardType(self, argument):
		if (int(argument[0])) == 1:
			BIOLOG_BINARY_LOADED["typeWindow"][0] = 1
		if (int(argument[0])) == 2:	
			BIOLOG_BINARY_LOADED["typeWindow"][0] = 2

		self.bonusValue[0].SetText("+ " + (str(argument[3])))
		self.bonusValue[1].SetText("+ " + (str(argument[5])))
		self.bonusValue[2].SetText("+ " + (str(argument[7])))

		self.SetText(str(argument[2]).replace("$"," "), 1)
		self.SetText(str(argument[4]).replace("$"," "), 2)
		self.SetText(str(argument[6]).replace("$"," "), 3)

	def _AcceptReward(self):
		if BIOLOG_BINARY_LOADED["typeWindow"][0] == 1:
			net.SendChatPacket("/biolog 92_reward_%d" % BIOLOG_BINARY_LOADED["checkIndex"][0])
			self.CloseSelectReward()

		if BIOLOG_BINARY_LOADED["typeWindow"][0] == 2:
			net.SendChatPacket("/biolog 94_reward_%d" % BIOLOG_BINARY_LOADED["checkIndex"][0])
			self.CloseSelectReward()
	def GetDialogQuestion(self):
		if BIOLOG_BINARY_LOADED["checkIndex"][0] != 0:
			self.dialogQuestion.SetWidth(300)
			self.dialogQuestion.SetText((pTableTranslate(1)))
			self.dialogQuestion.SetAcceptEvent(ui.__mem_func__(self._AcceptReward))
			self.dialogQuestion.SetCancelEvent(ui.__mem_func__(self._DeclineReward))
			self.dialogQuestion.Open()	
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, (pTableTranslate(2)))

	def _DeclineReward(self):
		if self.dialogQuestion:
			self.dialogQuestion.Close()

class Biolog_TimeExpired(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.LoadInfoBoard()

	def __del__(self):
		ui.Window.__del__(self)

	def LoadInfoBoard(self):
		self.thinBoard = ui.ThinBoard()
		self.thinBoard.SetParent(self)
		self.thinBoard.SetSize(300, 50)
		self.thinBoard.SetPosition(wndMgr.GetScreenWidth() - (300 + 30), wndMgr.GetScreenHeight() - (50 + 50))

		self.typeBiolog = ui.TextLine()
		self.typeBiolog.SetParent(self.thinBoard)
		self.typeBiolog.SetPackedFontColor(grp.GenerateColor(1.0, 0.7843, 0.0, 1.0))
		self.typeBiolog.SetText((pTableTranslate(3)))
		self.typeBiolog.SetPosition(0, 8)
		self.typeBiolog.SetHorizontalAlignCenter()
		self.typeBiolog.SetWindowHorizontalAlignCenter()

		self.timeExpired = ui.TextLine()
		self.timeExpired.SetParent(self.thinBoard)
		self.timeExpired.SetText((pTableTranslate(4)))
		self.timeExpired.SetPosition(13, 25)
		self.timeClosed = WaitingDialog()
		self.timeClosed.Open(10.0)
		self.timeClosed.SAFE_SetTimeOverEvent(self.Close)

	def OpenWindow(self):
		b = [self.thinBoard,self.timeExpired,self.typeBiolog]
		for a in b:
			a.Show()

	def Close(self):
		self.thinBoard.Hide()

class Biolog_FinishSlider(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
	def __del__(self):
		ui.ScriptWindow.__del__(self)
	def __LoadWindow(self):
		self.next_move = app.GetGlobalTimeStamp()
		self.biologWindow_sliding = 0
		self.end = 0
		self.createWindow = CreateWindow()
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/biolog_slider.py")
		except:
			import exception
			exception.Abort("Biolog.LoadWindow.LoadObject")
		try:
			self.loader_ = {
					'default' : {
						0 : self.GetChild("Board"),
						1 : self.GetChild("Background"),
						2 : self.GetChild("iRewardItemText"),
						},
					'loaded' : {
						0 : self.GetChild("iRewardItem"),
						1 : self.GetChild("iRewardType")
						}
				}		
			x = [self.loader_['loaded'][0], self.loader_['default'][2]]	
			for i in x:
				i.Hide()
		except:
			import exception
			exception.Abort("Biolog.LoadWindow.BindObject")

		self.iBonusName = {}
		self.iSlotBonus = {}
		self.iValueBonus = {}

		btn = 0
		pos_y = 1 + 10
		while btn < 2:
			self.iBonusName[btn] = self.createWindow._AppendTextLine(self.loader_['default'][1], '', 10, pos_y, self.createWindow.RGB(185, 218, 143))
			self.iSlotBonus[btn] = self.createWindow._AppendSlot(self.loader_['default'][1], '', 305, pos_y, 66,16)
			self.iValueBonus[btn] = self.createWindow._AppendTextLine(self.loader_['default'][1], '', 307, pos_y, self.createWindow.RGB(255, 255, 255))
			btn = btn + 1
			pos_y = pos_y + 20
	def BINARY_BiologPopUp_Load(self, argument):
		b = [self.loader_['loaded'][0], self.loader_['default'][2]]	

		self.loader_['loaded'][1].SetText((str(argument[0]).replace("$"," ")))

		if (int(argument[1])) > 0:
			self.loader_['loaded'][0].SetItemSlot(0, (int(argument[1])), 0)
			for a in b:
				a.Show()

		if (int(argument[5])) < 1:
			self.iBonusName[1].Hide()
			self.iSlotBonus[1] = self.createWindow._AppendSlot(self, '', 0, 0, 0,0)
			self.iValueBonus[1].Hide()

		self.iBonusName[0].SetText((str(argument[2]).replace("$"," ")))
		self.iBonusName[1].SetText((str(argument[4]).replace("$"," ")))
		self.iValueBonus[0].SetText("+ " + (str(argument[3]) + " [%]"))
		self.iValueBonus[1].SetText("+ " + (str(argument[5]) + " [%]"))
		self.biologWindow_sliding = 1

	def OnUpdate(self):
		if self.end:
			return
		if self.biologWindow_sliding:
			if app.GetGlobalTimeStamp() >= self.next_move and BIOLOG_BINARY_LOADED["coordonates"][0] != wndMgr.GetScreenHeight() - 50 + 500:
				self.loader_['default'][0].SetPosition(wndMgr.GetScreenWidth()/2 + 158, BIOLOG_BINARY_LOADED["coordonates"][0] - 10)
				BIOLOG_BINARY_LOADED["coordonates"][0] = BIOLOG_BINARY_LOADED["coordonates"][0] - 5
				self.next_move = app.GetGlobalTimeStamp()
			if BIOLOG_BINARY_LOADED["coordonates"][0] == wndMgr.GetScreenHeight() - 50 + 500:
				self.biologWindow_sliding = 0
				self.next_move =app.GetGlobalTimeStamp() + 3
		else:
			if app.GetGlobalTimeStamp() >= self.next_move and BIOLOG_BINARY_LOADED["coordonates"][0] != wndMgr.GetScreenHeight() - 50 + 900:
				self.loader_['default'][0].SetPosition(wndMgr.GetScreenWidth()/2 + 158, BIOLOG_BINARY_LOADED["coordonates"][0] + 10)
				BIOLOG_BINARY_LOADED["coordonates"][0] = BIOLOG_BINARY_LOADED["coordonates"][0] + 5
				self.next_move = app.GetGlobalTimeStamp()
			if BIOLOG_BINARY_LOADED["coordonates"][0] == wndMgr.GetScreenHeight() - 50 + 900:
				self.end = 1
				self.CloseInfoBoard()

	def CloseInfoBoard(self):
		self.loader_['default'][0].Hide()
		self.loader_['default'][1].Hide()
