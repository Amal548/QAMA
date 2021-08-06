# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connected Printing Services screen.

@author:Ivan
@create_date: Aug 27, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectedPrintingServices(SmartScreens):
    folder_name = "common"
    flow_name = "connected_printing_services"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectedPrintingServices, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Connected Printing Services screen load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connected_printing_sevices_continue_btn", timeout=timeout, raise_e=raise_e)

    def click_connected_printing_sevices_learn_more_link(self):
        '''
        This is a method to click Learn More link on Connected Printing Services screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[click_connected_printing_sevices_learn_more_link]-Click Learn More link.. ")

        self.driver.click("connected_printing_sevices_learn_more_link")

    def click_connected_printing_sevices_continue_btn(self):
        '''
        This is a method to click Continue button on Connected Printing Services screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectedPrintingServices]:[click_connected_printing_sevices_continue_btn]-Click Continue button.. ")

        self.driver.click("connected_printing_sevices_continue_btn", is_native_event=True)

# -------------------------------Verification Methods--------------------------
