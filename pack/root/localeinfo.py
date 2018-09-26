import app
import constInfo

MAP_TRENT02 = "MAP_TRENT02" # ÀÓ½Ã
MAP_WL = "MAP_WL" # ÀÓ½Ã
MAP_NUSLUCK = "MAP_NUSLUCK" # ÀÓ½Ã 
MAP_TREE2 = "MAP_TREE2"

BLEND_POTION_NO_TIME = "BLEND_POTION_NO_TIME"
BLEND_POTION_NO_INFO = "BLEND_POTION_NO_INFO"

APP_TITLE = "METIN2"

GUILD_HEADQUARTER = "Main Building"
GUILD_FACILITY = "Facility"
GUILD_OBJECT = "Object"
GUILD_MEMBER_COUNT_INFINITY = "INFINITY"

LOGIN_FAILURE_WEB_BLOCK = "BLOCK_LOGIN(WEB)"
LOGIN_FAILURE_BLOCK_LOGIN = "BLOCK_LOGIN"
CHANNEL_NOTIFY_FULL = "CHANNEL_NOTIFY_FULL"

GUILD_BUILDING_LIST_TXT = app.GetLocalePath() + "/GuildBuildingList.txt"

GUILD_MARK_MIN_LEVEL = "3"
GUILD_MARK_NOT_ENOUGH_LEVEL = "±æµå·¹º§ 3ÀÌ»ó ºÎÅÍ °¡´ÉÇÕ´Ï´Ù."

ERROR_MARK_UPLOAD_NEED_RECONNECT = "UploadMark: Reconnect to game"
ERROR_MARK_CHECK_NEED_RECONNECT = "CheckMark: Reconnect to game"

VIRTUAL_KEY_ALPHABET_LOWERS  = r"[1234567890]/qwertyuiop\=asdfghjkl;`'zxcvbnm.,"
VIRTUAL_KEY_ALPHABET_UPPERS  = r'{1234567890}?QWERTYUIOP|+ASDFGHJKL:~"ZXCVBNM<>'
VIRTUAL_KEY_SYMBOLS    = '!@#$%^&*()_+|{}:"<>?~'
VIRTUAL_KEY_NUMBERS    = "1234567890-=\[];',./`"
VIRTUAL_KEY_SYMBOLS_BR    = '!@#$%^&*()_+|{}:"<>?~áàãâéèêíìóòôõúùç'

__IS_ENGLISH	= "ENGLISH" == app.GetLocaleServiceName()	
__IS_HONGKONG	= "HONGKONG" == app.GetLocaleServiceName()
__IS_NEWCIBN	= "locale/newcibn" == app.GetLocalePath()
__IS_EUROPE		= "EUROPE" == app.GetLocaleServiceName()		
__IS_CANADA		= "locale/ca" == app.GetLocalePath()
__IS_BRAZIL		= "locale/br" == app.GetLocalePath()
__IS_SINGAPORE	= "locale/sg" == app.GetLocalePath()
__IS_VIETNAM	= "locale/vn" == app.GetLocalePath()
__IS_ARABIC		= "locale/ae" == app.GetLocalePath()
__IS_CIBN10		= "locale/cibn10" == app.GetLocalePath()
__IS_WE_KOREA	= "locale/we_korea" == app.GetLocalePath()
__IS_TAIWAN		= "locale/taiwan" == app.GetLocalePath()
__IS_JAPAN		= "locale/japan" == app.GetLocalePath()	
LOGIN_FAILURE_WRONG_SOCIALID = "ASDF"
LOGIN_FAILURE_SHUTDOWN_TIME = "ASDF"

if __IS_CANADA:
	__IS_EUROPE = True

def IsYMIR():
	return "locale/ymir" == app.GetLocalePath()

def IsJAPAN():
	return "locale/japan" == app.GetLocalePath()

def IsENGLISH():
	global __IS_ENGLISH
	return __IS_ENGLISH

def IsHONGKONG():
	global __IS_HONGKONG
	return __IS_HONGKONG

def IsTAIWAN():
	return "locale/taiwan" == app.GetLocalePath()

def IsNEWCIBN():
	return "locale/newcibn" == app.GetLocalePath()

def IsCIBN10():
	global __IS_CIBN10
	return __IS_CIBN10
	
def IsEUROPE():
	global __IS_EUROPE
	return __IS_EUROPE

def IsCANADA():
	global __IS_CANADA
	return __IS_CANADA

def IsBRAZIL():
	global __IS_BRAZIL
	return __IS_BRAZIL

def IsVIETNAM():
	global __IS_VIETNAM
	return __IS_VIETNAM

def IsSINGAPORE():
	global __IS_SINGAPORE
	return __IS_SINGAPORE
	
def IsARABIC():
	global __IS_ARABIC
	return __IS_ARABIC

def IsWE_KOREA():
	return "locale/we_korea" == app.GetLocalePath()
	
# SUPPORT_NEW_KOREA_SERVER
def LoadLocaleData():
	if IsYMIR():
		import net
		SERVER = "Äèµµ ¼­¹ö"
		if SERVER == net.GetServerInfo()[:len(SERVER)]:
			app.SetCHEONMA(0)
			app.LoadLocaleData("locale/we_korea")
			constInfo.ADD_DEF_BONUS_ENABLE = 0
		else:
			app.SetCHEONMA(1)
			app.LoadLocaleData("locale/ymir")
			constInfo.ADD_DEF_BONUS_ENABLE = 1
	else:
		app.LoadLocaleData(app.GetLocalePath())

def IsCHEONMA():
	return IsYMIR()		# ÀÌÁ¦ YMIR ·ÎÄÉÀÏÀº ¹«Á¶°Ç Ãµ¸¶¼­¹öÀÓ. Ãµ¸¶¼­¹ö°¡ ¹®À» ´Ý±â Àü±îÁö º¯ÇÒ ÀÏ ¾øÀ½.

# END_OF_SUPPORT_NEW_KOREA_SERVER

def mapping(**kwargs): return kwargs

def SNA(text):	
	def f(x):
		return text
	return f

def SA(text):
	def f(x):
		return text % x
	return f
	
def FormatTime(time):
	m, s = divmod(time, 60)
	h, m = divmod(m, 60)
	return "%02d:%02d:%02d" % (h, m, s)

