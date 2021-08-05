# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for Activity Center Fly-out.

@author: Ivan
@create_date: Jan 20, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ActivityCenterPrint(SmartScreens):

    folder_name = "activitycenter"
    flow_name = "activity_center_print"

    def __init__(self, driver):
        super(ActivityCenterPrint, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Activity Center Print page shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("activity_center_print_image", timeout=timeout, raise_e=raise_e)

    def click_activity_center_print_close_btn(self):
        '''
        This is a method to click Close button on Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_activity_center_print_close_btn]-Click Close button... ")

        self.driver.click("activity_center_print_close_btn", is_native_event=True)

    def click_activity_center_print_minimize_btn(self):
        '''
        This is a method to click Minimize button on Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]]:[click_activity_center_print_minimize_btn]-Click Minimize button... ")

        self.driver.click("activity_center_print_minimize_btn", is_native_event=True)

    def get_value_of_activity_center_print_title(self):
        '''
        This is a method to get value of title for Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_activity_center_print_title]-Get the value of title ...  ")

        return self.driver.get_value("activity_center_print_title")

    def get_value_of_activity_center_print_content_1(self):
        '''
        This is a method to get value of content - 1 for Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_activity_center_print_content_1]-Get the value of content - 1 ...  ")

        return self.driver.get_value("activity_center_print_content_1")

    def get_value_of_activity_center_print_content_2(self):
        '''
        This is a method to get value of content - 2 for Activity Center Print page.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterPrint]:[get_value_of_activity_center_print_content_2]-Get the value of content - 2 ...  ")

        return self.driver.get_value("activity_center_print_content_2")

# -------------------------------Verification Methods-------------------------------
    def verify_activity_center_print_page(self):
        '''
        This is a verification method to check UI strings of Activity Center Print Page.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Activity Center Print Page")
#         assert self.get_value_of_activity_center_print_title() == u""
#         assert self.get_value_of_activity_center_print_content_1() == u""
#         assert self.get_value_of_activity_center_print_content_2() == u""
