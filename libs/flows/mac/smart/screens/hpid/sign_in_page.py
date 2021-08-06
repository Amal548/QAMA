# encoding: utf-8
'''
It defines the operations of element and verification methods on Sign In Page.

@author: Ivan
@create_date: Aug 05, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SignInPage(SmartScreens):

    folder_name = "hpid"
    flow_name = "sign_in_page"

    def __init__(self, driver):
        super(SignInPage, self).__init__(driver)

#   -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Sign in page load.
        '''
        logging.debug("[SignInPage]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_in_page_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_sign_in_page_title(self):
        '''
        This is a method to get the value of Sign in Page title.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[get_value_of_sign_in_page_title]-Get the value of Sign in Page title...  ")

        return self.driver.get_value("sign_in_page_title")

    def get_value_of_sign_in_page_content(self):
        '''
        This is a method to get the value of Sign in Page content.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[get_value_of_sign_in_page_content]-Get the value of Sign in Page content...  ")

        return self.driver.get_value("sign_in_page_content")

    def get_value_of_sign_in_page_create_account_btn(self):
        '''
        This is a method to get the value of Create Account button on Sign in Page.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[get_value_of_sign_in_page_create_account_btn]-Get the value of Create Account button...  ")

        return self.driver.get_title("sign_in_page_create_account_btn")

    def get_value_of_sign_in_page_sign_in_btn(self):
        '''
        This is a method to get the value of Sign In button on Sign in Page.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[get_value_of_sign_in_page_sign_in_btn]-Get the value of Sign In button...  ")

        return self.driver.get_title("sign_in_page_sign_in_btn")

    def get_value_of_sign_in_page_close_btn(self):
        '''
        This is a method to get the value of Close button on Sign in Page.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[get_value_of_sign_in_page_close_btn]-Get the value of Close button...  ")

        return self.driver.get_value("sign_in_page_close_btn")

    def click_sign_in_page_create_account_btn(self):
        '''
        This is a method to click Create Account button on Sign in Page.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[click_sign_in_page_create_account_btn]-Click Create Account button... ")

        self.driver.click("sign_in_page_create_account_btn", is_native_event=True)

    def click_sign_in_page_sign_in_btn(self):
        '''
        This is a method to click Sign In button on Sign in Page.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[click_sign_in_page_sign_in_btn]-Click Sign In button... ")

        self.driver.click("sign_in_page_sign_in_btn", is_native_event=True)

    def click_sign_in_page_close_btn(self):
        '''
        This is a method to click Close button on Sign in Page.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[click_sign_in_page_close_btn]-Click Close button... ")

        self.driver.click("sign_in_page_close_btn", is_native_event=True)

    def click_sign_in_page_set_up_printer_btn(self):
        '''
        This is a method to click Set up printer button on Sign in Page.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[click_sign_in_page_set_up_printer_btn]-Click Set up printer button... ")

        self.driver.click("sign_in_page_set_up_printer_btn", is_native_event=True)

    def click_sign_in_page_explore_hp_smart_btn(self):
        '''
        This is a method to click Explore HP Smart button on Sign in Page.
        :parameter:
        :return:
        '''
        logging.debug("[SignInPage]:[click_sign_in_page_explore_hp_smart_btn]-Click Explore HP Smart button... ")

        self.driver.click("sign_in_page_explore_hp_smart_btn", is_native_event=True)

# -------------------------------Verification Methods-----------------------------------
    def verify_sign_in_page(self):
        '''
        This is a verification method to check UI strings of Sign in Page.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Sign in Page")
#         assert self.get_value_of_sign_in_page_title() == ""
#         assert self.get_value_of_sign_in_page_content() == ""
#         assert self.get_value_of_sign_in_page_create_account_btn() == ""
#         assert self.get_value_of_sign_in_page_sign_in_btn() == ""
#         assert self.get_value_of_sign_in_page_close_btn() == ""
