# encoding: utf-8
'''
ConnectingPrintertoWiFi screen

@author: ten
@create_date: July 25, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectingPrintertoWiFi(SmartScreens):
    folder_name = "oobe"
    flow_name = "connecting_printer_to_wifi"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectingPrintertoWiFi, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("you_must_stay_text", timeout=timeout, raise_e=raise_e)

    def get_value_of_connecting_printer_to_wifi_title(self):
        '''
        This is a method to get the value of Connecting printer to WiFi title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_connecting_printer_to_wifi_title]-Get the contents of connecting_printer_to_wifi_title...  ")

        return self.driver.get_value("connecting_printer_to_wifi_title")

    def get_value_of_you_must_stay_text(self):
        '''
        This is a method to get the value of you must stay text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_you_must_stay_text]-Get the contents of you must stay text...  ")

        return self.driver.get_value("you_must_stay_text")

    def get_value_of_printer_name(self):
        '''
        This is a method to get the value of Printer name on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_printer_name]-Get the contents of Printer name...  ")

        return self.driver.get_value("printer_name")

    def get_value_of_router_name(self):
        '''
        This is a method to get the value of Router name on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_router_name]-Get the contents of Router name...  ")

        return self.driver.get_value("router_name")

    def get_value_of_finding_the_printer_text(self):
        '''
        This is a method to get the value of Finding the printer text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_finding_the_printer_text]-Get the contents of Finding the printer text...  ")

        return self.driver.get_value("finding_the_printer_text")

    def get_value_of_configure_the_printer_text(self):
        '''
        This is a method to get the value of Configure the printer text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_configure_the_printer_text]-Get the contents of Configure the printer text...  ")

        return self.driver.get_value("configure_the_printer_text")

    def get_value_of_join_the_network_text(self):
        '''
        This is a method to get the value of Join the network text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_join_the_network_text]-Get the contents of Join the network text...  ")

        return self.driver.get_value("join_the_network_text")

    def get_value_of_finish_connections_text(self):
        '''
        This is a method to get the value of Finish connections text on Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[get_value_of_finish_connections_text]-Get the contents of Finish connections text...  ")

        return self.driver.get_value("finish_connections_text")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_connecting_printer_to_wifi_screen(self):
        '''
        This is a verification method to check UI strings of Connecting printer to WiFi screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        self.driver.wait_for_object("printer_image", timeout=30, raise_e=True)
        self.driver.wait_for_object("wifi_image", timeout=30, raise_e=True)
        logging.debug("Start to verify UI string of Connecting printer to WiFi screen")
#         assert self.get_value_of_connecting_printer_to_wifi_title() == u"Connecting printer to Wi-Fi…"
#         assert self.get_value_of_you_must_stay_text() == u""
#         assert self.get_value_of_printer_name() == u""
#         assert self.get_value_of_router_name() == u""
#         assert self.get_value_of_finding_the_printer_text() == u""
#         assert self.get_value_of_configure_the_printer_text() == u""
#         assert self.get_value_of_join_the_network_text() == u""
#         assert self.get_value_of_finish_connections_text() == u""
