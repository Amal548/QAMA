# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Install driver to print screen

@author: Ivan
@create_date: Aug 12, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class InstallDriverToPrint(SmartScreens):

    folder_name = "oobe"
    flow_name = "install_driver_to_print"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(InstallDriverToPrint, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait install driver to print screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("install_driver_to_print_title", timeout=timeout, raise_e=raise_e)

    def wait_for_install_success_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Success print installed dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[wait_for_install_success_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("ok_button", timeout=timeout, raise_e=raise_e)

    def click_ok_btn(self):
        '''
        This is a method to click OK button on Success print installed dialog.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[click_ok_btn_install_driver_to_print]-Click OK button... ")

        self.driver.click("ok_button")

    def get_value_of_success_print_installed_contents(self):
        '''
        This is a method to get value of Success print installed dialog content.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_success_print_installed_contents]-Get the contents of Success print installed dialog content...  ")

        return self.driver.get_value("success_print_installed_contents")

    def get_value_of_you_can_now_print_to_contents(self):
        '''
        This is a method to get value of Success print installed dialog content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_you_can_now_print_to_contents]-Get the contents of Success print installed dialog content - 1...  ")

        return self.driver.get_value("you_can_now_print_to_contents")

    def get_value_of_ok_button(self):
        '''
        This is a method to get value of OK button on Success print install dialog.
        :parameter:
        :return:
        '''
        logging.debug("[InstallDriverToPrint]:[get_value_of_ok_button]-Get the contents of OK button...  ")

        return self.driver.get_title("ok_button")

# -------------------------------Verification Methods--------------------------
    def verify_success_print_installed_dialog(self):
        '''
        This is a verification method to check UI strings of Success print installed dialog.
        :parameter:
        :return:
        '''
        self.wait_for_install_success_screen_load(300)
        self.driver.wait_for_object("successful_image", timeout=10, raise_e=True)
        logging.debug("Start to verify UI string of Success print installed dialog")
#         assert self.get_value_of_success_print_installed_contents()==u""
#         assert self.get_value_of_you_can_now_print_to_contents()==u""
#         assert self.get_value_of_ok_button() == u""
