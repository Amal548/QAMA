# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the forget this printer screen.

@author: ten
@create_date: Nov 20, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_setting_scroll import PrinterSettingScroll


class ForgetThisPrinter(PrinterSettingScroll, SmartScreens):
    folder_name = "printersettings"
    flow_name = "forget_this_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ForgetThisPrinter, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait print from other devices screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[ForgetThisPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("forget_this_printer_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_forget_this_printer_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait print from other devices screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[ForgetThisPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("forget_this_printer_dialog_title", timeout=timeout, raise_e=raise_e)

    def click_forget_this_print_btn(self):
        '''
        This is a method to click Forget this printer button.
        :parameter:
        :return:
        '''
        logging.debug("[ForgetThisPrinter]:[click_forget_this_print_btn]-Click Forget this printer button... ")

        self.driver.click("forget_this_printer_btn")

    def click_forget_printer_dialog_btn(self):
        '''
        This is a method to click Forget printer button.
        :parameter:
        :return:
        '''
        logging.debug("[ForgetThisPrinter]:[click_forget_print_btn]-Click Forget printer button... ")

        self.driver.click("forget_printer_dialog_btn")

# -------------------------------Verification Methods--------------------------
