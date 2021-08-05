#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: Test script for OOBE error conditions while computer is on WiFi.
Precondition:
1.Connect Computer to a 5GHz WiFi network
2.OOBE reset the printer, ink and paper removed prior to test. Make sure the printer SSID name shown has "SETUP" word in it.
3.Make sure the test printer only support 2.4GHz network.
4.Enter OOBE via any 1 of the OOBE entries.

@author: Ivan
@create_date: Aug 27, 2019
'''

import logging
import pytest

from MobileApps.libs.flows.mac.system.screens.system_preferences import SystemPreferences
from MobileApps.libs.flows.mac.smart.screens.oobe.initialize_page import InitializePage
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_connection_page import ChooseConnectionPage
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.wifi_network_problem_dialog import WiFiNetworkProblemDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_printer_to_wifi import ConnectPrintertoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_printer_help_dialog import ConnectPrinterHelpDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.select_wifi_network_dialog import SelectaWiFiNetworkDialog

pytest.app_info = "SMART"


class Test_Suite_11_OOBE_Error_WiFi_5G_Network(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.starting_up = InitializePage(self.driver)
        self.select_a_printer = SelectAPrinter(self.driver)
        self.wifi_network_problem_dialog = WiFiNetworkProblemDialog(self.driver)
        self.we_found_your_printer = WeFoundYourPrinter(self.driver)
        self.connect_printer_to_wifi = ConnectPrintertoWiFi(self.driver)
        self.choose_connection_page = ChooseConnectionPage(self.driver)
        self.network_page = SystemPreferences(self.driver)
        self.printer_name = "HP ENVY 7640 series"
        self.printer_name_2 = "HP ENVY 7800 series"

    def test_01_check_wifi_network_problem_dialog(self):
        '''
        TestRail: #C12701204
        Check WiFi Network Problem dialog, verify functionality.
        '''
        logging.debug("test_01_check_wifi_network_problem_dialog")

        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.common_flows.set_up_a_new_printer_menu_bar()
        self.starting_up.wait_for_initialize_page_load()

        if(self.select_a_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify select a printer screen displays if multiple network/USB printers are found.")
            self.select_a_printer.click_to_selected_printer(self.printer_name)
        elif(self.we_found_your_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify we found your printer screen displays if only one network/USB printer is found.")
            self.we_found_your_printer.verify_ui_string()
            self.we_found_your_printer.click_continue_btn()

        # TestRail: C12797888 C12797900
        self.wifi_network_problem_dialog.wait_for_screen_load()
        self.wifi_network_problem_dialog.verify_wifi_network_problem_ui_string()

    def test_02_click_network_button(self):
        '''
        TestRail: #C12701204
        Click Network button. Verify Network window is launched after click network button for MAC.
        '''
        logging.debug("test_02_click_network_button")

        self.wifi_network_problem_dialog.click_network_btn()
        self.network_page.wait_for_network_page_screen_load()
        self.network_page.click_close_network_page_btn()
        self.wifi_network_problem_dialog.wait_for_screen_load()

    def test_03_click_change_connection_button(self):
        '''
        TestRail: #C12701204
        Click Change connection button. Verify the How do you want to connect your printer? screen display after clicking the change connection button.
        '''
        logging.debug("test_03_click_change_connection_button")

        self.wifi_network_problem_dialog.click_change_connection_btn()
        self.choose_connection_page.wait_for_screen_load()
        self.common_flows.click_home_exit_flow_to_main_ui()

    def test_04_click_continue_button(self):
        '''
        TestRail: #C12701204
        Click Continue button. Verify the Connect Printer to WiFi screen display after clicking the continue button.
        '''
        logging.debug("test_04_click_continue_button")

        self.common_flows.set_up_a_new_printer_menu_bar()
        self.starting_up.wait_for_initialize_page_load()

        if(self.select_a_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify select a printer screen displays if multiple network/USB printers are found.")
            self.select_a_printer.click_to_selected_printer(self.printer_name)
        elif(self.we_found_your_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify we found your printer screen displays if only one network/USB printer is found.")
            self.we_found_your_printer.verify_ui_string()
            self.we_found_your_printer.click_continue_btn()

        self.wifi_network_problem_dialog.wait_for_screen_load()
        self.wifi_network_problem_dialog.click_continue_btn()
        self.connect_printer_to_wifi.wait_for_screen_load()

    def test_05_check_connect_printer_help_dialog(self):
        '''
        TestRail: #C12797521
        Check "Connect printer help" dialog, verify functionality
        '''
        logging.debug("test_05_check_connect_printer_help_dialog")

        self.connect_printer_to_wifi.click_info_btn()
        connect_printer_help_dialog = ConnectPrinterHelpDialog(self.driver)
        connect_printer_help_dialog.wait_for_screen_load()

        # Click Continue button. Verify the "Connect printer to WiFi" screen display.
        connect_printer_help_dialog.click_continue_btn()
        self.connect_printer_to_wifi.wait_for_screen_load()

        # Click Change connection button. Verify the How do you want to connect your printer? screen display.
        self.connect_printer_to_wifi.click_info_btn()
        connect_printer_help_dialog.wait_for_screen_load()
        connect_printer_help_dialog.click_change_connection_btn()
        self.choose_connection_page.wait_for_screen_load()
        self.common_flows.click_home_exit_flow_to_main_ui()

    def test_06_check_select_a_wifi_dialog(self):
        '''
        TestRail: #C12797524
        Check Select a WiFi network dialog. verify functionality.
        '''
        logging.debug("test_06_check_select_a_wifi_dialog")

        self.common_flows.set_up_a_new_printer_menu_bar()
        self.starting_up.wait_for_initialize_page_load()

        if(self.select_a_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify select a printer screen displays if multiple network/USB printers are found.")
            self.select_a_printer.click_to_selected_printer(self.printer_name_2)
        elif(self.we_found_your_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify we found your printer screen displays if only one network/USB printer is found.")
            self.we_found_your_printer.verify_ui_string()
            self.we_found_your_printer.click_continue_btn()

        self.connect_printer_to_wifi.wait_for_screen_load()
        self.connect_printer_to_wifi.click_change_network_link()

        select_wifi_network_dialog = SelectaWiFiNetworkDialog(self.driver)
        select_wifi_network_dialog.wait_for_screen_load()

        # Click Network button. Verify network window is launched.
        select_wifi_network_dialog.click_network_btn()
        self.network_page.wait_for_network_page_screen_load()
        self.network_page.click_close_network_page_btn()
        select_wifi_network_dialog.wait_for_screen_load()

        # Click continue button. Verify the "connect printer to WiFi" screen display.
        select_wifi_network_dialog.click_continue_btn()
        self.connect_printer_to_wifi.wait_for_screen_load()