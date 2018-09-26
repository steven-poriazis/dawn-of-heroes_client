import uiScriptLocale
import item

EQUIPMENT_START_INDEX = 180

window = {
    "name": "InventoryWindow",

    "x": SCREEN_WIDTH - 176,
    "y": SCREEN_HEIGHT - 37 - 565,

    "style": ("movable", "float",),

    "width": 176,
    "height": 545,

    "children":
        (
            ## Inventory, Equipment Slots
            {
                "name": "board",
                "type": "board",
                "style": ("attach",),

                "x": 0,
                "y": 0,

                "width": 176,
                "height": 545,

                "children":
                    (
                        ## Title
                        {
                            "name": "TitleBar",
                            "type": "titlebar",
                            "style": ("attach",),

                            "x": 8,
                            "y": 7,

                            "width": 161,
                            "color": "yellow",

                            "children":
                                (
                                    {"name": "TitleName", "type": "text", "x": 77, "y": 3,
                                     "text": uiScriptLocale.INVENTORY_TITLE, "text_horizontal_align": "center"},
                                ),
                        },

                        ## Equipment Slot
                        {
                            "name": "Equipment_Base",
                            "type": "expanded_image",

                            "x": 10,
                            "y": 33,

                            "image" : "locale/en/ui/costume/inventory_new_imagine_pet.tga",

                            "children":
                                (

                                    {
                                        "name": "EquipmentSlot",
                                        "type": "slot",

                                        "x": 3,
                                        "y": 3,

                                        "width": 150,
                                        "height": 182,

                                        "slot": (
                                            {"index": EQUIPMENT_START_INDEX + 0, "x": 39, "y": 37, "width": 32,
                                             "height": 64},
                                            {"index": EQUIPMENT_START_INDEX + 1, "x": 39, "y": 2, "width": 32,
                                             "height": 32},
                                            {"index": EQUIPMENT_START_INDEX + 2, "x": 39, "y": 145, "width": 32,
                                             "height": 32},
                                            {"index": EQUIPMENT_START_INDEX + 3, "x": 75, "y": 67, "width": 32,
                                             "height": 32},
                                            {"index": EQUIPMENT_START_INDEX + 4, "x": 3, "y": 3, "width": 32,
                                             "height": 96},
                                            {"index": EQUIPMENT_START_INDEX + 5, "x": 114, "y": 67, "width": 32,
                                             "height": 32},
                                            {"index": EQUIPMENT_START_INDEX + 6, "x": 114, "y": 35, "width": 32,
                                             "height": 32},
                                            {"index": EQUIPMENT_START_INDEX + 7, "x": 2, "y": 145, "width": 32,
                                             "height": 32},
                                            {"index": EQUIPMENT_START_INDEX + 8, "x": 75, "y": 145, "width": 32,
                                             "height": 32},
                                            {"index": EQUIPMENT_START_INDEX + 9, "x": 114, "y": 2, "width": 32,
                                             "height": 32},
                                            {"index": EQUIPMENT_START_INDEX + 10, "x": 75, "y": 35, "width": 32,
                                             "height": 32},
											 {"index":item.EQUIPMENT_BELT, "x":39, "y":106, "width":32, "height":32},
											 {"index":item.EQUIPMENT_PENDANT, "x":2, "y":106, "width":32, "height":32},
											 {"index":item.EQUIPMENT_PET, "x":75, "y":106, "width":32, "height":32},
											 {"index":item.EQUIPMENT_RING1, "x":114, "y":105, "width":32, "height":32},
											 {"index":item.EQUIPMENT_RING2, "x":114, "y":142, "width":32, "height":32},
                                        ),
                                    },
									## Dragon Soul Button
									{
										"name" : "DSSButton",
										"type" : "button",

										"x" : 114,
										"y" : 107,

										"tooltip_text" : uiScriptLocale.TASKBAR_DRAGON_SOUL,

										"default_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_011.tga",
										"over_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_022.tga",
										"down_image" : "d:/ymir work/ui/dragonsoul/dss_inventory_button_033.tga",
									},
                                    ## MallButton
                                    {
                                        "name": "MallButton",
                                        "type": "button",

                                        "x": 118,
                                        "y": 148,

                                        "tooltip_text": uiScriptLocale.MALL_TITLE,
                                        "default_image": "locale/en/ui/mall/mall_button_011.tga",
                                        "over_image": "locale/en/ui/mall/mall_button_022.tga",
                                        "down_image": "locale/en/ui/mall/mall_button_033.tga",
                                    },
                                    ## CostumeButton
                                    {
                                        "name": "CostumeButton",
                                        "type": "button",

                                        "x": 78,
                                        "y": 5,

                                        "tooltip_text": uiScriptLocale.COSTUME_TITLE,

                                        "default_image": "locale/en/ui/costume/costume_button_01.tga",
                                        "over_image": "locale/en/ui/costume/costume_button_02.tga",
                                        "down_image": "locale/en/ui/costume/costume_button_03.tga",
                                    },
                                    {
                                        "name": "Equipment_Tab_01",
                                        "type": "radio_button",

                                        "x": 86,
                                        "y": 161,

                                        "default_image": "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
                                        "over_image": "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
                                        "down_image": "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

                                        "children":
                                            (
                                                {
                                                    "name": "Equipment_Tab_01_Print",
                                                    "type": "text",

                                                    "x": 0,
                                                    "y": 0,

                                                    "all_align": "center",

                                                    "text": "I",
                                                },
                                            ),
                                    },
                                    {
                                        "name": "Equipment_Tab_02",
                                        "type": "radio_button",

                                        "x": 86 + 32,
                                        "y": 161,

                                        "default_image": "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
                                        "over_image": "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
                                        "down_image": "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

                                        "children":
                                            (
                                                {
                                                    "name": "Equipment_Tab_02_Print",
                                                    "type": "text",

                                                    "x": 0,
                                                    "y": 0,

                                                    "all_align": "center",

                                                    "text": "II",
                                                },
                                            ),
                                    },

                                ),
                        },

               {
                    "name" : "Inventory_Tab_01",
                    "type" : "radio_button",
  
                    "x" : 11,
                    "y" : 33 + 191,
  
                    "default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
                    "over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
                    "down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
                    "tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,
  
                    "children" :
                    (
                        {
                            "name" : "Inventory_Tab_01_Print",
                            "type" : "text",
  
                            "x" : 0,
                            "y" : 0,
  
                            "all_align" : "center",
  
                            "text" : "I",
                        },
                    ),
                },
                {
                    "name" : "Inventory_Tab_02",
                    "type" : "radio_button",
  
                    "x" : 13 + 37,
                    "y" : 33 + 191,
  
                    "default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
                    "over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
                    "down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
                    "tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,
  
                    "children" :
                    (
                        {
                            "name" : "Inventory_Tab_02_Print",
                            "type" : "text",
  
                            "x" : 0,
                            "y" : 0,
  
                            "all_align" : "center",
  
                            "text" : "II",
                        },
                    ),
                },
                {
                    "name" : "Inventory_Tab_03",
                    "type" : "radio_button",
  
                    "x" : 13 + 77,
                    "y" : 33 + 191,
  
                    "default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
                    "over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
                    "down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
                    "tooltip_text" : "3.Inventar",
  
                    "children" :
                    (
                        {
                            "name" : "Inventory_Tab_03_Print",
                            "type" : "text",
  
                            "x" : 0,
                            "y" : 0,
  
                            "all_align" : "center",
  
                            "text" : "III",
                        },
                    ),
                },
                {
                    "name" : "Inventory_Tab_04",
                    "type" : "radio_button",
  
                    "x" : 14 + 116,
                    "y" : 33 + 191,
  
                    "default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
                    "over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
                    "down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",
                    "tooltip_text" : "4.Inventar",
  
                    "children" :
                    (
                        {
                            "name" : "Inventory_Tab_04_Print",
                            "type" : "text",
  
                            "x" : 0,
                            "y" : 0,
  
                            "all_align" : "center",
  
                            "text" : "IV",
                        },
                    ),
                },

                        ## Item Slot
                        {
                            "name": "ItemSlot",
                            "type": "grid_table",

                            "x": 8,
                            "y": 246,

                            "start_index": 0,
                            "x_count": 5,
                            "y_count": 9,
                            "x_step": 32,
                            "y_step": 32,

                            "image": "d:/ymir work/ui/public/Slot_Base.sub"
                        },
                    ),
            },
        ),
}
