# encoding: utf-8
'''
Description: no printer printer settings dialog

@author: Ten
@create_date: Oct 15, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class No_Printer_Settings_Dialog(SmartScreens):

    folder_name = "common"
    flow_name = "no_printer_settings_dialog"

    def __init__(self, driver):
        super(No_Printer_Settings_Dialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[OpenFileDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_ok_btn(self):
        '''
        This is a method to click ok button.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_ok_btn]-Click ok_btn... ")

        self.driver.click("ok_btn", is_native_event=True)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_dialog_title]-Get dialog_title...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_ok_btn(self):
        '''
        This is a method to get value of ok_btn
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_ok_btn]-Get ok_btn..  ")

        return self.driver.get_title("ok_btn")

# -------------------------------Verification Methods---------------------------------------
    def verify_ui_string(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
        assert self.get_value_of_dialog_title() == "To use this feature, first select a printer."
        assert self.get_value_of_ok_btn() == "OK"
