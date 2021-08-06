import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_04_Ios_Edit_Text_Functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.edit = cls.fc.fd["edit"]
        cls.stack = request.config.getoption("--stack")

        # Navigating to home screen
        cls.fc.go_home(stack=cls.stack)

    def test_01_verify_edit_text(self):
        edit_text = "Testing Text"
        self.fc.go_to_edit_screen_with_camera_scan_image()
        img_before_edit = self.edit.edit_img_screenshot()
        self.edit.select_text_and_enter_txtstring(edit_text)
        self.edit.select_edit_cancel()
        self.edit.verify_edit_page_title()
        self.edit.verify_edit_text_displayed(edit_text)
        img_after_font_edit_cancel = self.edit.edit_img_screenshot()
        self.edit.select_text_and_enter_txtstring(edit_text)
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE)
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        img_after_font_edit_save = self.edit.edit_img_screenshot()
        self.edit.verify_edit_page_title()
        self.edit.verify_edit_text_displayed(edit_text)
        assert self.edit.edit_img_comparision(img_before_edit, img_after_font_edit_cancel) is False
        assert self.edit.edit_img_comparision(img_before_edit,
                                              img_after_font_edit_save) is True

    def test_02_verify_edit_text_font(self):
        edit_text = "Testing Text and font Options"
        self.edit_text_with_options(self.edit.TEXT_FONTS, self.edit.TEXT_FONT_OPTIONS[4],
                                    self.edit.TEXT_FONT_OPTIONS[6], edit_text)

    def test_03_verify_edit_text_color(self):
        edit_text = "Testing Text Color Options"
        self.edit_text_with_options(self.edit.TEXT_COLOR, self.edit.TEXT_COLOR_OPTIONS[4],
                                    self.edit.TEXT_COLOR_OPTIONS[8], edit_text)

    def test_04_verify_edit_text_bg_color(self):
        edit_text = "Testing Text bg color Options"
        self.edit_text_with_options(self.edit.TEXT_BGCOLOR, self.edit.TEXT_BGCOLOR_OPTIONS[2],
                                    self.edit.TEXT_BGCOLOR_OPTIONS[5], edit_text)

    def test_05_verify_edit_text_options_ui(self):
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.select_text_and_enter_txtstring("Testing Text Options")
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE)
        self.edit.verify_edit_ui_elements(self.edit.TEXT_OPTIONS)
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        text_font_options = self.edit.get_elements_in_collection_view(self.edit.TEXT_FONTS,
                                                                      self.edit.TEXT_FONT_OPTIONS, "text")
        self.edit.select_edit_cancel()
        text_color_options = self.edit.get_elements_in_collection_view(self.edit.TEXT_COLOR,
                                                                       self.edit.TEXT_COLOR_OPTIONS, "textColor")
        self.edit.select_edit_cancel()
        text_bg_color_options = self.edit.get_elements_in_collection_view(self.edit.TEXT_BGCOLOR,
                                                                          self.edit.TEXT_BGCOLOR_OPTIONS,
                                                                          "textColor")
        self.edit.select_edit_cancel()
        self.edit.select_edit_main_option(self.edit.TEXT_ALIGNMENT)
        assert self.edit.verify_undo_button_enabled() == 'true'
        assert set(text_font_options) == set(self.edit.TEXT_FONT_OPTIONS)
        assert set(text_color_options) == set(self.edit.TEXT_COLOR_OPTIONS)
        assert set(text_bg_color_options) == set(self.edit.TEXT_BGCOLOR_OPTIONS)

    def test_06_verify_edit_text_alignment(self):
        """
        Verify Edit text alignment options - C17023775
        :return:
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.select_text_and_enter_txtstring("Testing Text Alignment")
        self.edit.select_edit_done()
        img_before_alignment = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.TEXT_ALIGNMENT)
        assert self.edit.verify_undo_button_enabled() == 'true'
        img_after_alignment = self.edit.edit_img_screenshot()
        self.edit.select_edit_main_option(self.edit.TEXT_ALIGNMENT)
        img_after_alignment2 = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(img_before_alignment, img_after_alignment) is True
        assert self.edit.edit_img_comparision(img_after_alignment, img_after_alignment2) is True
        self.edit.select_edit_done()

    def test_07_verify_add_text_option(self):
        """
        Add text box by clicking + - C27761718
        """
        self.go_to_edit_text_screen()
        img_before_text = self.edit.edit_img_screenshot()
        self.edit.select_add_text()
        self.edit.add_txt_string("Testing Add Text Btn")
        self.edit.select_edit_done()
        img_after_text = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(img_before_text, img_after_text, compare_diff=0.3) is True
        self.edit.select_undo()
        img_after_undo = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(img_after_text, img_after_undo, compare_diff=0.3) is True
        self.edit.select_redo()
        img_after_redo = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(img_after_undo, img_after_redo, compare_diff=0.3) is True

    def test_08_delete_text_box(self):
        """
        Delete edit text box - C27761719
        """
        self.go_to_edit_text_screen()
        img_with_text = self.edit.edit_img_screenshot()
        self.edit.select_delete_text()
        img_after_delete_text = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(img_with_text, img_after_delete_text, compare_diff=0.5) is True

    def test_09_modify_text_box(self):
        """
         Modify Edit Text to add or append text - C27761720
        """
        self.go_to_edit_text_screen()
        img_with_text = self.edit.edit_img_screenshot()
        self.edit.modify_text_box("Text Append")
        img_text_appended = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(img_with_text, img_text_appended, compare_diff=0.3) is True
        self.edit.modify_text_box("Modify Text", clear_text=True)
        img_text_modified = self.edit.edit_img_screenshot()
        assert self.edit.edit_img_comparision(img_text_appended, img_text_modified, compare_diff=0.3) is True

    def edit_text_with_options(self, text_edit_feature, text_edit_option, text_edit_option2, edit_text):
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.select_text_and_enter_txtstring(edit_text)
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE)
        img_before_edit = self.edit.edit_img_screenshot()
        self.edit.select_edit_text_options(text_edit_feature, text_edit_option)
        self.edit.select_edit_cancel()
        self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE)
        img_after_font_edit_cancel = self.edit.edit_img_screenshot()
        self.edit.select_edit_text_options(text_edit_feature, text_edit_option2)
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE)
        img_after_font_edit_save = self.edit.edit_img_screenshot()
        self.edit.select_edit_done()
        self.edit.verify_edit_text_displayed(edit_text)
        self.edit.select_edit_done()
        assert self.edit.edit_img_comparision(img_before_edit, img_after_font_edit_cancel) is False
        assert self.edit.edit_img_comparision(img_after_font_edit_cancel,
                                              img_after_font_edit_save) is not False

    def go_to_edit_text_screen(self):
        if self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE) is False:
            self.fc.go_to_edit_screen_with_camera_scan_image()
            self.edit.select_text_and_enter_txtstring("Testing")
            self.edit.select_edit_done()
            self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE)