def LoadLocaleFile(srcFileName, localeDict):

	funcDict = {"SA":SA, "SNA":SNA}

	lineIndex = 1

	try:
		lines = pack_open(srcFileName, "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("LoadLocaleError(%(srcFileName)s)" % locals())
		app.Abort()

	for line in lines:
		try:		
			tokens = line[:-1].split("\t")
			if len(tokens) == 2:
				localeDict[tokens[0]] = tokens[1]
			elif len(tokens) >= 3:
				type = tokens[2].strip()
				if type:
					localeDict[tokens[0]] = funcDict[type](tokens[1])
				else:
					localeDict[tokens[0]] = tokens[1]
			else:
				raise RuntimeError, "Unknown TokenSize"

			lineIndex += 1
		except:
			import dbg
			dbg.LogBox("%s: line(%d): %s" % (srcFileName, lineIndex, line), "Error")
			raise


	
all = ["locale","error"]

if IsEUROPE()  and  IsBRAZIL()  :
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()
	constInfo.IN_GAME_SHOP_ENABLE = 0
elif IsSINGAPORE() :
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()
	constInfo.IN_GAME_SHOP_ENABLE = 0
elif IsNEWCIBN() :
	##°ÔÀÓ¸íÀÌ±úÁø´Ù.
	APP_TITLE = "ÐÂÒÐÌì2"
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()
	constInfo.IN_GAME_SHOP_ENABLE = 1
elif IsTAIWAN():
	APP_TITLE = "°«III°ê"
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()

	constInfo.IN_GAME_SHOP_ENABLE = 1
	
else:
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()

	constInfo.IN_GAME_SHOP_ENABLE = 1

LoadLocaleFile(LOCALE_FILE_NAME, locals())

########################################################################################################
## NOTE : ¾ÆÀÌÅÛÀ» ¹ö¸±¶§ "¹«¾ùÀ»/¸¦ ¹ö¸®½Ã°Ú½À´Ï±î?" ¹®ÀÚ¿­ÀÇ Á¶»ç ¼±ÅÃÀ» À§ÇÑ ÄÚµå
dictSingleWord = {
	"m":1, "n":1, "r":1, "M":1, "N":1, "R":1, "l":1, "L":1, "1":1, "3":1, "6":1, "7":1, "8":1, "0":1,
}

dictDoubleWord = {
	"°¡":1, "°¼":1, "°Å":1, "°Ü":1, "°í":1, "±³":1, "±¸":1, "±Ô":1, "±×":1, "±â":1, "°³":1, "°Â":1, "°Ô":1, "°è":1, "°ú":1, "±¥":1, "±Å":1, "±Ë":1, "±«":1, "±Í":1, "±á":1,
	"±î":1, "²¥":1, "²¨":1, "²¸":1, "²¿":1, "²Ø":1, "²Ù":1, "²ó":1, "²ô":1, "³¢":1, "±ú":1, "ƒÆ":1, "²²":1, "²¾":1, "²Ê":1, "²Ï":1, "²ã":1, "²ç":1, "²Ò":1, "²î":1, "…Ê":1,
	"³ª":1, "³Ä":1, "³Ê":1, "³à":1, "³ë":1, "´¢":1, "´©":1, "´º":1, "´À":1, "´Ï":1, "³»":1, "†v":1, "³×":1, "³é":1, "³ö":1, "‡R":1, "´²":1, "´´":1, "³ú":1, "´µ":1, "´Ì":1,
	"´Ù":1, "´ô":1, "´õ":1, "µ®":1, "µµ":1, "µÍ":1, "µÎ":1, "µà":1, "µå":1, "µð":1, "´ë":1, "ˆÛ":1, "µ¥":1, "µ³":1, "µÂ":1, "µÅ":1, "µÖ":1, "µØ":1, "µÇ":1, "µÚ":1, "µï":1,
	"µû":1, "‹x":1, "¶°":1, "¶Å":1, "¶Ç":1, "ŒÃ":1, "¶Ñ":1, "":1, "¶ß":1, "¶ì":1, "¶§":1, "‹š":1, "¶¼":1, "‹ó":1, "¶Ì":1, "¶Î":1, "Œô":1, "¶Ø":1, "¶Ï":1, "¶Ù":1, "¶ç":1,
	"¶ó":1, "·ª":1, "·¯":1, "·Á":1, "·Î":1, "·á":1, "·ç":1, "·ù":1, "¸£":1, "¸®":1, "·¡":1, "Žm":1, "·¹":1, "·Ê":1, "·Ö":1, "O":1, "·ï":1, "·ñ":1, "·Ú":1, "·ò":1, "l":1,
	"¸¶":1, "¸Ï":1, "¸Ó":1, "¸ç":1, "¸ð":1, "¹¦":1, "¹«":1, "¹Â":1, "¹Ç":1, "¹Ì":1, "¸Å":1, "Ù":1, "¸Þ":1, "¸ï":1, "¸ú":1, "‘À":1, "¹¹":1, "¹¾":1, "¸þ":1, "¹¿":1, "’Þ":1,
	"¹Ù":1, "¹ò":1, "¹ö":1, "º­":1, "º¸":1, "ºÌ":1, "ºÎ":1, "ºä":1, "ºê":1, "ºñ":1, "¹è":1, "“Ž":1, "º£":1, "º¶":1, "ºÁ":1, "ºÄ":1, "ºÛ":1, "ºÞ":1, "ºÆ":1, "ºß":1, "•‘":1,
	"ºü":1, "»²":1, "»µ":1, "»À":1, "»Ç":1, "»Ï":1, "»Ñ":1, "»Ø":1, "»Ú":1, "»ß":1, "»©":1, "•û":1, "»¾":1, "–§":1, "–Ø":1, "–ô":1, "—¨":1, "—Ä":1, "»Î":1, "—à":1, "˜u":1,
	"»ç":1, "»þ":1, "¼­":1, "¼Å":1, "¼Ò":1, "¼î":1, "¼ö":1, "½´":1, "½º":1, "½Ã":1, "»õ":1, "¼¨":1, "¼¼":1, "¼Î":1, "¼Ý":1, "¼â":1, "½¤":1, "½¦":1, "¼è":1, "½¬":1, "šÃ":1,
	"½Î":1, "›X":1, "½á":1, "›Ç":1, "½î":1, "¾¤":1, "¾¥":1, "o":1, "¾²":1, "¾¾":1, "½Ø":1, "›y":1, "½ê":1, "›ã":1, "½÷":1, "½û":1, "¾¬":1, "¾®":1, "½ý":1, "¾¯":1, "¾º":1,
	"¾Æ":1, "¾ß":1, "¾î":1, "¿©":1, "¿À":1, "¿ä":1, "¿ì":1, "À¯":1, "À¸":1, "ÀÌ":1, "¾Ö":1, "¾ê":1, "¿¡":1, "¿¹":1, "¿Í":1, "¿Ö":1, "¿ö":1, "¿þ":1, "¿Ü":1, "À§":1, "ÀÇ":1,
	"ÀÚ":1, "Àð":1, "Àú":1, "Á®":1, "Á¶":1, "ÁÒ":1, "ÁÖ":1, "Áê":1, "Áî":1, "Áö":1, "Àç":1, "À÷":1, "Á¦":1, "Áµ":1, "ÁÂ":1, "ÁÈ":1, "Áà":1, "Áâ":1, "ÁË":1, "Áã":1, "£p":1,
	"Â¥":1, "Â¹":1, "Â¼":1, "ÂÇ":1, "ÂÉ":1, "§c":1, "ÂÞ":1, "Âé":1, "Âê":1, "Âî":1, "Â°":1, "¤Š":1, "ÂÅ":1, "¥™":1, "ÂÒ":1, "ÂÖ":1, "Âå":1, "¨R":1, "ÂØ":1, "Âè":1, "©n":1,
	"Â÷":1, "Ã­":1, "Ã³":1, "ÃÄ":1, "ÃÊ":1, "ÃÝ":1, "Ãß":1, "Ãò":1, "Ã÷":1, "Ä¡":1, "Ã¤":1, "ª‰":1, "Ã¼":1, "ÃÇ":1, "ÃÒ":1, "¬‚":1, "Ãç":1, "Ãé":1, "ÃÖ":1, "Ãë":1, "¯M":1,
	"Ä«":1, "Ä¼":1, "Ä¿":1, "ÄÑ":1, "ÄÚ":1, "Äì":1, "Äí":1, "Å¥":1, "Å©":1, "Å°":1, "Ä³":1, "°m":1, "ÄÉ":1, "ÄÙ":1, "Äâ":1, "Äè":1, "Äõ":1, "Äù":1, "Äê":1, "Äû":1, "´”":1,
	"Å¸":1, "ÅË":1, "ÅÍ":1, "Åß":1, "Åä":1, "Åô":1, "Åõ":1, "Æ©":1, "Æ®":1, "Æ¼":1, "ÅÂ":1, "¶O":1, "Å×":1, "Åâ":1, "Åí":1, "Åï":1, "Åý":1, "Æ¡":1, "Åð":1, "Æ¢":1, "Æ·":1,
	"ÆÄ":1, "ÆÙ":1, "ÆÛ":1, "Æì":1, "Æ÷":1, "Ç¥":1, "Çª":1, "Ç»":1, "ÇÁ":1, "ÇÇ":1, "ÆÐ":1, "»—":1, "Æä":1, "Æó":1, "Ç¡":1, "½":1, "Ç´":1, "¿R":1, "Ç£":1, "Ç¶":1, "Àc":1,
	"ÇÏ":1, "Çá":1, "Çã":1, "Çô":1, "È£":1, "È¿":1, "ÈÄ":1, "ÈÞ":1, "Èå":1, "È÷":1, "ÇØ":1, "Á…":1, "Çì":1, "Çý":1, "È­":1, "È³":1, "ÈÌ":1, "ÈÑ":1, "È¸":1, "ÈÖ":1, "Èñ":1,
}

locale = mapping(
)


def GetAuxiliaryWordType(text):

	textLength = len(text)

	if textLength > 1:

		singleWord = text[-1]

		if (singleWord >= '0' and singleWord <= '9') or\
			(singleWord >= 'a' and singleWord <= 'z') or\
			(singleWord >= 'A' and singleWord <= 'Z'):
			if not dictSingleWord.has_key(singleWord):
				return 1

		elif dictDoubleWord.has_key(text[-2:]):
			return 1

	return 0



def CutMoneyString(sourceText, startIndex, endIndex, insertingText, backText):

	sourceLength = len(sourceText)

	if sourceLength < startIndex:
		return backText

	text = sourceText[max(0, sourceLength-endIndex):sourceLength-startIndex]

	if not text:
		return backText

	if long(text) <= 0:
		return backText

	text = str(int(text))

	if backText:
		backText = " " + backText

	return text + insertingText + backText

def SecondToDHM(time):
	if time < 60:
		if IsARABIC():
			return "%.2f %s" % (time, SECOND)
		else:
			return "0" + MINUTE
		
	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24
	day = int(int((time / 60) / 60) / 24)

	text = ""

	if day > 0:
		text += str(day) + DAY
		text += " "

	if hour > 0:
		text += str(hour) + HOUR
		text += " "

	if minute > 0:
		text += str(minute) + MINUTE

	return text

def SecondToHM(time):

	if time < 60:
		if IsARABIC():
			return "%.2f %s" % (time, SECOND)
		else:
			return "0" + MINUTE

	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60)

	text = ""

	if hour > 0:
		text += str(hour) + HOUR
		if hour > 0:
			text += " "

	if minute > 0:
		text += str(minute) + MINUTE

	return text
