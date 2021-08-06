# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the save dialog.

@author: Sophia
@create_date: May 8, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SaveDialog(SmartScreens):
    folder_name = "common"
    flow_name = "save_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(SaveDialog, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait save dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[SaveFileDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("save_as_text_field", timeout=timeout, raise_e=raise_e)

    def click_save_btn(self):
        '''
        This is a method to click save button.
        :parameter:
        :return:
        '''
        logging.debug("[SaveFileDialog]:[click_save_btn]-Click 'Save' button... ")

        self.driver.click("save_btn")

    def click_ok_btn_file_saved_sheet(self):
        '''
        This is a method to click OK button on the file saved sheet.
        :parameter:
        :return:
        '''
        logging.debug("[SaveFileDialog]:[click_ok_btn_file_saved_sheet]-Click 'OK' button on the file saved sheet... ")

        self.driver.click("ok_btn_sheet")

# -------------------------------Verification Methods--------------------------
