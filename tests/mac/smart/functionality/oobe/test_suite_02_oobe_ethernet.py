#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Test_Suite_01_OOBE_AWC

@author: ten
@create_date: July 28, 2019
'''
import logging
import pytest
import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_connection_page import ChooseConnectionPage
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_a_connection_method_dialog import ChooseCnnectionMethodDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_your_printer_to_your_network import ConnectYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connected import PrinterConnected
from MobileApps.libs.flows.mac.smart.flows import flows_oobe

# REQUIRED
pytest.app_info = "SMART"


class Test_Suite_02_OOBE_Ethernet(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.flows_oobe = flows_oobe.OOBEFlows(self.driver)
        self.choose_connection_page = ChooseConnectionPage(self.driver)
        self.connect_your_printer_to_your_network = ConnectYourPrinter(self.driver)

    def test_01_check_oobe_select_printer_screen(self):
        '''
        TestRail:#C12797508
        Check “Select a printer” screen with discovered printers
        '''
        logging.debug("Check “Select a printer” screen with discovered printers, verify functionality[C12797508]")
        select_a_printer = SelectAPrinter(self.driver)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_initial_screen()
        self.flows_oobe.go_to_select_printer_enthernet_flow()
        select_a_printer.click_refresh_link()
        select_a_printer.wait_for_busy_icon_display()
        select_a_printer.wait_for_busy_icon_disappear()

    def test_02_check_choose_connection_page(self):
        '''
        TestRail:#C12797543
        Check 'How do you want to connect your printer?' screen
        '''
        logging.debug("Check 'How do you want to connect your printer?' screen, verify functionality[C12797543]")
        choose_a_connection_method_dialog = ChooseCnnectionMethodDialog(self.driver)
        self.flows_oobe.go_to_choose_a_connection_method()
        self.choose_connection_page.verify_ui_string()
        self.choose_connection_page.click_info_btn()
        choose_a_connection_method_dialog.wait_for_screen_load()
        choose_a_connection_method_dialog.verify_ui_string()
        choose_a_connection_method_dialog.click_done_btn()

    def test_03_check_connect_your_printer_to_your_network_screen(self):
        '''
        TestRail:#C12797545
        Check 'Connect your printer to your network' screen
        '''
        logging.debug("Check 'Connect your printer to your network' screen, verify functionality[C12797545]")
        self.flows_oobe.go_to_connection_details_page_in_ethernet_flow()
        self.connect_your_printer_to_your_network.verify_ui_string()
        self.connect_your_printer_to_your_network.click_back_btn()
        self.choose_connection_page.wait_for_screen_load()
        self.flows_oobe.go_to_connection_details_page_in_ethernet_flow()

    def test_04_check_printer_connected_screen(self):
        '''
        TestRail:#C12797919
        Check 'Printer connected'screen
        '''
        logging.debug("Check 'Printer connected'screen, verify functionality[C12797919]")
        printer_connected = PrinterConnected(self.driver)
        self.flows_oobe.go_to_printer_connected_in_ethernet_flow()
        printer_connected.verify_ui_string()

    def test_05_check_printer_setup_incomplete_dialog(self):
        '''
        TestRail:#C12797957
        Check 'Printer connected'screen
        '''
        logging.debug("Check 'Printer connected'screen, verify functionality[C12797957]")
        self.common_flows.go_to_main_ui_skip_post_oobe()
        