from time import sleep

import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_02_Ios_Edit_Functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.edit = cls.fc.fd["edit"]
        cls.preview = cls.fc.fd["preview"]
        cls.stack = request.config.getoption("--stack")

        # Navigating to home screen
        cls.fc.go_home(stack=cls.stack)

    def test_01_verify_applying_auto_option(self):
        """
         Apply Edit option Auto, Save and verify result - C17023766
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        image_before_edit = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.AUTO)
        assert self.edit.verify_undo_button_enabled() == 'true'
        image_after_edit = self.edit.edit_img_screenshot()
        self.edit.select_edit_done()
        assert self.edit.edit_img_comparision(image_before_edit, image_after_edit) is True

    @pytest.mark.parametrize("edit_option", ["ADJUST", "FILTER_DOCUMENT", "FILTER_PHOTO", "CROP"])
    def test_02_verify_applying_edit_option(self, edit_option):
        """
         Apply Edit Adjust option, move slider (if displayed) Save and verify result -
         C27151707, C27151711, C27151939, C17023770
        """
        edit_sub_options = {"ADJUST": [self.edit.ADJUST, self.edit.ADJUST_OPTIONS[0]],
                            "FILTER_DOCUMENT": [self.edit.FILTER_DOCUMENT, self.edit.FILTER_DOCUMENT_OPTIONS[4]],
                            "FILTER_PHOTO": [self.edit.FILTER_PHOTO, self.edit.FILTER_PHOTO_OPTIONS[3]],
                            "CROP": [self.edit.CROP, self.edit.CROP_OPTIONS[2]]}
        org_preview_img = self.fc.get_preview_img_and_go_to_edit_screen()
        pre_edited_img = self.edit.edit_img_screenshot()
        if edit_option in ("FILTER_PHOTO", "FILTER_DOCUMENT"):
            self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.select_edit_main_option(edit_sub_options[edit_option][0])
        image_before_adjust = self.edit.edit_img_screenshot()
        self.edit.select_edit_child_option(edit_sub_options[edit_option][1], check_end=False)
        self.edit.verify_and_swipe_adjust_slider()
        if edit_option == "CROP":
            self.edit.apply_crop_rotate()
        image_after_adjust = self.edit.edit_img_screenshot()
        self.edit.select_edit_done()
        edited_img = self.edit.edit_img_screenshot()
        self.edit.select_edit_done()
        edited_preview_img = self.preview.preview_img_screenshot()
        assert self.edit.edit_img_comparision(image_before_adjust, image_after_adjust) is True
        assert self.edit.edit_img_comparision(pre_edited_img, edited_img) is True
        assert self.edit.edit_img_comparision(org_preview_img, edited_preview_img) is True

    def test_03_verify_crop_flip_rotate_scale_options(self):
        """
         Apply Edit crop_flip_rotate_scale_options, Save and compare images -
         C27151941, C27151945, C27151943
        """
        preview_img_before_edit = self.fc.get_preview_img_and_go_to_edit_screen()
        pre_edit_img = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.apply_crop_flip()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        flip_img = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.apply_crop_rotate()
        self.edit.select_edit_done()
        rotate_img = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.apply_crop_scale_picker()
        self.edit.select_edit_done()
        scale_picker_img = self.edit.edit_img_screenshot()
        self.edit.select_edit_done()
        self.preview.verify_preview_screen_title(self.preview.PREVIEW_TITLE)
        preview_img_after_edit = self.preview.preview_img_screenshot()
        assert self.edit.edit_img_comparision(pre_edit_img, flip_img) is True
        assert self.edit.edit_img_comparision(flip_img, rotate_img) is True
        assert self.edit.edit_img_comparision(rotate_img, scale_picker_img) is True
        assert self.edit.edit_img_comparision(preview_img_before_edit, preview_img_after_edit) is True
        # clean up
        self.preview.select_navigate_back()

    def test_04_verify_crop_reset_option(self):
        """
         Apply Edit Crop reset option - C17029650
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.select_edit_child_option("Reset")
        sleep(1)
        img_before_edit = self.edit.edit_img_screenshot()
        self.edit.select_edit_child_option(self.edit.CROP_OPTIONS[3])
        self.edit.apply_crop_flip()
        sleep(1)
        img_after_edit = self.edit.edit_img_screenshot()
        sleep(1)
        self.edit.select_edit_child_option("Reset")
        sleep(3)
        image_after_reset = self.edit.edit_img_screenshot()
        self.edit.select_edit_done()
        assert self.edit.edit_img_comparision(img_before_edit, img_after_edit) is True
        assert self.edit.edit_img_comparision(img_after_edit, image_after_reset) is True
        assert self.edit.edit_img_comparision(img_before_edit, image_after_reset) is False

    def test_05_verify_edit_text_options_fun(self):
        """
         Apply Edit Text, Font, Color, Background color save and verify preview img
        """
        preview_img_before_edit = self.fc.get_preview_img_and_go_to_edit_screen()
        self.edit.select_text_and_enter_txtstring("Edit Text Options and Print")
        self.edit.select_edit_done()
        self.edit.select_edit_text_options(self.edit.TEXT_FONTS, self.edit.TEXT_FONT_OPTIONS[4])
        self.edit.select_edit_done()
        self.edit.select_edit_text_options(self.edit.TEXT_COLOR, self.edit.TEXT_COLOR_OPTIONS[5])
        self.edit.select_edit_done()
        self.edit.select_edit_text_options(self.edit.TEXT_BGCOLOR, self.edit.TEXT_BGCOLOR_OPTIONS[6])
        self.edit.select_edit_done()
        self.edit.select_edit_main_option(self.edit.TEXT_ALIGNMENT)
        self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.preview.verify_preview_screen_title(self.preview.PREVIEW_TITLE)
        preview_img_after_text_edit = self.preview.preview_img_screenshot()
        assert self.edit.edit_img_comparision(preview_img_before_edit, preview_img_after_text_edit) is True