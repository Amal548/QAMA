# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on We Can Help Connect Your Printer screen.

@author: ten
@create_date: July 30, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class WeCanHelpConnectYourPrinter(SmartScreens):
    folder_name = "oobe"
    flow_name = "we_can_help_connect_your_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WeCanHelpConnectYourPrinter, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("info_btn", timeout=timeout, raise_e=raise_e)

    def click_info_btn(self):
        '''
        This is a method to click Info button on We can help connect your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[click_info_btn]-Click info_btn... ")

        self.driver.click("info_btn")

    def select_wireless_radio(self):
        '''
        This is a method to select Wireless radio opt on We can help connect your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[select_wireless_radio]- Select Wireless radio... ")

        self.driver.click("wireless_radio")

    def select_ethernet_radio(self):
        '''
        This is a method to select Ethernet radio opt on We can help connect your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[select_ethernet_radio]- Select Ethernet radio... ")

        self.driver.click("ethernet_radio")

    def select_usb_radio(self):
        '''
        This is a method to select USB radio opt on We can help connect your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[select_usb_radio]- Select USB radio... ")

        self.driver.click("usb_radio")

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on We can help connect your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[click_continue_btn]-Click continue_btn... ")

        self.driver.click("continue_btn")

    def get_value_of_we_can_help_connect_your_printer_title(self):
        '''
        This is a method to get value of We can help connect your printer screen title.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[get_value_of_we_can_help_connect_your_printer_title]-Get the contents of We can help connect your printer screen title...  ")

        return self.driver.get_value("we_can_help_connect_your_printer_title")

    def get_value_of_we_can_help_connect_your_printer_contents(self):
        '''
        This is a method to get value of We can help connect your printer screen contents.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter:[get_value_of_we_can_help_connect_your_printer_contents]-Get the contents of We can help connect your printer screen contents...  ")

        return self.driver.get_value("we_can_help_connect_your_printer_contents")

    def get_value_of_wireless_radio_option(self):
        '''
        This is a method to get value of Wireless radio opt on the screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[get_value_of_wireless_radio_option]-Get the contents of Wireless radio opt...  ")

        return self.driver.get_title("wireless_radio")

    def get_value_of_wireless_radio_contents(self):
        '''
        This is a method to get value of Wireless radio contents on the screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[get_value_of_wireless_radio_contents]-Get the contents of Wireless radio contents...  ")

        return self.driver.get_value("wireless_radio_contents")

    def get_value_of_ethernet_radio_option(self):
        '''
        This is a method to get value of Ethernet radio opt on the screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[get_value_of_ethernet_radio_option]-Get the contents of Ethernet radio opt...  ")

        return self.driver.get_title("ethernet_radio")

    def get_value_of_ethernet_radio_contents(self):
        '''
        This is a method to get value of Ethernet radio contents on the screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[get_value_of_ethernet_radio_contents]-Get the contents of Ethernet radio contents...  ")

        return self.driver.get_value("ethernet_radio_contents")

    def get_value_of_usb_radio_option(self):
        '''
        This is a method to get value of USB radio opt on the screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[get_value_of_usb_radio_option]-Get the contents of USB radio opt...  ")

        return self.driver.get_title("usb_radio")

    def get_value_of_usb_radio_contents(self):
        '''
        This is a method to get value of USB radio contents on the screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[get_value_of_usb_radio_contents]-Get the contents of USB radio contents...  ")

        return self.driver.get_value("usb_radio_contents")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on the screen.
        :parameter:
        :return:
        '''
        logging.debug("[WeCanHelpConnectYourPrinter]:[get_value_of_continue_btn]-Get the contents of Continue button...  ")

        return self.driver.get_title("continue_btn")

# -------------------------------Verification Methods----------------------
    def verify_we_can_help_connect_your_printer_screen(self):
        '''
        This is a verification method to check UI strings of We can help connect your printer screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of We can help connect your printer screen")
#         assert self.get_value_of_we_can_help_connect_your_printer_title()==u""
#         assert self.get_value_of_we_can_help_connect_your_printer_contents()==u""
#         assert self.get_value_of_wireless_radio_option()==u""
#         assert self.get_value_of_wireless_radio_contents()==u""
#         assert self.get_value_of_ethernet_radio_option()==u""
#         assert self.get_value_of_ethernet_radio_contents()==u""
#         assert self.get_value_of_usb_radio_option()==u""
#         assert self.get_value_of_usb_radio_contents()==u""
#         assert self.get_value_of_continue_btn()==u""