if app.ENABLE_MAINTENANCE_SYSTEM:
	def SecondToDHMS(time, ignoreSecTime = -1, useShortName = TRUE):
		text = ""
		if time < 0:
			time *= -1
			text = "-"

		second = int(time % 60)
		minute = int((time / 60) % 60)
		hour = int(((time / 60) / 60) % 24)
		day = int(((time / 60) / 60) / 24)

		if ignoreSecTime > 0 and time >= ignoreSecTime:
			second = 0

		if day > 0:
			if day == 1:
				text += str(day) + " Zi "
			else:
				text += str(day) + " Zile "

		if hour > 0:
			text += str(hour) + " "
			if useShortName == TRUE:
				text += "H. "
			else:
				if hour == 1:
					text += "Ora "
				else:
					text += "Ore "

		if minute > 0:
			text += str(minute) + " "
			if useShortName == TRUE:
				text += "Min. "
			else:
				if minute == 1:
					text += "Minut "
				else:
					text += "Minute "

		if second > 0 or (day == 0 and hour == 0 and minute == 0):
			text += str(second) + " "
			if useShortName == TRUE:
				text += "Sec. "
			else:
				if second == 1:
					text += "Secunda "
				else:
					text += "Secunde "

		return text[:-1]

def GetAlignmentTitleName(alignment):
	if alignment >= 12000:
		return TITLE_NAME_LIST[0]
	elif alignment >= 8000:
		return TITLE_NAME_LIST[1]
	elif alignment >= 4000:
		return TITLE_NAME_LIST[2]
	elif alignment >= 1000:
		return TITLE_NAME_LIST[3]
	elif alignment >= 0:
		return TITLE_NAME_LIST[4]
	elif alignment > -4000:
		return TITLE_NAME_LIST[5]
	elif alignment > -8000:
		return TITLE_NAME_LIST[6]
	elif alignment > -12000:
		return TITLE_NAME_LIST[7]

	return TITLE_NAME_LIST[8]


OPTION_PVPMODE_MESSAGE_DICT = {
	0 : PVP_MODE_NORMAL,
	1 : PVP_MODE_REVENGE,
	2 : PVP_MODE_KILL,
	3 : PVP_MODE_PROTECT,
	4 : PVP_MODE_GUILD,
}

error = mapping(
	CREATE_WINDOW = GAME_INIT_ERROR_MAIN_WINDOW,
	CREATE_CURSOR = GAME_INIT_ERROR_CURSOR,
	CREATE_NETWORK = GAME_INIT_ERROR_NETWORK,
	CREATE_ITEM_PROTO = GAME_INIT_ERROR_ITEM_PROTO,
	CREATE_MOB_PROTO = GAME_INIT_ERROR_MOB_PROTO,
	CREATE_NO_DIRECTX = GAME_INIT_ERROR_DIRECTX,
	CREATE_DEVICE = GAME_INIT_ERROR_GRAPHICS_NOT_EXIST,
	CREATE_NO_APPROPRIATE_DEVICE = GAME_INIT_ERROR_GRAPHICS_BAD_PERFORMANCE,
	CREATE_FORMAT = GAME_INIT_ERROR_GRAPHICS_NOT_SUPPORT_32BIT,
	NO_ERROR = ""
)


GUILDWAR_NORMAL_DESCLIST = [GUILD_WAR_USE_NORMAL_MAP, GUILD_WAR_LIMIT_30MIN, GUILD_WAR_WIN_CHECK_SCORE]
GUILDWAR_WARP_DESCLIST = [GUILD_WAR_USE_BATTLE_MAP, GUILD_WAR_WIN_WIPE_OUT_GUILD, GUILD_WAR_REWARD_POTION]
GUILDWAR_CTF_DESCLIST = [GUILD_WAR_USE_BATTLE_MAP, GUILD_WAR_WIN_TAKE_AWAY_FLAG1, GUILD_WAR_WIN_TAKE_AWAY_FLAG2, GUILD_WAR_REWARD_POTION]

MINIMAP_ZONE_NAME_DICT = {
	"metin2_map_a1"  : MAP_A1,
	"map_a2"         : MAP_A2,
	"metin2_map_a3"  : MAP_A3,
	"metin2_map_b1"  : MAP_B1,
	"map_b2"         : MAP_B2,
	"metin2_map_b3"  : MAP_B3,
	"metin2_map_c1"  : MAP_C1,
	"map_c2"         : MAP_C2,
	"metin2_map_c3"  : MAP_C3,
	"map_n_snowm_01" : MAP_SNOW,
	"metin2_map_n_flame_01" : MAP_FLAME,
	"metin2_map_n_desert_01" : MAP_DESERT,
	"metin2_map_milgyo" : MAP_TEMPLE,
	"metin2_map_spiderdungeon" : MAP_SPIDER,
	"metin2_map_deviltower1" : MAP_SKELTOWER,
	"metin2_map_guild_01" : MAP_AG,
	"metin2_map_guild_02" : MAP_BG,
	"metin2_map_guild_03" : MAP_CG,
	"metin2_map_trent" : MAP_TREE,
	"metin2_map_trent02" : MAP_TREE2,
	"season1/metin2_map_WL_01" : MAP_WL,
	"season1/metin2_map_nusluck01" : MAP_NUSLUCK,
    "Metin2_map_CapeDragonHead" : MAP_CAPE,
    "metin2_map_Mt_Thunder" : MAP_THUNDER,
    "metin2_map_dawnmistwood" : MAP_DAWN,
    "metin2_map_BayBlackSand" : MAP_BAY,
}



JOBINFO_TITLE = [
	[JOB_WARRIOR0, JOB_WARRIOR1, JOB_WARRIOR2,],
	[JOB_ASSASSIN0, JOB_ASSASSIN1, JOB_ASSASSIN2,],
	[JOB_SURA0, JOB_SURA1, JOB_SURA2,],
	[JOB_SHAMAN0, JOB_SHAMAN1, JOB_SHAMAN2,],
]

