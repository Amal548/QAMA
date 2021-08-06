# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the choose a printer sheet.

@author: Sophia
@create_date: May 21, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ChooseAPrinterSheet(SmartScreens):
    folder_name = "common"
    flow_name = "choose_a_printer_sheet"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ChooseAPrinterSheet, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait choose a printer sheet shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("choose_a_printer_title", timeout=timeout, raise_e=raise_e)

    def click_skip_btn(self):
        '''
        This is a method to click skip button.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseAPrinterSheet]:[click_skip_btn]-Click 'Skip' button... ")

        self.driver.click("skip_btn")

# -------------------------------Verification Methods--------------------------
