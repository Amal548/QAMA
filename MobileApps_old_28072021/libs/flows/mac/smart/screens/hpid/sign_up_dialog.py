# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Sign up hp account dialog.

@author: Ivan
@create_date: Sep 30, 2019
@update_date: Aug 24, 2020
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SignUpDialog(SmartScreens):

    folder_name = "hpid"
    flow_name = "sign_up_dialog"

    def __init__(self, driver):
        super(SignUpDialog, self).__init__(driver)

#   -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Sign Up dialog load.
        '''
        logging.debug("[SignUpDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("first_name_textfield", timeout=timeout, raise_e=raise_e)

    def input_first_name(self, contents):
        '''
        This is a method to Input First name on Sign Up dialog.
        :parameter: contents - The contents that input into the textfield
        :return:
        '''
        logging.debug("[SignUpDialog]:[input_first_name]-Input First name on Sign Up dialog... ")

        self.driver.send_keys("first_name_textfield", contents)

    def input_last_name(self, contents):
        '''
        This is a method to Input Last name on Sign Up dialog.
        :parameter: contents - The contents that input into the textfield
        :return:
        '''
        logging.debug("[SignUpDialog]:[input_last_name]-Input Last name on Sign Up dialog... ")

        self.driver.send_keys("last_name_textfield", contents)

    def input_email_address(self, contents):
        '''
        This is a method to Input Email address on Sign Up dialog.
        :parameter: contents - The contents that input into the textfield
        :return:
        '''
        logging.debug("[SignUpDialog]:[input_email_address]-Input Email address on Sign Up dialog... ")

        self.driver.send_keys("email_address_textfield", contents)

    def input_phone_number(self, contents):
        '''
        This is a method to Input Phone Number on Sign Up dialog.
        :parameter: contents - The contents that input into the textfield
        :return:
        '''
        logging.debug("[SignUpDialog]:[input_phone_number]-Input Phone Number on Sign Up dialog... ")

        self.driver.send_keys("phone_number_textfield", contents)

    def input_password(self, contents):
        '''
        This is a method to Input Password on Sign Up dialog.
        :parameter: contents - The contents that input into the textfield
        :return:
        '''
        logging.debug("[SignUpDialog]:[input_password]-Input Password on Sign Up dialog... ")

        self.driver.send_keys("password_textfield", contents)

    def input_confirm_password(self, contents):
        '''
        This is a method to Input Confirm Password on Sign Up dialog.
        :parameter: contents - The contents that input into the textfield
        :return:
        '''
        logging.debug("[SignUpDialog]:[input_confirm_password]-Input Confirm Password on Sign Up dialog... ")

        self.driver.send_keys("confirm_password_textfield", contents)

    def click_email_address_textfield(self):
        '''
        This is a method to click Email Address text field on Sign up dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignUpDialog]:[click_email_address_textfield]-Click Email Address text field... ")

        self.driver.click("email_address_textfield")

    def click_hp_may_email_me_checkbox(self):
        '''
        This is a method to click HP may email me check box on Sign up dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignUpDialog]:[click_hp_may_email_me_checkbox]-Click HP may email me check box... ")

        self.driver.click("hp_may_email_me_checkbox")

    def click_create_account_btn(self):
        '''
        This is a method to click Create Account button on Sign up dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignUpDialog]:[click_create_account_btn]-Click Create Account button... ")

        self.driver.scroll_on_app()
        sleep(1)
        self.driver.click("create_account_btn")

    def click_already_have_an_hp_account_sign_in_btn(self):
        '''
        This is a method to Scroll and Click Already have an HP account? Sign in button on Sign up dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignUpDialog]:[click_already_have_an_hp_account_sign_in_btn]-Click Already have an HP account? Sign in button... ")

        self.driver.scroll_on_app()
        sleep(1)
        self.driver.click("already_have_an_hp_account_sign_in_btn", is_native_event=True)

    def click_close_btn(self):
        '''
        This is a method to click close button on Sign up dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignUpDialog]:[click_close_btn]-Click 'Close' button... ")

        self.driver.click("close_btn", is_native_event=True)

# -------------------------------Verification Methods-----------------------------------
