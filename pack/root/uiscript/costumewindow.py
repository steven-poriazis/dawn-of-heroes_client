import uiScriptLocale
import item

COSTUME_START_INDEX = item.COSTUME_SLOT_START

window = {
	"name" : "CostumeWindow",
	"x" : SCREEN_WIDTH - 175 - 140,
	"y" : SCREEN_HEIGHT - 37 - 565,
	"style" : ("movable", "float",),
	"width" : 140,
	"height" : (180 + 59+8),
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 140,
			"height" : (180 + 59+8),
			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 6,
					"y" : 6,
					"width" : 130,
					"color" : "yellow",
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":60, "y":3, "text":uiScriptLocale.COSTUME_WINDOW_TITLE, "text_horizontal_align":"center", "r":0.0, "g":0.0, "b":0.0, "a":1.0},
					),
				},
				
				{
					"name" : "Costume_Base",
					"type" : "image",
					"x" : 13,
					"y" : 38,
					"image" : "locale/en/ui/costume/new_costume_bg.jpg",
					"children" :
					(
						{
							"name" : "CostumeSlot",
							"type" : "slot",
							"x" : 3,
							"y" : 3,
							"width" : 127,
							"height" : 180,
							"slot" : (
										{"index":COSTUME_START_INDEX+0, "x":62, "y":39, "width":32, "height":64},
										{"index":COSTUME_START_INDEX+1, "x":62, "y": 5, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+2, "x":62, "y":122-6, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+3, "x":13, "y":122-6, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+4, "x":13, "y":9+3+2, "width":32, "height":96},
										{"index":COSTUME_START_INDEX+5, "x":62, "y":157-4, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+6, "x":13, "y":157-4, "width":32, "height":32},
							),
						},
					),
				},
			),
		},
	),
}

