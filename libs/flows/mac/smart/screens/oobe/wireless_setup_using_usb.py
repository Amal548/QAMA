# encoding: utf-8
'''
check wireless setup using usb screen

@author: ten
@create_date: Aug 22, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class WirelessSetupUsingUSB(SmartScreens):

    folder_name = "oobe"
    flow_name = "wireless_setup_using_usb"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WirelessSetupUsingUSB, self).__init__(driver)

# -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("info_btn", timeout=timeout, raise_e=raise_e)

    def click_info_btn(self):
        '''
        Click info button
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[click_info_btn]-click_info_btn.. ")

        self.driver.click("info_btn")

    def click_back_btn(self):
        '''
        Click back button
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[click_back_btn]-Click back_btn.. ")

        self.driver.click("back_btn")

    def click_continue_btn(self):
        '''
        Click continue button
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[click_continue_btn]-Click continue_btn.. ")

        self.driver.click("continue_btn")

    def get_value_of_wireless_setup_using_usb_title(self):
        '''
        get_value_of_wireless_setup_using_usb_title
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[get_value_of_wireless_setup_using_usb_title]-Get the contents of wireless_setup_using_usb_title...  ")

        return self.driver.get_value("oobe_screen_title")

    def get_value_of_contents_1(self):
        '''
        get_value_of_contents_1
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[get_value_of_contents_1]-Get the contents of contents_1...  ")

        return self.driver.get_value("contents_1")

    def get_value_of_contents_2(self):
        '''
        get_value_of_contents_2
        :parameter:
        :return:
        '''
        logging.debug("[WirelessSetupUsingUSB]:[get_value_of_contents_2]-Get the contents of contents_2...  ")

        return self.driver.get_value("contents_2")

# -------------------------------Verification Methods-----------------------------
    # def verify_ui_string(self):
    #     '''
    #     verify_ui_string
    #     :parameter:
    #     :return:
    #     '''
    #     logging.debug("Verify strings are translated correctly and matching string table.[C12961688][C12961695]")
    #     assert self.get_value_of_wireless_setup_using_usb_title() == u''
    #     assert self.get_value_of_contents_1() == u''
    #     assert self.get_value_of_contents_2() == u''
