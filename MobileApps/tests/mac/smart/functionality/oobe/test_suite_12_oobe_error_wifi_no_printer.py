#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: Test script for OOBE error conditions while computer is on WiFi.
Precondition:
1.Connect Computer to a WiFi network
2.Make sure no printer in the network
3.Enter OOBE via any 1 of the OOBE entries.

@author: Ivan
@create_date: Aug 28, 2019
'''

import logging
import pytest

from MobileApps.libs.flows.mac.system.screens.system_preferences import SystemPreferences
from MobileApps.libs.flows.mac.smart.screens.oobe.initialize_page import InitializePage
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_connection_page import ChooseConnectionPage
from MobileApps.libs.flows.mac.smart.screens.oobe.we_could_not_find_your_printer_dialog import WeCouldNotFindYourPrinterDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_incomplete_dialog import PrinterSetupIncompleteDialog

pytest.app_info = "SMART"


class Test_Suite_12_OOBE_Error_WiFi_No_Printer(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.initialize_page = InitializePage(self.driver)

    def test_01_check_we_could_not_find_your_printer_dialog(self):
        '''
        TestRail: #C12797528
        Check "We're sorry, we could not find your printer" dialog, verify functionality.
        '''
        logging.debug("test_01_check_we_could_not_find_your_printer_dialog")

        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.common_flows.set_up_a_new_printer_menu_bar()

        self.initialize_page.wait_for_initialize_page_load()

        choose_connection_page = ChooseConnectionPage(self.driver)
        choose_connection_page.wait_for_screen_load(90)
        choose_connection_page.click_ethernet_cable_opt()
        choose_connection_page.click_continue_btn()
        self.initialize_page.wait_for_initialize_page_load()

        # TestRail: C12797894, C12797903
        we_could_not_find_your_printer = WeCouldNotFindYourPrinterDialog()
        we_could_not_find_your_printer.wait_for_screen_load(180)
        we_could_not_find_your_printer.verify_we_could_not_find_your_printer_ui_string()

        # Click Network button. Verify network window is launched.
        we_could_not_find_your_printer.click_network_btn()
        network_page = SystemPreferences(self.driver)
        network_page.wait_for_network_page_screen_load()
        network_page.click_close_network_page_btn()
        we_could_not_find_your_printer.wait_for_screen_load()

        # Click Exit Setup button. Verify "Printer setup incomplete" dialog pops up.
        we_could_not_find_your_printer.click_exit_setup_btn()
        printer_setup = PrinterSetupIncompleteDialog(self.driver)
        printer_setup.click_back_btn()
        we_could_not_find_your_printer.wait_for_screen_load()

        # Click Try Again button. Verify the "Connecting to the printer..." screen with a loading process ring display. and "We're sorry, we could not find your printer" dialog eventually displays if no printer found, "We found your printer!" screen shows if printer is found.
        we_could_not_find_your_printer.click_try_again_btn()
        self.initialize_page.wait_for_initialize_page_load()
        we_could_not_find_your_printer.wait_for_screen_load(180)
