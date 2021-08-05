#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: Test script for OOBE flow from different entries.

@author: Ivan
@create_date: August 7, 2019
'''

import os
import logging
import pytest

import MobileApps.resources.const.mac.const as smart_const
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.system.flows.flows_system import SystemFlows
from MobileApps.libs.flows.mac.smart.flows.flows_oobe import OOBEFlows
from MobileApps.libs.flows.mac.smart.screens.common.device_picker import DevicePicker
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter

# REQUIRED(SMART - launch driver & APP; DESKTOP - launch driver only.)
pytest.app_info = "SMART"


class Test_Suite_05_OOBE_Entry(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Define driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.flows_oobe = OOBEFlows(self.driver)
        self.select_a_printer = SelectAPrinter(self.driver)
        self.we_found_your_printer = WeFoundYourPrinter(self.driver)
        self.main_ui = MainUI(self.driver)
        self.wifi_password = '12345678'
        self.printer_type = smart_const.OWS_TYPE.PALERMO_GEN2_INKJET
        self.printer_name = "HP ENVY Photo 7800 series"

    def test_01_oobe_setup_precondition(self):
        '''
        Precondition: Go to Main UI with skipping post-OOBE.
        '''
        logging.debug("test_01_oobe_setup_precondition")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe(printer_name=None)

    def test_02_oobe_from_menu_bar(self):
        '''
        TestRail:#C12797546
        Test an OOBE flow from 'Set up a new printer' link on menu bar, verify setup is successful
        '''
        logging.debug("test_02_oobe_from_menu_bar")

        self.common_flows.set_up_a_new_printer_menu_bar()

        if(self.we_found_your_printer.wait_for_screen_load(raise_e=False)):
            self.we_found_your_printer.verify_ui_string()
            self.we_found_your_printer.click_continue_btn()
        elif(self.select_a_printer.wait_for_screen_load(raise_e=False)):
            self.select_a_printer.click_to_selected_printer(self.printer_name)

        self.flows_oobe.go_through_connected_to_wifi_flow(self.wifi_password)
        self.flows_oobe.go_through_ows_flow(self.printer_type)
        self.flows_oobe.after_ows_to_main_ui_flow()

        self.main_ui.wait_for_printer_status_load(60)

    def test_03_oobe_from_device_picker(self):
        '''
        TestRail:#C12797861
        Test an OOBE flow from 'Set up a new printer' link on device picker, verify setup is successful
        '''
        logging.debug("test_03_oobe_from_device_picker")

        self.common_flows.forget_this_printer_from_menu_bar()

        # Clean up HP smart folder
        smart_utility.delete_all_files(os.path.expanduser('~/Library/Application Support/HP Smart'))

        # Clean up and delete all installed printers
        system_flows = SystemFlows(self.driver)
        system_flows.delete_all_printers_and_fax()

        self.common_flows.set_up_a_new_printer_device_picker()

        if(self.we_found_your_printer.wait_for_screen_load(raise_e=False)):
            self.we_found_your_printer.verify_ui_string()
            self.we_found_your_printer.click_continue_btn()
        elif(self.select_a_printer.wait_for_screen_load(raise_e=False)):
            self.select_a_printer.click_to_selected_printer(self.printer_name)

        self.flows_oobe.go_through_connected_to_wifi_flow(self.wifi_password)
        self.flows_oobe.go_through_ows_flow(self.printer_type)
        self.flows_oobe.after_ows_to_main_ui_flow()

        self.main_ui.wait_for_printer_status_load(60)

    def test_04_oobe_from_beaconing_printer(self):
        '''
        TestRail:#C12797882
        Test an OOBE flow from clicking on the beaconing printer on device picker, verify setup is successful
        '''
        logging.debug("test_04_oobe_from_beaconing_printer")

        self.common_flows.forget_this_printer_from_navigation_pane()

        # Clean up HP smart folder
        smart_utility.delete_all_files(os.path.expanduser('~/Library/Application Support/HP Smart'))

        # Clean up and delete all installed printers
        system_flows = SystemFlows(self.driver)
        system_flows.delete_all_printers_and_fax()

        device_picker = DevicePicker(self.driver)
        device_picker.wait_for_screen_load(120)
        device_picker.click_beaconing_printer_chose(self.printer_name)

        self.we_found_your_printer.wait_for_screen_load()
        self.we_found_your_printer.click_continue_btn()

        self.flows_oobe.go_through_connected_to_wifi_flow(self.wifi_password)
        self.flows_oobe.go_through_ows_flow(self.printer_type)
        self.flows_oobe.after_ows_to_main_ui_flow()

        self.main_ui.wait_for_printer_status_load(60)
