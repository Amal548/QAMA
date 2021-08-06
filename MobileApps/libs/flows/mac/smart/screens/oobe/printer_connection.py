# encoding: utf-8
'''
Description: It defines classes_and_methods for Printer Connection screen

@author: Ivan
@create_date: Oct 24, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PrinterConnection(SmartScreens):
    folder_name = "oobe"
    flow_name = "printer_connection"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterConnection, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_connection_content_1", timeout=timeout, raise_e=raise_e)

    def click_not_now_btn(self):
        '''
        This is a method to click not now button
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[click_not_now_btn]-Click Not Now button... ")

        self.driver.click("not_now_btn")

    def click_connect_to_wifi_network_btn(self):
        '''
        This is a method to click connect to wifi network button
        :parameter:
        :return:
        '''
        logging.debug("[PrinterConnection]:[click_connect_to_wifi_network_btn]-Click Connect to Wifi network button... ")

        self.driver.click("connect_to_wifi_network_btn")

# -------------------------------Verification Methods-------------------------------------------------
