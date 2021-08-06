# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on set language dialog

@author: ten
@create_date: Dec 19, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SetLanguageWarningDialog(SmartScreens):

    folder_name = "common"
    flow_name = "set_language_warning_dialog"

    def __init__(self, driver):
        super(SetLanguageWarningDialog, self).__init__(driver)

#  -------------------------------Operate Elements------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[SetLanguageWarningDialog]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("set_language_title", timeout=timeout, raise_e=raise_e)

    def click_close_btn(self):
        '''
        This is a method to click Close button .
        :parameter:
        :return:
        '''
        logging.debug("[SetLanguageWarningDialog]:[close_btn]-Click Close button... ")

        self.driver.click("close_btn")

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[SetLanguageWarningDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("set_language_title")

    def get_value_of_dialog_contents(self):
        '''
        This is a method to get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[SetLanguageWarningDialog]:[get_value_of_set_language_content]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("set_language_content")

    def get_value_of_close_btn(self):
        '''
        This is a method to get value of close_btn
        :parameter:
        :return:
        '''
        logging.debug("[SetLanguageWarningDialog]:[get_value_of_close_btn]-Get the contents of dialog_contents ...  ")

        return self.driver.get_title("close_btn")

# -------------------------------Verification Methods-------------------------------
    def verify_set_language_warning_dialog(self):
        '''
        This is a verification method to check UI strings of Set Language Warning Dialog
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Unable to sign in dialog")
#         assert self.get_value_of_dialog_title() == u""
#         assert self.get_value_of_dialog_contents() == u""
#         assert self.get_value_of_close_btn() == u""
