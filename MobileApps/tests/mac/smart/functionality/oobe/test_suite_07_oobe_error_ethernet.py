#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: Test script for OOBE error conditions while computer is on Ethernet.

@author: Ivan
@create_date: Aug 21, 2019
'''

import os
import logging
import pytest

from MobileApps.libs.flows.mac.smart.flows.flows_oobe import OOBEFlows
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.system.flows.flows_system import SystemFlows
from MobileApps.libs.flows.mac.system.screens.system_preferences import SystemPreferences
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_this_computer_to_wifi import ConnectComputerToWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.lets_connect_this_computer_to_wifi import LetsConnectThisComputerToWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.initialize_page import InitializePage
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_connection_page import ChooseConnectionPage
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connected import PrinterConnected
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_incomplete_dialog import PrinterSetupIncompleteDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.let_find_your_printer import FindYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connected_to_wifi import PrinterConnectedtoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.connecting_printer_to_wifi_wireless_setup import ConnectingPrintertoWiFiSetup

pytest.app_info = "SMART"


class Test_Suite_07_OOBE_Error_Ethernet(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.printer_setup = PrinterSetupIncompleteDialog(self.driver)
        self.connect_this_computer_to_wifi = ConnectComputerToWiFi(self.driver)
        self.searching_for_printers = InitializePage(self.driver)

    def test_01_printer_setup_incomplete_1(self):
        '''
        TestRail: #C12865244
        Check "Printer Setup incomplete" dialog on the Let's connect this computer to WiFi screen, verify functionality.
        '''
        logging.debug("test_01_printer_setup_incomplete_1")

        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.common_flows.set_up_a_new_printer_menu_bar()
        self.connect_this_computer_to_wifi.wait_for_screen_load()

        # Click back button on "Printer Setup incomplete" dialog, verify dialog dismisses.
        self.common_flows.click_back_dismiss_printer_setup_incomplete()
        self.connect_this_computer_to_wifi.wait_for_screen_load()

        # Click OK button on "Printer Setup incomplete" dialog, verify exit the OOBE flow to main UI.
        self.common_flows.click_home_exit_flow_to_main_ui()

    def test_02_no_continue_with_ethernet_flow(self):
        '''
        TestRail: #C12612367
        Check next "Let's connect your computer to WiFi" screen after "No, continue with Ethernet" button is clicked, verify functionality.
        '''
        logging.debug("test_02_no_continue_with_ethernet_flow")

        self.common_flows.set_up_a_new_printer_menu_bar()

        # TestRail: C12612365, C12865247, C12612387
        # Check "Let's connect your computer to WiFi" screen UI/localization
        self.connect_this_computer_to_wifi.wait_for_screen_load()
        self.connect_this_computer_to_wifi.verify_connect_this_computer_to_wifi_screen()
        self.connect_this_computer_to_wifi.click_no_continue_with_ethernet_opt()
        self.connect_this_computer_to_wifi.wait_for_continue_btn_display()
        self.connect_this_computer_to_wifi.click_continue_btn()

        self.searching_for_printers.wait_for_initialize_page_load()

        we_found_your_printer = WeFoundYourPrinter(self.driver)
        select_a_printer = SelectAPrinter(self.driver)
        choose_connection_page = ChooseConnectionPage(self.driver)
        if(we_found_your_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("We found your printer screen will display if only one network/installed USB printer is searched out")
            we_found_your_printer.verify_ui_string()
        elif(select_a_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Select a printer screen will display if multiple network/installed USB printers are searched out")
            pass
        elif(choose_connection_page.wait_for_screen_load(raise_e=False)):
            logging.debug("How do you want to connect your printer screen will display if no printer is searched out")
            choose_connection_page.verify_ui_string()

        self.common_flows.click_home_exit_flow_to_main_ui()

    def test_03_printer_setup_incomplete_2(self):
        '''
        TestRail: #C12686368
        Check "Printer Setup incomplete" dialog on the next "Let's connect this computer to WiFi" screen, verify functionality.
        '''
        logging.debug("test_03_printer_setup_incomplete_2")

        self.common_flows.set_up_a_new_printer_menu_bar()
        self.connect_this_computer_to_wifi.wait_for_screen_load()
        self.connect_this_computer_to_wifi.click_yes_switch_to_wifi_opt()
        self.connect_this_computer_to_wifi.click_continue_btn()

        lets_connect_this_computer_to_wifi = LetsConnectThisComputerToWiFi(self.driver)
        lets_connect_this_computer_to_wifi.wait_for_screen_load()

        self.common_flows.click_back_dismiss_printer_setup_incomplete()
        lets_connect_this_computer_to_wifi.wait_for_screen_load()

        self.common_flows.click_home_exit_flow_to_main_ui()

    def test_04_yes_switch_to_wifi_flow_without_wifi_connected(self):
        '''
        TestRail: #C12686368
        Click continue button on Let's connect your computer to WiFi screen without connecting to WiFi.
        '''
        logging.debug("test_04_yes_switch_to_wifi_flow_without_wifi_connected")

        self.common_flows.set_up_a_new_printer_menu_bar()

        self.connect_this_computer_to_wifi.wait_for_screen_load()
        self.connect_this_computer_to_wifi.click_yes_switch_to_wifi_opt()
        self.connect_this_computer_to_wifi.wait_for_continue_btn_display()
        self.connect_this_computer_to_wifi.click_continue_btn()

        # TestRail: C12865248, C12612396
        # Check next "Let's connect your computer to WiFi" screen after "Yes, switch to WiFi" + Continue button UI/localization
        lets_connect_this_computer_to_wifi = LetsConnectThisComputerToWiFi(self.driver)
        lets_connect_this_computer_to_wifi.wait_for_screen_load()
        lets_connect_this_computer_to_wifi.verify_lets_connect_this_computer_to_wifi_screen()
        lets_connect_this_computer_to_wifi.click_network_button()
        network_page = SystemPreferences(self.driver)
        network_page.wait_for_network_page_screen_load()
        network_page.click_close_network_page_btn()
        lets_connect_this_computer_to_wifi.wait_for_continue_btn_display()
        lets_connect_this_computer_to_wifi.click_continue_btn()

        self.searching_for_printers.wait_for_initialize_page_load()

        we_found_your_printer = WeFoundYourPrinter(self.driver)
        choose_connection_page = ChooseConnectionPage(self.driver)
        select_a_printer = SelectAPrinter(self.driver)
        if(we_found_your_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("We found your printer screen will display if only one network/installed USB printer is searched out")
            we_found_your_printer.verify_ui_string()
        elif(select_a_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Select a printer screen will display if multiple network/installed USB printers are searched out")
            pass
        elif(choose_connection_page.wait_for_screen_load(raise_e=False)):
            logging.debug("How do you want to connect your printer screen will display if no printer is searched out")
            choose_connection_page.verify_ui_string()

        self.common_flows.click_home_exit_flow_to_main_ui()

    def test_05_yes_switch_to_wifi_flow_with_wifi_connected(self):
        '''
        TestRail: #C12686368
        Click continue button on Let's connect your computer to WiFi screen after connecting to WiFi.
        '''
        logging.debug("test_05_yes_switch_to_wifi_flow_with_wifi_connected")

        self.common_flows.set_up_a_new_printer_menu_bar()

        self.connect_this_computer_to_wifi.wait_for_screen_load()
        self.connect_this_computer_to_wifi.click_yes_switch_to_wifi_opt()
        self.connect_this_computer_to_wifi.click_continue_btn()

        # TestRail: C12865248, C12612396
        # Check next "Let's connect your computer to WiFi" screen after "Yes, switch to WiFi" + Continue button UI/localization
        lets_connect_this_computer_to_wifi = LetsConnectThisComputerToWiFi(self.driver)
        lets_connect_this_computer_to_wifi.wait_for_screen_load()
        lets_connect_this_computer_to_wifi.click_network_button()
        network_page = SystemPreferences(self.driver)
        network_page.wait_for_network_page_screen_load()
        network_page.click_wifi_option()
        network_page.wait_for_network_wifi_screen_load()
        network_page.click_turn_wifi_on_btn()
        network_page.click_close_network_page_btn()
        lets_connect_this_computer_to_wifi.click_continue_btn()

        self.searching_for_printers.wait_for_initialize_page_load()

        we_found_your_printer = WeFoundYourPrinter(self.driver)
        select_a_printer = SelectAPrinter(self.driver)
        let_find_your_printer = FindYourPrinter(self.driver)
        if(we_found_your_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("We found your printer screen displays if there is only one beaconing printer found.")
            we_found_your_printer.verify_ui_string()
        elif(select_a_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Select a printer screen will display if multiple beaconing printer found.")
            pass
        elif(let_find_your_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Let's find your printer so we can get it connected screen displays if no beaconing printer is found.")
            let_find_your_printer.verify_lets_find_your_printer_screen()

        self.common_flows.click_home_exit_flow_to_main_ui()
