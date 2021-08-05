#!/usr/local/bin/python2.7
# encoding: utf-8
'''
oobe wireless setup using front panel

@author: ten
@create_date: Aug 21, 2019
'''

import pytest
import logging

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.flows import flows_oobe
from MobileApps.libs.flows.mac.smart.screens.oobe.connecting_printer_to_wifi_wireless_setup import ConnectingPrintertoWiFiSetup
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_connection_page import ChooseConnectionPage
from MobileApps.libs.flows.mac.smart.screens.oobe.wireless_setup_using_usb import WirelessSetupUsingUSB
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_your_hp_laserjet_dialog import ConnectYourHPLaserJetDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter


pytest.app_info = "SMART"


class Test_Suite_06_OOBE_Wireless_Setup_Using_FP(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.flows_oobe = flows_oobe.OOBEFlows(self.driver)
        self.connecting_printer_to_wifi_wireless_setup = ConnectingPrintertoWiFiSetup(self.driver)
        self.printer_bonjour_name = "HP ENVY 4500 series [DB9B7D]"

    def test_01_go_to_choose_a_connection_method_screen(self):
        '''
        TestRail:#C13578800
        go to choose a connection method screen
        '''
        logging.debug("go to choose a connection method screen")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_initial_screen()
        self.flows_oobe.go_to_choose_a_connection_method_directly()

    def test_02_check_connecting_printer_to_wifi_screen(self):
        '''
        TestRail:#C12917436,#C12917436,#12917438,#C12917439,#C12961432,#C12961546
        go to connecting printer to wifi.. screen and check some button
        '''
        logging.debug("go to connecting printer to wifi.. screen")
        self.flows_oobe.go_to_connecting_printer_to_wifi_wireless_setup()

        logging.debug("click back button")
        choose_connection_page = ChooseConnectionPage(self.driver)
        self.connecting_printer_to_wifi_wireless_setup.click_back_btn()
        choose_connection_page.wait_for_screen_load()

        logging.debug("click no button")
        self.flows_oobe.go_to_connecting_printer_to_wifi_wireless_setup()
        self.flows_oobe.go_to_wireless_setup_using_usb()

        logging.debug("click yes button")
        wireless_setup_using_usb = WirelessSetupUsingUSB(self.driver)
        wireless_setup_using_usb.click_back_btn()
        self.flows_oobe.go_to_connecting_printer_to_wifi_wireless_setup()
        self.connecting_printer_to_wifi_wireless_setup.click_yes_opt()
        self.connecting_printer_to_wifi_wireless_setup.verify_ui_string()

    def test_03_check_connect_your_hp_laserjet_dialog(self):
        '''
        TestRail:#C12961635,#C12961651
        check connect your HP LaserJet dialog
        '''
        logging.debug("click here link")
        connect_your_hp_laserjet_dialog = ConnectYourHPLaserJetDialog(self.driver)
        self.connecting_printer_to_wifi_wireless_setup.click_here_link()
        connect_your_hp_laserjet_dialog.wait_for_screen_load()
        connect_your_hp_laserjet_dialog.verify_ui_string()
        connect_your_hp_laserjet_dialog.click_continue_btn()

    def test_04_check_continue_on_connecting_printer_to_wifi_screen(self):
        '''
        TestRail:#C12917438
        install driver
        '''
        logging.debug("Start to installed a printer... and click continue button ")
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)
        self.connecting_printer_to_wifi_wireless_setup.click_continue_btn()
        we_found_your_printer.wait_for_screen_load()
        we_found_your_printer.verify_we_found_your_printer_title_no_existed()
