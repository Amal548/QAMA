import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_03_Print_Settings_Page_Range_Func(object):

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

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        # General Setup
        self.fc.select_a_google_drive_file_and_go_to_print_preview()

    def test_03_verify_page_range_selection(self):
        """
        verify selection/unselection of pages in page range screen- C16932518, C16932517
        :return:
         """
        # Validation
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == 'All'
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PAGE_RANGE)
        assert self.fc.fd["preview"].get_page_range() == 'Pages 1-4'
        assert self.fc.fd["preview"].verify_pages_selected('1') is not False
        assert self.fc.fd["preview"].verify_pages_selected('3') is not False
        self.fc.fd["preview"].select_or_unselect_pages(['1', '3'])
        assert self.fc.fd["preview"].verify_pages_selected('1') is False
        assert self.fc.fd["preview"].verify_pages_selected('3') is False
        assert self.fc.fd["preview"].get_page_range() == 'Pages 2, 4'
        self.fc.fd["preview"].select_or_unselect_pages('3')
        assert self.fc.fd["preview"].verify_pages_selected('3') is not False
        assert self.fc.fd["preview"].get_page_range() == 'Pages 2-4'
        self.fc.fd["preview"].select_navigate_back()
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == '2-4'
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_04_verify_page_range_select_all_option(self):
        """
        verify selection/unselection of pages in page range screen- C16932519
        :return:
         """
        # Validation
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == 'All'
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PAGE_RANGE)
        assert self.fc.fd["preview"].get_page_range() == 'Pages 1-4'
        self.fc.fd["preview"].select_or_unselect_pages(['2', '4'])
        assert self.fc.fd["preview"].verify_pages_selected('2') is False
        assert self.fc.fd["preview"].verify_pages_selected('4') is False
        assert self.fc.fd["preview"].get_page_range() == 'Pages 1, 3'
        self.fc.fd["preview"].select_static_text(Preview.PAGE_RANGE_OPTIONS[3])
        assert self.fc.fd["preview"].verify_pages_selected('1') is not False
        assert self.fc.fd["preview"].verify_pages_selected('3') is not False
        assert self.fc.fd["preview"].get_page_range() == 'Pages 1-4'
        self.fc.fd["preview"].select_navigate_back()
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == 'All'

    def test_05_verify_page_range_deselect_all_option(self):
        """
        verify deselect all of pages in page range screen- C16932520
        :return:
         """
        # Validation
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == 'All'
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PAGE_RANGE)
        assert self.fc.fd["preview"].verify_static_text('Pages 1-4') is not False
        self.fc.fd["preview"].select_static_text(Preview.PAGE_RANGE_OPTIONS[4])
        assert self.fc.fd["preview"].verify_pages_selected('1') is False
        assert self.fc.fd["preview"].verify_pages_selected('3') is False
        assert self.fc.fd["preview"].verify_static_text('Pages 1-4') is False
        self.fc.fd["preview"].select_navigate_back()
        assert self.fc.fd["preview"].check_manual_input_pop_up_msg() is not False
        self.fc.fd["preview"].select_ok()

    def test_06_verify_page_range_manual_input_option(self):
        """
        verify selection/unselection of pages in page range screen- C16932521
        :return:
         """
        # Validation
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == 'All'
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PAGE_RANGE)
        assert self.fc.fd["preview"].get_page_range() == 'Pages 1-4'
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

    def test_07_verify_invalid_manual_input(self):
        """
        verify selection/unselection of pages in page range screen- C16932522
        :return:
         """
        # Validation
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PAGE_RANGE)
        assert self.fc.fd["preview"].get_page_range() == 'Pages 1-4'
        self.fc.fd["preview"].select_static_text(Preview.PAGE_RANGE_OPTIONS[5])
        assert self.fc.fd["preview"].check_manual_input_pop_up_msg(input_page_range=True) is not False
        self.fc.fd["preview"].enter_page_range('5')
        self.fc.fd["preview"].select_done()
        assert self.fc.fd["preview"].check_manual_input_pop_up_msg() is not False
        self.fc.fd["preview"].select_ok()
        assert self.fc.fd["preview"].check_manual_input_pop_up_msg(input_page_range=True) is not False
        self.fc.fd["preview"].select_cancel()
        assert self.fc.fd["preview"].check_manual_input_pop_up_msg(input_page_range=True) is False
        assert self.fc.fd["preview"].get_page_range() == 'Pages 1-4'
        self.fc.fd["preview"].select_navigate_back()