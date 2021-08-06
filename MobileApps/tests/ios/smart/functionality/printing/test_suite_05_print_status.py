from time import sleep

import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

# Longer wait times in this test suite are to accommodate printing verification
class Test_Suite_05_Print_Status(object):

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
        cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])

    def test_01_verify_multi_printing_button(self):
        """
        verify multi print progress btn and cancel buttons - C25367427
        """
        # General Setup
        prev_job_id = self.get_prev_job_id_and_go_to_print_preview(no_of_photos=2)
        # Validation
        self.fc.fd["preview"].select_button(Preview.PRINT)
        # Printing times varies on every printer and need long timeout to verify print job status
        self.fc.fd["preview"].verify_printing_status_btn_changes(multi_print=True, timeout=120)
        assert self.fc.get_latest_job_status(self.p, prev_job_id, timeout=120) == 'Completed'

    def test_05_verify_print_reprint_and_done_buttons(self):
        """
        verify print, re-print and done button functionality on print preview screen-
                C17128720, C17128723, C27099491
        """
        # General Setup
        previous_job_id = self.get_prev_job_id_and_go_to_print_preview(no_of_photos=1)
        self.fc.fd["preview"].select_button(Preview.PRINT)
        # Validation
        self.fc.fd["preview"].verify_printing_status_btn_changes()
        assert self.fc.get_latest_job_status(self.p, previous_job_id, timeout=70) == 'Completed'
        newest_job_id = self.p.get_newest_job_id()
        self.fc.fd["preview"].verify_an_element_and_click(Preview.RE_PRINT_BTN)
        self.fc.fd["preview"].verify_job_sent_and_reprint_buttons_on_print_preview()
        assert self.fc.get_latest_job_status(self.p, newest_job_id, timeout=70) == 'Completed'
        self.fc.fd["preview"].verify_an_element_and_click(Preview.DONE_BUTTON)
        assert self.fc.fd["home"].verify_home_tile() is not False

    def test_06_verify_print_button_with_no_printer_added(self):
        """
         Verify Print button disabled when no printer added , add printer and print - C17128725
        """
        self.fc.go_to_home_screen()
        self.fc.remove_default_paired_printer()
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.fd["preview"].go_to_print_preview_pan_view(pan_view=False)
        assert self.fc.fd["preview"].verify_printer_name_displayed('Choose your Printer') is not False
        assert self.fc.fd["preview"].verify_button(Preview.PRINT).is_enabled() is False
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PRINTER_NAME, format_specifier=['Choose your Printer'])
        self.fc.fd["printers"].verify_printers_nav()
        self.fc.fd["printers"].select_printer_from_printer_list(self.p.get_printer_information()["ip address"])
        assert self.fc.fd["preview"].verify_printer_name_displayed(
            self.p.get_printer_information()['bonjour name']) is not False
        assert self.fc.fd["preview"].verify_button(Preview.PRINT).is_enabled() is not False
        self.fc.select_print_button_and_verify_print_job(self.p)

    def get_prev_job_id_and_go_to_print_preview(self, no_of_photos=1):
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.select_multiple_photos_to_preview(no_of_photos=no_of_photos)
        self.fc.fd["preview"].go_to_print_preview_pan_view(pan_view=False)
        return self.p.get_newest_job_id()