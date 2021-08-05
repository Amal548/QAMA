from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_05_Photo_Edit_Text(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]

    def test_01_text_ui(self):
        """
        Description:
         1. Load to Preview screen through My Photos
         2. Click on Edit button
         3. Click on Text button
         
        Expected Results:
         2. Verify Text screen with:
            - Title
            - Cancel button
            - Done button
        """
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.verify_screen_title(self.edit.TEXT)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)

    @pytest.mark.parametrize("font_type", ["abril", "arvo", "concert", "commorant", "dancing_script", "lora", "meie_script", "montserrat", "old_standard", "oswald", "playfair_display", "rakkas", "roboto", "ubuntu", "yatra_one"])
    def test_02_text_by_fonts_type(self, font_type):
        """
        Description:
         1. Load to Edit screen through My Photos
         2. Click on Text button
         3. Type a text
         4. Click on Done button
         5. Click on Fonts button
         6. Do change based on Fonts type
         7. Click on Done button
         
        Expected Results:
         7. Verify Edit screen, and make sure photo is changed success based on font type
        """
        font_types = {"abril": self.edit.ABRIL,
                      "arvo": self.edit.ARVO,
                      "concert": self.edit.CONCERT,
                      "commorant": self.edit.COMMIRANT,
                      "dancing_script": self.edit.DANCING_SCRIPT,
                      "lora": self.edit.LORA,
                      "meie_script": self.edit.MEIE_SCRIPT,
                      "montserrat": self.edit.MONTSERRAT,
                      "old_standard": self.edit.OLD_STANDARD,
                      "oswald": self.edit.OSWALD,
                      "playfair_display": self.edit.PLAYFAIR_DISPLAY,
                      "rakkas": self.edit.RAKKAS,
                      "roboto": self.edit.ROBOTO,
                      "ubuntu": self.edit.UBUNTU,
                      "yatra_one": self.edit.YATRA_ONE
                      }
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        self.edit.select_edit_main_option(self.edit.TEXT_FONTS)
        self.edit.verify_screen_title(self.edit.FONTS_TITLE)
        self.edit.select_edit_child_option(font_types[font_type], direction="right", check_end=False, str_id=True)
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTION_TITLE)
    
    @pytest.mark.parametrize("btn_name", ["add", "delete", "to_front"])
    def test_03_text_add_text(self, btn_name):
        """
        Description:
         1. Load to Preview screen through My Photos
         2. Click on Edit button
         3. Click on Text button
         4. Type a text, and Click on Done button
         5. If btn_name = "add", then Click on Add Text button "+"
            If btn_name = "delete", then click on Delete button
         6. Click on Done button
         
        Expected Results:
         6. Make sure all new changes did success on Text Options screen
        """
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        current_image = self.edit.edit_img_screenshot()
        if btn_name == "add":
            self.edit.select_add_text()
            self.edit.add_txt_string("QAMA Functionality Testing")
            self.edit.select_edit_done()
        elif btn_name == "to_front":
            self.edit.select_to_front()
        else:
            self.edit.select_delete_text()
        new_image = self.edit.edit_img_screenshot()
        if btn_name == "to_front":
            assert(saf_misc.img_comp(current_image, new_image) == 0), "Text shouldn't be changed with to front function"
        else:
            assert(saf_misc.img_comp(current_image, new_image) != 0), "Text didn't add or delete successfully."
    
    @pytest.mark.parametrize("btn_name", ["color", "bg_color"])
    def test_04_color_ui(self, btn_name):
        """
        Description:
         1. Load to Preview screen through My Photos
         2. Click on Edit button
         3. Click on Text button
         4. Add text, and click on Done button
         5. If btn_name == "color", then Click on Color
            If btn_name == "bg_color",then Click on BG Color
         
        Expected Results:
         5. Verify Color Or BG screen with:
            - Title
            - Cancel button
            - Done button
        """
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        if btn_name == "color":
            self.edit.select_edit_main_option(self.edit.COLOR_BTN)
        else:
            self.edit.select_edit_main_option(self.edit.TEXT_BGCOLOR)
        self.edit.verify_screen_title(self.edit.TEXT_COLOR)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
    
    @pytest.mark.parametrize("color_type", ["gray", "black", "light_blue", "blue", "purple", "orchid", "pink", "red", "orange", "gold", "yellow", "olive", "green", "aquamarin"])
    def test_05_text_by_color(self, color_type):
        """
        Description:
         1. Load to Edit screen through My Photos
         2. Click on Text button
         3. Type a text
         4. Click on Done button
         5. Click on Fonts button
         6. Do change based on Fonts type
         7. Click on Done button
         
        Expected Results:
         7. Verify Edit screen, and make sure photo is changed success based on font type
        """
        color_types = {"gray": self.edit.GRAY,
                      "black": self.edit.BLACK,
                      "light_blue": self.edit.LIGHT_BLUE,
                      "blue": self.edit.BLUE,
                      "purple": self.edit.PURPLE,
                      "orchid": self.edit.ORCHID,
                      "pink": self.edit.PINK,
                      "red": self.edit.RED,
                      "orange": self.edit.ORANGE,
                      "gold": self.edit.GOLD,
                      "yellow": self.edit.YELLOW,
                      "olive": self.edit.OLIVE,
                      "green": self.edit.GREEN,
                      "aquamarin": self.edit.AQUAMARIN
                      }
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.TEXT)
        self.edit.add_txt_string("QAMATesting")
        self.edit.select_edit_done()
        self.edit.select_edit_main_option(self.edit.COLOR_BTN)
        self.edit.select_color(color_types[color_type])
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTION_TITLE)