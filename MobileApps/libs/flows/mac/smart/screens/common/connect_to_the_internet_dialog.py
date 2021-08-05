# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect to the Internet dialog.

@author: Ivan
@create_date: Aug 28, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectToTheInternetDialog(SmartScreens):

    folder_name = "common"
    flow_name = "connect_to_the_internet_dialog"

    def __init__(self, driver):
        super(ConnectToTheInternetDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Connect to the Internet dialog load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_to_the_internet_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_connect_to_the_internet_title(self):
        '''
        This is a method to get value of Connect to the Internet dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_connect_to_the_internet_title]-Get the value of Connect to the Internet dialog title...  ")

        return self.driver.get_value("connect_to_the_internet_title")

    def get_value_of_connect_to_the_internet_content_1(self):
        '''
        This is a method to get value of Content - 1 on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_connect_to_the_internet_content_1]-Get the value of Content - 1...  ")

        return self.driver.get_value("connect_to_the_internet_content_1")

    def get_value_of_connect_to_the_internet_content_2(self):
        '''
        This is a method to get value of Content - 2 on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_connect_to_the_internet_content_2]-Get the value of Content - 2...  ")

        return self.driver.get_value("connect_to_the_internet_content_2")

    def get_value_of_connect_to_the_internet_content_3(self):
        '''
        This is a method to get value of Content - 3 on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_connect_to_the_internet_content_3]-Get the value of Content - 3...  ")

        return self.driver.get_value("connect_to_the_internet_content_3")

    def get_value_of_connect_to_the_internet_continue_btn(self):
        '''
        This is a method to get value of Continue button on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[get_value_of_connect_to_the_internet_continue_btn]-Get the value of Continue button...  ")

        return self.driver.get_title("connect_to_the_internet_continue_btn")

    def click_connect_to_the_internet_continue_btn(self):
        '''
        This is a method to click Continue button on Connect to the Internet dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectToTheInternetDialog]:[click_connect_to_the_internet_continue_btn]-Click Continue button... ")

        self.driver.click("connect_to_the_internet_continue_btn")

# -------------------------------Verification Methods-------------------------------
    def verify_connect_to_the_internet_dialog(self):
        '''
        This is a verification method to check UI strings of Connect to the Internet dialog
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of Connect to the Internet dialog")
#         assert self.get_value_of_connect_to_the_internet_title() == ""
#         assert self.get_value_of_connect_to_the_internet_content_1() == ""
#         assert self.get_value_of_connect_to_the_internet_content_2() == ""
#         assert self.get_value_of_connect_to_the_internet_content_3() == ""
#         assert self.get_value_of_connect_to_the_internet_continue_btn() == ""

    def verify_dialog_disappear(self, timeout=10):
        '''
        This is a verification method to check Connect to the Internet dialog disappear after clicking Continue button with Internect connected.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("connect_to_the_internet_title", timeout=timeout, raise_e=False)
