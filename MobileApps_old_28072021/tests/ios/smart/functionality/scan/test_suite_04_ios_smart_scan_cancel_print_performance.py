import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_04_Ios_Smart_Scan_cancel_print_performance(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.stack = request.config.getoption("--stack")
        cls.scan = cls.fc.fd["scan"]
        cls.preview = cls.fc.fd["preview"]

        # Navigating to home screen
        cls.fc.go_home(stack=cls.stack)

    def test_01_validate_scan_cancel_msg(self):
        """
         Validate message while cancelling scan job- C15077477
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.scan.verify_scanning_screen()
        self.scan.select_cancel_scanning_job()
        # Validation scanning messages
        self.fc.fd["scan"].verify_scan_canceling_msg()
        self.scan.verify_scan_button()

    def test_02_perform_multiple_scans_and_print(self):
        """
         Validate message while cancelling scan job- C15077477
        """
        page_count =10
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(no_of_pages=page_count)
        assert self.preview.get_no_pages_from_preview_label() == page_count
        # long timeout is to verify 10 pages print job completion
        self.fc.select_print_button_and_verify_print_job(self.p, timeout=500)

    def test_03_print_performance(self):
        """
          Validate Printing of 10 pages PDF
        """
        test_file = "ten_page_pdf"
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, test_file, no_of_pages=10)
        self.fc.select_a_file_and_go_to_print_preview(test_file)
        #long timeout is to verify 10 pages print job completion
        self.fc.select_print_button_and_verify_print_job(self.p, timeout=500)





