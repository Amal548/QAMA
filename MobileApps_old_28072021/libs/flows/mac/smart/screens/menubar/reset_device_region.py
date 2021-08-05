# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Reset Device Region screen.

@author: Ivan
@create_date: Dec 26, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ResetDeviceRegion(SmartScreens):

    folder_name = "menubar"
    flow_name = "reset_device_region"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ResetDeviceRegion, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Reset Device Region screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("reset_device_region_title", timeout=timeout, raise_e=raise_e)

    def click_reset_device_btn(self):
        '''
        This is a method to click Reset Device Button on Reset Device Region screen.
        :parameter:
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[click_reset_device_btn]-Click Reset Device button... ")

        self.driver.click("reset_device_btn")

    def get_value_of_reset_device_region_title(self):
        '''
        This is a method to get the value of Reset Device Region screen title.
        :parameter:
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[get_value_of_reset_device_region_title]-Get the value of screen title...")

        return self.driver.get_value("reset_device_region_title")

    def get_value_of_provide_the_information_section(self):
        '''
        This is a method to get the value of Provide the Information section on Reset Device Region screen.
        :parameter:
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[get_value_of_provide_the_information_section]-Get the value of Provide the Information section...")

        return self.driver.get_value("provide_the_information_section")

    def get_value_of_enter_the_reset_code_section(self):
        '''
        This is a method to get the value of Enter the Reset Code section on Reset Device Region screen.
        :parameter:
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[get_value_of_enter_the_reset_code_section]-Get the value of Enter the Reset Code section...")

        return self.driver.get_value("enter_the_reset_code_section")

    def get_value_of_reset_device_btn(self):
        '''
        This is a method to get the value of Reset Device button on Reset Device Region screen.
        :parameter:
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[get_value_of_reset_device_btn]-Get the value of Reset Device button...")

        return self.driver.get_title("reset_device_btn")

    def input_code_on_41_textbox(self, contents):
        '''
        This is a method to input the code into the 41 text_box on Reset Device Region screen.
        :parameter: contents - 4 Digital required.
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[input_code_on_41_textbox]-Input the code into 41 text_box...")

        self.driver.send_keys("41_item_textbox", contents)

    def input_code_on_42_textbox(self, contents):
        '''
        This is a method to input the code into the 42 text_box on Reset Device Region screen.
        :parameter: contents - 4 Digital required.
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[input_code_on_42_textbox]-Input the code into 42 text_box...")

        self.driver.send_keys("42_item_textbox", contents)

    def input_code_on_43_textbox(self, contents):
        '''
        This is a method to input the code into the 43 text_box on Reset Device Region screen.
        :parameter: contents - 4 Digital required.
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[input_code_on_43_textbox]-Input the code into 43 text_box...")

        self.driver.send_keys("43_item_textbox", contents)

    def input_code_on_44_textbox(self, contents):
        '''
        This is a method to input the code into the 44 text_box on Reset Device Region screen.
        :parameter: contents - 4 Digital required.
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[input_code_on_44_textbox]-Input the code into 44 text_box...")

        self.driver.send_keys("44_item_textbox", contents)

    def input_code_on_45_textbox(self, contents):
        '''
        This is a method to input the code into the 45 text_box on Reset Device Region screen.
        :parameter: contents - 4 Digital required.
        :return:
        '''
        logging.debug("[ResetDeviceRegion]:[input_code_on_45_textbox]-Input the code into 45 text_box...")

        self.driver.send_keys("45_item_textbox", contents)

# -------------------------------Verification Methods---------------------------
    def verify_reset_device_region_screen(self):
        '''
        This is a verification method to check UI strings of Reset Device Region screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Reset Device Region screen")
#         assert self.get_value_of_reset_device_region_title() == u""
#         assert self.get_value_of_provide_the_information_section() == u""
#         assert self.get_value_of_enter_the_reset_code_section() == u""
#         assert self.get_value_of_reset_device_btn() == u""

    def input_5_codes(self, code1, code2, code3, code4, code5):
        '''
        This is a verification method to check UI strings of Reset Device Region screen.
        :parameter:
        :return:
        '''
        self.input_code_on_41_textbox(code1)
        self.input_code_on_42_textbox(code2)
        self.input_code_on_43_textbox(code3)
        self.input_code_on_44_textbox(code4)
        self.input_code_on_45_textbox(code5)
