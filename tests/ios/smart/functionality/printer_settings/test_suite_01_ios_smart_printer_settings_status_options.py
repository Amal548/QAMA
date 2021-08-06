import time
import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings

pytest.app_info = "SMART"


class Test_Suite_01_Ios_Smart_Printer_Status_Options(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,  request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")

        # Define Variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"][
            "username"]

        # Navigate to home screen
        cls.fc.go_home(stack=cls.stack)
        # cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])
        # cls.fc.fd["home"].close_smart_task_awareness_popup()

    def test_01_validate_printer_status(self):
        """
        Add a printer, check printer status, navigate to status screen and back to printer settings
        C13927533 , C16770062
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.fc.fd["printer_settings"].verify_printer_status_screen('Ready')
        self.fc.fd["printer_settings"].select_navigate_back()

    def test_02_verify_printer_settings_screen_objects(self):
        """
        :return: Add printer, navigate to printer settings screen and verify options displayed
        C13927532
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.fc.fd["printer_settings"].verify_ui_elements(PrinterSettings.PS_SCREEN_OPTIONS)

    def test_03_verify_print_from_other_devices_screen(self):
        """
        Navigate to Print from other devices screen and verify UI elements, tap 123.hp.com link and navigate back
         C13927540
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.fc.fd["printer_settings"].go_to_print_from_other_devices_screen()
        self.fc.fd["printer_settings"].verify_print_from_other_device_screen_ui_elements()
        self.fc.fd['printer_settings'].go_to_123_hp_com_page_and_navigate_back()

    def test_04_verify_send_link(self):
        """
        Navigate to Print from other devices screen, tap send link, send link (email) and verify link sent screen
        C16798088
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.fc.fd["printer_settings"].go_to_print_from_other_devices_screen()
        self.fc.fd["printer_settings"].ps_select_send_link()
        self.fc.fd["share"].verify_share_popup()
        self.fc.fd["share"].select_mail()
        subject = self.fc.fd["gmail"].get_email_navigation_bar_title()
        self.fc.send_and_verify_email(from_email_id=self.email_address, to_email_id=self.email_address, subject=subject)
        self.fc.fd["printer_settings"].verify_link_sent_screen_ui_elements()
        self.fc.fd["printer_settings"].select_navigate_back()

    def test_05_verify_select_a_different_printer(self):
        """
        Navigate to select a different printer screen, select a printer and verify printer added to
        home screen printer carousel - C13927541
        """
        self.fc.go_to_home_screen()
        first_printer_name = self.fc.fd["home"].get_printer_name_from_device_carousel()
        self.fc.go_to_printer_settings_screen(self.p)
        self.fc.fd["printer_settings"].select_select_a_different_printer()
        self.fc.fd["printers"].verify_printers_nav()
        self.fc.fd["printers"].select_a_diff_printer(first_printer_name)
        self.fc.fd["printer_settings"].verify_printer_settings_screen()
        self.fc.fd["printer_settings"].select_navigate_back()
        self.fc.fd["home"].verify_home_tile(raise_e=True)
        assert self.fc.fd["home"].get_printer_name_from_device_carousel("DeviceCarouselInfo-2") != first_printer_name
        time.sleep(5)
        # Clean up
        self.fc.fd["home"].remove_printer_by_forget_printer_option()

    def test_06_verify_rename_my_printer_ui_elements(self):
        """
        Navigate to rename my printer screen, verify ui elements - C13927543
        """
        self.fc.go_to_printer_settings_screen(self.p)
        if not self.fc.fd["printer_settings"].verify_ui_option_displayed(PrinterSettings.PS_RENAME_MY_PRINTER):
            pytest.skip("Rename Printer not displayed".format(self.p.get_printer_information()["bonjour name"]))
        else:
            self.fc.fd["printer_settings"].select_ui_option(PrinterSettings.PS_RENAME_MY_PRINTER)
            self.fc.fd["printer_settings"].verify_ui_elements(PrinterSettings.PS_RENAME_PRINTER_UI_ELEMENTS)
            assert self.driver.get_attribute(PrinterSettings.SAVE_BUTTON, attribute="enabled").lower() == "false"
            self.fc.fd["printer_settings"].select_navigate_back()

