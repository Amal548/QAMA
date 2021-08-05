# encoding: utf-8
'''
It defines the operations of element and verification methods on Sign in hp account dialog.

@author: ten
@create_date: Sep 10, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SigninDialog(SmartScreens):

    folder_name = "hpid"
    flow_name = "sign_in_dialog"

    def __init__(self, driver):
        super(SigninDialog, self).__init__(driver)

#   -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for User name input box load on Sign in dialog.
        '''
        logging.debug("[ClassName]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_in_dialog_username_inputbox", timeout=timeout, raise_e=raise_e)

    def wait_for_sign_in_dialog_password_inputbox_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[SigninDialog]:[wait_for_sign_in_dialog_password_inputbox_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_in_dialog_password_inputbox", timeout=timeout, raise_e=raise_e)

    def input_username_inputbox(self, contents):
        '''
        This is a method to Input User name on Sign In dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SigninDialog]:[input_username_inputbox]-Input User name on Sign In dialog... ")

        self.driver.send_keys("sign_in_dialog_username_inputbox", contents, press_enter=True)

    def input_password_inputbox(self, contents):
        '''
        This is a method to Input Password on Sign In dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SigninDialog]:[input_password_inputbox]-Input Password on Sign In dialog... ")

        self.driver.send_keys("sign_in_dialog_password_inputbox", contents, press_enter=True)

    def click_sign_in_dialog_next_btn(self):
        '''
        This is a method to click Next button on Sign In dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SigninDialog]:[click_sign_in_dialog_next_btn]-Click Next button on Sign In dialog... ")

        self.driver.click("sign_in_dialog_next_btn")

    def click_sign_in_dialog_sign_in_btn(self):
        '''
        This is a method to click Sign In button on Sign In dialog
        :parameter:
        :return:
        '''
        logging.debug("[SigninDialog]:[click_sign_in_dialog_sign_in_btn]-Click Sign In button on Sign In dialog... ")

        self.driver.click("sign_in_dialog_sign_in_btn")

    def click_sign_in_dialog_close_btn(self):
        '''
        This is a method to click Close button on Sign In dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SigninDialog]:[click_sign_in_dialog_close_btn]-Click Close button... ")

        self.driver.click("sign_in_dialog_close_btn")

# -------------------------------Verification Methods-----------------------------------
    def verify_dialog_disappear(self, timeout=30):
        '''
        This is a verification method to verify Sign in dialog disappear after sign in/out successfully or close it.
        :parameter:
        :return:
        '''
        return self.driver.wait_for_object_disappear("sign_in_dialog_close_btn", timeout=timeout, raise_e=False)