JOBINFO_DATA_LIST = [
	[
		["Å¸°í³­ ¿ë¸Í°ú ±ÁÈ÷Áö ¾Ê´Â ¹«»çÀÇ",
		"±â°³¸¦ »ç¶÷µéÀº ÀÏÄÃ¾î [¿ëÀÚ]¶ó°í",
		"ºÎ¸¥´Ù. ¾î¶°ÇÑ À§±â¿¡¼­µµ ±×µéÀº ",
		"µÚ·Î ¹°·¯¼­Áö ¾ÊÀ¸¸ç, ´ÙÄ¡°í ¿òÁ÷",
		"ÀÌ±â Èûµç µ¿·á¸¦ À§ÇØ ´Ü½ÅÀ¸·Î",
		"Àûµé°ú ¸¶ÁÖ ½Î¿ì±âµµ ÇÑ´Ù. ÀÌµéÀº",
		"Àß ´Ü·ÃµÈ ±ÙÀ°°ú Èû, °­·ÂÇÑ °ø°Ý·Â",
		"À¸·Î ÀüÀå ÃÖ¼±µÎ¿¡¼­ °ø°ÝÁøÀ¸·Î",
		"È°¾àÇÑ´Ù.                      ",],
		["°¡Àå ÀÏ¹ÝÀûÀÎ °ø°ÝÇü ¹«»ç·Î, ",
		"ÀûÁ¢Àü¿¡ µû¸¥ Á÷Á¢ °ø°ÝÀ¸·Î ÀüÀå",
		"¿¡¼­ È°¾àÇÑ´Ù. ±ºÁ÷ Æ¯¼º»ó ±Ù·ÂÀ»",
		"¸ÞÀÎÀ¸·Î ½ºÅÝ Æ÷ÀÎÆ®¸¦ ÅõÀÚÇÏµÇ, ",
		"ÀûÁ¢Àü¿¡ µû¸¥ »ý¸í·Â / ¹æ¾î·Â",
		"È®º¸¸¦ À§ÇØ Ã¼·ÂÀ» ¿Ã¸°´Ù. ¶ÇÇÑ",
		"°ø°ÝÀÇ Á¤È®¼ºÀ» ³ôÀÌ±â À§ÇØ ¹ÎÃ¸",
		"¿¡µµ Æ÷ÀÎÆ®¸¦ ÅõÀÚÇÒ ÇÊ¿ä°¡ ÀÖ´Ù.",],
		["»ó´ç ¼öÁØÀÇ Á¤½Å·ÂÀ» ÀÌ¿ëÇÏ´Â",
		"Áß/±Ù°Å¸® Á¢ÀüÇü ¹«»ç·Î, °¢ ±â¼ú",
		"ÇÏ³ªÇÏ³ªÀÇ ³ôÀº °ø°Ý·ÂÀ¸·Î ÀüÀå¿¡¼­",
		"È°¾àÇÑ´Ù. ±ºÁ÷ Æ¯¼º»ó ±Ù·ÂÀ» ¸ÞÀÎ",
		"À¸·Î ½ºÅÈ Æ÷ÀÎÆ®¸¦ ÅõÀÚÇÏµÇ, ",
		"Áß/±Ù°Å¸® °ø°ÝÀÇ Á¤È®¼º°ú ¸íÁß·üÀ»",
		"À§ÇØ ¹ÎÃ¸À» ¿Ã¸°´Ù. ¶ÇÇÑ Á¢Àü ½Ã ",
		"Àû °ø°Ý¿¡ µû¸¥ »ý¸í·Â / ¹æ¾î·Â",
		"È®º¸¸¦ À§ÇØ Ã¼·Â¿¡µµ Æ÷ÀÎÆ®¸¦",
		"ÅõÀÚÇÒ ÇÊ¿ä°¡ ÀÖ´Ù.        ",],		
	],
	[
		["ÀÚ°´Àº ¾î¶°ÇÑ »óÈ²¿¡¼­µµ ÀÚ½ÅÀÇ",
		"¸öÀ» ¼û±â°í Àº¹ÐÇÑ ¾îµÒÀÇ ÀÓ¹«¸¦",
		"¼öÇàÇÏ¸é¼­ ÀüÀåÀÇ ÈÄÀ§¸¦ Áö¿øÇÏ´Â", 
		"ÀÚµéÀÌ´Ù. ÀÌµéÀº ¾ÆÁÖ ºü¸£°í ½Å¼Ó",
		"ÇÏ¸ç, ºñÇÒ µ¥ ¾øÀÌ °ú°¨ÇÏ°í ÀýÁ¦µÈ",
		"Çàµ¿À¸·Î ÀûÀÇ ±Þ¼Ò¿¡ Ä¡¸íÅ¸¸¦ ³¯¸®",
		"µÇ, ÀüÀå¿¡¼± ÀûÁøÀ» ÇâÇØ ¹«¼öÇÑ",
		"È­»ìÀ» ³»»ÕÀ¸¸ç ÀÚ½ÅÀÇ ¿ë¸ÍÀ»",
		"¼±º¸ÀÎ´Ù.                   "],
		["µÎ¼Õ ´Ü°ËÀ» ÁÖ¹«±â·Î ´Ù·ç¸ç, ½Å¼Ó",
		"ÇÏ°Ô Ä¡°í ºüÁö´Â ÀÚ°´ Æ¯À¯ÀÇ ¿òÁ÷ÀÓ",
		"À¸·Î ÀüÀå¿¡¼­ È°¾àÇÑ´Ù. ±ºÁ÷ Æ¯¼º»ó",
		"¹ÎÃ¸À» ¸ÞÀÎÀ¸·Î ½ºÅÝ Æ÷ÀÎÆ®¸¦ ÅõÀÚ",
		"ÇÏµÇ, ±Ù·ÂÀ» ¿Ã·Á °ø°Ý·ÂÀ» ³ôÀÎ´Ù.",
		"¶ÇÇÑ ±ÙÁ¢Àü¿¡ µû¸¥ »ý¸í·Â/¹æ¾î·Â ",
		"»ó½ÂÀ» À§ÇØ Ã¼·Â¿¡µµ Æ÷ÀÎÆ®¸¦",
		"ÅõÀÚÇÒ ÇÊ¿ä°¡ ÀÖ´Ù.          ",],
		["È°À» ÁÖ¹«±â·Î ´Ù·ç¸ç, ±ä ½Ã¾ß¿Í",
		"»çÁ¤°Å¸®¿¡ µû¸¥ ¿ø°Å¸® °ø°ÝÀ¸·Î",
		"ÀüÀå¿¡¼­ È°¾àÇÑ´Ù. ±ºÁ÷ Æ¯¼º»ó",
		"°ø°Ý ¼º°ø·üÀÇ Áõ°¡¸¦ À§ÇØ ¹ÎÃ¸À»",
		"¸ÞÀÎÀ¸·Î ¿Ã·Á¾ß ÇÏ¸ç, ¿ø°Å¸®",
		"°ø°ÝÀÇ µ¥¹ÌÁö Áõ°¡¸¦ À§ÇØ ±Ù·ÂÀ»",
		"¿Ã¸± ÇÊ¿ä°¡ ÀÖ´Ù. ¶ÇÇÑ Àûµé¿¡°Ô",
		"Æ÷À§µÇ¾úÀ» ½Ã, Àû °ø°Ý¿¡ ¹öÆ¼±â",
		"À§ÇÑ »ý¸í·Â/¹æ¾î·Â »ó½ÂÀ» À§ÇØ",
		"Ã¼·Â¿¡µµ Æ÷ÀÎÆ®¸¦ ÅõÀÚÇÒ ÇÊ¿ä°¡",
		"ÀÖ´Ù.                        ", ],
	],
	[
		["¼ö¶ó´Â [µ¶Àº µ¶À¸·Î]ÀÇ ¼Ó¼ºÀ¸·Î",
		"Ã¢¼³µÈ Æ¯¼ö ¼Ó¼ºÀÇ ±ºÁ÷ÀÌ´Ù. ",
		"±×µéÀº ÀüÀå¿¡¼­ ÀûµéÀÇ »ç±â¸¦ ÀúÇÏ",
		"½ÃÅ°°í, ¾Ç¸¶ÀÇ ÈûÀ» ½ÇÀº ¸¶ÅºÀ¸·Î",
		"ÀûÀÇ ¿µÈ¥°ú À°½ÅÀ» Áþ¹¶°µ´Ù. ¶§·Î",
		"ÀÌµéÀº ÀÚ½ÅÀÇ °Ë°ú °©¿Ê¿¡ ¾îµÒÀÇ",
		"ÈûÀ» ½Ç¾î, ÀüÀå¿¡¼­ ¹«»ç ¸øÁö ¾ÊÀº",
		"°ø°Ý·ÂÀ» ¹ßÈÖÇÏ±âµµ ÇÏ´Âµ¥, ÀûµéÀ»",
		"Á×¿©´ë´Â±× ¸ð½ÀÀÌ ¿ö³«¿¡ ²ûÂïÇØ",
		"»ç¶÷µéÀº ¼ö¶ó¸¦ ÀÏÄÃ¾î [¸¶½Å]ÀÌ¶ó",
		"ºÎ¸£±â¸¦ ÁÖÀú ¾É´Â´Ù."],
		["È¯¹«±ºÀÇ ¼ö¶ó´Â ¾Ç¸¶ÀÇ ¾¾¿¡¼­",
		"¾ò¾îÁö´Â ¸¶·ÂÀ» ¹«±â³ª ¹æ¾î±¸¿¡",
		"½Ç¾î ¹«»ç ¸øÁö ¾ÊÀº ÀüÅõ·ÂÀ¸·Î",
		"ÀüÀå¿¡¼­ È°¾àÇÑ´Ù. ±ºÁ÷ Æ¯¼º»ó",
		"Áö´ÉÀÌ ³ô¾ÆÁú¼ö·Ï Âø¿ë Àåºñ¿¡", 
		"½Ç¸®´Â ¸¶·ÂÀÇ À§·ÂÀÌ Áõ´ëµÇ¹Ç·Î,",
		"Áö´É°ú ±Ù·ÂÀ» ¸ÞÀÎÀ¸·Î ½ºÅÈ",
		"Æ÷ÀÎÆ®¸¦ ÅõÀÚÇÏµÇ, Á¢Àü¿¡ µû¸¥",
		"»ý¸í·Â/¹æ¾î·Â È®º¸¸¦ À§ÇØ Ã¼·ÂÀ»",
		"¿Ã¸°´Ù. ¶ÇÇÑ °ø°ÝÀÇ Á¤È®¼º°ú",
		"È¸ÇÇ¸¦ À§ÇØ¼­ ¹ÎÃ¸¿¡µµ Æ÷ÀÎÆ®¸¦",
		"ÅõÀÚÇÒ ÇÊ¿ä°¡ ÀÖ´Ù.           ",],
		["Èæ¸¶±ºÀÇ ¼ö¶óµéÀº °¢Á¾ ¾îµÒÀÇ",
		"ÁÖ¹®°ú ¾Ç¸¶ÀÇ ¸¶¹ýÀ¸·Î ÀüÀå¿¡¼­",
		"È°¾àÇÑ´Ù. ±ºÁ÷ Æ¯¼º»ó ¸¶¹ý °ø°ÝÀÌ",
		"ÁÖÀÌ¹Ç·Î Áö´ÉÀ» ¸ÞÀÎÀ¸·Î ½ºÅÝ",
		"Æ÷ÀÎÆ®¸¦ ÅõÀÚÇÏµÇ, ¿ø°Å¸® ¸¶¹ý",
		"°ø°ÝÀÇ Á¤È®¼ºÀ» À§ÇØ ¹ÎÃ¸À» ¿Ã¸°´Ù.",
		"¶ÇÇÑ Æ÷À§ µÇ¾úÀ»½Ã, Àû °ø°Ý¿¡ µû¸¥",
		"»ý¸í·Â / ¹æ¾î·Â È®º¸¸¦ À§ÇØ Ã¼·Â¿¡µµ",
		"Æ÷ÀÎÆ®¸¦ ÅõÀÚÇÒ ÇÊ¿ä°¡ ÀÖ´Ù.    ",],
	],
	[
		["¹«´çÀº ¿ë½Å°ú ÀÚ¿¬, µÎ °í´ëÀÇ",
		"ÈûÀ» ´Ù·ê ¼ö ÀÖ´Â À¯ÀÏÇÑ Á÷Á¾ÀÌ´Ù.",
		"±×µéÀº ÈÄ¹æ¿¡¼­ ¾Æ±ºÀ» º¸Á¶ÇÏ°í",
		"´ÙÄ£ µ¿·áÀÇ ºÎ»óÀ» È¸º¹ ½ÃÅ°¸ç",
		"¶³¾îÁø »ç±â¸¦ »ó½Â½ÃÅ²´Ù. ±×µéÀº",
		"¾Æ±ºÀÇ ¼ö¸é°ú ÈÞ½ÄÀ» ¹æÇØÇÏ´Â ÀÚ¸¦ ",
		"Àý´ë ¿ë¼­ÇÏÁö ¾ÊÀ¸¸ç, ±×·± ÀÚµé",
		"¿¡°Ô´Â ÇÑ Á¡ ÁÖÀú ¾øÀÌ ÁÖ¹®À»",
		"ÅÍÆ®·Á ±× ºñ°ÌÇÔÀ» ¾öÈ÷ Â¡°èÇÑ´Ù.",],
		["Ãµ·æ±ºÀÇ ¹«´çµéÀº °¢Á¾ ºÎÀû¼ú°ú",
		"º¸Á¶ÁÖ¹®¿¡ ´ÉÇÏ¸ç, ÀûÀÇ Á÷ / °£Á¢",
		"°ø°ÝÀ¸·ÎºÎÅÍ ¾Æ±ºÀ» ÁöÅ²´Ù. ±ºÁ÷",
		"Æ¯¼º»ó ¸¶¹ý ´É·ÂÀÌ ÁÖÀÌ¹Ç·Î Áö´ÉÀ»",
		"¸ÞÀÎÀ¸·Î ½ºÅÝ Æ÷ÀÎÆ®¸¦ ÅõÀÚÇÏµÇ,",
		"Æ÷À§µÇ¾úÀ» ½Ã, Àû °ø°Ý¿¡ µû¸¥",
		"»ý¸í·Â / ¹æ¾î·Â È®º¸¸¦ À§ÇØ Ã¼·ÂÀ»",
		"¿Ã¸°´Ù. ¶ÇÇÑ ¿ø°Å¸® ¸¶¹ý °ø°ÝÀÇ",
		"Á¤È®¼ºÀ» À§¿¡ ¹ÎÃ¸¿¡µµ Æ÷ÀÎÆ®¸¦",
		"ÅõÀÚÇÒ ÇÊ¿ä°¡ ÀÖ´Ù.           ",],
		["±¤·Ú±ºÀÇ ¹«´çµéÀº ÀÚ¿¬ÀÇ ÈûÀ»",
		"ºô·Á ¾Æ±ºÀ» È¸º¹ÇÏ°í, ³ú½ÅÀÇ ",
		"ÈûÀ¸·Î ¹ÐÁýÇÑ Àûµé¿¡°Ô Å« Ãæ°ÝÀ»",
		"ÀÔÈú ¼ö ÀÖ´Â ÀÌµéÀÌ´Ù. ±ºÁ÷ÀÇ",
		"Æ¯¼º»ó ¸¶¹ý ´É·ÂÀÌ ÁÖÀÌ¹Ç·Î Áö´ÉÀ»",
		"¸ÞÀÎÀ¸·Î ½ºÅÝ Æ÷ÀÎÆ®¸¦ ÅõÀÚÇÏµÇ,",
		"Æ÷À§µÇ¾úÀ»½Ã, Àû °ø°Ý¿¡ µû¸¥",
		"»ý¸í·Â / ¹æ¾î·Â È®º¸¸¦ À§ÇØ Ã¼·ÂÀ»",
		"¿Ã¸°´Ù. ¶ÇÇÑ ¿ø°Å¸® ¸¶¹ý °ø°ÝÀÇ",
		"Á¤È®¼ºÀ» À§¿¡ ¹ÎÃ¸¿¡µµ Æ÷ÀÎÆ®¸¦",
		"ÅõÀÚÇÒ ÇÊ¿ä°¡ ÀÖ´Ù.             "],
	],
]


