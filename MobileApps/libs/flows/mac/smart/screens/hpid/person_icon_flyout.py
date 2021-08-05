# encoding: utf-8
'''
It defines the operations of element and verification methods on Person Icon Flyout.

@author: Ivan
@create_date: Aug 24, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PersonIconFlyout(SmartScreens):

    folder_name = "hpid"
    flow_name = "person_icon_flyout"

    def __init__(self, driver):
        super(PersonIconFlyout, self).__init__(driver)

#   -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Person Icon Flyout load before Sign in
        '''
        logging.debug("[PersonIconFlyout]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("create_account_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_sign_in(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Person Icon Flyout load after Sign in
        :parameter:
        :return:
        '''
        logging.debug("[PersonIconFlyout]:[wait_for_screen_load_sign_in]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_out_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_your_hp_account_offers_text(self):
        '''
        This is a method to get the value of Your HP Accounter offers text on Person Icon flyout before Sign in.
        :parameter:
        :return:
        '''
        logging.debug("[PersonIconFlyout]:[get_value_of_your_hp_account_offers_text]-Get the value of Your HP Accounter offers text...  ")

        return self.driver.get_value("your_hp_account_offers_text")

    def get_value_of_create_account_btn(self):
        '''
        This is a method to get the value of Create Account button on Person Icon flyout before Sign in.
        :parameter:
        :return:
        '''
        logging.debug("[PersonIconFlyout]:[get_value_of_create_account_btn]-Get the value of Create Account button...  ")

        return self.driver.get_title("create_account_btn")

    def get_value_of_hi_text(self):
        '''
        This is a method to get the value of Hi text on Person Icon flyout after sign in.
        :parameter:
        :return:
        '''
        logging.debug("[PersonIconFlyout]:[get_value_of_hi_text]-Get the value of Hi text...  ")

        return self.driver.get_value("hi_text")

    def get_value_of_my_hp_account_btn(self):
        '''
        This is a method to get the value of My HP Account button on Person Icon flyout after sign in.
        :parameter:
        :return:
        '''
        logging.debug("[PersonIconFlyout]:[get_value_of_my_hp_account_btn]-Get the value of My HP Account button...  ")

        return self.driver.get_title("my_hp_account_btn")

    def get_value_of_sign_out_btn(self):
        '''
        This is a method to get the value of Sign out button on Person Icon flyout after sign in.
        :parameter:
        :return:
        '''
        logging.debug("[PersonIconFlyout]:[get_value_of_sign_out_btn]-Get the value of Sign out button...  ")

        return self.driver.get_title("sign_out_btn")

    def click_create_account_btn(self):
        '''
        This is a method to click Create Account button on Person Icon flyout before sign in HP Account.
        :parameter:
        :return:
        '''
        logging.debug("[PersonIconFlyout]:[click_create_account_btn]-Click Create Account button... ")

        self.driver.click("create_account_btn", is_native_event=True)

    def click_my_hp_account_btn(self):
        '''
        This is a method to click My HP Account button on Person Icon flyout after sign in HP Account.
        :parameter:
        :return:
        '''
        logging.debug("[PersonIconFlyout]:[click_my_hp_account_btn]-Click My HP Account button... ")

        self.driver.click("my_hp_account_btn", is_native_event=True)

    def click_sign_out_btn(self):
        '''
        This is a method to click Sign Out button on Person Icon flyout after sign in HP Account.
        :parameter:
        :return:
        '''
        logging.debug("[PersonIconFlyout]:[click_sign_out_btn]-Click Sign Out button... ")

        self.driver.click("sign_out_btn", is_native_event=True)

# -------------------------------Verification Methods-----------------------------------
    def verify_person_icon_flyout_before_sign_in(self):
        '''
        This is a verification method to check UI strings of Person Icon Flyout before sign in.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Person Icon Flyout before sign in")
#         assert self.get_value_of_your_hp_account_offers_text() == ""
#         assert self.get_value_of_create_account_btn() == ""

    def verify_person_icon_flyout_after_sign_in(self):
        '''
        This is a verification method to check UI strings of Person Icon Flyout after sign in.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load_sign_in()
        logging.debug("Start to check UI strings of Person Icon Flyout after sign in")
#         assert self.get_value_of_hi_text() == ""
#         assert self.get_value_of_my_hp_account_btn() == ""
#         assert self.get_value_of_sign_out_btn() == ""
