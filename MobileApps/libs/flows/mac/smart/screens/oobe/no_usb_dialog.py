# encoding: utf-8
'''
check No USB dialog

@author: ten
@create_date: Aug 23, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class NoUSBDialog(SmartScreens):

    folder_name = "oobe"
    flow_name = "no_usb_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(NoUSBDialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[NoUSBDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_done_btn(self):
        '''
        Click done button
        :parameter:
        :return:
        '''
        logging.debug("[NoUSBDialog]:[click_done_btn]-click_done_btn.. ")

        self.driver.click("done_btn")

# -------------------------------Verification Methods--------------------------------------------
