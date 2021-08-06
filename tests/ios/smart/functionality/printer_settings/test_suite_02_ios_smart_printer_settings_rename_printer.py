from time import sleep

import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_02_Ios_Smart_Printer_Settings_Rename_Printer(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup, request, load_printers_session):

        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.ssid, cls.password = get_wifi_info(request)
        cls.printer_actual_bonjour_name = cls.p.get_printer_information()["bonjour name"]
        cls.printer_actual_direct_name = cls.p.get_wifi_direct_information()["name"]
        cls.stack = request.config.getoption("--stack")

        # Go Home
        cls.fc.go_home(stack=cls.stack)

        def clean_up_class():
            cls.p.reset_network_connection()
            cls.p.connect_to_wifi(cls.ssid, cls.password)
        request.addfinalizer(clean_up_class)

    def test_07_verify_rename_my_printer_functionality(self):
        """
        Navigate to rename my printer screen, edit printer name and verify printer name updated on
        home screen - C16798177
        """
        rename_printer = "Test Printer"
        self.rename_printer_name(PrinterSettings.PS_RENAME_MY_PRINTER, rename_printer)
        self.fc.fd["printer_settings"].select_navigate_back()
        self.fc.fd["home"].verify_home_tile(raise_e=True)
        edited_printer_name = self.fc.fd["home"].get_printer_name_from_device_carousel()
        # clean up- Reset printer name back to Bonjour name
        self.rename_printer_name(PrinterSettings.PS_RENAME_MY_PRINTER, self.printer_actual_bonjour_name)
        assert edited_printer_name == rename_printer

    def test_03_verify_bonjour_name_edit_screen(self):
        """
        Navigate to Bonjour name edit screen, verify ui elements and edit name - C16825221
        """
        new_bonjour_name = "Test Printer"
        self.rename_printer_name(PrinterSettings.NETWORK_INFO_BONJOUR_NAME, new_bonjour_name)
        edited_bonjour_name = self.fc.fd["printer_settings"].verify_title_and_get_value("Bonjour Name")
        # clean up
        self.rename_printer_name(PrinterSettings.NETWORK_INFO_BONJOUR_NAME, self.printer_actual_bonjour_name)
        self.fc.fd["printer_settings"].select_navigate_back()
        assert edited_bonjour_name == new_bonjour_name

    def test_04_verify_direct_connection_name_edit_screen(self):
        """
        Navigate to Direct Connection Name Edit screen, verify ui elements and edit name - C16825270
        """
        new_direct_name = "Direct-Test-Printer"
        self.rename_printer_name(PrinterSettings.NETWORK_INFO_DIRECT_CONNECTION_NAME, new_direct_name)
        edited_direct_name = self.fc.fd["printer_settings"].verify_title_and_get_value("Wi-Fi Direct Name")
        self.fc.fd["printer_settings"].select_navigate_back()
        assert new_direct_name in edited_direct_name

    def test_05_verify_bonjour_and_direct_name_edit_screen_ui_elements(self):
        """
        Verify Bonjour and Direct Name edit screen UI elements
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.fc.fd["printer_settings"].select_ui_option(PrinterSettings.PS_NETWORK_INFORMATION)
        self.fc.fd["printer_settings"].select_ui_option(PrinterSettings.NETWORK_INFO_BONJOUR_NAME)
        self.fc.fd["printer_settings"].verify_ui_elements(PrinterSettings.PS_RENAME_PRINTER_UI_ELEMENTS)
        assert self.driver.get_attribute(PrinterSettings.SAVE_BUTTON, attribute="enabled").lower() == "false"
        self.fc.fd["printer_settings"].select_cancel()
        self.fc.fd["printer_settings"].go_to_wi_fi_direct()
        self.fc.fd["printer_settings"].select_ui_option(PrinterSettings.NETWORK_INFO_DIRECT_CONNECTION_NAME)
        self.fc.fd["printer_settings"].verify_rename_printer_screen()
        assert self.driver.get_attribute(PrinterSettings.SAVE_BUTTON, attribute="enabled").lower() == "false"
        # clean up
        self.fc.fd["printer_settings"].select_cancel()
        self.fc.fd["printer_settings"].select_navigate_back()

    def rename_printer_name(self, element, printer_name):
        if not self.fc.fd["printer_settings"].verify_printer_settings_screen():
            self.fc.go_to_printer_settings_screen(self.p)
        if element != PrinterSettings.PS_RENAME_MY_PRINTER:
            self.fc.fd["printer_settings"].select_ui_option(PrinterSettings.PS_NETWORK_INFORMATION)
        if element == PrinterSettings.NETWORK_INFO_DIRECT_CONNECTION_NAME:
            self.fc.fd["printer_settings"].go_to_wi_fi_direct()
        if not self.fc.fd["printer_settings"].verify_ui_option_displayed(element):
            pytest.skip(element+"not displayed".format(self.printer_actual_bonjour_name))
        else:
            self.fc.fd["printer_settings"].select_ui_option(element)
            self.fc.fd["printer_settings"].verify_rename_printer_screen()
            self.fc.fd["printer_settings"].edit_printer_name_and_save(printer_name)