import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_01_Ios_Edit_Screen_UI_Validation(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.edit = cls.fc.fd["edit"]
        cls.preview = cls.fc.fd["preview"]
        cls.stack = request.config.getoption("--stack")

        # Navigating to home screen
        cls.fc.go_home(stack=cls.stack)

    def test_01_edit_screen_ui_validation(self):
        """
        Edit screen UI - C17023765
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.verify_edit_ui_elements(self.edit.EDIT_OPTIONS)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.select_edit_cancel()
        self.preview.verify_preview_screen_title(self.preview.PREVIEW_TITLE)

    def test_02_verify_adjust_options_ui(self):
        """
        Edit - Adjust screen UI - C17023767
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        adjust_options = self.edit.get_elements_in_collection_view(self.edit.ADJUST,
                                                                   self.edit.ADJUST_OPTIONS,
                                                                   "adjustments")
        self.edit.verify_screen_title(self.edit.ADJUST)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        # Test Clean UPs
        self.edit.select_edit_cancel()
        assert set(adjust_options) == set(self.edit.ADJUST_OPTIONS)
        # Test clean up
        self.edit.select_edit_cancel()

    def test_03_verify_filter_options_ui(self):
        """
        Edit- Filter screen UI - C17023768
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.verify_screen_title(self.edit.FILTERS)
        self.edit.verify_edit_ui_elements(self.edit.FILTER_OPTIONS)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        filters_document_options = self.edit.get_elements_in_collection_view(self.edit.FILTER_DOCUMENT,
                                                                             self.edit.FILTER_DOCUMENT_OPTIONS,
                                                                             "filter")
        filters_photo_options = self.edit.get_elements_in_collection_view(self.edit.FILTER_PHOTO,
                                                                          self.edit.FILTER_PHOTO_OPTIONS, "filter")
        self.edit.select_edit_cancel()
        assert set(filters_photo_options) == set(self.edit.FILTER_PHOTO_OPTIONS)
        assert set(filters_document_options) == set(self.edit.FILTER_DOCUMENT_OPTIONS)
        # Test clean up
        self.edit.select_edit_cancel()

    def test_04_verify_crop_options_ui(self):
        """
        Edit- Crop  screen UI - C17023769
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        crop_options = self.edit.get_elements_in_collection_view(self.edit.CROP,
                                                                 self.edit.CROP_OPTIONS,
                                                                 "transform")
        self.edit.verify_screen_title(self.edit.CROP)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.verify_edit_ui_elements(self.edit.CROP_BUTTONS)
        self.edit.select_edit_cancel()
        assert set(crop_options) == set(self.edit.CROP_OPTIONS)
        # Test clean up
        self.edit.select_edit_cancel()

    def test_05_verify_add_text_screen_ui(self):
        """
        Verify Edit add text UI options - C17023771
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.select_text_and_enter_txtstring("Testing Text Options")
        self.edit.verify_edit_ui_elements(self.edit.ADD_TEXT_UI)
        self.edit.select_edit_done()

    def test_06_verify_text_options_screen_ui(self):
        """
        Verify Edit text options UI  - C27151982
        """
        self.go_to_text_edit_screen()
        self.edit.verify_edit_ui_elements(self.edit.TEXT_OPTIONS)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.verify_edit_ui_elements(self.edit.TEXT_OPTIONS_SCREEN_BUTTONS)

    def test_07_verify_font_screen_ui(self):
        """
        Verify Edit font UI options - C17023772
        """
        self.go_to_text_edit_screen()
        text_font_options = self.edit.get_elements_in_collection_view(self.edit.TEXT_FONTS,
                                                                      self.edit.TEXT_FONT_OPTIONS, "text")
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.select_edit_done()
        assert set(text_font_options) == set(self.edit.TEXT_FONT_OPTIONS)

    def test_08_verify_text_color_ui(self):
        """
        Verify Edit text color UI options - C17023773
        """
        self.go_to_text_edit_screen()
        text_color_options = self.edit.get_elements_in_collection_view(self.edit.TEXT_COLOR,
                                                                       self.edit.TEXT_COLOR_OPTIONS, "textColor")
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.select_edit_done()
        assert set(text_color_options) == set(self.edit.TEXT_COLOR_OPTIONS)

    def test_09_verify_text_bg_color_ui(self):
        """
        Verify Edit text background UI options - C17023774
        """
        self.go_to_text_edit_screen()
        text_bg_color_options = self.edit.get_elements_in_collection_view(self.edit.TEXT_BGCOLOR,
                                                                          self.edit.TEXT_BGCOLOR_OPTIONS,
                                                                          "textColor")
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        self.edit.select_edit_done()
        assert set(text_bg_color_options) == set(self.edit.TEXT_BGCOLOR_OPTIONS)

    def test_10_verify_discard_confirmation_ui(self):
        """
        Click cancel to discard edit changes and verify discard confirmation pop-up - C17029645
        """
        self.go_to_text_edit_screen()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        self.edit.select_edit_cancel()
        self.edit.verify_edit_ui_elements(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS)

    def go_to_text_edit_screen(self):
        if self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE) is False:
            self.fc.go_to_edit_screen_with_camera_scan_image()
            self.edit.select_text_and_enter_txtstring("Testing Text Options")
            self.edit.select_edit_done()