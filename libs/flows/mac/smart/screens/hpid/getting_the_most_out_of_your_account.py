# encoding: utf-8
'''
It defines the operations of element and verification methods on Getting the most out of your account Page.

@author: Ivan
@create_date: Aug 13, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class GettingTheMostOutOfYourAccount(SmartScreens):

    folder_name = "hpid"
    flow_name = "getting_the_most_out_of_your_account"

    def __init__(self, driver):
        super(GettingTheMostOutOfYourAccount, self).__init__(driver)

#   -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Getting the most out of your account page load.
        '''
        logging.debug("[GettingTheMostOutOfYourAccount]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("getting_the_most_out_of_your_account_continue_btn", timeout=timeout, raise_e=raise_e)

    def get_value_of_getting_the_most_out_of_your_account_title(self):
        '''
        This is a method to get the value of Getting the most out of your account Page title.
        :parameter:
        :return:
        '''
        logging.debug("[GettingTheMostOutOfYourAccount]:[get_value_of_getting_the_most_out_of_your_account_title]-Get the value of Getting the most out of your account Page title...  ")

        return self.driver.get_title("getting_the_most_out_of_your_account_title")

    def get_value_of_getting_the_most_out_of_your_account_content(self):
        '''
        This is a method to get the value of Getting the most out of your account Page content.
        :parameter:
        :return:
        '''
        logging.debug("[GettingTheMostOutOfYourAccount]:[get_value_of_getting_the_most_out_of_your_account_content]-Get the value of Getting the most out of your account Page content...  ")

        return self.driver.get_value("getting_the_most_out_of_your_account_content")

    def get_value_of_getting_the_most_out_of_your_account_learn_more_link(self):
        '''
        This is a method to get the value of Learn More link on Getting the most out of your account Page.
        :parameter:
        :return:
        '''
        logging.debug("[GettingTheMostOutOfYourAccount]:[get_value_of_getting_the_most_out_of_your_account_learn_more_link]-Get the value of Learn More link...  ")

        return self.driver.get_title("getting_the_most_out_of_your_account_learn_more_link")

    def get_value_of_getting_the_most_out_of_your_account_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Getting the most out of your account Page.
        :parameter:
        :return:
        '''
        logging.debug("[GettingTheMostOutOfYourAccount]:[get_value_of_getting_the_most_out_of_your_account_continue_btn]-Get the value of Continue button...  ")

        return self.driver.get_title("getting_the_most_out_of_your_account_continue_btn")

    def click_getting_the_most_out_of_your_account_learn_more_link(self):
        '''
        This is a method to click Learn More link on Getting the most out of your account Page.
        :parameter:
        :return:
        '''
        logging.debug("[GettingTheMostOutOfYourAccount]:[click_getting_the_most_out_of_your_account_learn_more_link]-Click Learn More link... ")

        self.driver.click("getting_the_most_out_of_your_account_learn_more_link", is_native_event=True)

    def click_getting_the_most_out_of_your_account_title(self):
        '''
        This is a method to click on Getting the most out of your account Page title.
        :parameter:
        :return:
        '''
        logging.debug("[GettingTheMostOutOfYourAccount]:[click_getting_the_most_out_of_your_account_title]-Click Getting the most out of your account Page title... ")

        self.driver.click("getting_the_most_out_of_your_account_title", is_native_event=True)

    def click_getting_the_most_out_of_your_account_continue_btn(self):
        '''
        This is a method to click Continue button on Getting the most out of your account Page.
        :parameter:
        :return:
        '''
        logging.debug("[GettingTheMostOutOfYourAccount]:[click_getting_the_most_out_of_your_account_continue_btn]-Click Continue button... ")

        self.driver.click("getting_the_most_out_of_your_account_continue_btn", is_native_event=True)

# -------------------------------Verification Methods-----------------------------------
    def verify_getting_the_most_out_of_your_account_page(self):
        '''
        This is a verification method to check UI strings of Getting the most out of your account Page.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Getting the most out of your account Page")
#         assert self.get_value_of_getting_the_most_out_of_your_account_title() == ""
#         assert self.get_value_of_getting_the_most_out_of_your_account_content() == ""
#         assert self.get_value_of_getting_the_most_out_of_your_account_learn_more_link() == ""
#         assert self.get_value_of_getting_the_most_out_of_your_account_continue_btn() == ""
