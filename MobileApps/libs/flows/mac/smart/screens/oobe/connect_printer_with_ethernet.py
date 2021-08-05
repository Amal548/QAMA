# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect Printer with Ethernet screen.

@author: ten
@create_date: July 25, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class ConnectPrinterWithEthernet(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_printer_with_ethernet"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectPrinterWithEthernet, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterWithEthernet]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_printer_with_ethernet_image", timeout=timeout, raise_e=raise_e)

    def click_back_btn(self):
        '''
        This is a method to click Back button on Connect Printer with Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterWithEthernet]:[click_back_btn]-Click Back button... ")

        self.driver.click("back_btn")

    def click_connect_printer_btn(self):
        '''
        This is a method to click Connect printer button on Connect Printer with Ethernet screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterWithEthernet]:[click_connect_printer_btn]-Click Connect printer button... ")

        self.driver.click("connect_printer_btn")

    def get_value_of_connect_printer_with_ethernet_title(self):
        '''
        This is a method to get value of Connect Printer with Ethernet screen title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterWithEthernet]:[get_value_of_connect_printer_with_ethernet_title]-Get the contents of screen title...  ")

        return self.driver.get_value("connect_printer_with_ethernet_title")

    def get_value_of_connect_printer_with_ethernet_contents(self):
        '''
        This is a method to get value of Connect Printer with Ethernet screen contents
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterWithEthernet]:[get_value_of_connect_printer_with_ethernet_contents]-Get the contents of screen contents..  ")

        return self.driver.get_value("connect_printer_with_ethernet_contents")

    def get_value_of_back_btn(self):
        '''
        This is a method to get value of Back button on Connect Printer with Ethernet screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterWithEthernet]:[get_value_of_back_btn]-Get the contents of Back button...  ")

        return self.driver.get_title("back_btn")

    def get_value_of_connect_printer_btn(self):
        '''
        This is a method to get value of Connect printer button on Connect Printer with Ethernet screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterWithEthernet]:[get_value_of_connect_printer_btn]-Get the contents of Connect printer button...  ")

        return self.driver.get_title("connect_printer_btn")

    # -------------------------------Verification Methods-------------------------------------------------
    def verify_connect_printer_with_ethernet_screen(self):
        '''
        This is a verification method to check UI strings of Connect Printer with Ethernet screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Connect Printer with Ethernet screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='connect_printer_with_ethernet_screen')
        assert self.get_value_of_connect_printer_with_ethernet_title() == test_strings['connect_printer_with_ethernet_title']
#         assert self.get_value_of_connect_printer_with_ethernet_contents() == test_strings['connect_printer_with_ethernet_contents']
        assert self.get_value_of_back_btn() == test_strings['back_btn']
        assert self.get_value_of_connect_printer_btn() == test_strings['connect_printer_btn']
