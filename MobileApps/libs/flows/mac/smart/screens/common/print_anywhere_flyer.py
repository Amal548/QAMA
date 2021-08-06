# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the print anywhere flyer.

@author: Sophia
@create_date: May 21, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from selenium.common.exceptions import TimeoutException


class PrintAnywhereFlyer(SmartScreens):
    folder_name = "common"
    flow_name = "print_anywhere_flyer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrintAnywhereFlyer, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait print anywhere flyer shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[PrintAnywhereFlyer]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_anywhere_dialog_title", timeout=timeout, raise_e=raise_e)

    def click_close_btn(self):
        '''
        This is a method to click close button on the print anywhere flyer.
        :parameter:
        :return:
        '''
        logging.debug("[PrintAnywhereFlyer]:[click_close_btn]-Click 'Close' button... ")

        self.driver.click("close_btn", is_native_event=True)

    def click_get_started_btn(self):
        '''
        This is a method to click Get Started
        :parameter:
        :return:
        '''
        logging.debug("[PrintAnywhereDialog]:[get_started_button]-Click 'get_started' button... ")

        self.driver.click("get_started_btn")

    def get_value_of_print_anywhere_dialog_title(self):
        '''
        get_value_of_print_anywhere_dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[PrintAnywhereDialog]:[get_value_of_print_anywhere_dialog_title]-Get the contents of print_anywhere_dialog_title ...  ")

        return self.driver.get_value("print_anywhere_dialog_title")

    def get_value_of_print_anywhere_contents(self):
        '''
        get_value_of_print_anywhere_contents
        :parameter:
        :return:
        '''
        logging.debug("[PrintAnywhereDialog]:[get_value_of_print_anywhere_contents]-Get the contents of print_anywhere_contents ...  ")

        return self.driver.get_value("print_anywhere_contents")

    def get_value_of_get_started_btn(self):
        '''
        get_value_of_get_started_btn
        :parameter:
        :return:
        '''
        logging.debug("[PrintAnywhereDialog]:[get_value_of_get_started_btn]-Get the contents of get_started_btn ...  ")

        return self.driver.get_title("get_started_btn")


# -------------------------------Verification Methods-------------------------------------------
    # def verify_ui_string(self):
    #     '''
    #     verify_ui_string
    #     :parameter:
    #     :return:
    #     '''
    #     logging.debug("Verify strings are translated correctly and matching string")
#         assert self.get_value_of_print_anywhere_dialog_title() == u""
#         assert self.get_value_of_print_anywhere_contents() == u""
#         assert self.get_value_of_get_started_btn() == u""

    def verify_print_anywhere_dialog_no_display(self, timeout=10):
        '''
        verify_print_anywhere_dialog_no_display
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("print_anywhere_dialog_title", timeout=timeout, raise_e=False)
