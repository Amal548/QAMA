from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import *
from networkcfg.connectionInfo import Adapter
import pytest
from selenium.common.exceptions import TimeoutException
import time
import logging

pytest.app_info = "SMART"

class Test_Suite_01_GA_Moobe(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup,load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.moobe_awc = cls.fc.flow[FLOW_NAMES.MOOBE_AWC]
        cls.moobe_ows = cls.fc.flow[FLOW_NAMES.MOOBE_OWS]
        cls.moobe_setup_complete = cls.fc.flow[FLOW_NAMES.MOOBE_SETUP_COMPLETE]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]

        # Define variables
        cls.system_cfg = ma_misc.load_system_config_file()
        cls.ssid = pytest.config.getoption("--wifi-ssid") if pytest.config.getoption("--wifi-ssid") else \
            cls.system_cfg["default_wifi"]["ssid"]
        cls.password = pytest.config.getoption("--wifi-pass") if pytest.config.getoption("--wifi-pass") else \
            cls.system_cfg["default_wifi"]["passwd"]

    def test_01_ga_moobe(self):
        """
        Steps:
        - Launch HP Smart
        - Verify Home screen with big "+" on printer area
        - Click on big "+" icon button
        - Verify Printers screen
        - Click on +Add Printer button
        - Verify Search from printer? popup
        - Click on Continue button of popup
        - Allow App Permission permission for location of device if it displays
        - If Add Printer screen display message no printer, then verify Add Printer screen with no printer
        - Verify Add Printer with a beacoming printer
        - Click on beacoming printer on Add Printer screen
        - Verify Connect Printer to Wi-Fi
        - Click on Need Password help? link button
        - Verify Network Password Help popup
        - Click on OK button of the popup
        - Click on "i" icon button on right top screen
        - Verify Connect Printer to Wi-Fi popup
        - Click on Done button of the popup
        - Click on Change Network link button
        - Verify Change Network or Printer popup
        - Press Back button of device
        - Enter valid password to text field, then click on Continue button
        - Verify "Finding the printer...." or "Printer found" screen
        - Verify "Preparing the printer" with substring "Starting printer setup..."
        - Verify "Preparing the printer" with substring "Accessing the network..."
        - Verify "Obtaining IP address" or "Obtained IP Address" screen
        - Verify Connected to Wi-FI screen display start measuring time
        - Click on Continue button
        - Verify "Checking printer status" screen
        - Verify first page of OWS screen display
        - Click on Back button
        - Verify "Are you sure?" popup
        - Click on Yes button of this popup
        - CLick on Skip button from three dot icon
        - Verify Print from other devices screen
        - Click on Send Link button
        - Verify Send Via popup
        - Click on Gmail
        - Press Back button until Share sent screen popup
        - Verify Share Printer sent screen
        - Click on Share Again button
        - Verify Send via popup
        - Press Back key of mobile device
        - Verify Share printer sent screen
        - Click on Done button
        - Verify Setup complete-Let's print! screen
        - Click on Not Now button
        - Verify Home screen with a connected printer
        """
        # Set printer to OOBE mode
        self.p.printer_setup_for_moobe(ignore_usb=True)
        self.p.set_mech_mode()
        self.p.fake_unsleep_mode()

        #Start MOOBE Process
        moobe_ssid = Adapter("wifi1", self.p.p_con).Ssid()  # moobe name of printer
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer()
        self.home.select_big_add_icon()
        self.printers.verify_printers_screen()
        self.printers.select_add()
        self.printers.dismiss_search_for_printers_popup(ga=True)
        self.printers.verify_add_printers_list(is_empty=False)
        #Starting Timer counting function when select a printer in setup mode
        self.printers.select_oobe_printer(moobe_ssid)

        # Start MOOBE AWC process
        self.moobe_awc.verify_connect_printer_to_wifi_screen(printer_ssid=self.ssid)
        self.moobe_awc.select_need_pwd_help_btn()
        self.moobe_awc.verify_need_pwd_help_screen()
        self.moobe_awc.select_ok_btn()
        self.moobe_awc.select_info_btn()
        self.moobe_awc.verify_connect_printer_to_wifi_info_screen()
        self.moobe_awc.select_done_btn()
        self.moobe_awc.select_change_network_btn()
        self.moobe_awc.verify_change_network_or_printer_screen()
        self.driver.press_key_back()
        if not self.moobe_awc.is_correct_network_ssid(self.ssid):
            raise TimeoutException("The displayed network's ssid is not u'{}'".format(self.ssid))
        self.moobe_awc.enter_network_password(self.password)
        self.moobe_awc.select_continue(ga=True)
        self.moobe_awc.verify_connecting_screen()
        self.moobe_awc.verify_invisible_connecting_screen()
        try:
            self.moobe_awc.verify_wrong_password_popup()
            self.moobe_awc.reenter_network_password(self.password)
            self.moobe_awc.verify_connecting_screen()
            self.moobe_awc.verify_invisible_connecting_screen()
        except TimeoutException:
            logging.info("Wrong Password popup does not display")
        #Stop Timer counting when user get to Connect Sussess screen (/moobe/connect/success)
        self.moobe_awc.verify_printer_connected_to_wifi_screen(printer_name=moobe_ssid)
        self.moobe_awc.select_continue(ga=False)
        # Start MOOBE OWS
        self.moobe_ows.verify_checking_printer_status_screen()
        self.moobe_ows.verify_invisible_checking_printer_status_screen()
        self.moobe_ows.select_more_option_icon()
        self.moobe_ows.select_skip_btn()
        self.moobe_ows.verify_are_you_sure_popup()
        self.moobe_ows.select_yes_btn()
        self.moobe_ows.select_more_option_icon()
        self.moobe_ows.select_skip_btn()
        self.moobe_ows.verify_are_you_sure_popup()
        self.moobe_ows.select_yes_btn()
        time.sleep(3)
        # Start Moobe Setup Complete
        self.moobe_setup_complete.verify_print_other_devices_screen()
        self.moobe_setup_complete.select_send_link()
        self.moobe_setup_complete.verify_send_via_popup()
        self.moobe_setup_complete.select_gmail_icon()
        self.driver.press_key_back()
        self.moobe_setup_complete.verify_link_sent_screen()
        self.moobe_setup_complete.select_send_another_link_btn()
        self.moobe_setup_complete.verify_send_via_popup()
        self.driver.press_key_back()
        self.moobe_setup_complete.verify_link_sent_screen()
        self.moobe_setup_complete.select_done_btn()
        self.moobe_setup_complete.verify_setup_complete_screen()
        self.moobe_setup_complete.select_setup_complete_not_now()
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()