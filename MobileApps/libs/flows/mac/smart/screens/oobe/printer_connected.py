# encoding: utf-8
'''
Description: It defines classes_and_methods for Printer Connected screen

@author: itest
@create_date: July 29, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PrinterConnected(SmartScreens):
    folder_name = "oobe"
    flow_name = "printer_connected"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterConnected, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnected]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_connected_contents", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Printer connected screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnected]:[click_continue_btn]-Click Continue_btn... ")

        self.driver.click("continue_btn")

    def get_value_of_printer_connected_title(self):
        '''
        This is a method to get value of Printer Connected screen title
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnected]:[get_value_of_printer_connected_title]-Get the contents of Printer Connected screen title...  ")

        return self.driver.get_value("printer_connected_title")

    def get_value_of_printer_connected_contents(self):
        '''
        This is a method to get value of Printer Connected screen contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnected]:[get_value_of_printer_connected_contents]-Get the contents of Printer Connected screen contents...  ")

        return self.driver.get_value("printer_connected_contents")

    def get_value_of_printer_name(self):
        '''
        This is a method to get value of Printer name on Printer Connected screen
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnected]:[get_value_of_printer_name]-Get the contents of Printer name...  ")

        return self.driver.get_value("printer_name")

    def get_value_of_ethernet_usb_words(self):
        '''
        This is a method to get value of Ethernet on Printer Connected screen
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnected]:[get_value_of_ethernet_words]-Get the contents of Ethernet on Printer Connected screen...  ")

        return self.driver.get_value("ethernet_usb_words")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on Printer Connected screen
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnected]:[get_value_of_continue_btn]-Get the contents of Continue button...  ")

        return self.driver.get_title("continue_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_printer_connected_screen(self):
        '''
        This is a verification method to check UI strings of Printer connected screen for Ethernet connection.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of Printer connected screen")
#         assert self.get_value_of_printer_connected_to_wifi_title()==u""
#         assert self.get_value_of_printer_connected_contents()==u"Let's continue our guided setup!"
#         assert self.get_value_of_printer_name() == u""
#         assert self.get_value_of_ethernet_usb_words() == u"Ethernet"
#         assert self.get_value_of_continue_btn() == u""

    def verify_printer_connected_screen_usb(self):
        '''
        This is a verification method to check UI strings of Printer connected screen for USB connection
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of Printer connected screen")
#         assert self.get_value_of_printer_connected_to_wifi_title()==u""
#         assert self.get_value_of_printer_connected_contents()==u"Let's continue our guided setup!"
#         assert self.get_value_of_printer_name() == u""
#         assert self.get_value_of_ethernet_usb_words() == u"USB"
#         assert self.get_value_of_continue_btn() == u""
