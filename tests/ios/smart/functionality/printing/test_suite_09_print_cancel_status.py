from time import sleep

import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_09_Print_Cancel_Status(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.preview = cls.fc.fd["preview"]

        # Printer variables
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])

    def test_02_verify_print_cancel_pop_up_ui(self):
        """
        verify print progress and cancel buttons - C17128721
        """
        # General Setup
        self.get_prev_job_id_and_go_to_print_preview(no_of_photos=3)
        # Validation
        self.preview.select_button(self.preview.PRINT)
        self.preview.verify_an_element_and_click(self.preview.CANCEL_BUTTON)
        self.fc.fd["preview"].verify_array_of_elements(self.preview.CANCEL_JOB_ELEMENTS)
        # Long timeout is to complete sending print job
        self.preview.verify_job_sent_and_reprint_buttons_on_print_preview(timeout=180)

    def test_03_verify_print_cancel_yes_button_functionality(self):
        """
        Select Yes on Cancel and verify printjob is cancelled and user back on preview screen
         - C25355762
        """
        # General Setup
        previous_job_id = self.get_prev_job_id_and_go_to_print_preview(no_of_photos=10)
        # Validation
        self.preview.select_button(self.preview.PRINT)
        sleep(2)
        self.preview.verify_an_element_and_click(self.preview.CANCEL_BUTTON)
        assert self.preview.verify_an_element_and_click(self.preview.YES_BTN) is not False
        self.preview.verify_printing_status_btn_changes()
        assert self.preview.verify_preview_screen_title(self.preview.PRINT_PREVIEW_TITLE) is not False
        latest_job_status = self.fc.get_latest_job_status(self.p, previous_job_id, raise_e=False)
        assert latest_job_status == 'Canceled' or latest_job_status is False

    def test_04_verify_print_cancel_no_button_functionality(self):
        """
        Select No on cancel button and verify print job is not interrupted - C25355763
        """
        # General Setup
        previous_job_id = self.get_prev_job_id_and_go_to_print_preview(no_of_photos=3)
        # Validation
        self.preview.select_button(self.preview.PRINT)
        sleep(2)
        self.preview.verify_an_element_and_click(self.preview.CANCEL_BUTTON)
        assert self.preview.verify_an_element_and_click(self.preview.NO_BTN) is not False
        # long timeout is to verify 10 pages print job completion
        self.preview.verify_printing_status_btn_changes(multi_print=True, timeout=250)
        assert self.preview.verify_preview_screen_title(self.preview.PRINT_PREVIEW_TITLE) is not False
        assert self.fc.get_latest_job_status(self.p, previous_job_id) == 'Completed'

    def get_prev_job_id_and_go_to_print_preview(self, no_of_photos=1):
        self.fc.select_multiple_photos_to_preview(no_of_photos=no_of_photos)
        self.preview.go_to_print_preview_pan_view(pan_view=False)
        return self.p.get_newest_job_id()