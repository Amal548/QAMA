from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_02_Photo_Edit_Adjust(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]

    def test_01_adjust_ui(self):
        """
        Description:
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. Click on Adjust button
         
        Expected Results:
         2. Verify Adjust screen with:
            - Title
            - Cancel button
            - Done button
        """
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.ADJUST)
        self.edit.verify_screen_title(self.edit.ADJUST)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)

    @pytest.mark.parametrize("adjust_type", ["brightness", "saturation", "contrast", "clarity", "exposure", "shadows", "highlights", "whites", "blacks", "temperature"])
    def test_02_adjust_photo_by_type(self, adjust_type):
        """
        Description:
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. Click on Adjust, select adjust type based on adjust_type value
         4. Do change through scroll bar 
         5. Click on Done button
         
        Expected Results:
         5. Verify Edit screen, and make sure photo is changed success based on adjust type
        """
        adjust_types = {"brightness": self.edit.BRIGHTNESS,
                        "saturation": self.edit.SATURATION,
                        "contrast": self.edit.CONTRAST,
                        "clarity": self.edit.CLARITY,
                        "exposure": self.edit.EXPOSURE,
                        "shadows": self.edit.SHADOWS,
                        "highlights": self.edit.HIGHLIGHTS,
                        "whites": self.edit.WHITES,
                        "blacks": self.edit.BLACKS,
                        "temperature": self.edit.TEMPERATURE}
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.ADJUST)
        self.edit.select_edit_child_option(adjust_types[adjust_type], direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()

    @pytest.mark.parametrize("btn_name", ["cancel", "undo"])
    def test_03_adjust_cancel(self, btn_name):
        """
        Description:
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. Click on Adjust button
         4. Click on Brightness,do some change
         5. Click on Cancel button
         
        Expected Results:
         2. Verify Edit screen with photo no any change
        """
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.ADJUST)
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_child_option(self.edit.BRIGHTNESS, direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider()
        if btn_name == "cancel":
            self.edit.select_edit_cancel()
            self.edit.verify_edit_page_title()
        else:
            self.edit.select_undo()
            new_image = self.edit.edit_img_screenshot()
            assert(saf_misc.img_comp(current_image, new_image) < 0.06), "Photo should be same with previous one after clicking undo button"