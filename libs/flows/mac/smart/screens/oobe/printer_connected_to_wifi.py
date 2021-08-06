# encoding: utf-8
'''
PrinterConnectedtoWiFi screen

@author: ten
@create_date: July 29, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PrinterConnectedtoWiFi(SmartScreens):
    folder_name = "oobe"
    flow_name = "printer_connected_to_wifi"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterConnectedtoWiFi, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnectedtoWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_connected_to_wifi_content", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Printer connected to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnectedtoWiFi]:[click_continue_btn]-Click Continue_btn... ")

        self.driver.click("printer_connected_to_wifi_continue_btn")

    def get_value_of_printer_connected_to_wifi_title(self):
        '''
        This is a method to get value of Printer connected to WiFi screen title
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnectedtoWiFi]:[get_value_of_printer_connected_to_wifi_title]-Get the contents of Printer connected to WiFi screen title...  ")

        return self.driver.get_value("printer_connected_to_wifi_title")

    def get_value_of_printer_connected_to_wifi_content(self):
        '''
        This is a method to get value of Printer connected to WiFi screen contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnectedtoWiFi]:[get_value_of_printer_connected_to_wifi_content]-Get the contents of Printer connected to WiFi screen contents...  ")

        return self.driver.get_value("printer_connected_to_wifi_content")

    def get_value_of_printer_connected_to_wifi_printer_name(self):
        '''
        This is a method to get value of Print name on Printer connected to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnectedtoWiFi]:[get_value_of_printer_connected_to_wifi_printer_name]-Get the contents of Print name...  ")

        return self.driver.get_value("printer_connected_to_wifi_printer_name")

    def get_value_of_printer_connected_to_wifi_router_name(self):
        '''
        This is a method to get value of Router name on Printer connected to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnectedtoWiFi]:[get_value_of_printer_connected_to_wifi_router_name]-Get the contents of Router name...  ")

        return self.driver.get_value("printer_connected_to_wifi_router_name")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on Printer connected to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnectedtoWiFi]:[get_value_of_continue_btn]-Get the contents of Continue button...  ")

        return self.driver.get_title("printer_connected_to_wifi_continue_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_printer_connected_to_wifi_screen(self):
        '''
        This is a verification method to check UI strings of Printer connected to WiFi screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(600)
        self.driver.wait_for_object("printer_connected_to_wifi_printer_image", timeout=10, raise_e=True)
        self.driver.wait_for_object("printer_connected_to_wifi_success_image", timeout=10, raise_e=True)
        self.driver.wait_for_object("printer_connected_to_wifi_wireless_image", timeout=10, raise_e=True)
        logging.debug("Start to verify UI string of Printer connected to WiFi screen")
#         assert self.get_value_of_printer_connected_to_wifi_title()==u""
#         assert self.get_value_of_printer_connected_to_wifi_content()==u""
#         assert self.get_value_of_printer_connected_to_wifi_printer_name() == u""
#         assert self.get_value_of_printer_connected_to_wifi_router_name() == u""
#         assert self.get_value_of_continue_btn() == u""
