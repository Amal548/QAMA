import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview
from SAF.misc import saf_misc

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_02_Print_Settings_Functionality(object):

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
        cls.fc.add_printer_by_ip(printer_ip=cls.p.get_printer_information()["ip address"])

    def test_01_verify_print_copy_setting(self):
        """
        Verifies Print copy settings +, -  - C16845756
        :return:
        """
        # General Setup
        self.fc.scan_and_go_to_print_preview_pan_view(self.p)
        # Validation
        assert self.fc.fd["preview"].get_copies_btn_enabled_status(Preview.COPIES_MINUS_BTN) == "false"
        assert self.fc.fd["preview"].get_copies_btn_enabled_status(Preview.COPIES_PLUS_BTN) == "true"
        self.fc.fd["preview"].change_print_copies(Preview.COPIES_PLUS_BTN, no_of_copies=4)
        assert self.fc.fd["preview"].get_no_of_copies() == 5
        assert self.fc.fd["preview"].get_copies_btn_enabled_status(Preview.COPIES_PLUS_BTN) == "false"
        self.fc.fd["preview"].change_print_copies(Preview.COPIES_MINUS_BTN, no_of_copies=3)
        assert self.fc.fd["preview"].get_no_of_copies() == 2
        self.fc.select_print_button_and_verify_print_job(self.p)
        # Clean up
        self.fc.fd["preview"].change_print_copies(Preview.COPIES_MINUS_BTN, no_of_copies=1)
        assert self.fc.fd["preview"].get_no_of_copies() == 1

    def test_02_verify_color_options(self):
        """
        Verifies color options ui, select each option and verify its select on
          print preview pan- C16845764, C17028909, C17028907
        :return:
        """
        # General Setup
        self.fc.scan_and_go_to_print_preview_pan_view(self.p)
        # Validation
        self.fc.fd["preview"].verify_an_element_and_click(Preview.COLOR_OPTION)
        assert set(self.fc.fd["preview"].get_options_listed(Preview.PRINT_SETTING_OPTIONS)) == set(
            Preview.COLOR_OPTIONS)
        self.fc.fd["preview"].select_navigate_back()
        assert set(self.fc.select_and_get_print_option_value(Preview.COLOR_OPTION, Preview.COLOR_OPTIONS[0])) == \
               set(Preview.COLOR_OPTIONS[0])
        assert set(self.fc.select_and_get_print_option_value(Preview.COLOR_OPTION, Preview.COLOR_OPTIONS[1])) == \
               set(Preview.COLOR_OPTIONS[1])
        assert set(self.fc.select_and_get_print_option_value(Preview.COLOR_OPTION, Preview.COLOR_OPTIONS[2])) == \
               set(Preview.COLOR_OPTIONS[2])
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_03_verify_print_quality(self):
        """
        Verifies print quality options ui, select each option and verify its select on
          print preview pan- C17056241, C17056448, C17056547
        :return:
        """
        # General Setup
        self.fc.scan_and_go_to_print_preview_pan_view(self.p)
        # Validation
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PRINT_QUALITY)
        assert self.fc.fd["preview"].verify_default_option_selected(Preview.PRINT_QUALITY_OPTIONS[1]) is not False
        assert set(self.fc.fd["preview"].get_options_listed(Preview.PRINT_SETTING_OPTIONS)) == set(
            Preview.PRINT_QUALITY_OPTIONS)
        self.fc.fd["preview"].select_navigate_back()
        assert set(
            self.fc.select_and_get_print_option_value(Preview.PRINT_QUALITY, Preview.PRINT_QUALITY_OPTIONS[0])) == \
               set(Preview.PRINT_QUALITY_OPTIONS[0])
        assert set(
            self.fc.select_and_get_print_option_value(Preview.PRINT_QUALITY, Preview.PRINT_QUALITY_OPTIONS[1])) == \
               set(Preview.PRINT_QUALITY_OPTIONS[1])
        assert set(
            self.fc.select_and_get_print_option_value(Preview.PRINT_QUALITY, Preview.PRINT_QUALITY_OPTIONS[2])) == \
               set(Preview.PRINT_QUALITY_OPTIONS[2])
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_04_verify_print_2sided(self):
        """
        Verifies print 2 sided options ui, select each option and verify its selected on
          print preview pan- C17117139,C17117255, C17117283
        :return:
        """
        # General Setup
        self.fc.select_a_google_drive_file_and_go_to_print_preview()
        # Validation
        if self.fc.fd["preview"].verify_an_element_and_click(Preview.TWO_SIDED) is False:
            pytest.skip("Two Sided option is not applicable")
        assert self.fc.fd["preview"].verify_default_option_selected(Preview.TWO_SIDED_OPTIONS[1]) is not False
        assert set(self.fc.fd["preview"].get_options_listed(Preview.PRINT_SETTING_OPTIONS)) == set(
            Preview.TWO_SIDED_OPTIONS)
        self.fc.fd["preview"].select_navigate_back()
        assert set(self.fc.select_and_get_print_option_value(Preview.TWO_SIDED, Preview.TWO_SIDED_OPTIONS[0])) == \
               set(Preview.TWO_SIDED_OPTIONS[0])
        assert set(self.fc.select_and_get_print_option_value(Preview.TWO_SIDED, Preview.TWO_SIDED_OPTIONS[1])) == \
               set(Preview.TWO_SIDED_OPTIONS[1])
        assert set(self.fc.select_and_get_print_option_value(Preview.TWO_SIDED, Preview.TWO_SIDED_OPTIONS[2])) == \
               set(Preview.TWO_SIDED_OPTIONS[2])
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_05_verify_page_range_func(self):
        """
        verify page range options and functionality
        :return:
         """
        # General Setup
        self.fc.select_a_google_drive_file_and_go_to_print_preview()
        # Validation
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == 'All'
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PAGE_RANGE)
        assert self.fc.fd["preview"].get_page_range() == 'Pages 1-4'
        self.fc.fd["preview"].select_or_unselect_pages(['1', '3'])
        assert self.fc.fd["preview"].verify_pages_selected('1') is False
        assert self.fc.fd["preview"].verify_pages_selected('3') is False
        assert self.fc.fd["preview"].get_page_range() == 'Pages 2, 4'
        self.fc.fd["preview"].select_or_unselect_pages('3')
        assert self.fc.fd["preview"].verify_pages_selected('3') is not False
        assert self.fc.fd["preview"].get_page_range() == 'Pages 2-4'
        self.fc.fd["preview"].select_navigate_back()
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == '2-4'
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PAGE_RANGE)
        self.fc.fd["preview"].select_static_text(Preview.PAGE_RANGE_OPTIONS[4])
        assert self.fc.fd["preview"].verify_pages_selected('2') is False
        assert self.fc.fd["preview"].verify_pages_selected('4') is False
        self.fc.fd["preview"].select_static_text(Preview.PAGE_RANGE_OPTIONS[3])
        assert self.fc.fd["preview"].verify_static_text('Pages 1-4') is not False
        self.fc.fd["preview"].select_static_text(Preview.PAGE_RANGE_OPTIONS[5])
        assert self.fc.fd["preview"].check_manual_input_pop_up_msg(input_page_range=True) is not False
        self.fc.fd["preview"].enter_page_range('1, 3')
        self.fc.fd["preview"].select_done()
        assert self.fc.fd["preview"].verify_pages_selected('1') is not False
        assert self.fc.fd["preview"].verify_pages_selected('3') is not False
        assert self.fc.fd["preview"].verify_pages_selected('2') is False
        assert self.fc.fd["preview"].verify_pages_selected('4') is False
        assert self.fc.fd["preview"].get_page_range() == 'Pages 1, 3'
        self.fc.fd["preview"].select_navigate_back()
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == '1, 3'
        self.fc.select_print_button_and_verify_print_job(self.p)