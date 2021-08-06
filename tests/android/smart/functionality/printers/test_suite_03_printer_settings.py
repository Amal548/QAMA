from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import PACKAGE
import pytest
import time
from SPL.driver.reg_printer import PrinterNotReady


pytest.app_info = "SMART"

class Test_Suite_03_Printer_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]

        # Define the variable
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]

    def test_01_printer_settings_ui(self):
        """
        Description:
         1. Load Home screen
         2. Click on Add icon to access printers list
         3. Select a target printer
         4. Click on Printer Settings tile or icon from navigation bar on Home screen

        Expected Result:
         4. Verify Printer Settings screen with below points:
            + Title (Printer Bonjour name)
            + Printer Status
        """
        self.__load_printer_settings_screen()
        self.printer_settings.verify_my_printer(self.p.get_printer_information()["bonjour name"])

    def test_02_printer_print_anywhere(self):
        """
        Description:
         1. Load Home screen without use onbaording login
         2. CLick on Add icon to access printers list
         3. Select a target printer

        Expected Result:
         3. Print Anywhere should be disappear
        """
        self.__load_printer_settings_screen()
        self.printer_settings.verify_printer_settings_items(self.printer_settings.PRINT_ANYWHERE, invisible=True)

    def test_03_printer_settings_print_from_other_device(self):
        """
        Description:
         1. Load Printer Settings screen
         2. Click on Print from other device

        Expected Result:
         2. Verify Print from other device screen
        """
        self.__load_printer_settings_opt(self.printer_settings.PRINT_FROM_OTHER_DEVICES)
        self.printer_settings.verify_print_from_other_devices_screen()

    def test_04_printer_settings_supported_supplies(self):
        """
        Description:
         1. Load Printer Settings screen
         2. Click on Supported Supplies

        Expected Result:
         2. Verify if browser popup or not
        """
        self.__load_printer_settings_opt(self.printer_settings.SUPPORTED_CARTRIDGES)
        self.printer_settings.verify_supported_supplies_webview()

    @pytest.mark.parametrize("item_name", ["printer_display_lights", "tray_and_paper", "quiet_mode", "print_quality_tools"])
    def test_05_printer_settings_preferences_by_opt(self, item_name):
        """
         Description:
         1. Load Printer Settings screen
         2. Click on below items under Preference one by one: (Depends on Printer we connect to, some printers doesn't support all below items )
            + Naples / Naples Plus/ Naples Super doesn't have mobile EWS page, so this test cases for all printers except Naples/Plus/Super
            + Printer Display Lights
            + Tray and Paper
            + Quiet Mode
        Or Click below items on Printer Settings screen (If Printer doesn't support this item, then won't display on App)
            + Print Quality Tools

        Expected Result:
         2. Verify each item screen popup in browser
        """
        items_name = {"printer_display_lights": [self.printer_settings.PRINTER_DISPLAY_LIGHTS, "pgDisplaySettings"],
                      "tray_and_paper": [self.printer_settings.TRAY_PAPER, ["pgTrayAndPaperMgmt", "pgSimpleTrayMgmt"]],
                      "quiet_mode": [self.printer_settings.QUIET_MODE, "pgQuietMode"],
                      "print_quality_tools": [self.printer_settings.PRINT_QUALITY_TOOLS, "pgDevServ"]
                      }
        current_printer_name = self.printer_name[0:self.printer_name.rfind("[")]
        if not self.p.get_ews_supported_pages(raise_e=False):
            pytest.skip("skip test this item since {} printer doesn't support mobile version EWS".format(current_printer_name))
        else:
            items_from_printer = self.p.get_ews_supported_pages()
            if item_name == "tray_and_paper":
                in_printer = any(item in items_from_printer for item in items_name[item_name][1])
            else:
                in_printer = items_name[item_name][1] in items_from_printer
            self.__load_printer_settings_screen()
            if self.printer_settings.verify_printer_settings_items(items_name[item_name][0], invisible=True, raise_e=False):
                pytest.skip("skip test this item since {} printer doesn't support mobile version EWS".format(items_name[item_name][0]))
            else:
                if not in_printer:
                    raise AssertionError("item in app {} is mismatch with item in printer {}".format(items_name[item_name][0], in_printer))
                self.printer_settings.select_printer_setting_opt(items_name[item_name][0])
                time.sleep(10)
                assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    @pytest.mark.parametrize("report_name",["printer_status", "demo_page", "network_configuration", "print_quality_report", "wireless_test_report", "web_access_report"])
    def test_06_printer_settings_printer_report_by_name(self, report_name):
        """
         Description:
         1. Load Printer Settings screen
         2. Click on Printer Reports
         3. Click on report by name one by one:
            PRINTER_STATUS_REPORT
            NETWORK CONFIGURATION REPORT
            PRINT QUALITY REPORT
            WIRELESS REPORT
            WEB ACCESS REPORT

        Expected Result:
         2. Verify Printer Reports screen
         3. Verify a print job is on the printer
        :param report_name:
        """
        reports_name = {"printer_status": [self.printer_settings.REPORT_PRINTER_STATUS, "configurationPage"],
                        "demo_page": [self.printer_settings.REPORT_DEMO_PAGE, "demoPage"],
                        "network_configuration": [self.printer_settings.REPORT_NETWORK_CONFIG, "networkDiagnosticPage"],
                        "print_quality_report": [self.printer_settings.REPORT_PRINT_QUALITY, "pqDiagnosticsPage"],
                        "wireless_test_report": [self.printer_settings.REPORT_WIRELESS_TEST, "wirelessNetworkPage"],
                        "web_access_report": [self.printer_settings.REPORT_WEB_ACCESS, "webAccessReport"]
                        }
        reports_from_printer = self.p.get_printer_supported_reports()
        report_in_printer = reports_name[report_name][1] in reports_from_printer
        self.__load_printer_settings_opt(self.printer_settings.PRINTER_REPORTS)
        report_in_app = self.printer_settings.verify_printer_report_by_name(reports_name[report_name][0], raise_e=False)
        current_job_id = self.p.get_newest_job_id()
        if bool(report_in_app) != report_in_printer:
            raise AssertionError("{} on app is mismatch with {} on printer".format(report_in_app, report_in_printer))
        elif not bool(report_in_app) and not report_in_printer:
            pytest.skip("skip test this item, printer doesn't support this report {}".format(reports_name[report_name][0]))
        else:
            self.printer_settings.select_printer_reports_report_btn(reports_name[report_name][0])
            self.printer_settings.verify_printer_report_by_name(reports_name[report_name][0])

    def test_07_printer_settings_advanced_settings(self):
        """
        Description:
         1. Load Printer Settings screen
         2. Click on Advanced Settings item

        Expected Result:
         2. Should be open a page with the browser
        """
        current_printer_name = self.printer_name[0:self.printer_name.rfind("[")]
        in_link = bool (self.p.get_ews_supported_pages(raise_e=False))
        self.__load_printer_settings_screen()
        in_app = self.printer_settings.verify_printer_settings_items(self.printer_settings.ADVANCED_SETTINGS, invisible=False, raise_e=False)
        if not in_link and not in_app:
            pytest.skip("skip test this item since {} printer doesn't support advanced settings option".format(current_printer_name))
        elif in_link != in_app:
            raise AssertionError("Advanced Settings should be displayed on screen")
        else:
            self.printer_settings.select_printer_setting_opt(self.printer_settings.ADVANCED_SETTINGS)
            assert(self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_printer_settings_screen(self):
        """
        - Load Home screen.
        - click on big + button if no printer connected before,
              otherwise clicking on small "+" button on Home screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        self.fc.flow_home_verify_ready_printer(self.p.get_printer_information()["bonjour name"])
        self.home.load_printer_info()

    def __load_printer_settings_opt(self, opt):
        """
        - Load to Printer Settings screen.
        - click on the each item from printer settings screen
        :param opt:
        """
        self.__load_printer_settings_screen()
        self.printer_settings.select_printer_setting_opt(opt=opt)