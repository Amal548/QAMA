#!/usr/local/bin/python2.7
# encoding: utf-8
'''
OOBE wireless set up using USB

@author: Ten
@create_date: Aug 23, 2019
'''

import pytest
import logging

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.flows import flows_oobe
from MobileApps.libs.flows.mac.smart.screens.oobe.wireless_setup_using_usb import WirelessSetupUsingUSB
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_connection_page import ChooseConnectionPage
from MobileApps.libs.flows.mac.smart.screens.oobe.no_usb_dialog import NoUSBDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_printer_to_wifi import ConnectPrintertoWiFi

pytest.app_info = "SMART"


class Test_Suite_08_OOBE_Wireless_Setup_Using_USB(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.flows_oobe = flows_oobe.OOBEFlows(self.driver)
        self.printer_bonjour_name = "HP ENVY Photo 7800 series"
        self.wifi_password = "12345678"

    def test_01_go_to_choose_a_connection_method_screen(self):
        '''
        TestRail:#C13578802
        go to choose a connection method screen
        '''
        logging.debug("go to choose a connection method screen")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_initial_screen()
        self.flows_oobe.go_to_choose_a_connection_method_directly()

    def test_02_check_wireless_setup_using_usb_screen(self):
        '''
        TestRail:#C12917435,#C12961688,#C12961695
        go to wireless setup using usb  screen and check some button
        '''
        logging.debug("go to wireless setup using usb screen")
        self.flows_oobe.go_to_connecting_printer_to_wifi_wireless_setup()
        self.flows_oobe.go_to_wireless_setup_using_usb()
 
        logging.debug("click back button")
        wireless_setup_using_usb = WirelessSetupUsingUSB(self.driver)
        wireless_setup_using_usb.click_back_btn()
        choose_connection_page = ChooseConnectionPage(self.driver)
        choose_connection_page.wait_for_screen_load()

        logging.debug("click info icon")
        no_usb_dialog = NoUSBDialog(self.driver)
        self.flows_oobe.go_to_connecting_printer_to_wifi_wireless_setup()
        self.flows_oobe.go_to_wireless_setup_using_usb()
        wireless_setup_using_usb.click_info_btn()
        no_usb_dialog.wait_for_screen_load()

        logging.debug("click continue icon")
        no_usb_dialog.click_done_btn()
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)
        wireless_setup_using_usb.click_continue_btn()

    def test_03_check_unplug_usb_cable_screen(self):
        '''
        TestRail:#C12917435,#C12961688,#C12961695
        go to wireless setup using usb  screen and check some button
        '''
        logging.debug("go to wireless setup using usb screen")
        we_found_your_printer = WeFoundYourPrinter(self.driver)

        we_found_your_printer.wait_for_screen_load(90)
        we_found_your_printer.verify_we_found_your_printer_title_no_existed()
        we_found_your_printer.click_continue_btn()

        connect_printer_to_wifi = ConnectPrintertoWiFi(self.driver)
        connect_printer_to_wifi.wait_for_screen_load()
        connect_printer_to_wifi.input_enter_wifi_password_box(self.wifi_password)
        connect_printer_to_wifi.click_continue_btn()
