# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect your computer to the network screen.

@author: Ivan
@create_date: Nov 19, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectYourComputerToTheWiFiNetwork(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_your_computer_to_the_wifi_network"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectYourComputerToTheWiFiNetwork, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_your_computer_to_the_wifi_network_image", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Connect your computer to the WiFi network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("continue_btn", is_native_event=True)
        if self.wait_for_screen_load(raise_e=False):
            self.driver.click("continue_btn", is_native_event=True)

    def click_open_network_settings_btn(self):
        '''
        This is a method to click Open Network Settings button on Connect your computer to the WiFi network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[click_open_network_settings_btn]-Click Open Network Settings button... ")

        self.driver.click("open_network_settings_btn")

    def get_value_of_screen_title(self):
        '''
        This is a method to get value of Connect your computer to the WiFi network screen title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[get_value_of_screen_title]-Get the contents of screen title...  ")

        return self.driver.get_value("connect_your_computer_to_the_wifi_network_title")

    def get_value_of_content_1(self):
        '''
        This is a method to get value of Connect your computer to the WiFi network screen content - 1
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[get_value_of_content_1]-Get the contents of screen content - 1...  ")

        return self.driver.get_value("connect_your_computer_to_the_wifi_network_content_1")

    def get_value_of_content_2(self):
        '''
        This is a method to get value of Connect your computer to the WiFi network screen content - 2
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[get_value_of_content_2]-Get the contents of screen content - 2...  ")

        return self.driver.get_value("connect_your_computer_to_the_wifi_network_content_2")

    def get_value_of_content_3(self):
        '''
        This is a method to get value of Connect your computer to the WiFi network screen content - 3
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[get_value_of_content_3]-Get the contents of screen content - 3...  ")

        return self.driver.get_value("connect_your_computer_to_the_wifi_network_content_3")

    def get_value_of_content_4(self):
        '''
        This is a method to get value of Connect your computer to the WiFi network screen content - 4
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[get_value_of_content_4]-Get the contents of screen content - 4...  ")

        return self.driver.get_value("connect_your_computer_to_the_wifi_network_content_4")

    def get_value_of_content_5(self):
        '''
        This is a method to get value of Connect your computer to the WiFi network screen content - 5
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[get_value_of_content_5]-Get the contents of screen content - 5...  ")

        return self.driver.get_value("connect_your_computer_to_the_wifi_network_content_5")

    def get_value_of_open_network_settings_btn(self):
        '''
        This is a method to get value of Open Network Settings button on Connect your computer to the WiFi network screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[get_value_of_open_network_settings_btn]-Get the contents of Open Network Settings button...  ")

        return self.driver.get_title("open_network_settings_btn")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on Connect your computer to the WiFi network screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourComputerToTheWiFiNetwork]:[get_value_of_continue_btn]-Get the contents of Continue button...  ")

        return self.driver.get_title("continue_btn")

    # -------------------------------Verification Methods-------------------------------------------------
    def verify_connect_your_computer_to_the_wifi_network_screen(self):
        '''
        This is a verification method to check UI strings of Connect your computer to the WiFi network screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Connect your computer to the WiFi network screen")
#         assert self.get_value_of_screen_title()==u""
#         assert self.get_value_of_content_1()==u""
#         assert self.get_value_of_content_2()==u""
#         assert self.get_value_of_content_3()==u""
#         assert self.get_value_of_content_4()==u""
#         assert self.get_value_of_content_5()==u""
#         assert self.get_value_of_open_network_settings_btn()==u""
#         assert self.get_value_of_continue_btn()==u""
