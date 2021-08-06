# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect your computer to the network screen.

@author: Ivan
@create_date: Nov 19, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectYourComputerToTheNetwork(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_your_computer_to_the_network"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectYourComputerToTheNetwork, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheNetwork]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_your_computer_to_the_network_image", timeout=timeout, raise_e=raise_e)

    def select_no_continue_without_network_opt(self):
        '''
        This is a method to select "No, continue without network connection" option on Connect your computer to the network screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheNetwork]:[select_no_continue_without_network_opt]-Select 'No, continue without network connection' option.. ")

        self.driver.click("no_continue_without_network_opt", is_native_event=True)

    def select_yes_connect_to_network_opt(self):
        '''
        This is a method to select "Yes, connect to network" option on Connect your computer to the network screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheNetwork]:[select_yes_connect_to_network_opt]-Select 'Yes, connect to network' option.. ")

        self.driver.click("yes_connect_to_network_opt", is_native_event=True)

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Connect your computer to the network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheNetwork]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("continue_btn")

    def get_value_of_connect_your_computer_to_the_network_title(self):
        '''
        This is a method to get value of Connect your computer to the network screen title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheNetwork]:[get_value_of_connect_your_computer_to_the_network_title]-Get the contents of screen title...  ")

        return self.driver.get_value("connect_your_computer_to_the_network_title")

    def get_value_of_connect_your_computer_to_the_network_contents(self):
        '''
        This is a method to get value of Connect your computer to the network screen contents
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheNetwork]:[get_value_of_connect_your_computer_to_the_network_contents]-Get the contents of screen contents..  ")

        return self.driver.get_value("connect_your_computer_to_the_network_contents")

    def get_value_of_yes_connect_to_network_opt(self):
        '''
        This is a method to get value of "Yes, connect to network" option on Connect your computer to the network screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheNetwork]:[get_value_of_yes_connect_to_network_opt]-Get the contents of 'Yes, connect to network' option...  ")

        return self.driver.get_title("yes_connect_to_network_opt")

    def get_value_of_no_continue_without_network_opt(self):
        '''
        This is a method to get value of "No, continue without network connection" option on Connect your computer to the network screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheNetwork]:[get_value_of_no_continue_without_network_opt]-Get the contents of 'No, continue without network connection' option...  ")

        return self.driver.get_title("no_continue_without_network_opt")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on Connect your computer to the network screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheNetwork]:[get_value_of_continue_btn]-Get the contents of Continue button...  ")

        return self.driver.get_title("continue_btn")

    # -------------------------------Verification Methods-------------------------------------------------
    def verify_connect_your_computer_to_the_network_screen(self):
        '''
        This is a verification method to check UI strings of Connect your computer to the network screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Connect your computer to the network screen")
#         assert self.get_value_of_connect_your_computer_to_the_network_title()==u""
#         assert self.get_value_of_connect_your_computer_to_the_network_contents()==u""
#         assert self.get_value_of_yes_connect_to_network_opt()==u""
#         assert self.get_value_of_no_continue_without_network_opt()==u""
#         assert self.get_value_of_continue_btn()==u""
