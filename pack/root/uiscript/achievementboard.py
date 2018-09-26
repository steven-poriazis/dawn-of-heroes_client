import uiScriptLocale
import app

BOARD_WIDTH = 250
BOARD_HEIGHT = 355	
BOARD_EXTEND = 100
window = {
	"name" : "AchievementBoard",

	"x" : SCREEN_WIDTH / 2 - BOARD_WIDTH / 2,
	"y" : SCREEN_HEIGHT / 2 - BOARD_HEIGHT / 2,

	"style" : ("movable", "float",),

	"width"  : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"title" : uiScriptLocale.ACHIEVEMENT_TITLE,

			"children" :
			(
				{
					"name" : "current_achievement_title",
					"type" : "text",

					"x" : 0,
					"y" : 38,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : uiScriptLocale.ACHIEVEMENT_CURRENT_TITLE,
				},
				{
					"name" : "current_achievement",
					"type" : "text",

					"x" : 0,
					"y" : 54,

					"horizontal_align" : "center",
					"text_horizontal_align" : "center",

					"text" : "",
				},
				{
					"name" : "achievement_selection_wnd",

					"x" : 20,
					"y" : 80,

					"width" : BOARD_WIDTH - 20*2,
					"height" : 10 + 17 * 6 + 10 + 21 + BOARD_EXTEND + 20,

					"children" :
					(
						{
							"name" : "select_button",
							"type" : "button",

							"x" : 10 / 2 - 5,
							"y" : 10 + 17 * 6 + 10 + BOARD_EXTEND + 17,

							"horizontal_align" : "center",

							"default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							"over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							"down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",

							"text" : uiScriptLocale.ACHIEVEMENT_SELECT_BUTTON,
						},
						# {
							# "name" : "item_button",
							# "type" : "button",

							# "x" : 88 / 2 + 5,
							# "y" : 10 + 17 * 6 + 10 + BOARD_EXTEND + 17,

							# "horizontal_align" : "center",

							# "default_image" : "d:/ymir work/ui/public/Large_Button_01.sub",
							# "over_image" : "d:/ymir work/ui/public/Large_Button_02.sub",
							# "down_image" : "d:/ymir work/ui/public/Large_Button_03.sub",

							# "text" : uiScriptLocale.ACHIEVEMENT_ITEM_BUTTON,
						# },
						{
							"name" : "seperating_line",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"horizontal_align" : "center",

							"image" : "locale/%s/ui/game/achievement/seperating_line.tga" % (app.GetLocaleName()),
						},
						{
							"name" : "selectionbox",
							"type" : "listbox",

							"x" : 0,
							"y" : 10,

							"width" : BOARD_WIDTH - 20*2 - 17,
							"height" : 17 * 6 + BOARD_EXTEND + 25,
						},
						{
							"name" : "selectionscroll",
							"type" : "scrollbar",

							"x" : BOARD_WIDTH - 20*2 - 17,
							"y" : 10,

							"size" : 17 * 6 + BOARD_EXTEND + 25,
						},
					),
				},
			),
		},
	),
}
