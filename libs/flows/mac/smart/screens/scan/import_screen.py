# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the import screen.

@author: Sophia
@create_date: May 8, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ImportScreen(SmartScreens):
    folder_name = "scan"
    flow_name = "import"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ImportScreen, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait import screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ImportScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("apply_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_first_import_dialog(self, timeout=30, raise_e=True):
        '''
        This is a method to wait first import sheet shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ImportScreen]:[wait_for_first_import_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("first_import_title", timeout=timeout, raise_e=raise_e)

    def click_apply_btn(self):
        '''
        This is a method to click apply button.
        :parameter:
        :return:
        '''
        logging.debug("[ImportScreen]:[click_apply_btn]-Click 'Apply' button... ")

        self.driver.click("apply_btn")

    def click_ok_btn_on_first_import_sheet(self):
        '''
        This is a method to click OK button on the first import sheet.
        :parameter:
        :return:
        '''
        logging.debug("[ImportScreen]:[click_ok_btn_on_first_import_sheet]-Click 'OK' button on first import sheet... ")

        self.driver.click("ok_btn_first_import_sheet")

# -------------------------------Verification Methods--------------------------
