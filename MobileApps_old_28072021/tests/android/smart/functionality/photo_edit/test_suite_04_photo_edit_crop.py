from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_04_Photo_Edit_Crop(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]

    def test_01_crop_ui(self):
        """
        Description:
         1. Load to Preview screen through Scan
         2. Click on Edit button
         3. Click on Crop button
         
        Expected Results:
         2. Verify Crop screen with:
            - Title
            - Cancel button
            - Done button
        """
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.verify_screen_title(self.edit.CROP)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)

    @pytest.mark.parametrize("crop_type", ["flip", "rotate", "custom", "square", "letter", "a4", "size_5_7", "size_4_6", "size_3_5_5"])
    def test_02_crop_photo(self, crop_type):
        """
        Description:
         1. Load to Edit screen through Scan
         2. Click on Crop button
         3. Do change through Crop type
         4. Click on Done button
         
        Expected Results:
         5. Verify Edit screen, and make sure photo is changed success based on document type
        """
        crop_types = {"custom": self.edit.CUSTOM,
                      "square": self.edit.SQUARE,
                      "letter": self.edit.LETTER,
                      "a4": self.edit.A4,
                      "size_5_7": self.edit.SIZE_5_7,
                      "size_4_6": self.edit.SIZE_4_6,
                      "size_3_5_5": self.edit.SIZE_3_5_5}
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.CROP)
        current_image = self.edit.edit_img_screenshot()
        if crop_type == "flip":
            self.edit.apply_crop_flip()
        elif crop_type == "rotate":
            self.edit.apply_crop_rotate()
        else:
            self.edit.select_edit_child_option(crop_types[crop_type], direction="right", check_end=False, str_id=True)
            self.edit.apply_crop_scale_picker()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        new_image = self.edit.edit_img_screenshot()
        assert(saf_misc.img_comp(current_image, new_image) != 0), "Crop type {} didn't change successfully".format(crop_type)