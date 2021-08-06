# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect your printer to your network screen.

@author: ten
@create_date: July 25, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectYourPrinterToYourNetwork(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_your_printer_to_your_network"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectYourPrinterToYourNetwork, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourPrinterToYourNetwork]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_your_printer_to_your_network_image", timeout=timeout, raise_e=raise_e)

    def click_back_btn(self):
        '''
        This is a method to click Back button on Connect your printer to your network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourPrinterToYourNetwork]:[click_back_btn]-Click Back button... ")

        self.driver.click("back_btn")

    def click_connect_printer_btn(self):
        '''
        This is a method to click Connect printer button on Connect your printer to your network screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourPrinterToYourNetwork]:[click_connect_printer_btn]-Click Connect printer button... ")

        self.driver.click("connect_printer_btn")

    def get_value_of_connect_your_printer_to_your_network_title(self):
        '''
        This is a method to get value of Connect your printer to your network screen title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourPrinterToYourNetwork]:[get_value_of_connect_your_printer_to_your_network_title]-Get the contents of screen title...  ")

        return self.driver.get_value("connect_your_printer_to_your_network_title")

    def get_value_of_connect_your_printer_to_your_network_contents(self):
        '''
        This is a method to get value of Connect your printer to your network screen contents
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourPrinterToYourNetwork]:[get_value_of_connect_your_printer_to_your_network_contents]-Get the contents of screen contents..  ")

        return self.driver.get_value("connect_your_printer_to_your_network_contents")

    def get_value_of_back_btn(self):
        '''
        This is a method to get value of Back button on Connect your printer to your network screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourPrinterToYourNetwork]:[get_value_of_back_btn]-Get the contents of Back button...  ")

        return self.driver.get_title("back_btn")

    def get_value_of_connect_printer_btn(self):
        '''
        This is a method to get value of Connect printer button on Connect your printer to your network screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourPrinterToYourNetwork]:[get_value_of_connect_printer_btn]-Get the contents of Connect printer button...  ")

        return self.driver.get_title("connect_printer_btn")

    # -------------------------------Verification Methods-------------------------------------------------
    def verify_connect_your_printer_to_your_network_screen(self):
        '''
        This is a verification method to check UI strings of Connect your printer to your network screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Connect your printer to your network screen")
#         assert self.get_value_of_connect_your_printer_to_your_network_title()==u""
#         assert self.get_value_of_connect_your_printer_to_your_network_contents()==u""
#         assert self.get_value_of_back_btn()==u""
#         assert self.get_value_of_connect_printer_btn()==u""
