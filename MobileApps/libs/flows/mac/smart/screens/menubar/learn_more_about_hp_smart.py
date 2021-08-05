# encoding: utf-8
'''
Description: It defines the operations of element and verification methods 
on learn more about hp smart page

@author: Ten
@create_date: Nov 12, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class Learn_More_About_HP_Smart(SmartScreens):

    folder_name = "menubar"
    flow_name = "learn_more_about_hp_smart"

    def __init__(self, driver):
        super(Learn_More_About_HP_Smart, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[ClassName]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("printer_setup_title", timeout=timeout, raise_e=raise_e)

# -------------------------------Verification Methods------------------------------
