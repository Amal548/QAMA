#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: This is a test case for Help & Support function testing on Non-ENU OS.

@author: Ivan
@create_date: Sep 17, 2019
'''
import pytest

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.helpsupport.help_support import HelpSupport


pytest.app_info = "DESKTOP"


class Test_Suite_01_Help_Support_Non_ENU(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.main_ui = MainUI(self.driver)
        self.help_support = HelpSupport(self.driver)
        self.appname = smart_const.APP_NAME.SMART
        self.printer = {"printerBonjourName": "HP ENVY Photo 7800 series [093B66]", "printerIP": "192.168.10.186"}

    def test_01_help_support_with_printer_added(self):
        '''
        TestRail: #C14715629
        (Non-ENU) Check 'Chat with Virtual Agent' option on the list view, verify Virtual Agent option is hidden.
        '''
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.common_flows.add_printer_to_carousel(self.printer, is_first_add=True, is_skip_ows=True)
        self.main_ui.click_help_center_tile()
        self.help_support.verify_virtual_agent_information_non_enu()
        self.common_flows.close_HPSmart_app()