WHISPER_ERROR = {
	1 : CANNOT_WHISPER_NOT_LOGON,
	2 : CANNOT_WHISPER_DEST_REFUSE,
	3 : CANNOT_WHISPER_SELF_REFUSE,
}

NOTIFY_MESSAGE = {
	"CANNOT_EQUIP_SHOP" : CANNOT_EQUIP_IN_SHOP,
	"CANNOT_EQUIP_EXCHANGE" : CANNOT_EQUIP_IN_EXCHANGE,
}


ATTACK_ERROR_TAIL_DICT = {
	"IN_SAFE" : CANNOT_ATTACK_SELF_IN_SAFE,
	"DEST_IN_SAFE" : CANNOT_ATTACK_DEST_IN_SAFE,
}

SHOT_ERROR_TAIL_DICT = {
	"EMPTY_ARROW" : CANNOT_SHOOT_EMPTY_ARROW,
	"IN_SAFE" : CANNOT_SHOOT_SELF_IN_SAFE,
	"DEST_IN_SAFE" : CANNOT_SHOOT_DEST_IN_SAFE,
}
	
USE_SKILL_ERROR_TAIL_DICT = {	
	"IN_SAFE" : CANNOT_SKILL_SELF_IN_SAFE,
	"NEED_TARGET" : CANNOT_SKILL_NEED_TARGET,
	"NEED_EMPTY_BOTTLE" : CANNOT_SKILL_NEED_EMPTY_BOTTLE,
	"NEED_POISON_BOTTLE" : CANNOT_SKILL_NEED_POISON_BOTTLE,
	"REMOVE_FISHING_ROD" : CANNOT_SKILL_REMOVE_FISHING_ROD,
	"NOT_YET_LEARN" : CANNOT_SKILL_NOT_YET_LEARN,
	"NOT_MATCHABLE_WEAPON" : CANNOT_SKILL_NOT_MATCHABLE_WEAPON,
	"WAIT_COOLTIME" : CANNOT_SKILL_WAIT_COOLTIME,
	"NOT_ENOUGH_HP" : CANNOT_SKILL_NOT_ENOUGH_HP,
	"NOT_ENOUGH_SP" : CANNOT_SKILL_NOT_ENOUGH_SP,
	"CANNOT_USE_SELF" : CANNOT_SKILL_USE_SELF,
	"ONLY_FOR_ALLIANCE" : CANNOT_SKILL_ONLY_FOR_ALLIANCE,
	"CANNOT_ATTACK_ENEMY_IN_SAFE_AREA" : CANNOT_SKILL_DEST_IN_SAFE,
	"CANNOT_APPROACH" : CANNOT_SKILL_APPROACH,
	"CANNOT_ATTACK" : CANNOT_SKILL_ATTACK,
	"ONLY_FOR_CORPSE" : CANNOT_SKILL_ONLY_FOR_CORPSE,
	"EQUIP_FISHING_ROD" : CANNOT_SKILL_EQUIP_FISHING_ROD, 
	"NOT_HORSE_SKILL" : CANNOT_SKILL_NOT_HORSE_SKILL,
	"HAVE_TO_RIDE" : CANNOT_SKILL_HAVE_TO_RIDE,
}

LEVEL_LIST=["", HORSE_LEVEL1, HORSE_LEVEL2, HORSE_LEVEL3]

HEALTH_LIST=[
	HORSE_HEALTH0,
	HORSE_HEALTH1, 
	HORSE_HEALTH2,
	HORSE_HEALTH3,
]


USE_SKILL_ERROR_CHAT_DICT = {	
	"NEED_EMPTY_BOTTLE" : SKILL_NEED_EMPTY_BOTTLE,
	"NEED_POISON_BOTTLE" : SKILL_NEED_POISON_BOTTLE, 
	"ONLY_FOR_GUILD_WAR" : SKILL_ONLY_FOR_GUILD_WAR,
}

