#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: This is a test case for Help & Support function testing.

@author: Ivan
@create_date: Sep 17, 2019
'''
import os
import logging
import pytest
from selenium import webdriver
from time import sleep

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.helpsupport.help_support import HelpSupport
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar

pytest.app_info = "DESKTOP"


class Test_Suite_01_Help_Support(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.main_ui = MainUI(self.driver)
        self.tool_bar = ToolBar(self.driver)
        self.help_support = HelpSupport(self.driver)
        self.browser = webdriver.Safari(executable_path='/usr/bin/safaridriver')
        self.appname = smart_const.APP_NAME.SMART
        self.printer = {"printerBonjourName": "HP ENVY Photo 7800 series [093B66]", "printerIP": "192.168.10.186"}
        self.log_path = os.path.expanduser('~/Library/Containers/com.hp.SmartMac/Data/Library/Application Support/HP Smart/HP Smart.log')  # "/Users/itest/Library/Containers/com.hp.SmartMac/Data/Library/Application Support/HP Smart"
        self.URL = "Payload URL: https://www.hpsmartstage.com/us/en/in-app-help/desktop"
        self.URL2 = "ret payload:{\"chatbotLink\":{\"href\":\"https://virtualagent-dev.hpcloud.hp.com?botclient=hpsmart&botsubclient=mac&LaunchPoint=HelpCenter"
        self.URL3 = "http://h20180.www2.hp.com/apps"

    def test_01_precondition_reset_hp_smart_data(self):
        '''
        This is a precondition to reset the data of HP smart. Make sure cookies banner can be showed at the first time.
        '''
        # TODO

    def test_02_help_support_no_printer_added(self):
        '''
        TestRail: #C14715638
        (No Printer Added) Click "Help Center" tile on the Main UI, Verify WebView opens within the HP Smart.
        '''
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.main_ui.click_help_center_tile()
        self.help_support.wait_for_screen_load(120)
        self.help_support.wait_for_cookies_banner_screen(120)
#         self.help_support.click_close_on_cookies_banner()
        # GOTH-8021
        self.help_support.wait_for_screen_load()
        self.tool_bar.click_home_btn()
        self.main_ui.wait_for_screen_load()

    def test_03_help_support_with_printer_added(self):
        '''
        TestRail: #C15991975
        Click 'Help Center' Tile on the Main UI, Verify the help center web view opens within the app.
        '''
        self.common_flows.add_printer_to_carousel(self.printer, is_first_add=True, is_skip_ows=True)
        self.main_ui.click_help_center_tile()
        logging.debug("TestRail: C14715626 -> (ENU only) Check 'Chat with Virtual Agent' link on list view, verify 'Chat with Virtual Agent' link shows in the help center web view")
        self.help_support.verify_virtual_agent_information_enu
        self.help_support.wait_for_cookies_banner_screen(120)
        logging.debug("Verify correct URL shows in the Gotham log.")
        f = open(self.log_path, 'r')
#        f.encoding = 'utf-8'
        for line in f.readlines():
            if self.URL in line:
                print (line)
            else:
                print ("The expected URL does not show in the Gotham log")
            break
        f.close()
        logging.debug("TestRail: C14779127 -> Click X on the accept cookie banner, verify accept cookies shows every time whenever you launch the help center")
        self.help_support.click_close_on_cookies_banner()
        self.tool_bar.click_home_btn()
        self.main_ui.wait_for_screen_load()
        self.main_ui.click_help_center_tile()
        self.help_support.wait_for_cookies_banner_screen(120)

        logging.debug("TestRail: C14779128 -> Click Accept Cookies on accept cookie banner, verify accept cookies doesn't show every time whenever you launch the help center")
        self.help_support.click_accept_cookies_on_cookies_banner()
        logging.debug("TestRail: C14715624 -> Click back arrow, verify user navigates to the HP Smart home page")
        self.tool_bar.click_back_btn()
        self.main_ui.wait_for_screen_load()
        self.main_ui.click_help_center_tile()
        self.help_support.wait_for_screen_load(120)
        self.help_support.verify_accept_cookies_banner_does_not_show(120)

    def test_04_click_chat_with_virtual_agent_link(self):
        '''
        TestRail: #C14715627, #C14715628
        (No Internet) Click "Chat with Virtual Agent" link, verify Gotham log shows correct URL。
        (English only) Click "Chat with Virtual Agent" link, verify virtual agent chat window opens in the web browser.
        '''
        self.help_support.click_chat_with_virtual_agent_link()
        sleep(5)
        logging.debug("Verify correct Website opens in the external web browser")
        assert ("Virtual Agent" in self.browser.title)
        os.system("pkill Safari")

        logging.debug("Disconnect computer network")
        os.system("networksetup -setairportpower en1 off")
        self.help_support.click_chat_with_virtual_agent_link()
        sleep(5)
        os.system("pkill Safari")
        logging.debug("Verify correct URL shows in the Gotham log line check for 'SupportViewModel: GenerateHelpCenterPayload' with 'ret payload:' in the logs")
        f = open(self.log_path, 'r')
        for line in f.readlines():
            if self.URL2 in line:
                print (line)
            else:
                print ("The expected URL does not show in the Gotham log")
            break
        f.close()
        logging.debug("Reconnect computer network")
        os.system("networksetup -setairportpower en1 on")

    def test_05_click_other_options_on_list_view(self):
        '''
        TestRail: #C14715630, #C14715631, #C14715632, #C14715633, #C14715635
        Click 'Print Support' / 'Print Anywhere Online Support' / 'Smart Tasks Online Support' / 'HP Mobile Printing' / 'Contact HP' on the list view. verify correct website opens in external web browser.
        '''
        self.help_support.select_printer_support_item()
        assert ("Untitled" in self.browser.title)
        os.system("pkill Safari")
        logging.debug("Verify correct URL shows in the Gotham log line check for 'SupportViewModel: GenerateHelpCenterPayload' with 'ret payload:' in the logs")
        f = open(self.log_path, 'r')
        for line in f.readlines():
            if self.URL3 in line:
                print (line)
            else:
                print ("The expected URL does not show in the Gotham log")
            break
        f.close()

        self.help_support.select_print_anywhere_online_support_item()
        sleep(5)
        assert("HP Printers - Print Anywhere with the HP Smart App" in self.browser.title)
        os.system("pkill Safari")

        self.help_support.select_smart_tasks_online_support_item()
        sleep(5)
        assert("HP Printers - HP Smart: Using Smart Tasks" in self.browser.title)
        os.system("pkill Safari")

        self.help_support.select_hp_mobile_printing()
        sleep(5)
        assert("HP Mobile Printing from a Smartphone or Tablet" in self.browser.title)
        os.system("pkill Safari")

        self.help_support.select_contact_hp()
        sleep(5)
        assert("Contact HP Customer Support" in self.browser.title)
        os.system("pkill Safari")

    def test_06_help_support_without_internet_connection(self):
        '''
        TestRail: #C14721035, #C14721036, #C14721037, #C14721038
        Click 'Help Center' tile on the Main UI without Internet connection, verify 'No Internet Connection' dialog shows, Check UI/String.
        '''
        self.tool_bar.click_home_btn()
        self.main_ui.wait_for_screen_load()
        os.system("networksetup -setairportpower en1 off")
        self.main_ui.click_help_center_tile()
        self.help_support.wait_for_no_internet_connection_screen_load()
        logging.debug("Click OK button on No Internet Connection dialog, verify dialog got dismissed.")
        self.help_support.click_ok_on_no_internet_connection_dialog()
        self.main_ui.wait_for_screen_load()
        os.system("networksetup -setairportpower en1 on")
        self.common_flows.close_HPSmart_app()
