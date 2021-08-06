# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
safari web app.

@author: Sophia
@create_date: May 27, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class WebAppScreen(SmartScreens):
    folder_name = "webapp"
    flow_name = "web_app_screen"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WebAppScreen, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self):
        pass

    def wait_for_do_you_want_to_allow_to_open_hp_smart_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for Do you want to allow to open HP Smart dialog load.
        '''
        logging.debug("[WebAppScreen]:[wait_for_do_you_want_to_allow_to_open_hp_smart_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("do_you_want_to_allow_to_open_hp_smart_dialog_allow_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_web_browser_address(self):
        '''
        This is a method to get value of web browser address
        :parameter:
        :return:
        '''
        logging.debug("[WebAppScreen]:[get_value_of_web_browser_address]-Get value of URL ...  ")

        return self.driver.get_value("web_browser_address")

    def click_do_you_want_to_allow_to_open_hp_smart_dialog_cancel_btn(self):
        '''
        This is a method to click Cancel button on Do you want to allow to open HP Smart dialog.
        :parameter:
        :return:
        '''
        logging.debug("[WebAppScreen]:[click_do_you_want_to_allow_to_open_hp_smart_dialog_cancel_btn]-Click Cancel button... ")

        self.driver.click("do_you_want_to_allow_to_open_hp_smart_dialog_cancel_btn")

    def click_do_you_want_to_allow_to_open_hp_smart_dialog_allow_btn(self):
        '''
        This is a method to click Allow button on Do you want to allow to open HP Smart dialog.
        :parameter:
        :return:
        '''
        logging.debug("[WebAppScreen]:[click_do_you_want_to_allow_to_open_hp_smart_dialog_allow_btn]-Click Allow button... ")

        self.driver.click("do_you_want_to_allow_to_open_hp_smart_dialog_allow_btn")
