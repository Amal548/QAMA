#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: Test script for OOBE error conditions while computer is on WiFi.
Precondition:
1.Connect Computer to a WiFi network
2.Make sure not beaconing printer in the network.
3.Enter OOBE via any 1 of the OOBE entries.

@author: Ivan
@create_date: Aug 26, 2019
'''

import logging
import pytest

from MobileApps.libs.flows.mac.smart.screens.oobe.initialize_page import InitializePage
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_connection_page import ChooseConnectionPage
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_incomplete_dialog import PrinterSetupIncompleteDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.let_find_your_printer import FindYourPrinter

pytest.app_info = "SMART"


class Test_Suite_09_OOBE_Error_WiFi_No_Beaconing_Printer(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.let_find_your_printer = FindYourPrinter(self.driver)

    def test_01_printer_setup_incomplete(self):
        '''
        TestRail: #C12797870
        Check "Printer Setup incomplete" dialog on the Let's find your printer so we can get it connected screen, verify functionality.
        '''
        logging.debug("test_01_printer_setup_incomplete")

        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.common_flows.set_up_a_new_printer_menu_bar()
        self.let_find_your_printer.wait_for_screen_load()

        # Click back button on "Printer Setup incomplete" dialog, verify dialog dismisses.
        self.common_flows.click_back_dismiss_printer_setup_incomplete()
        self.let_find_your_printer.wait_for_screen_load()

        # Click OK button on "Printer Setup incomplete" dialog, verify exit the OOBE flow to main UI.
        self.common_flows.click_home_exit_flow_to_main_ui()

    def test_02_go_through_lets_find_your_printer(self):
        '''
        TestRail: #C12701193
        Check "Lets's find your printer so we can get it connected!" screen, verify functionality.
        '''
        logging.debug("test_02_go_through_lets_find_your_printer")

        self.common_flows.set_up_a_new_printer_menu_bar()

        # TestRail: C12797883, C12797898
        self.let_find_your_printer.wait_for_screen_load()
        self.let_find_your_printer.verify_lets_find_your_printer_screen()
        self.let_find_your_printer.click_continue_btn()

        searching_for_printers = InitializePage(self.driver)
        searching_for_printers.wait_for_initialize_page_load()

        we_found_your_printer = WeFoundYourPrinter(self.driver)
        select_a_printer = SelectAPrinter(self.driver)
        choose_connection_page = ChooseConnectionPage(self.driver)
        if(we_found_your_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify We found your printer! screen display if no beaconing printer but have normal printer or there is one beaconing printer in the network")
            we_found_your_printer.verify_ui_string()
        elif(select_a_printer.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify Select a printer screen display if there are two or more beaconing printers in the network")
            pass
        elif(choose_connection_page.wait_for_screen_load(raise_e=False)):
            logging.debug("Verify How do you want to connect your printer? screen display if no beaconing printer and no normal printer in the network")
            choose_connection_page.verify_ui_string()

        self.common_flows.click_home_exit_flow_to_main_ui()
