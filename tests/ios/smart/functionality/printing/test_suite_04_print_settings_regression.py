import logging

import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_04_Print_Settings_Regression(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")

        # Printer variables
        cls.fc.go_home(stack=cls.stack)
        cls.file_name = "test_reg_file_2"
        cls.fc.scan_and_save_file_in_hp_smart_files(cls.p, cls.file_name, no_of_pages=4)

    def test_01_verify_print_color_options(self):
        """
        Verifies print quality options, select each option and verify its select on
          print preview pan-
        :return:
        """
        # General Setup
        self.fc.scan_and_go_to_print_preview_pan_view(self.p)
        color_option_failed = self.select_and_verify_each_print_option(Preview.COLOR_OPTION, Preview.COLOR_OPTIONS)
        assert len(color_option_failed) == 0, "Failed to selected following color options {}".format(
            color_option_failed)
        logging.info("All color options selected successfully")
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_02_verify_print_quality_options(self):
        """
        Verifies print quality options, select each option and verify its select on
          print preview pan-
        :return:
        """
        # # General Setup
        self.fc.scan_and_go_to_print_preview_pan_view(self.p)
        print_quality_options_failed = self.select_and_verify_each_print_option(Preview.PRINT_QUALITY,
                                                                                Preview.PRINT_QUALITY_OPTIONS)
        assert len(print_quality_options_failed) == 0, "Failed to selected following color options {}".format(
            print_quality_options_failed)
        logging.info("All print quality options selected successfully")
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_03_verify_print_2sided_options(self):
        """
        Verifies print 2 sided options, select each option and verify its select on
          print preview pan-
        :return:
        """
        # General Setup
        self.fc.select_a_file_and_go_to_print_preview(self.file_name)
        if self.fc.fd["preview"].verify_an_element_and_click(Preview.TWO_SIDED, click=False) is False:
            pytest.skip("Two Sided option is not applicable")
        two_sided_options_failed = self.select_and_verify_each_print_option(Preview.TWO_SIDED,
                                                                            Preview.TWO_SIDED_OPTIONS)
        assert len(two_sided_options_failed) == 0, "Failed to selected following color options {}".format(
            two_sided_options_failed)
        logging.info("All 2sided options selected successfully")
        self.fc.select_print_button_and_verify_print_job(self.p)

    def select_and_verify_each_print_option(self, print_feature_option, options_list):
        option_selection_failed = []
        for option in options_list:
            selected_option = self.fc.select_and_get_print_option_value(print_feature_option, option)
            if selected_option != option:
                option_selection_failed.append(option)
        return option_selection_failed
