import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings

pytest.app_info = "SMART"

class Test_Suite_04_Ios_Smart_Printer_Settings_Tools(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")

        # Navigate to Home screen
        cls.fc.go_home(stack=cls.stack)

    def test_01_verify_printer_reports_ui_elements(self):
        """
           Navigate to printer reports screen and verify UI Elements - C13927547
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.fc.fd["printer_settings"].select_ui_option(PrinterSettings.PS_PRINTER_REPORTS)
        self.fc.fd["printer_settings"].verify_ui_elements(PrinterSettings.PRINTER_REPORTS_UI_ELEMENTS,
                                                          PrinterSettings.PRINT_BUTTON)
        self.fc.fd["printer_settings"].select_navigate_back()

    def test_02_verify_print_quality_tools_ui_elements(self):
        """
           Navigate to printer reports screen and verify UI Elements - C13927548
        """
        self.fc.go_to_printer_settings_screen(self.p)
        self.fc.fd["printer_settings"].select_ui_option(PrinterSettings.PS_PRINT_QUALITY_TOOLS)
        self.fc.fd["printer_settings"].verify_ui_elements(PrinterSettings.PQ_TOOLS_CLEAN_PRINTHEAD,
                                                          PrinterSettings.PQ_TOOLS_CLEAN_BUTTON)
        self.fc.fd["printer_settings"].verify_ui_elements(PrinterSettings.PQ_TOOLS_ALIGN_PRINTER,
                                                          PrinterSettings.PQ_TOOLS_ALIGN_BUTTON)