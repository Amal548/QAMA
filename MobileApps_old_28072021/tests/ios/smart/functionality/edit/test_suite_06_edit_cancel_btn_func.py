from time import sleep

import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_06_Ios_Edit_Cancel_Btn_Func(object):

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

    def test_06_verify_edit_cancel_btn(self):
        """
         Apply Edit Cancel button - C17029644
        """
        preview_img_before_edit = self.fc.get_preview_img_and_go_to_edit_screen()
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.apply_crop_flip()
        sleep(1)
        self.edit.select_edit_cancel()
        self.edit.verify_edit_page_title()
        self.edit.select_edit_cancel()
        self.preview.verify_preview_screen_title(self.preview.PREVIEW_TITLE)
        preview_img_after_edit_cancel = self.preview.preview_img_screenshot()
        assert self.edit.edit_img_comparision(preview_img_before_edit, preview_img_after_edit_cancel) is False

    def test_07_verify_cancel_discard_edits_confirmation(self):
        """
        Verify cancel discard pop-up- C17029645
        """
        self.fc.go_to_edit_screen_with_selected_photo()
        edit_screen_before_edit = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.CROP)
        self.edit.apply_crop_flip()
        self.edit.select_edit_done()
        edit_screen_after_edit = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(edit_screen_before_edit, edit_screen_after_edit) is True
        self.edit.select_edit_cancel()
        # select cancel on discard popup
        self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[3])
        edit_screen_after_discard_cancel = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(edit_screen_after_edit, edit_screen_after_discard_cancel) is False

    def test_08_verify_discard_edits(self):
        """
        Click cancel to discard edit changes and verify discard confirmation pop-p - C17029645
        """
        preview_img_before_edit = self.fc.get_preview_img_and_go_to_edit_screen()
        edit_screen_img_before_edit = self.edit.edit_img_screenshot()
        self.edit.select_text_and_enter_txtstring("Testing Discard")
        self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        edit_screen_img_after_edit = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(edit_screen_img_before_edit, edit_screen_img_after_edit) is True
        self.edit.select_edit_cancel()
        self.edit.select_discard_changes_btn()
        self.preview.verify_preview_screen_title(self.preview.PREVIEW_TITLE)
        preview_img_after_edit_discard = self.preview.preview_img_screenshot()
        assert self.edit.edit_img_comparision(preview_img_before_edit, preview_img_after_edit_discard) is False