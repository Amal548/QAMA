# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on No Internet Connection dialog.

@author: Ivan
@create_date: Oct 12, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class NoInternetConnectionDialog(SmartScreens):

    folder_name = "common"
    flow_name = "no_internet_connection_dialog"

    def __init__(self, driver):
        super(NoInternetConnectionDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait no Internet connection dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("no_internet_connection_title", timeout=timeout, raise_e=raise_e)

    def click_ok_btn(self):
        '''
        This is a method to click OK button on No Internet Connection dialog.
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[click_ok_btn]-Click ok_btn... ")

        self.driver.click("no_internet_connection_ok_btn")

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("no_internet_connection_title")

    def get_value_of_dialog_contents(self):
        '''
        This is a method to get value of contents_1
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[get_value_of_dialog_contents]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("no_internet_connnection_contents")

    def get_value_of_ok_btn(self):
        '''
        This is a method to get value of ok_btn
        :parameter:
        :return:
        '''
        logging.debug("[NoInternetConnectionDialog]:[get_value_of_ok_btn]-Get the contents of ok_btn ...  ")

        return self.driver.get_title("no_internet_connection_ok_btn")

# -------------------------------Verification Methods-------------------------------
    def verify_ui_string(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Verify strings are translated correctly and matching string table.")
#         assert self.get_value_of_dialog_title() == u""
#         assert self.get_value_of_dialog_contents() == u""
#         assert self.get_value_of_ok_btn() == u""
        pass

    def verify_dialog_disappear(self, timeout=10):
        '''
        verify No Internet Connection dialog disappear after clicking OK button.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("no_internet_connection_title", timeout=timeout, raise_e=False)
