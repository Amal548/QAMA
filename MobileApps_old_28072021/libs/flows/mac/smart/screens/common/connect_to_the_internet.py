# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on No Connect to the Internet screen.

@author: ten
@create_date: Aug 13, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class ConnecttotheInternet(SmartScreens):

    folder_name = "common"
    flow_name = "connect_to_the_internet"

    def __init__(self, driver):
        super(ConnecttotheInternet, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait no Internet connection dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ConnecttotheInternet]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click Continue button
        :parameter:
        :return:
        '''
        logging.debug("[ConnecttotheInternet]:[click_continue_btn]-Click continue_btn... ")

        self.driver.click("continue_btn")

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[ConnecttotheInternet]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_contents(self):
        '''
        This is a method to get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[ConnecttotheInternet]:[get_value_of_dialog_contents]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("dialog_content_text")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of ok_btn
        :parameter:
        :return:
        '''
        logging.debug("[ConnecttotheInternet]:[get_value_of_ok_btn]-Get the contents of ok_btn ...  ")

        return self.driver.get_title("continue_btn")

# -------------------------------Verification Methods-------------------------------
    def verify_ui_string(self):
        '''
        This is a verification method to check UI strings of No Internet Connection dialog
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of No Internet Connection dialog")
#         assert self.get_value_of_dialog_title() == u""
#         assert self.get_value_of_dialog_contents() == u""
#         assert self.get_value_of_continue_btn() == u""

    def verify_dialog_disappear(self):
        '''
        verify No Internet Connection dialog disappear after clicking OK button.
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("dialog_title", raise_e=False):
            raise UnexpectedItemPresentException("the screen display")
        return True
