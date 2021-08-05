# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Mobile Fax value prop screen.

@author: Ivan
@create_date: Dec 4, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class MobileFaxValueProp(SmartScreens):

    folder_name = "mobilefax"
    flow_name = "mobile_fax_value_prop"

    def __init__(self, driver):
        super(MobileFaxValueProp, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax value prop screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxValueProp]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("get_started_btn", timeout=timeout, raise_e=raise_e)

    def click_get_started_btn(self):
        '''
        This is a method to click Get Started button on Mobile Fax value prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxValueProp]:[click_get_started_btn]-Click Get Started button... ")

        self.driver.click("get_started_btn", is_native_event=True)

    def click_no_thanks_btn(self):
        '''
        This is a method to click No Thanks button on Mobile Fax value prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxValueProp]:[click_no_thanks_btn]-Click No thanks button... ")

        self.driver.click("no_thanks_btn", is_native_event=True)

    def get_value_of_mobile_fax_title(self):
        '''
        This is a method to get value of screen title of Mobile Fax value prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxValueProp]:[get_value_of_mobile_fax_title] - Get value of screen title...  ")

        return self.driver.get_title("mobile_fax_title")

    def get_value_of_screen_mobile_fax_content_1(self):
        '''
        This is a method to get value of screen content - 1 on Mobile Fax value prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxValueProp]:[get_value_of_printer_status] - Get value of screen content - 1...  ")

        return self.driver.get_value("mobile_fax_content_1")

    def get_value_of_mobile_fax_content_2(self):
        '''
        This is a method to get value of screen content - 2 on Mobile Fax value prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxValueProp]:[get_value_of_mobile_fax_content_2] - Get value of screen - 2...  ")

        return self.driver.get_value("mobile_fax_content_2")

    def get_value_of_get_started_btn(self):
        '''
        This is a method to get value of Get Started button on Mobile Fax value prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxValueProp]:[get_value_of_printer_status] - Get value of Get Started button...  ")

        return self.driver.get_value("get_started_btn")

    def get_value_of_no_thanks_btn(self):
        '''
        This is a method to get value of No Thanks button on Mobile Fax value prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxValueProp]:[get_value_of_no_thanks_btn] - Get value of No thanks button...  ")

        return self.driver.get_value("no_thanks_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_mobile_fax_value_prop_screen(self):
        '''
        This is a verification method to check UI strings of Mobile Fax value prop screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(120)
        logging.debug("Start to check UI strings of Mobile Fax value prop screen")
#         assert self.get_value_of_mobile_fax_title() == u""
#         assert self.get_value_of_screen_mobile_fax_content_1() == u""
#         assert self.get_value_of_mobile_fax_content_2() == u""
#         assert self.get_value_of_get_started_btn() == u""
#         assert self.get_value_of_no_thanks_btn() == u""
