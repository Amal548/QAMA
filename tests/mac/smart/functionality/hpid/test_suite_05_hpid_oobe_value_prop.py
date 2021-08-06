#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: This is a test case for Sign In/Sign Up/Sign Out testing via value prop during OOBE flow.
Note: InkGen2 printer
@author: Ivan
@create_date: Sep 29, 2019
'''

import logging
import pytest
from time import sleep

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.smarttasks.smart_tasks import SmartTasks
from MobileApps.libs.flows.mac.smart.screens.oobe.ows import OWS
from MobileApps.libs.flows.mac.smart.flows.flows_oobe import OOBEFlows
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter
from MobileApps.libs.flows.mac.smart.screens.common.sign_up_dialog import SignUpDialog

pytest.app_info = "SMART"


class Test_Suite_01_HPID_OOBE_Value_Prop(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.main_ui = MainUI(self.driver)
        self.tool_bar = ToolBar(self.driver)
        self.smart_tasks = SmartTasks(self.driver)
        self.ows_screen = OWS(self.driver)
        self.appname = smart_const.APP_NAME.SMART
        self.printer_name = "HP ENVY Photo 7800"
        self.wifi_password = "12345678"
        self.username = "stagegotham@gmail.com"
        self.password = "aio1test"

    def test_01_go_through_oobe_flow_to_value_prop(self):
        '''
        Setup test precondition--Go through OOBE flow to value prop screen.
        '''
        logging.debug("Goto Main UI by skipping the post OOBE.")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.common_flows.set_up_a_new_printer_device_picker()

        we_found_your_printer = WeFoundYourPrinter(self.driver)
        select_a_printer = SelectAPrinter(self.driver)
        if(we_found_your_printer.wait_for_screen_load(raise_e=False)):
            we_found_your_printer.verify_ui_string()
            we_found_your_printer.click_continue_btn()
        elif(select_a_printer.wait_for_screen_load(raise_e=False)):
            select_a_printer.click_to_selected_printer(self.printer_name)

        flows_oobe = OOBEFlows(self.driver)
        flows_oobe.go_through_connected_to_wifi_flow(self.wifi_password)
        ows_screen = OWS(self.driver)
        ows_screen.wait_for_enjoy_hp_account_load(360)
        sleep(2)
        ows_screen.click_continue_btn_enjoy_hp_account()

    def test_02_sign_in_on_value_prop_page(self):
        '''
        TestRail: #C14715880
        Sign in via value prop during OOBE flow, verify user can sign in without issue.
        '''
        logging.debug("Sign in HP account and then sign out")
        sign_up_dialog = SignUpDialog(self.driver)
        sign_up_dialog.wait_for_screen_load(120)
        sign_up_dialog.select_already_have_an_hp_account_link()
        self.common_flows.go_through_sign_in_flow(self.username, self.password)

    def test_03_sign_out(self):
        '''
        Sign out HP account.
        '''
        self.common_flows.click_home_exit_flow_to_main_ui()
        logging.debug("Sign out by clicking Person Icon")
        self.common_flows.sign_out_hp_account()
        self.main_ui.wait_for_screen_load()
        self.common_flows.close_HPSmart_app()
