###################################################################
# title_name		: Professional Biolog System
# date_created		: 2016.08.07
# filename			: biolog_slider.py
# author			: VegaS
# version_actual	: Version 0.0.8
#
import uiScriptLocale
vegas_x = 270
vegas_y = 10

window = {
	"name" : "BiologSliderFinishGrade", "x" : 0, "y" : 0, "style" : ("movable", "float",),  "width" : 200, "height" : 300,
	"children" :
	(
		{
			"name" : "Board", "type" : "board_with_titlebar", "x" : 0, "y" : 0, "width" : 0, "height" : 0, "title" : "",
			"children" :
			(
				{
					"name" : "Background_Title", "type" : "thinboard", "x" : -255, "y" : -158-530, "width" : 290, "height" : 20,
					"children" :
					(
						{
							"name" : "iRewardType", "type" : "text", "x" : 9, "y" : 3, "multi_line" : 3, "fontname" : "Tahoma:19", "text" : "", "color" : -151012246,
						},
					),
				},
				{
					"name" : "Background", "type" : "thinboard", "x" : -324, "y" : -158-500, "width" : 425, "height" : 60,
					"children" :
					(
						{
							"name" : "iRewardItem", "type" : "grid_table", "x" : 385, "y" : 15, "start_index" : 0, "x_count" : 1, "y_count" : 1, "x_step" : 32, "y_step" : 32, "image" : "d:/ymir work/ui/public/Slot_Base.sub"
						},
						{
							"name" : "iRewardItemText", "type" : "text", "x" : 85, "y" : 5, "multi_line" : 1, "fontname" : "Tahoma:18", "text" : "", "color" : -151012246,
						},
					),	
				},	
			),
		},
	),
}