SHOP_ERROR_DICT = {
	"NOT_ENOUGH_MONEY" : SHOP_NOT_ENOUGH_MONEY,
	"SOLDOUT" : SHOP_SOLDOUT,
	"INVENTORY_FULL" : SHOP_INVENTORY_FULL,
	"INVALID_POS" : SHOP_INVALID_POS,
	"NOT_ENOUGH_MONEY_EX" : SHOP_NOT_ENOUGH_MONEY_EX,
}

STAT_MINUS_DESCRIPTION = {
	"HTH-" : STAT_MINUS_CON,
	"INT-" : STAT_MINUS_INT,
	"STR-" : STAT_MINUS_STR,
	"DEX-" : STAT_MINUS_DEX,
}

MODE_NAME_LIST = ( PVP_OPTION_NORMAL, PVP_OPTION_REVENGE, PVP_OPTION_KILL, PVP_OPTION_PROTECT, )
TITLE_NAME_LIST = ( PVP_LEVEL0, PVP_LEVEL1, PVP_LEVEL2, PVP_LEVEL3, PVP_LEVEL4, PVP_LEVEL5, PVP_LEVEL6, PVP_LEVEL7, PVP_LEVEL8, )

if app.ENABLE_ACHIEVEMENT:
	ACHIEVEMENT_NAME_LIST = [ACHIEVEMENT_TITLE_ANIMAL_ABUSER, ACHIEVEMENT_TITLE_THUG_LIFE, ACHIEVEMENT_TITLE_STABLE, ACHIEVEMENT_TITLE_UNSTOPPABLE,\
	ACHIEVEMENT_TITLE_DIRTY, ACHIEVEMENT_TITLE_TREE, ACHIEVEMENT_TITLE_ON_FIRE, ACHIEVEMENT_TITLE_BEAR_GRYLLS, ACHIEVEMENT_TITLE_PERSISTENT,\
	ACHIEVEMENT_TITLE_INDESTRUCTIBLE, ACHIEVEMENT_TITLE_GODLIKE, ACHIEVEMENT_TITLE_PENTAKILL, ACHIEVEMENT_TITLE_DEMON_HUNTER, ACHIEVEMENT_TITLE_EW,\
	ACHIEVEMENT_TITLE_NINJA_TURTLE, ACHIEVEMENT_TITLE_IGNEEL, ACHIEVEMENT_TITLE_ASCENSION, ACHIEVEMENT_TITLE_CURSED, ACHIEVEMENT_TITLE_COLUMBUS,\
	ACHIEVEMENT_TITLE_PIGLET, ACHIEVEMENT_TITLE_TEAMPLAYER, ACHIEVEMENT_TITLE_SOLOPLAYER, ACHIEVEMENT_TITLE_DEAD_CERTAIN, ACHIEVEMENT_TITLE_DIRECT_SUPPORT,\
	ACHIEVEMENT_TITLE_NEXT_TO_DISGUISE, ACHIEVEMENT_TITLE_RIVAL, ACHIEVEMENT_TITLE_DEMORALIZATION, ACHIEVEMENT_TITLE_SHOT_DOWN, ACHIEVEMENT_TITLE_BOUNTY_HUNTER,\
	ACHIEVEMENT_TITLE_RAIN_OF_FIRE, ACHIEVEMENT_TITLE_STATE_ENEMY, ACHIEVEMENT_TITLE_SILENT_HIT, ACHIEVEMENT_TITLE_ICEMAN, ACHIEVEMENT_TITLE_DEATH_ANGEL,\
	ACHIEVEMENT_TITLE_GOD_HAND, ACHIEVEMENT_TITLE_PHANTOM, ACHIEVEMENT_TITLE_BELLIGERENCE, ACHIEVEMENT_TITLE_HARD_GOAL, ACHIEVEMENT_TITLE_FRIEND_AND_SUPPORTER,\
	ACHIEVEMENT_TITLE_HARDCORE, ACHIEVEMENT_TITLE_FINAL_TOUCHES, ACHIEVEMENT_TITLE_LONG_LIFE, ACHIEVEMENT_TITLE_INTERGALACTIC, ACHIEVEMENT_TITLE_HARD_TO_KILL,\
	ACHIEVEMENT_TITLE_BULLY, ACHIEVEMENT_TITLE_STAB_IN_THE_BACK, ACHIEVEMENT_TITLE_BLOOD_BROTHERS, ACHIEVEMENT_TITLE_GHOSTRIDER, ACHIEVEMENT_TITLE_FATE_TURNER,\
	ACHIEVEMENT_TITLE_SEAMAN, ACHIEVEMENT_TITLE_REVIVE, ACHIEVEMENT_TITLE_FAILURE, ACHIEVEMENT_TITLE_CAPTAIN, ACHIEVEMENT_TITLE_AMOROUS,\
	ACHIEVEMENT_TITLE_DIVORCED, ACHIEVEMENT_TITLE_REVOLUTIONARY, ACHIEVEMENT_TITLE_ORC, ACHIEVEMENT_TITLE_ICE_LION, ACHIEVEMENT_TITLE_PANTYWAIST,\
	ACHIEVEMENT_TITLE_FARM_HORNY, ACHIEVEMENT_TITLE_SPIDERMAN, ACHIEVEMENT_TITLE_QUICK_CHANGE_ARTIST, ACHIEVEMENT_TITLE_TIGER, ACHIEVEMENT_TITLE_PRINCESS,\
	ACHIEVEMENT_TITLE_HASCHTAG, ACHIEVEMENT_TITLE_FRIENDS_FOR_LIFE, ACHIEVEMENT_TITLE_BAKA, ACHIEVEMENT_IS_SUPPOSED_TO_BE, ACHIEVEMENT_FOREVER_ALONE,
	ACHIEVEMENT_FLAMER, ACHIEVEMENT_AKKELOS, ACHIEVEMENT_FURRY, ACHIEVEMENT_AZZLACK, ACHIEVEMENT_IS_KING, ACHIEVEMENT_SHADOWHUNTER, ACHIEVEMENT_PROANGLER,\
	ACHIEVEMENT_DEVIL_SORCERER, ACHIEVEMENT_GUILDMASTER, ACHIEVEMENT_BANDIT, ACHIEVEMENT_ROCKY, ACHIEVEMENT_CHARWOMAN, ACHIEVEMENT_QUIZKING,\
	ACHIEVEMENT_POKEMON_MASTER, ACHIEVEMENT_ARENA_LEADER, ACHIEVEMENT_OVER_9000, ACHIEVEMENT_FAMOUS, ACHIEVEMENT_MODERN, ACHIEVEMENT_WUKONG,\
	ACHIEVEMENT_IM_LEGEND, ACHIEVEMENT_BANKER, ACHIEVEMENT_HEAVYWEIGHT, ACHIEVEMENT_ILLUMINAT, ACHIEVEMENT_KURIRIN, ACHIEVEMENT_DRAGONHUNTER,\
	ACHIEVEMENT_DRAGONCOLLECTOR, ACHIEVEMENT_PVP_CHAMP, ACHIEVEMENT_PVM_LEGEND, ACHIEVEMENT_KAISER, ACHIEVEMENT_STATEMAN, ACHIEVEMENT_NOBLE,\
	ACHIEVEMENT_CHEATER, ACHIEVEMENT_FISHKING, ACHIEVEMENT_REPORTED, ACHIEVEMENT_METINKILLER, ACHIEVEMENT_SERVICE_YEARS, ACHIEVEMENT_BOOKWORM,\
	ACHIEVEMENT_EGG_SEARCH, ACHIEVEMENT_TRADER, ACHIEVEMENT_WEAPON_NUT, ACHIEVEMENT_CALL_ME_DAMAGE, ACHIEVEMENT_DEAPSEA_COLLECTOR, ACHIEVEMENT_MYSTIC,\
	ACHIEVEMENT_PERFECTIONIST, ACHIEVEMENT_STRONGER_THAN_DEATH, ACHIEVEMENT_SORCERER, ACHIEVEMENT_FARMMASTER, ACHIEVEMENT_DEATH_CONQUEROR, ACHIEVEMENT_ACCOMPLICE,\
	ACHIEVEMENT_THUNDERGOD, ACHIEVEMENT_PETERMAN, ACHIEVEMENT_WIMP, ACHIEVEMENT_DANCINGSTAR, ACHIEVEMENT_POISON_DWARF, ACHIEVEMENT_LUCKY_CHILD,\
	ACHIEVEMENT_BATH_WITH_TIREZ, ACHIEVEMENT_ROMANTIC, ACHIEVEMENT_POTT_SELLER, ACHIEVEMENT_SECRETLY_LOVE, ACHIEVEMENT_PET_TAMER, ACHIEVEMENT_PANDA,\
	ACHIEVEMENT_RESEARCHER, ACHIEVEMENT_ICE_HOLY, ACHIEVEMENT_FIRE_HOLY, ACHIEVEMENT_EARTH_HOLY, ACHIEVEMENT_AIR_HOLY, ACHIEVEMENT_LAST_AIRBENDER,\
	ACHIEVEMENT_WOODCUTTER, ACHIEVEMENT_ANARCHIST, ACHIEVEMENT_FLOWER_CHILD, ACHIEVEMENT_BUDDHA, ACHIEVEMENT_RED_RIDING_HOOD, ACHIEVEMENT_UNFORGIVING,\
	ACHIEVEMENT_STRATEGIST, ACHIEVEMENT_HISTORIAN, ACHIEVEMENT_DOMPTEUR, ACHIEVEMENT_HOTHEAD, ACHIEVEMENT_WICKED, ACHIEVEMENT_CHILBLAIN, ACHIEVEMENT_FASHION_EXPERT,\
	ACHIEVEMENT_PEARL_COLLECTOR, ACHIEVEMENT_WEREWOLF, ACHIEVEMENT_SHAPESHIFTER, ACHIEVEMENT_GOLD_DIGGER, ACHIEVEMENT_SOULBINDER, ACHIEVEMENT_TRAITOR,\
	ACHIEVEMENT_SHREDDER, ACHIEVEMENT_APPRENTICE, ACHIEVEMENT_GHOSTBUSTER, ACHIEVEMENT_TOXIC, ACHIEVEMENT_EGOIST, ACHIEVEMENT_STONE_COLLECTOR, ACHIEVEMENT_CHALLENGER,\
	ACHIEVEMENT_KING, ACHIEVEMENT_PVP_KING, ACHIEVEMENT_CRAZY_GUY, ACHIEVEMENT_PVP_KING2,ACHIEVEMENT_PVP_KING3,ACHIEVEMENT_PVP_KING4,ACHIEVEMENT_PVP_KING5,ACHIEVEMENT_PVP_KING6]

