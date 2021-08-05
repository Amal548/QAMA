import pytest
import logging
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.flows.android.smart.flow_container as smart_flowcontainer
import MobileApps.libs.flows.android.hpps.flow_container as hpps_flowcontainer
from MobileApps.libs.flows.android.wprint_test.wprint_test import WPrintTest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *

pytest.app_info = "WPRINT_TEST"


class Test_Suite_HPPS_wprint_remote_print_test(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup, load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup
        self.wprint_test = WPrintTest(self.driver)

        # Initializing Smart Flows
        self.smart_fc = smart_flowcontainer.FlowContainer(self.driver)

        # Wifi variables
        self.default_wifi_ssid = ma_misc.load_system_config_file()["default_wifi"]["ssid"]
        self.default_wifi_pwd = ma_misc.load_system_config_file()["default_wifi"]["passwd"]
        self.secondary_wifi_ssid = ma_misc.load_system_config_file()["secondary_wifi"]["ssid"]
        self.secondary_wifi_pwd = ma_misc.load_system_config_file()["secondary_wifi"]["passwd"]

        # Initializing printer
        self.sys_config = ma_misc.load_system_config_file()
        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()
        self.p.connect_to_wifi(self.default_wifi_ssid, self.default_wifi_pwd)

        # Define HPID variables
        self.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_03"][
            "username"]
        self.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_03"][
            "password"]

        # launch to HP Smart and sign in, Once it is logged in, HPPS will receive a token and do token exchange
        self.smart_fc.flow_load_home_screen()
        self.smart_fc.flow_app_settings_sign_in_hpid(self.hpid_username, self.hpid_pwd)
        self.smart_fc.select_back()

        # Change printer wifi
        self.change_wifi =self.p.connect_to_wifi(self.secondary_wifi_ssid, self.secondary_wifi_pwd)

    def test_01_wprint_test_app_remote_print_document_system_ui(self):
        """
         Description:
           Note: Register printer to HPConnect cloud before we run the tests
           1. Launch HP Smart and go to Home screen
           2. Click on App Settings in More Option menu
           3. Click on Sign In button
           4. Sign to the target account
           5. Go to Android Settings -> Wifi to change Wifi network
           6. Launch WprintTestApp
           7. Click on "PRINT DOCUMENT VIA PRINT SYSTEM"
           8. Click on "all printers"
           9. Click on "Search" box and search the remote printer
           10. Select a remote printer
           11. Click the print button once the preview and print button displayed
           12. Enable HPPS and send the printing job
           13. Open android notifications from the notification drawer
           14. Select the Print notification and check the results

         Expected Result:
           Verify if printing job is success or not
         """
        self.wprint_test.open_wprint_test()
        self.wprint_test.select_print_document_via_print_system()
        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.flow["system_ui"].select_all_printers()
        self.fc.flow["all_printer"].select_search()
        self.fc.flow["all_printer"].search_remote_printer()
        self.fc.flow["system_ui"].select_remote_printer()
        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.set_printer_options_in_system_ui()
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)

    def test_02_wprint_test_app_remote_print_photo_system_ui(self):
        """
         Description:
           Note: Register printer to HPConnect cloud before we run the tests
           1. Launch HP Smart and go to Home screen
           2. Click on App Settings in More Option menu
           3. Click on Sign In button
           4. Sign to the target account
           5. Go to Android Settings -> Wifi to change Wifi network
           6. Launch WprintTestApp
           7. Click on "PRINT PHOTO VIA PRINT SYSTEM"
           8. Click on "all printers"
           9. Click on "Search" box and search the remote printer
           10. Select a remote printer
           11. Click the print button once the preview and print button displayed
           12. Enable HPPS and send the printing job
           13. Open android notifications from the notification drawer
           14. Select the Print notification and check the results

         Expected Result:
           Verify if printing job is success or not
         """
        self.wprint_test.open_wprint_test()
        self.wprint_test.select_print_photo_via_print_system()
        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.flow["system_ui"].select_all_printers()
        self.fc.flow["all_printer"].select_search()
        self.fc.flow["all_printer"].search_remote_printer()
        self.fc.flow["system_ui"].select_remote_printer()
        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.set_printer_options_in_system_ui()
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)

    def test_03_wprint_test_app_remote_print_document_backdoor(self):
        """
         Description:
           Note: Register printer to HPConnect cloud before we run the tests
           1. Launch HP Smart and go to Home screen
           2. Click on App Settings in More Option menu
           3. Click on Sign In button
           4. Sign to the target account
           5. Go to Android Settings -> Wifi to change Wifi network
           6. Launch WprintTestApp
           7. Click on "PRINT DOCUMENT VIA BACKDOOR"
           8. Click on "Search" box and search the remote printer
           9. Select a remote printer
           10. Click the print button once the preview and print button displayed
           11. Enable HPPS and send the printing job
           12. Open android notifications from the notification drawer
           13. Select the Print notification and check the results

         Expected Result:
           Verify if printing job is success or not
         """
        self.wprint_test.open_wprint_test()
        self.wprint_test.select_print_document_via_backdoor()
        self.fc.flow["trap_door"].verify_search_printer_screen()
        self.fc.flow["trap_door"].select_search()
        self.fc.flow["all_printer"].search_remote_printer()
        self.fc.flow["trap_door"].select_remote_printer()
        self.fc.flow["trap_door"].verify_remote_preview_screen_with_print_button()
        self.fc.set_printer_options_in_system_ui()
        self.fc.flow["trap_door"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()
        self.fc.flow["trap_door"].select_print()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)

    def test_04_wprint_test_app_remote_print_photo_backdoor(self):
        """
         Description:
           Note: Register printer to HPConnect cloud before we run the tests
           1. Launch HP Smart and go to Home screen
           2. Click on App Settings in More Option menu
           3. Click on Sign In button
           4. Sign to the target account
           5. Go to Android Settings -> Wifi to change Wifi network
           6. Launch WprintTestApp
           7. Click on "PRINT PHOTO VIA BACKDOOR"
           8. Click on "Search" box and search the remote printer
           9. Select a remote printer
           10. Click the print button once the preview and print button displayed
           11. Enable HPPS and send the printing job
           12. Open android notifications from the notification drawer
           13. Select the Print notification and check the results

         Expected Result:
           Verify if printing job is success or not
         """
        self.wprint_test.open_wprint_test()
        self.wprint_test.select_print_photo_via_backdoor()
        self.fc.flow["trap_door"].verify_search_printer_screen()
        self.fc.flow["trap_door"].select_search()
        self.fc.flow["all_printer"].search_remote_printer()
        self.fc.flow["trap_door"].select_remote_printer()
        self.fc.flow["trap_door"].verify_remote_preview_screen_with_print_button()
        self.fc.set_printer_options_in_system_ui()
        self.fc.flow["trap_door"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()
        self.fc.flow["trap_door"].select_print()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)