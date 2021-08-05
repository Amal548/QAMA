# encoding: utf-8
'''
It defines the operations of element and verification methods on To Sign in and Signing Out dialog for Mac os 10.14 and lower.

@author: Ivan
@create_date: Aug 25, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ToSignInAndSigningOutDialog(SmartScreens):

    folder_name = "hpid"
    flow_name = "to_sign_in_and_signing_out_dialog"

    def __init__(self, driver):
        super(ToSignInAndSigningOutDialog, self).__init__(driver)

#   -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for To Sign In dialog or Signing out Dialog load.
        '''
        logging.debug("[ToSignInAndSigningOutDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("to_sign_in_and_signing_out_dialog_title", timeout=timeout, raise_e=raise_e)

    def click_dialog_continue_btn(self):
        '''
        This is a method to click Continue button on To Sign In dialog or Signing out dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ToSignInAndSigningOutDialog]:[click_dialog_continue_btn]-Click Continue button... ")

        self.driver.click("to_sign_in_and_signing_out_dialog_continue_btn", is_native_event=True)

    def click_dialog_cancel_btn(self):
        '''
        This is a method to click Cancel button on To Sign In dialog or Signing out dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ToSignInAndSigningOutDialog]:[click_dialog_cancel_btn]-Click Cancel button... ")

        self.driver.click("to_sign_in_and_signing_out_dialog_cancel_btn", is_native_event=True)

# -------------------------------Verification Methods-----------------------------------
    def verify_dialog_disappear(self, timeout=30):
        '''
        This is a verification method to verify To Sign In dialog or Signing out dialog disappear after clicking Continue or Cancel button.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object_disappear("to_sign_in_and_signing_out_dialog_continue_btn", timeout=timeout, raise_e=False)
