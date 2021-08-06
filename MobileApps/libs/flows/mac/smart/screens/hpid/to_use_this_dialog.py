# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on To Use This.. dialog.

@author: ten
@create_date: Jan 19, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ToUseThisDialog(SmartScreens):

    folder_name = "hpid"
    flow_name = "to_use_this_dialog"

    def __init__(self, driver):
        super(ToUseThisDialog, self).__init__(driver)

    #   ------------------------------Operate Elements---------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[ToUseThisDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("contents", timeout=timeout, raise_e=raise_e)

    def get_value_of_contents(self):
        '''
        This is a method to get value of contents.
        :parameter:
        :return:
        '''
        logging.debug("[ToUseThisDialog]:[get_value_of_contents]-Get the contents of contents  ...  ")

        return self.driver.get_value("contents")

    def get_value_of_ok_btn(self):
        '''
        This is a method to get value of ok button.
        :parameter:
        :return:
        '''
        logging.debug("[ToUseThisDialog]:[get_value_of_ok_btn-Get the contents of ok_btn  ...  ")

        return self.driver.get_title("ok_btn")

    def click_ok_btn(self):
        '''
        This is a method to click ok button.
        :parameter:
        :return:
        '''
        logging.debug("[ToUseThisDialog]:[click_ok_btn]-Click 'ok' button... ")

        self.driver.click("ok_btn")
    #   -------------------------------Verification Methods-------------------------------------
    def verify_ui_string(self):
        '''
        verify UI string for dialog
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
#         assert self.get_value_of_contents() == u""
#         assert self.get_value_of_ok_btn() == u""
