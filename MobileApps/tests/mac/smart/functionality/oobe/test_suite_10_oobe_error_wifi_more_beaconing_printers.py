#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: Test script for OOBE error conditions while computer is on WiFi.
Precondition:
1.Connect Computer to a WiFi network
2.OOBE reset the printer, ink and paper removed prior to test. Make sure the printer SSID name shown has "SETUP" word in it.
3.Make sure multiple beaconing printers in the network.
4.Enter OOBE via any 1 of the OOBE entries.

@author: Ivan
@create_date: Aug 27, 2019
'''

import logging
import pytest

from MobileApps.libs.flows.mac.smart.screens.oobe.initialize_page import InitializePage
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_connection_page import ChooseConnectionPage
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter

pytest.app_info = "SMART"


class Test_Suite_10_OOBE_Error_WiFi_More_Beaconing_Printers(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.starting_up = InitializePage(self.driver)
        self.select_a_printer = SelectAPrinter(self.driver)

    def test_01_printer_setup_incomplete(self):
        '''
        TestRail: #C12797870
        Check "Printer Setup incomplete" dialog on the select a printer screen with multiple beaconing printers found, verify functionality.
        '''
        logging.debug("test_01_printer_setup_incomplete")

        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.common_flows.set_up_a_new_printer_menu_bar()
        self.starting_up.wait_for_initialize_page_load()
        self.select_a_printer.wait_for_screen_load()

        # Click back button on "Printer Setup incomplete" dialog, verify dialog dismisses.
        self.common_flows.click_back_dismiss_printer_setup_incomplete()
        self.select_a_printer.wait_for_screen_load()

        # Click OK button on "Printer Setup incomplete" dialog, verify exit the OOBE flow to main UI.
        self.common_flows.click_home_exit_flow_to_main_ui()

    def test_02_go_through_select_a_printer(self):
        '''
        TestRail: #C12701188
        Check "Select a printer" screen with multiple beaconing printers found, verify functionality.
        '''
        logging.debug("test_02_go_through_select_a_printer")

        self.common_flows.set_up_a_new_printer_menu_bar()

        self.starting_up.wait_for_initialize_page_load()
        # TestRail: C12797885,C12797899
        self.select_a_printer.wait_for_screen_load()

        # Click Refresh link, verify a loading icon shows under printer list
        self.select_a_printer.click_refresh_link()
        self.select_a_printer.wait_for_busy_icon_display()
        # Verify all beaconing printers are found and displayed on Select a printer screen after the progress complete.
        self.select_a_printer.wait_for_screen_load(90)

        # Need to confirm! CR?
        # [Excepted] Refresh and Printer not listed link is displayed but disabled during printer searching.
        # [Actual] No refresh and Printer not listed link is displayed during printer searching.

        # Click Printer not listed link
        self.select_a_printer.click_printer_not_listed_link()

        we_found_your_printer = WeFoundYourPrinter(self.driver)
        choose_connection_page = ChooseConnectionPage(self.driver)
        if(self.select_a_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify select a printer screen displays if multiple network/USB printers are found.")
            pass
        elif(we_found_your_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify we found your printer screen displays if only one network/USB printer is found.")
            we_found_your_printer.verify_ui_string()
        elif(choose_connection_page.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify How do you want to connect your printer? screen display if no network/USB printer is found.")
            choose_connection_page.verify_ui_string()

        self.common_flows.click_home_exit_flow_to_main_ui()
