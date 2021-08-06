# encoding: utf-8
'''
Description: It defines classes_and_methods for Switch to Using WiFi_2 screen

@author: Ivan
@create_date: Aug 22, 2019
'''
import logging
from selenium.common.exceptions import TimeoutException

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class SwitchToUsingWiFi2(SmartScreens):
    folder_name = "oobe"
    flow_name = "switch_to_using_wifi_2"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(SwitchToUsingWiFi2, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait main UI screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("switch_to_using_wifi_2_title", timeout=timeout, raise_e=raise_e)

    def wait_for_continue_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to check continue button is displayed after choosing a option.
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[wait_for_continue_btn_display]-Wait for continue button display... ")

        return self.driver.wait_for_object("continue_btn", timeout=timeout, raise_e=raise_e)

    def click_open_network_settings_button(self):
        '''
        This is a method to click Open Network Settings button
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[click_open_network_settings_button]-Click network button.. ")

        self.driver.click("open_network_settings_btn")

    def click_continue_btn(self):
        '''
        This is a method to click Continue button
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[click_continue_btn]-Click continue_btn.. ")

        self.driver.click("continue_btn")

    def get_value_of_switch_to_using_wifi_2_title(self):
        '''
        This is a method to get the value of Switch to Using WiFi_2 screen title
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[get_value_of_switch_to_using_wifi_2_title]-Get the value of screen title...  ")

        return self.driver.get_value("switch_to_using_wifi_2_title")

    def get_value_of_switch_to_using_wifi_2_content_1(self):
        '''
        This is a method to get the value of screen content_1
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[get_value_of_switch_to_using_wifi_2_content_1]-Get the value of screen content_1...  ")

        return self.driver.get_value("switch_to_using_wifi_2_content_1")

    def get_value_of_switch_to_using_wifi_2_content_2(self):
        '''
        This is a method to get the value of screen content_2
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[get_value_of_switch_to_using_wifi_2_content_2]-Get the value of screen content_2...  ")

        return self.driver.get_value("switch_to_using_wifi_2_content_2")

    def get_value_of_switch_to_using_wifi_2_content_3(self):
        '''
        This is a method to get the value of screen content_3
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[get_value_of_switch_to_using_wifi_2_content_3]-Get the value of screen content_3...  ")

        return self.driver.get_value("switch_to_using_wifi_2_content_3")

    def get_value_of_switch_to_using_wifi_2_content_4(self):
        '''
        This is a method to get the value of screen content_4
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[get_value_of_switch_to_using_wifi_2_content_4]-Get the value of screen content_4...  ")

        return self.driver.get_value("switch_to_using_wifi_2_content_4")

    def get_value_of_switch_to_using_wifi_2_content_5(self):
        '''
        This is a method to get the value of screen content_5
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[get_value_of_switch_to_using_wifi_2_content_5]-Get the value of screen content_5...  ")

        return self.driver.get_value("switch_to_using_wifi_2_content_5")

    def get_value_of_open_network_settings_btn(self):
        '''
        This is a method to get the value of Open Network Settings button on Switch to Using WiFi_2 screen.
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[get_value_of_open_network_settings_btn]-Get the value of Open Network Settings button...  ")

        return self.driver.get_value("open_network_settings_btn")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get the value of Continue button on Switch to Using WiFi_2 screen.
        :parameter:
        :return:
        '''
        logging.debug("[SwitchToUsingWiFi2]:[get_value_of_continue_btn]-Get the value of Continue button...  ")

        return self.driver.get_value("continue_btn")

# -------------------------------Verification Methods--------------------------
    def verify_continue_btn_is_disabled(self):
        '''
        This is a method to verify continue button is disabled on the screen before clicking Open network settings.
        :parameter:
        :return:
        '''
        logging.debug("Verify continue button is disabled on the screen before clicking Open network settings")

        if self.driver.is_enable("continue_btn"):
            raise UnexpectedItemPresentException("Continue button is enabled")
        return True

    def verify_continue_btn_is_enabled(self):
        '''
        This is a method to verify continue button is enabled on the screen after clicking Open network settings.
        :parameter:
        :return:
        '''
        logging.debug("Verify continue button is enabled on the screen after clicking Open network settings")

        if not self.driver.is_enable("continue_btn"):
            raise UnexpectedItemPresentException("Continue button is disabled")
        return True

    def verify_swtich_to_using_wifi_2_screen(self):
        '''
        This is a verification method to check UI strings of Switch to Using WiFi_2 screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        self.verify_continue_btn_is_disabled()
        self.driver.wait_for_object("switch_to_using_wifi_2_image", timeout=30, raise_e=True)
        logging.debug("Start to verify UI string of Switch to Using WiFi_2 screen")
#         assert self.get_value_of_switch_to_using_wifi_2_title() == u""
#         assert self.get_value_of_switch_to_using_wifi_2_content_1() == u""
#         assert self.get_value_of_switch_to_using_wifi_2_content_2() == u""
#         assert self.get_value_of_switch_to_using_wifi_2_content_3() == u""
#         assert self.get_value_of_switch_to_using_wifi_2_content_4() == u""
#         assert self.get_value_of_switch_to_using_wifi_2_content_5() == u""
#         assert self.get_value_of_open_network_settings_btn() == u""
