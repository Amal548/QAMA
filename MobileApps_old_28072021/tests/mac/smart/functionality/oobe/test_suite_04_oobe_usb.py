#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Test_Suite_04_OOBE_USB

@author: ten
@create_date: Aug 13, 2019
'''
import logging
import pytest
import time

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.flows import flows_oobe
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_connection_page import ChooseConnectionPage
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_using_usb import ConnectusingUSB
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connected import PrinterConnected
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_lets_print import PrinterSetupLetsPrint


pytest.app_info = "SMART"


class Test_Suite_04_OOBE_USB(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.flows_oobe = flows_oobe.OOBEFlows(self.driver)
        self.choose_connection_page = ChooseConnectionPage(self.driver)
        self.connect_using_usb = ConnectusingUSB(self.driver)
        self.we_found_your_printer = WeFoundYourPrinter(self.driver)
        self.printer_connected = PrinterConnected(self.driver)
        self.printer_setup_lets_print = PrinterSetupLetsPrint(self.driver)
        self.printer_bonjour_name = "HP ENVY Photo 7800 series"
        self.printer_type = smart_const.OWS_TYPE.PALERMO_GEN2_INKJET

    def test_01_go_through_agreement_screen(self):
        '''
        go through agreement
        '''
        logging.debug("go through agreement...")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_inital_screen()

    def test_02_go_to_choose_a_connection_methed_screen(self):
        '''
        go_to_choose_a_connection_methed_screen
        '''
        logging.debug("go_to_choose_a_connection_methed_screen...")
        self.flows_oobe.go_to_oobe_choose_a_connection_method_directly()

    def test_03_check_connect_using_usb_screen(self):
        '''
        check connect using usb screen
        '''
        logging.debug("check connect using usb screen...")
        self.choose_connection_page.click_usb_cable_opt()
        self.choose_connection_page.click_continue_btn()
        self.connect_using_usb.verify_ui_string()

    def test_04_install_printer(self):
        '''
        TestRail:#C12805528,#C12805479
        install USB driver
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)

    def test_05_go_to_ows_screen(self):
        '''
        go to ows screen
        '''
        logging.debug("go_to_ows_screen... ")
        self.connect_using_usb.click_continue_btn()
        self.we_found_your_printer.wait_for_screen_load()
        self.we_found_your_printer.verify_we_found_your_printer_title_no_existed()
        self.we_found_your_printer.click_continue_btn()
        self.printer_connected.wait_for_screen_load()
        self.printer_connected.verify_printer_connected_to_usb_screen_display()
        self.printer_connected.click_continue_btn()

    def test_06_go_through_ows_flow(self):
        '''
        Go through OWS workflow
        '''
        logging.debug("Go through OWS workflow")
        self.flows_oobe.go_through_ows_flow()

    def test_06_go_to_main_ui(self):
        '''
        Go to home screen
        '''
        logging.debug("Go to home screen")
        self.printer_setup_lets_print.wait_for_screen_load()
        self.printer_setup_lets_print.click_print_btn()
        time.sleep(3)
        self.printer_setup_lets_print.click_print_btn_on_dialog()
