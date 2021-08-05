# encoding: utf-8
'''
Description: It defines classes_and_methods for Switch to Using WiFi screen

@author: ten
@create_date: July 24, 2019
'''
import logging
from selenium.common.exceptions import TimeoutException

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class SwitchToUsingWiFi(SmartScreens):
    folder_name = "oobe"
    flow_name = "switch_to_using_wifi"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(SwitchToUsingWiFi, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("switch_to_using_wifi_title", timeout=timeout, raise_e=raise_e)

    def click_no_continue_with_ethernet_opt(self):
        '''
        This is a method to select "no, continue with Ethernet" option
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi]:[click_no_continue_with_ethernet_opt]-Click 'No, continue with Ethernet' option.. ")

        self.driver.click("no_continue_with_ethernet_radio")

    def click_yes_switch_to_wifi_opt(self):
        '''
        This is a method to select "yes, switch to WiFi(Recommended)" option
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi]:[click_yes_switch_to_wifi_opt]-Select 'yes, switch to WiFi' option.. ")

        self.driver.click("yes_switch_to_wifi_radio")

    def click_continue_btn(self):
        '''
        This is a method to click continue button
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi]:[click_continue_btn]-Click continue_btn.. ")

        self.driver.click("continue_btn")

    def get_value_of_switch_to_using_wifi_title(self):
        '''
        This is a method to get the value of Switch to Using WiFi screen title
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi]:[get_value_of_switch_to_using_wifi_title]-Get the value of Switch to Using WiFi screen title...  ")

        return self.driver.get_value("switch_to_using_wifi_title")

    def get_value_of_switch_to_using_wifi_content(self):
        '''
        This is a method to get the value of Switch to Using WiFi screen Content
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi]:[get_value_of_switch_to_using_wifi_content]-Get the value of Switch to Using WiFi screen Content...  ")

        return self.driver.get_value("switch_to_using_wifi_content")

    def get_value_of_yes_switch_to_wifi_radio(self):
        '''
        This is a method to get the value of "Yes, switch to WiFi" radio on Switch to Using WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi]:[get_value_of_yes_switch_to_wifi_radio]-Get the value of Yes, switch to WiFi radio...  ")

        return self.driver.get_title("yes_switch_to_wifi_radio")

    def get_value_of_no_continue_with_ethernet_radio(self):
        '''
        This is a method to get the value of "No, continue with Ethernet" radio on Switch to Using WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi]:[get_value_of_no_continue_with_ethernet_radio]-Get the value of No, continue with Ethernet radio...  ")

        return self.driver.get_title("no_continue_with_ethernet_radio")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Switch to Using WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi]:[get_value_of_continue_btn]-Get the value of Continue button...  ")

        return self.driver.get_title("continue_btn")

# -------------------------------Verification Methods--------------------------
    def verify_continue_btn_is_disabled(self):
        '''
        This is a method to verify continue button is disabled on the screen before select opt.
        :parameter:
        :return:
        '''
        logging.debug("Verify continue button is disabled on the screen before select opt")

        if self.driver.is_enable("continue_btn"):
            raise UnexpectedItemPresentException("Continue button is enabled")
        return True          

    def verify_continue_btn_is_enabled(self):
        '''
        This is a method to verify continue button is enabled on the screen after select opt.
        :parameter:
        :return:
        '''
        logging.debug("Verify continue button is enabled on the screen after select opt")

        if not self.driver.is_enable("continue_btn"):
            raise UnexpectedItemPresentException("Continue button is disabled")
        return True        

    def verify_swtich_to_using_wifi_screen(self):
        '''
        This is a verification method to check UI strings of Switch to Using WiFi screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        self.verify_continue_btn_is_disabled()
        self.driver.wait_for_object("switch_to_using_wifi_image", timeout=30, raise_e=True)
        logging.debug("Start to verify UI string of Switch to Using WiFi screen")
#         assert self.get_value_of_switch_to_using_wifi_title() == u""
#         assert self.get_value_of_switch_to_using_wifi_content() == u""
#         assert self.get_value_of_yes_switch_to_wifi_radio() == u""
#         assert self.get_value_of_no_continue_with_ethernet_radio() == u""
