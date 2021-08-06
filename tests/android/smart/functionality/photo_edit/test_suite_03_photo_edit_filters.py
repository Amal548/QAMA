from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_03_Photo_Edit_Filters(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]

    def test_01_filters_ui(self):
        """
        Description:
         1. Load to Preview screen through My Photos
         2. Click on Edit button
         3. Click on Filters button
         
        Expected Results:
         2. Verify Filter screen with:
            - Title
            - Cancel button
            - Done button
        """
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.verify_screen_title(self.edit.FILTERS)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)

    @pytest.mark.parametrize("document_type", ["bw", "bw2", "greyscale", "alabaster"])
    def test_02_filters_photo_by_document_type(self, document_type):
        """
        Description:
         1. Load to Edit screen through My Photos
         2. Click on Filters button
         3. Click on Document
         4. Do change through Document type
         5. Click on Done button
         
        Expected Results:
         5. Verify Edit screen, and make sure photo is changed success based on document type
        """
        document_types = {"bw": self.edit.BW,
                          "bw2": self.edit.BW2,
                          "greyscale": self.edit.GREYSCALE,
                          "alabaster": self.edit.ALABASTER}
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.FILTERS)
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.FILTER_DOCUMENT)
        self.edit.select_edit_child_option(document_types[document_type], direction="left", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        new_image = self.edit.edit_img_screenshot()
        assert(saf_misc.img_comp(current_image, new_image) != 0), "Filters document type {} didn't change successfully".format(document_types[document_type])

    @pytest.mark.parametrize("photo_type", ["summer", "aurora", "ultraviolet", "ink_stains", "alabaster", "dusk", "noir", "daydream", "embers", "moonlight", "snowshine", "atmospheric", "honeybee", "fireside", "glacial", "sauna", "seafarer", "cameo", "timeworn", "sunlight"])
    def test_03_filters_photo_by_photo(self,photo_type):
        """
        Description:
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. Click on Filters button
         4. Click on Photo,do some change
         5. Click on Done button
         
        Expected Results:
         5. Verify Edit screen, and make sure photo is changed success based on photo type
        """
        photo_types = {"summer": self.edit.SUMMER,
                        "aurora": self.edit.AURORA,
                        "ultraviolet": self.edit.ULTRAVIOLET,
                        "ink_stains": self.edit.INK_STAINS,
                        "alabaster": self.edit.ALABASTER,
                        "dusk": self.edit.DUSK,
                        "noir": self.edit.NOIR,
                        "daydream": self.edit.DAYDREAM,
                        "embers": self.edit.EMBERS,
                        "moonlight": self.edit.MOONLIGHT,
                        "snowshine": self.edit.SNOWSHINE,
                        "atmospheric": self.edit.ATMOSPHERIC,
                        "honeybee": self.edit.HONEYBEE,
                        "fireside": self.edit.FIRESIDE,
                        "glacial": self.edit.GLACIAL,
                        "sauna": self.edit.SAUNA,
                        "seafarer": self.edit.SEAFARER,
                        "cameo": self.edit.CAMEMO,
                        "timeworn": self.edit.TIMEWORN,
                        "sunlight": self.edit.SUNLIGHT
                        }
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.FILTERS)
        current_image = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.FILTER_PHOTO)
        self.edit.select_edit_child_option(photo_types[photo_type], direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        new_image = self.edit.edit_img_screenshot()
        assert(saf_misc.img_comp(current_image, new_image) != 0), "Filters photo type {} didn't change successfully".format(photo_types[photo_type])