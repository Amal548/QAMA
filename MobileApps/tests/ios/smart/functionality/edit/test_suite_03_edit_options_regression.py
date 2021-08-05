import pytest
import logging

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_03_Ios_Edit_Options_Regression(object):

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

    def test_01_regress_adjust_options(self):
        """
        Apply all Adjust option,
        move slider (if displayed) Save and verify result with undo button enabled- C27151708
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        adjust_option_failed = []
        for edit_option in self.edit.ADJUST_OPTIONS:
            self.edit.apply_edits(self.edit.ADJUST, edit_option)
            if self.edit.verify_undo_button_enabled() != 'true':
                adjust_option_failed.append(edit_option)
        assert len(adjust_option_failed) == 0, "Failed to apply following adjust options {}".format(
            adjust_option_failed)
        logging.info("All adjust options applied successfully")
        # Clean up steps
        self.fc.verify_preview_screen_and_go_home()

    def test_02_regress_filters_document_options(self):
        """
         Apply all Filter Document options, Save and verify results
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.apply_edits(self.edit.FILTER_DOCUMENT, self.edit.FILTER_DOCUMENT_OPTIONS[4])
        del self.edit.FILTER_DOCUMENT_OPTIONS[0:2]
        self.edit.FILTER_DOCUMENT_OPTIONS.remove('Photo')
        edit_failed = self.edit.apply_and_verify_all_edit_options(self.edit.FILTERS, self.edit.FILTER_DOCUMENT_OPTIONS)
        assert len(edit_failed) == 0, "Failed to apply following Filter Document options {}".format(edit_failed)
        logging.info("All Filter document options applied successfully")
        # Clean up steps
        self.fc.verify_preview_screen_and_go_home()

    def test_03_regress_filters_photo_options(self):
        """
            Apply all Filter Photo options, Save and verify results
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.select_edit_main_option(self.edit.FILTERS)
        self.edit.apply_edits(self.edit.FILTER_PHOTO, self.edit.FILTER_PHOTO_OPTIONS[4])
        del self.edit.FILTER_PHOTO_OPTIONS[0:3]
        edit_failed = self.edit.apply_and_verify_all_edit_options(self.edit.FILTERS, self.edit.FILTER_PHOTO_OPTIONS)
        assert len(edit_failed) == 0, "Failed to apply following Filter Photo options {}".format(edit_failed)
        logging.info("All Filter Photo options applied successfully")
        # Clean up steps
        self.fc.verify_preview_screen_and_go_home()

    def test_04_regress_crop_options(self):
        """
          Apply all  Crop options, Save and verify results
        """
        self.fc.go_to_edit_screen_with_camera_scan_image()
        self.edit.apply_edits(self.edit.CROP, self.edit.CROP_OPTIONS[3])
        edit_failed = self.edit.apply_and_verify_all_edit_options(self.edit.CROP, self.edit.CROP_OPTIONS)
        assert len(edit_failed) == 0, "Failed to apply following Crop options {}".format(edit_failed)
        logging.info("All Crop options applied successfully")
