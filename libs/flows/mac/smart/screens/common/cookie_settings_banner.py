# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Cookie Settings Banner.

@author:Ivan
@create_date: Aug 26, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class CookieSettingsBanner(SmartScreens):
    folder_name = "common"
    flow_name = "cookie_settings_banner"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(CookieSettingsBanner, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Cookie Settings Banner load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[CookieSettingsBanner]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("cookie_settings_banner_title", timeout=timeout, raise_e=raise_e)

    def click_cookie_settings_banner_cookie_settings_btn(self):
        '''
        This is a method to click Cookie Settings button on Cookie Settings Banner.
        :parameter:
        :return:
        '''
        logging.debug("[CookieSettingsBanner]:[click_cookie_settings_banner_cookie_settings_btn]-Click Cookie Settings button.. ")

        self.driver.click("cookie_settings_banner_cookie_settings_btn")

    def click_cookie_settings_banner_accept_all_cookies_btn(self):
        '''
        This is a method to click Accept All Cookies button on Cookie Settings Banner.
        :parameter:
        :return:
        '''
        logging.debug("[CookieSettingsBanner]:[click_cookie_settings_banner_accept_all_cookies_btn]-Click Accept All Cookies button.. ")

        self.driver.click("cookie_settings_banner_accept_all_cookies_btn")

    def click_cookie_settings_banner_close_btn(self):
        '''
        This is a method to click Close button on Cookie Settings Banner.
        :parameter:
        :return:
        '''
        logging.debug("[CookieSettingsBanner]:[click_cookie_settings_banner_close_btn]-Click Close button.. ")

        self.driver.click("cookie_settings_banner_close_btn")

# -------------------------------Verification Methods--------------------------
