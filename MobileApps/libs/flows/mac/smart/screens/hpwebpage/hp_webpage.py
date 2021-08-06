# encoding: utf-8
'''
Description: It defines verify the URL that pops up after clicking the link

@author: ten
@create_date: Nov 15, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class HPWebPage(SmartScreens):

    folder_name = "hpwebpage"
    flow_name = "hp_webpage"

    def __init__(self, driver):
        super(HPWebPage, self).__init__(driver)

# ------------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[ClassName]:[wait_for_screen_load]-Wait for screen loading... ")
        pass

    def wait_for_hp_privacy_statement_website_load(self, timeout=120, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[ClassName]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("hp_privacy_statement_website", timeout=timeout, raise_e=raise_e)

    def wait_for_hp_smart_terms_of_use_website_load(self, timeout=120, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[ClassName]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("hp_smart_terms_of_use_website", timeout=timeout, raise_e=raise_e)

    def wait_for_end_user_license_agreement_website_load(self, timeout=120, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[ClassName]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("end_user_license_agreement_website", timeout=timeout, raise_e=raise_e)

    def wait_for_enroll_printer_website_load(self, timeout=120, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[ClassName]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("enroll_printer_website", timeout=timeout, raise_e=raise_e)

# -------------------------------Verification Methods-------------------------
