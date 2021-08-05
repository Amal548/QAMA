from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from networkcfg.connectionInfo import Adapter
import time

pytest.app_info = "SMART"

class Test_Suite_01_GA_PrinterLists(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]

        # Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress
        cls.wifi_direct_wrong_pwd = "11111111"

    def test_01_ga_printer_list(self):
        """
        Steps:
        - Launch HP Smart
        - Verify Home screen with big "+" on printer area
        - Click on big "+" button
        - Verify Printer screen
        - Click on Search button
        - Verify Printer list searching screen
        - Click on back button on left  top
        - Click on +Add Printer
        - Verify Search Printers? screen
        - Click on Continue button
        - Verify Permission screen
        - Click on Allow button on App Permission popup
        - Verify No Setup Model Printer found screen
        - Click on My Printer is not listed button
        - Verify Setup printer screen
        - Click on device back button
        - Verify No Setup Mode printer found screen
        - Click on back button on left top
        - Verify Printers screen
        - Click on Looking for Wi-Fi Direct screen
        - Verify Wi-Fi Direct printer screen
        - Select any Wi-Fi Direct printer
        - Verify Wi-Fi Direct printer connect screen
        - Click on Connect to the printer button
        - Verify Wi-Fi Direct printer connect password screen
        - Click on Connect button with wrong password
        - Verify Wi-Fi Direct printer connect screen with incorrect password
        - Click on Connect button with correct password
        - Verify Home screen with connected printer
        - Click on top "+" icon on Navigation bar
        - Verify Printers screen
        - Click on Looking for Wi-Fi Direct Printers
        - Verify Wi-Fi Direct printer screen
        - Select the Wi-Fi Direct printer connected before
        - Verify Wi-Fi Direct printer connected successful screen
        """
        self.p.toggle_wifi_direct(on=True)
        wifi_direct_name = Adapter('wifi1', self.p.p_con).Ssid()  # WiFi Direct name of printer
        wifi_direct_pwd = Adapter('wifi1', self.p.p_con).Passcode  # WiFi Direct pwd of printer
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer()
        self.home.select_big_add_icon()
        self.printers.verify_printers_screen()
        self.printers.select_search_icon()
        self.printers.verify_search_printers_screen()
        self.fc.select_back()
        self.printers.select_add()
        self.printers.dismiss_search_for_printers_popup(ga=True)
        self.printers.verify_add_printers_list(is_empty=True)
        self.printers.select_my_printer_is_not_listed()
        self.printers.verify_setup_printers_instruction_screen()
        self.driver.press_key_back()
        self.printers.verify_add_printers_list(is_empty=True)
        self.fc.select_back()
        self.printers.verify_printers_screen()

        # GA events tracking for WiFi Direct printers
        self.printers.select_looking_for_wifi_direct_printers()
        self.printers.verify_wifi_direct_printers_screen()
        self.printers.select_printer(wifi_direct_name, wifi_direct=True)
        self.printers.verify_connect_printers_wifi_direct_screen(is_disconnect=False)
        self.printers.select_connect_to_the_printer()
        self.printers.verify_setup_authentication_screen()
        self.printers.connect_to_wifi_direct_printer(self.wifi_direct_wrong_pwd)
        time.sleep(30)
        self.printers.verify_visible_wifi_direct_wrong_pwd_txt()
        self.printers.connect_to_wifi_direct_printer(wifi_direct_pwd)
        time.sleep(5)
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()
        self.home.select_nav_add_icon()
        self.printers.verify_printers_screen()
        self.printers.select_looking_for_wifi_direct_printers()
        self.printers.verify_wifi_direct_printers_screen()
        self.printers.select_printer(wifi_direct_name, wifi_direct=True)
        self.printers.verify_connect_printers_wifi_direct_screen(is_disconnect=True)