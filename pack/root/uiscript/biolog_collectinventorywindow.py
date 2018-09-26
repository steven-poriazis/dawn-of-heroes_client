###################################################################
# title_name		: Professional Biolog System
# date_created		: 2016.08.07
# filename			: biolog_collectinventorywindow.py
# author			: VegaS
# version_actual	: Version 0.0.8
#
import uiScriptLocale
import item

window = {
	"name" : "BeltInventoryWindow", "x" : SCREEN_WIDTH - 176 - 300, "y" : SCREEN_HEIGHT - 37 - 565 + 209 + 32, "width" : 148, "height" : 90, "type" : "image", "image" : "d:/ymir work/ui/game/belt_inventory/bg.tga",
	"children" :
	(
		{
			"name" : "ExpandBtn", "type" : "button", "x" : 2+4, "y" : 25, "default_image" : "d:/ymir work/ui/game/biolog_system_vegas/btn_expand_normal.tga", "over_image" : "d:/ymir work/ui/game/biolog_system_vegas/btn_expand_over.tga", "down_image" : "d:/ymir work/ui/game/biolog_system_vegas/btn_expand_down.tga", "disable_image" : "d:/ymir work/ui/game/biolog_system_vegas/btn_expand_disabled.tga",
		},
		{
			"name" : "BeltInventoryLayer", "x" : 5, "y" : 0, "width" : 148, "height" : 86,
			"children" :
			(
				{
					"name" : "MinimizeBtn", "type" : "button", "x" : 2+4, "y" : 25, "width" : 10, "default_image" : "d:/ymir work/ui/game/biolog_system_vegas/btn_minimize_normal.tga", "over_image" : "d:/ymir work/ui/game/biolog_system_vegas/btn_minimize_over.tga", "down_image" : "d:/ymir work/ui/game/biolog_system_vegas/btn_minimize_down.tga", "disable_image" : "d:/ymir work/ui/game/biolog_system_vegas/btn_minimize_disabled.tga",
				},
				{
					"name" : "BeltInventoryBoard", "type" : "board", "style" : ("attach", "float"), "x" : 10, "y" : 5, "width" : 138, "height" : 90,
					"children" :
					(
						{
							"name" : "BeltInventorySlot", "type" : "grid_table", "x" : 15, "y" : 52-36, "start_index" : 0, "x_count" : 1, "y_count" : 1, "x_step" : 32, "y_step" : 32, "image" : "d:/ymir work/ui/public/Slot_Base.sub"
						},
						{
							"name" : "send_biolog", "type" : "button", "x" : 41, "y" : 52-36+45, "text" : "", "default_image" : "d:/ymir work/ui/game/biolog_system_vegas/acceptbutton00.tga", "over_image" : "d:/ymir work/ui/game/biolog_system_vegas/acceptbutton01.tga", "down_image" : "d:/ymir work/ui/game/biolog_system_vegas/acceptbutton02.tga",
						},
						{
							"name" : "LineUp", "type" : "line", "x"	: 60, "y" : 10, "width" : 0, "height" : 43, "color" : 0xffffffff,
						},
						{
							"name" : "bar_", "type" : "slotbar", "x" : 66, "y" : 57-24, "width" : 60, "height" : 21,
							"children" :
							(
								{
									"name" : "count_value", "type" : "text", "x" : 0, "y" : 0, "all_align" : "center", "text" : "0/0",
								},
							),
						},
						{
							"name" : "time", "type" : "slotbar", "x" : 66, "y" : 57-47, "width" : 60, "height" : 21,
							"children" :
							(
								{
									"name" : "time_value", "type" : "text", "x" : 0, "y" : 0, "all_align" : "center", "text" : "00:00:00",
								},
							),
						},
					),
				},
			)
		},
	),
}
