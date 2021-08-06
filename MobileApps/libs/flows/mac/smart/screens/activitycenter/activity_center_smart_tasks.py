# encoding: utf-8
'''
Description: It defines the operations of element and verification methods for Activity Center Fly-out.

@author: Ivan
@create_date: Jan 20, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ActivityCenterSmartTasks(SmartScreens):

    folder_name = "activitycenter"
    flow_name = "activity_center_smart_tasks"

    def __init__(self, driver):
        super(ActivityCenterSmartTasks, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Activity Center Fly-out shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterSmartTasks]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("activity_center_print", timeout=timeout, raise_e=raise_e)

    def click_activity_center_print(self):
        '''
        This is a method to click Print option under Bell menu after clicking Bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterSmartTasks]]:[click_activity_center_print]-Click Print option... ")

        self.driver.click("activity_center_print", is_native_event=True)

    def click_activity_center_smart_tasks(self):
        '''
        This is a method to click Smart Tasks option under Bell menu after clicking Bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterSmartTasks]]:[click_activity_center_smart_tasks]-Click Smart Tasks option... ")

        self.driver.click("activity_center_smart_tasks", is_native_event=True)

    def click_activity_center_mobile_fax(self):
        '''
        This is a method to click Mobile Fax option under Bell menu after clicking Bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterSmartTasks]]:[click_activity_center_mobile_fax]-Click Mobile Fax option... ")

        self.driver.click("activity_center_mobile_fax", is_native_event=True)

    def get_value_of_activity_center_print(self):
        '''
        This is a method to get value of Print option under Activity Center Fly-out
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterSmartTasks]:[get_value_of_dialog_title]-Get the value of Print option ...  ")

        return self.driver.get_title("upload_file_error_dialog_title")

    def get_value_of_activity_center_smart_tasks(self):
        '''
        This is a method to get value of Smart Tasks option under Activity Center Fly-out
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterSmartTasks]:[get_value_of_activity_center_smart_tasks]-Get the value of Smart Tasks option ...  ")

        return self.driver.get_title("activity_center_smart_tasks")

    def get_value_of_activity_center_mobile_fax(self):
        '''
        This is a method to get value of Mobile Fax option under Activity Center Fly-out
        :parameter:
        :return:
        '''
        logging.debug("[ActivityCenterSmartTasks]:[get_value_of_activity_center_mobile_fax]-Get the value of Mobile Fax option ...  ")

        return self.driver.get_title("activity_center_mobile_fax")

# -------------------------------Verification Methods-------------------------------
    def verify_activity_center_flyout_screen(self):
        '''
        This is a verification method to check UI strings of Activity Center Fly-out screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Activity Center Fly-out screen")
#         assert self.get_value_of_activity_center_print() == u""
#         assert self.get_value_of_activity_center_smart_tasks() == u""
#         assert self.get_value_of_activity_center_mobile_fax() == u""

    def verify_dialog_disappear(self, timeout=10):
        '''
        verify Activity Center Fly-out screen disappear after select one of the options.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("activity_center_mobile_fax", timeout=timeout, raise_e=False)
