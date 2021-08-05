#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: Test script for the basic testing of Advanced Settings with an online/offline application printer
Note: Please use a real printer for this testing

@author: Ivan
@create_date: Sep 2, 2019
'''

import os
import pytest
import logging

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.common.device_picker import DevicePicker
from MobileApps.libs.flows.mac.smart.screens.printersettings.advanced_settings import AdvancedSettings
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_information import PrinterInformation
from MobileApps.libs.flows.mac.system.screens.system_preferences import SystemPreferences
from time import sleep

pytest.app_info = "DESKTOP"


class Test_Suite_01_Advanced_Settings_Basic_WiFi(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup

        self.main_screen = MainUI(self.driver)
        self.ews = AdvancedSettings(self.driver)
        self.tool_bar = ToolBar(self.driver)
        self.printer_information = PrinterInformation(self.driver)
        self.appname = smart_const.APP_NAME.SMART
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [093B66]"
        self.printer_2 = {"printerBonjourName": "HP PageWide MFP P77740-60z [98301E]", "printerIP": "192.168.10.145"}

    def test_01_advanced_settings_online_application_printer(self):
        '''
        TestRail: #C16942852
        Go to "Advance Settings" with an online application printer, verify printer EWS displays.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)
        logging.debug("Start to check welcome workflow... ")
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        logging.debug("Start to check post OOBE workflow... ")
        self.common_flows.go_to_main_ui_skip_post_oobe()

        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()

        if (self.main_screen.wait_for_right_arrow_icon_display(raise_e=False)):
            self.main_screen.click_right_arrow_icon()
        self.main_screen.click_printer_settings_tile()

        self.ews.wait_for_printer_home_page_item_load()
        self.ews.click_printer_home_page_item()
        self.ews.wait_for_screen_load()
        sleep(2)
        logging.debug("TestRail: C15541084/C15541085 -> Randomly check some information in the printer EWS WebView and modify some settings, verify accuracy and the settings can be saved")
        self.ews.change_energy_save_mode_option()

        logging.debug("TestRail: C15541086 -> Click back arrow on printer EWS screen, verify home page shows. [GOTH-7384. Last page shows]")
        self.tool_bar.click_back_btn()
        printer_information = PrinterInformation(self.driver)
        printer_information.wait_for_screen_load()

        logging.debug("TestRail: C15541111 -> Click Home icon on top left corner on EWS screen, verify Home page shows.")
        self.ews.click_printer_home_page_item()
        self.ews.wait_for_screen_load()
        self.common_flows.back_main_ui_from_printer_settings()

    def test_02_advanced_settings_more_online_application_printers(self):
        '''
        TestRail: #C15541087
        Switch between a few different printers. verify EWS info.
        '''
        logging.debug("Add the second different printer")
        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()
        self.common_flows.add_printer_to_carousel(self.printer_2, is_first_add=False, is_skip_ows=True)
        sleep(10)
        os.system("pkill Safari")
        if (self.main_screen.wait_for_right_arrow_icon_display(raise_e=False)):
            self.main_screen.click_right_arrow_icon()
        self.main_screen.click_printer_settings_tile()
        self.ews.wait_for_printer_home_page_item_load()
        self.ews.click_printer_home_page_item()
        self.ews.wait_for_screen_load(60)
        self.common_flows.back_main_ui_from_printer_settings()

    def test_03_advanced_settings_offline_application_printer(self):
        '''
        TestRail:#C15541075
        Go to "Advance Settings" with an offline application printer, verify "Can't open printer home or EWS page" dialog displays.
        '''
#         self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()
#
#         if (self.main_screen.wait_for_right_arrow_icon_display(raise_e=False)):
#             self.main_screen.click_right_arrow_icon()
        self.main_screen.click_printer_settings_tile()
        self.printer_information.wait_for_screen_load()

        logging.debug("Turn off computer WiFi")
        self.system_flows.turn_off_computer_wifi_connection()

        logging.debug("TestRail: C15541076,C15541077 -> Check 'Can't open printer home or EW page' dialog UI")
        self.ews.click_printer_home_page_item()
        self.ews.wait_for_cant_open_dialog_load()
        self.ews.verify_cant_open_printer_home_dialog_ui()

        logging.debug("TestRail: C15541078 -> Click OK button on the 'Can't open printer home or EW page' dialog, verify home page shows. [GOTH-6703. Blank EWS page shows]")
        self.ews.click_ok_btn_on_dialog()
        self.system_flows.turn_on_computer_wifi_connection()
        self.common_flows.close_HPSmart_app()
