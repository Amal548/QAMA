from time import sleep
import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.preview import Preview
import logging

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_02_Ios_Smart_Scan_Func(object):

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
        cls.edit = cls.fc.fd["edit"]
        # Define Variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"][
            "username"]
        # Navigating to home screen
        cls.fc.go_home(stack=cls.stack)

    def test_01_validate_message_during_scan(self):
        """
         Validate scanning and scan finished messages - C15077477
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd["scan"].select_scan_job_button()
        # Validation scanning messages
        self.fc.fd["scan"].verify_scanning_messages()
        sleep(2)
        self.fc.fd["preview"].nav_detect_edges_screen()
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)

    def test_03_validate_message_during_previewing_scan(self):
        """
          Validate scanning and scan finished messages - C15077505
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd["scan"].select_preview_on_scanner_screen()
        # Validation scanning messages
        self.fc.fd["scan"].verify_scanning_messages()
        self.fc.fd["scan"].verify_preview_button_on_scan_screen()

    def test_07_verify_preview_screen_add_page_delete_page_and_back_buttons(self):
        """
        Add multi pages to preview through source scanner , verify X icon displays
        and clicking X deletes add images until last page - C15081189, C15968005
        :return:
        """
        pages_scanned = 3
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(pages_scanned)
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        assert self.fc.fd["preview"].get_no_pages_from_preview_label() == int(pages_scanned)
        assert self.fc.fd["preview"].verify_delete_page_x_icon() is not False
        self.fc.fd["preview"].select_delete_pages_in_current_job(no_of_pages_to_delete=pages_scanned)
        assert self.fc.fd["preview"].verify_delete_button() is False
        #verify navigate back button and go home
        self.fc.fd["preview"].go_home_from_preview_screen()

    def test_08_verify_printing_scanned_image(self):
        """
        Scan any file using scanner source and send the job to print and
        verify printed successfully - C16017814
        :return:
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        # Test case specific setup test conditions
        self.fc.fd["scan"].select_scan_job_button()
        self.fc.fd["preview"].nav_detect_edges_screen()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.select_print_button_and_verify_print_job(self.p)
        # Test Case clean up
        self.fc.fd["preview"].select_done()
    
    
    def test_09_verify_edit_for_scan_with_source_scanner_new(self):
        """
        C27655064 - Verify edit for multiple scanned images- new
        """
        pages_scanned = 3
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(pages_scanned)
        self.fc.go_to_edit_screen_with_selected_photo()
        adjust_option_failed = []
        self.edit.apply_edits(self.edit.ADJUST, "Brightness")
        if self.edit.verify_undo_button_enabled() != 'true':
            adjust_option_failed.append("Brightness")
        self.fc.fd["edit"].select_edit_done()
        self.fc.fd["preview"].verify_preview_screen_title(self.fc.fd["preview"].PREVIEW_TITLE)
        self.fc.select_print_button_and_verify_print_job(self.p)
        # Test Case clean up
        self.fc.fd["preview"].select_done()