def GetLetterImageName():
	return "season1/icon/scroll_close.tga"
def GetLetterOpenImageName():
	return "season1/icon/scroll_open.tga"
def GetLetterCloseImageName():
	return "season1/icon/scroll_close.tga"
	
def AddPointToNumberString(n) :
	if n <= 0 :
		return "0"
	return "%s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]))

if 949 == app.GetDefaultCodePage():
	def EUL(name):
		if GetAuxiliaryWordType(name):
			return "¸¦ "
		else:
			return "À» "

	def I(name):
		if GetAuxiliaryWordType(name):
			return "°¡ "
		else:
			return "ÀÌ "

	def DO_YOU_SELL_ITEM(sellItemName, sellItemCount, sellItemPrice):
		name = sellItemName
		if sellItemCount > 1:
			name += " "
			name += str(sellItemCount)
			name += "°³"

		return name + EUL(name) + str(sellItemPrice) + "³É¿¡ ÆÄ½Ã°Ú½À´Ï±î?"

	def DO_YOU_BUY_ITEM(sellItemName, sellItemCount, sellItemPrice):
		name = sellItemName
		if sellItemCount > 1:
			name += " "
			name += str(sellItemCount)
			name += "°³"

		return name + EUL(name) + str(sellItemPrice) + "¿¡ »ç½Ã°Ú½À´Ï±î?"

	def REFINE_FAILURE_CAN_NOT_ATTACH(attachedItemName):
		return attachedItemName+EUL(attachedItemName)+"ºÎÂøÇÒ ¼ö ¾ø´Â ¾ÆÀÌÅÛÀÔ´Ï´Ù"

	def REFINE_FAILURE_NO_SOCKET(attachedItemName):
		return attachedItemName+EUL(attachedItemName)+"ºÎÂøÇÒ ¼ö ÀÖ´Â ¼ÒÄÏÀÌ ¾ø½À´Ï´Ù"	

	def REFINE_FAILURE_NO_GOLD_SOCKET(attachedItemName):
		return attachedItemName+EUL(attachedItemName)+"ºÎÂøÇÒ ¼ö ÀÖ´Â È²±Ý ¼ÒÄÏÀÌ ¾ø½À´Ï´Ù"	

	def HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, dropItemCount):
		name = dropItemName
		if dropItemCount > 1:
			name += " "
			name += str(dropItemCount)
			name += "°³"

		return name+EUL(name)+"¹ö¸®½Ã°Ú½À´Ï±î?"

	def NumberToMoneyString(number):
		if number <= 0:
			return "0³É"

		number = str(number)
		result = CutMoneyString(number, 0, 4, "", "")
		result = CutMoneyString(number, 4, 8, "¸¸", result)
		result = CutMoneyString(number, 8, 12, "¾ï", result)
		result = result + "³É"

		return result

	def NumberToSecondaryCoinString(number):
		if number <= 0:
			return "0Àü"

		number = str(number)
		result = CutMoneyString(number, 0, 4, "", "")
		result = CutMoneyString(number, 4, 8, "¸¸", result)
		result = CutMoneyString(number, 8, 12, "¾ï", result)
		result = result + "Àü"

		return result

	def FISHING_NOTIFY(isFish, fishName):
		if isFish:
			return fishName + I(fishName) + "¹® µí ÇÕ´Ï´Ù."
		else:
			return fishName + I(fishName) + "°É¸°µí ÇÕ´Ï´Ù."

	def FISHING_SUCCESS(isFish, fishName):
		if isFish:
			return fishName + EUL(fishName) + "Àâ¾Ò½À´Ï´Ù!"
		else:
			return fishName + EUL(fishName) + "¾ò¾ú½À´Ï´Ù!"

elif 932 == app.GetDefaultCodePage():
	def DO_YOU_SELL_ITEM(sellItemName, sellItemCount, sellItemPrice):
		if sellItemCount > 1 :
			return "%s %s ŒÂ‚ð %s‚É”„‚è‚Ü‚·‚©H" % ( sellItemName, sellItemCount, NumberToMoneyString(sellItemPrice) )
		else:
			return "%s ‚ð %s‚Å”„‚è‚Ü‚·‚©H" % (sellItemName, NumberToMoneyString(sellItemPrice) )

	def DO_YOU_BUY_ITEM(buyItemName, buyItemCount, buyItemPrice) :
		if buyItemCount > 1 :
			return "%s %sŒÂ‚ð %s‚Å”ƒ‚¢‚Ü‚·‚©H" % ( buyItemName, buyItemCount, buyItemPrice )
		else:
			return "%s‚ð %s‚Å”ƒ‚¢‚Ü‚·‚©H" % ( buyItemName, buyItemPrice )
			
	def REFINE_FAILURE_CAN_NOT_ATTACH(attachedItemName) :
		return "%s‚ð‘•’…‚Å‚«‚È‚¢ƒAƒCƒe?‚Å‚·B" % (attachedItemName)

	def REFINE_FAILURE_NO_SOCKET(attachedItemName) :
		return "%s‚ð‘•’…‚·‚é?ƒPƒbƒg‚ª‚ ‚è‚Ü‚¹‚ñB" % (attachedItemName)

	def REFINE_FAILURE_NO_GOLD_SOCKET(attachedItemName) :
		return "%s‚ð‘•’…‚Å‚«‚é‰©‹à?ƒPƒbƒg‚ª‚ ‚è‚Ü‚¹‚ñB" % (attachedItemName)
		
	def HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, dropItemCount) :
		if dropItemCount > 1 :
			return "%s %d ŒÂ‚ðŽÌ‚Ä‚Ü‚·‚©H" % (dropItemName, dropItemCount)
		else :	
			return "%s‚ðŽÌ‚Ä‚Ü‚·‚©H" % (dropItemName)

	def FISHING_NOTIFY(isFish, fishName) :
		if isFish :
			return "%s ‚ªH‚¢‚Â‚¢‚½‚æ‚¤‚Å‚·" % ( fishName )
		else :
			return "%s ‚ª‚©‚©‚Á‚½‚æ‚¤‚Å‚·" % ( fishName )

	def FISHING_SUCCESS(isFish, fishName) :
		if isFish :
			return "%s ‚ð•ß‚Ü‚¦‚Ü‚µ‚½I" % (fishName)
		else :
			return "%s ‚ðŽè‚É“ü‚ê‚Ü‚µ‚½I" % (fishName)
			
	def NumberToMoneyString(number) :
		if number <= 0 :
			return "0—¼"

		number = str(number)
		result = CutMoneyString(number, 0, 4, "", "")
		result = CutMoneyString(number, 4, 8, "–œ", result)
		result = CutMoneyString(number, 8, 12, "‰­", result)
		result = result + "—¼"

		return result
	def NumberToSecondaryCoinString(number) :
		if number <= 0 :
			return "0jun"

		number = str(number)
		result = CutMoneyString(number, 0, 4, "", "")
		result = CutMoneyString(number, 4, 8, "–œ", result)
		result = CutMoneyString(number, 8, 12, "‰­", result)
		result = result + "jun"

		return result
