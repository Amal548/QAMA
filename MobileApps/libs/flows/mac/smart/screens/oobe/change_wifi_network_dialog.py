# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Change WiFi Network dialog.

@author: ten
@create_date: July 25, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ChangeWiFiNetworkDialog(SmartScreens):
    folder_name = "oobe"
    flow_name = "change_wifi_network_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ChangeWiFiNetworkDialog, self).__init__(driver)


# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("network_btn", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click Continue Button on Change WiFi Network dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("continue_btn", is_native_event=True)

    def click_network_btn(self):
        '''
        This is a method to click Network Button on Change WiFi Network dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[click_network_btn]-Click Network_btn... ")

        self.driver.click("network_btn", is_native_event=True)

    def get_value_of_change_wifi_network_title(self):
        '''
        This is a method to get the value of Change WiFi Network dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[get_value_of_change_wifi_network_title]-Get the value of Change WiFi Network dialog title...  ")

        return self.driver.get_value("change_wifi_network_dialog")

    def get_value_of_change_wifi_network_content_1(self):
        '''
        This is a method to get the value of Change WiFi Network dialog Content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[get_value_of_change_wifi_network_content_1]-Get the value of Change WiFi Network dialog Content - 1...  ")

        return self.driver.get_value("change_wifi_network_content_1")

    def get_value_of_change_wifi_network_content_2(self):
        '''
        This is a method to get the value of Change WiFi Network dialog Content - 2.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[get_value_of_change_wifi_network_content_2]-Get the value of Change WiFi Network dialog Content - 2...  ")

        return self.driver.get_value("change_wifi_network_content_2")

    def get_value_of_change_wifi_network_content_3(self):
        '''
        This is a method to get the value of Change WiFi Network dialog Content - 3.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[get_value_of_change_wifi_network_content_3]-Get the value of Change WiFi Network dialog Content - 3...  ")

        return self.driver.get_value("change_wifi_network_content_3")

    def get_value_of_change_wifi_network_content_4(self):
        '''
        This is a method to get the value of Change WiFi Network dialog Content - 4.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[get_value_of_change_wifi_network_content_4]-Get the value of Change WiFi Network dialog Content - 4...  ")

        return self.driver.get_value("change_wifi_network_content_4")

    def get_value_of_change_wifi_network_content_5(self):
        '''
        This is a method to get the value of Change WiFi Network dialog Content - 5.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[get_value_of_change_wifi_network_content_5]-Get the value of Change WiFi Network dialog Content - 5...  ")

        return self.driver.get_value("change_wifi_network_content_5")

    def get_value_of_network_btn(self):
        '''
        This is a method to get the value of Change WiFi Network dialog Network button.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[get_value_of_network_btn]-Get the value of Change WiFi Network dialog Network button...  ")

        return self.driver.get_title("network_btn")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get the value of Change WiFi Network dialog Continue button.
        :parameter:
        :return:
        '''
        logging.debug("[ChangeWiFiNetworkDialog]:[get_value_of_continue_btn]-Get the value of Change WiFi Network dialog Continue button...  ")

        return self.driver.get_title("continue_btn")

    # -------------------------------Verification Methods-------------------------------------------------
    def verify_change_wifi_network_dialog(self):
        '''
        This is a verification method to check UI strings of Change WiFi Network dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Change WiFi Network dialog")
#         assert self.get_value_of_change_wifi_network_title() == u"Select a Wi-Fi network."
#         assert self.get_value_of_change_wifi_network_content_1() == u""
#         assert self.get_value_of_change_wifi_network_content_2() == u""
#         assert self.get_value_of_change_wifi_network_content_3() == u""
#         assert self.get_value_of_change_wifi_network_content_4() == u""
#         assert self.get_value_of_change_wifi_network_content_5() == u""
#         assert self.get_value_of_network_btn() == u""
