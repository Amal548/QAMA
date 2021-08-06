# encoding: utf-8
'''
It defines the operations of element and verification methods on Sign out hp account dialog.

@author: ten
@create_date: Sep 11, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SignoutDialog(SmartScreens):

    folder_name = "hpid"
    flow_name = "sign_out_dialog"

    def __init__(self, driver):
        super(SignoutDialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[SignoutDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_out_dialog_title", timeout=timeout, raise_e=raise_e)

    def wait_for_sign_out_safari_dialog_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[SignoutDialog]:[wait_for_sign_out_safari_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_out_safari_dialog_we_are_logging_out_text", timeout=timeout, raise_e=raise_e)

    def click_sign_out_btn(self):
        '''
        This is a method to click sign out button.
        :parameter:
        :return:
        '''
        logging.debug("[SignoutDialog:[click_sign_out_btn]-Click 'sign_out' button... ")

        self.driver.click("sign_out_btn", is_native_event=True)

# -------------------------------Verification Methods-----------------------------------

    def verify_dialog_disappear(self, timeout=30):
        '''
        This is a verification method to verify Sign out dialog disappear after sign out successfully.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object_disappear("sign_out_safari_dialog_we_are_logging_out_text", timeout=timeout, raise_e=False)