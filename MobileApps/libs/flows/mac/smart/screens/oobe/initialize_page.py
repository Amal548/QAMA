# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Starting up screen.

@author: Ivan
@create_date: Aug 13, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class InitializePage(SmartScreens):

    folder_name = "oobe"
    flow_name = "initialize_page"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(InitializePage, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for initialize page loaded (including starting up screen and searching for printer screen).
        :parameter:
        :return:
        '''
        logging.debug("[InitializePage]:[wait_for_initialize_page_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("busy_indicator", timeout=timeout, raise_e=raise_e)

# -------------------------------Verification Methods--------------------------
