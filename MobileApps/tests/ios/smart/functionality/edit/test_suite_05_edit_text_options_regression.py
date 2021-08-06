from time import sleep

import pytest
import logging

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_05_Ios_Edit_Text_Options_Regression(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.edit = cls.fc.fd["edit"]
        cls.stack = request.config.getoption("--stack")
        # Navigating to home screen
        cls.fc.go_home(stack=cls.stack)

    def test_01_regress_edit_text_font_options(self):
        self.regress_edit_text_options("Text Fonts Regression", self.edit.TEXT_FONTS,
                                       self.edit.TEXT_FONT_OPTIONS)

    def test_02_regress_edit_text_color_options(self):
        self.regress_edit_text_options("Text Color Regression", self.edit.TEXT_COLOR,
                                       self.edit.TEXT_COLOR_OPTIONS)

    def test_03_regress_edit_text_bgcolor_options(self):
        self.regress_edit_text_options("Text BGColor Regression", self.edit.TEXT_BGCOLOR,
                                       self.edit.TEXT_BGCOLOR_OPTIONS)

    def regress_edit_text_options(self, edit_text, edit_feature, edit_feature_options,diff=0):
        self.fc.go_to_edit_screen_with_selected_photo()
        self.edit.select_text_and_enter_txtstring(edit_text)
        self.edit.select_edit_done()
        self.edit.verify_screen_title(self.edit.TEXT_OPTIONS_TITLE)
        self.edit.apply_edits(edit_feature, edit_feature_options[1])
        # validation
        edit_failed = self.edit.apply_and_verify_all_edit_options(edit_feature,
                                                                  edit_feature_options, diff=diff)
        assert len(edit_failed) == 0, "Failed to apply following edit options {}".format(edit_failed)
        logging.info("All {} edit options applied successfully".format(edit_feature))
        #Clean up
        self.edit.select_edit_cancel()
        self.edit.select_edit_cancel()
        sleep(1)
        self.edit.select_discard_changes_btn()