elif IsHONGKONG():
	def DO_YOU_SELL_ITEM(sellItemName, sellItemCount, sellItemPrice):
		if sellItemCount > 1 :
			return DO_YOU_SELL_ITEM2 % (sellItemName, sellItemCount, NumberToMoneyString(sellItemPrice) )
		else:
			return DO_YOU_SELL_ITEM1 % (sellItemName, NumberToMoneyString(sellItemPrice) )

	def DO_YOU_BUY_ITEM(buyItemName, buyItemCount, buyItemPrice) :
		if buyItemCount > 1 :
			return DO_YOU_BUY_ITEM2 % ( buyItemName, buyItemCount, buyItemPrice )
		else:
			return DO_YOU_BUY_ITEM1 % ( buyItemName, buyItemPrice )
			
	def REFINE_FAILURE_CAN_NOT_ATTACH(attachedItemName) :
		return REFINE_FAILURE_CAN_NOT_ATTACH0 % (attachedItemName)

	def REFINE_FAILURE_NO_SOCKET(attachedItemName) :
		return REFINE_FAILURE_NO_SOCKET0 % (attachedItemName)

	def REFINE_FAILURE_NO_GOLD_SOCKET(attachedItemName) :
		return REFINE_FAILURE_NO_GOLD_SOCKET0 % (attachedItemName)
		
	def HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, dropItemCount) :
		if dropItemCount > 1 :
			return HOW_MANY_ITEM_DO_YOU_DROP2 % (dropItemName, dropItemCount)
		else :	
			return HOW_MANY_ITEM_DO_YOU_DROP1 % (dropItemName)

	def FISHING_NOTIFY(isFish, fishName) :
		if isFish :
			return FISHING_NOTIFY1 % ( fishName )
		else :
			return FISHING_NOTIFY2 % ( fishName )

	def FISHING_SUCCESS(isFish, fishName) :
		if isFish :
			return FISHING_SUCCESS1 % (fishName)
		else :
			return FISHING_SUCCESS2 % (fishName)
			
	def NumberToMoneyString(number) :
		if number <= 0 :
			return "0 %s" % (MONETARY_UNIT0)

		number = str(number)
		result = CutMoneyString(number, 0, 4, 	"", "")
		result = CutMoneyString(number, 4, 8, 	MONETARY_UNIT1, result)
		result = CutMoneyString(number, 8, 12, 	MONETARY_UNIT2, result)
		result = result + MONETARY_UNIT0

		return result

	def NumberToSecondaryCoinString(number) :
		if number <= 0 :
			return "0 %s" % (MONETARY_UNIT_JUN)

		number = str(number)
		result = CutMoneyString(number, 0, 4, 	"", "")
		result = CutMoneyString(number, 4, 8, 	MONETARY_UNIT1, result)
		result = CutMoneyString(number, 8, 12, 	MONETARY_UNIT2, result)
		result = result + MONETARY_UNIT_JUN

		return result

elif IsNEWCIBN() or IsCIBN10():
	def DO_YOU_SELL_ITEM(sellItemName, sellItemCount, sellItemPrice):
		if sellItemCount>1:
			return "È·¶¨Òª°Ñ%s¸ö%sÒÔ%s½ð±ÒÂôµôÂð£¿" % (str(sellItemCount), sellItemName, str(sellItemPrice))
		else:
			return "È·¶¨Òª°Ñ%sÒÔ%s½ð±ÒÂôµôÂð£¿" % (sellItemName, str(sellItemPrice))

	def DO_YOU_BUY_ITEM(sellItemName, sellItemCount, sellItemPrice):
		if sellItemCount>1:
			return "È·¶¨Òª°Ñ%s¸ö%sÒÔ%s½ð±ÒÂò½øÂð£¿" % (str(sellItemCount), sellItemName, str(sellItemPrice))
		else:
			return "È·¶¨Òª°Ñ%sÒÔ%s½ð±ÒÂò½øÂð£¿" % (sellItemName, str(sellItemPrice))

	def REFINE_FAILURE_CAN_NOT_ATTACH(attachedItemName):
		return "ÎÞ·¨ÏâÇ¶%s µÄ×°±¸" % (attachedItemName)

	def REFINE_FAILURE_NO_SOCKET(attachedItemName):
		return "Ã»ÓÐ¿ÉÒÔÏâÇ¶%s µÄ¿×" % (attachedItemName)

	def REFINE_FAILURE_NO_GOLD_SOCKET(attachedItemName):
		return "Ã»ÓÐ¿ÉÒÔÏâÇ¶%s µÄ»Æ½ð¿×" % (attachedItemName)

	def HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, dropItemCount):
		if dropItemCount>1:
			return "È·¶¨ÒªÈÓµô%d¸ö%sÂð?" % (dropItemCount, dropItemName)
		else:
			return "È·¶¨ÒªÈÓµô%sÂð?" % (dropItemName)

	def FISHING_NOTIFY(isFish, fishName):
		if isFish:
			return fishName # º»·¡ ¿©±â¿¡ ¾î¶² ¸»ÀÌ ºÙ¾îÀÖ´Âµ¥, ÀÎÄÚµùÀÌ ±úÁ®ÀÖ¾î¼­ º¹¿øÇÒ ¼ö°¡ ¾ø´Ù ¤Ð¤Ð... cython¿¡¼­ ÀÎÄÚµù ¿¡·¯ ³ª¼­ Áö¿ö¹ö¸²...
		else:
			return "µö×Å" + fishName + "ÁË¡£"

	def FISHING_SUCCESS(isFish, fishName):
		if isFish:
			return "µö×Å" + fishName + "ÁË¡£"
		else:
			return "»ñµÃ" + fishName + "ÁË¡£"

	def NumberToMoneyString(number):

		if number <= 0:
			return "0Á½"

		number = str(number)
		result = CutMoneyString(number, 0, 4, "", "")
		result = CutMoneyString(number, 4, 8, "Íò", result)
		result = CutMoneyString(number, 8, 12, "ÒÚ", result)
		result = result + "Á½"

		return result

	def NumberToSecondaryCoinString(number):

		if number <= 0:
			return "0JUN"

		number = str(number)
		result = CutMoneyString(number, 0, 4, "", "")
		result = CutMoneyString(number, 4, 8, "Íò", result)
		result = CutMoneyString(number, 8, 12, "ÒÚ", result)
		result = result + "JUN"

		return result		
elif IsEUROPE() and not IsWE_KOREA() and not IsYMIR():
	def DO_YOU_SELL_ITEM(sellItemName, sellItemCount, sellItemPrice):
		if sellItemCount > 1 :
			return DO_YOU_SELL_ITEM2 % (sellItemName, sellItemCount, NumberToMoneyString(sellItemPrice) )
		else:
			return DO_YOU_SELL_ITEM1 % (sellItemName, NumberToMoneyString(sellItemPrice) )

	def DO_YOU_BUY_ITEM(buyItemName, buyItemCount, buyItemPrice) :
		if buyItemCount > 1 :
			return DO_YOU_BUY_ITEM2 % ( buyItemName, buyItemCount, buyItemPrice )
		else:
			return DO_YOU_BUY_ITEM1 % ( buyItemName, buyItemPrice )
			
	def REFINE_FAILURE_CAN_NOT_ATTACH(attachedItemName) :
		return REFINE_FAILURE_CAN_NOT_ATTACH0 % (attachedItemName)

	def REFINE_FAILURE_NO_SOCKET(attachedItemName) :
		return REFINE_FAILURE_NO_SOCKET0 % (attachedItemName)

	def REFINE_FAILURE_NO_GOLD_SOCKET(attachedItemName) :
		return REFINE_FAILURE_NO_GOLD_SOCKET0 % (attachedItemName)
		
	def HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, dropItemCount) :
		if dropItemCount > 1 :
			return HOW_MANY_ITEM_DO_YOU_DROP2 % (dropItemName, dropItemCount)
		else :	
			return HOW_MANY_ITEM_DO_YOU_DROP1 % (dropItemName)

	def FISHING_NOTIFY(isFish, fishName) :
		if isFish :
			return FISHING_NOTIFY1 % ( fishName )
		else :
			return FISHING_NOTIFY2 % ( fishName )

	def FISHING_SUCCESS(isFish, fishName) :
		if isFish :
			return FISHING_SUCCESS1 % (fishName)
		else :
			return FISHING_SUCCESS2 % (fishName)
			
	def NumberToMoneyString(n) :
		if n <= 0 :
			return "0 %s" % (MONETARY_UNIT0)

		return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), MONETARY_UNIT0) 

	def NumberToSecondaryCoinString(n) :
		if n <= 0 :
			return "0 %s" % (MONETARY_UNIT_JUN)

		return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), MONETARY_UNIT_JUN) 

def NumberToMoney(n) :
	if n <= 0 :
		return "0"
	
	return "%s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]))