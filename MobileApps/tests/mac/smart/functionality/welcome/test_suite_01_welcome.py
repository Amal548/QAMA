# encoding: utf-8
'''
Description: This is a test suite to check welcome flow and UI string.

@author: ten
@create_date: July 25, 2019
'''
import logging
import pytest
import os

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.welcome import Welcome
from MobileApps.libs.flows.mac.smart.screens.common.agreement import Agreement
from MobileApps.libs.flows.mac.smart.screens.menubar.learn_more_about_hp_smart import Learn_More_About_HP_Smart
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.mac.const import TEST_DATA
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility

# REQUIRED
pytest.app_info = "DESKTOP"


class Test_Suite_01_Welcome(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.welcome = Welcome(self.driver)
        self.agreement = Agreement(self.driver)

        self.appname = smart_const.APP_NAME.SMART
        self.file_path = ma_misc.load_json_file(TEST_DATA.MAC_SMART_APP_INFO)["mac_smart"]["app_log_file"]["file_path"]

    def test_01_launch_app_and_verify_welcome_flow(self):
        '''
        TestRail:#C17451797,#C17451799,#C17451800,#C17451802,#C17451803,#C17451804,#C17451805,#C17451806
        This is a test case to verify 'welcome' screen
        '''
        logging.debug("launch the app, verify 'welcome' screen display")
        self.common_flows.launch_HPSmart_app(self.appname)
        self.welcome.wait_for_screen_load()
        logging.debug("check contents on welcome screen")
        self.welcome.verify_welcomepage()
        logging.debug("check all the links on welcome screen")
        self.verify_collects_analyzes_link()
        self.welcome.verify_links_on_welcome()
        self.common_flows.close_HPSmart_app()

    def test_02_relaunch_app_and_verify_welcome_flow(self):
        '''
        TestRail:#C17451807,#C17451808,#C17451810,#C17451811,#C17451812
        This is a test case to verify pepto page and welcome flow after clicking YES button
        '''
        logging.debug("relaunch the app, verify welcome flow")
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()

        logging.debug("verify pepto page contents")
        self.agreement.verify_agreementPage()
        self.agreement.verify_hp_privacy_statement_link()
        logging.debug("verify welcome flow after click YES button")
        self.agreement.click_yes_btn()
        self.agreement.verify_go_to_awc_flow()
        self.common_flows.close_HPSmart_app()

    def test_03_relaunch_app_and_verify_welcome_flow(self):
        '''
        TestRail:#C17451813
        This is a test case to verify welcome flow after clicking NO button
        '''
        smart_utility.delete_all_files(os.path.expanduser(self.file_path))
        logging.debug("relaunch the app, verify welcome flow after click NO button")
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.agreement.click_no_btn()
        self.agreement.verify_go_to_awc_flow()
        self.common_flows.close_HPSmart_app()


# ----------------      PRIVATE FUNCTION     --------------------------
    def verify_collects_analyzes_link(self):
        self.welcome.click_collects_analyzes_link()

        learn_more_about_hp_smart = Learn_More_About_HP_Smart(self.driver)
        learn_more_about_hp_smart.wait_for_screen_load()

        tool_bar = ToolBar(self.driver)
        tool_bar.click_back_btn()
