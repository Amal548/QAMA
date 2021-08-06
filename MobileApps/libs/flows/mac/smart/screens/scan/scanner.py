# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the scanner screen.

@author: Sophia
@create_date: May 8, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class Scanner(SmartScreens):
    folder_name = "scan"
    flow_name = "scanner"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(Scanner, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait scanner screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug(
            "[ScannerScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("scan_btn", timeout=timeout, raise_e=raise_e)

    def click_import_btn(self):
        '''
        This is a method to click import button.
        :parameter:
        :return:
        '''
        logging.debug(
            "[ScannerScreen]:[click_import_btn]-Click 'Import' button... ")

        self.driver.click("import_btn")

    def click_scan_btn(self):
        '''
        This is a method to click scan button.
        :parameter:
        :return:
        '''
        logging.debug(
            "[ScannerScreen]:[click_scan_btn]-Click 'Scan' button... ")

        self.driver.click("scan_btn")

# -------------------------------Verification Methods--------------------------
