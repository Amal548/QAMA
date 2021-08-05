# encoding: utf-8
'''
Description: It defines operations of element and verification methods on the smart tasks screen.

@author: Ivan
@create_date: Sep 26, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SmartTasks(SmartScreens):

    folder_name = "smarttasks"
    flow_name = "smart_tasks"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(SmartTasks, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait instant ink sign in page load.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("welcome_modal_head", timeout=timeout, raise_e=raise_e)

    def wait_for_empty_smart_tasks_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait create smart tasks screen load.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[wait_for_empty_smart_tasks_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("empty_smart_tasks_content", timeout=timeout, raise_e=raise_e)

    def wait_for_create_smart_tasks_screen(self, timeout=30, raise_e=True):
        '''
        This is a method to wait create smart tasks screen load - Without smart tasks created.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[wait_for_create_smart_tasks_screen]-Wait for screen loading... ")

        return self.driver.wait_for_object("create_smart_tasks_content_right_side", timeout=timeout, raise_e=raise_e)

    def wait_for_my_smart_tasks_screen(self, timeout=30, raise_e=True):
        '''
        This is a method to wait my smart tasks screen load - With smart tasks created.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[wait_for_my_smart_tasks_screen]-Wait for screen loading... ")

        return self.driver.wait_for_object("my_smart_tasks_content", timeout=timeout, raise_e=raise_e)

    def wait_for_exit_without_saving_changes_dialog(self, timeout=30, raise_e=True):
        '''
        This is a method to wait exit without saving changes dialog load.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[wait_for_exit_without_saving_changes_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("exit_dialog_title", timeout=timeout, raise_e=raise_e)

    def click_get_started_btn(self):
        '''
        This is a method to click get started button on smart tasks welcome modal screen.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[click_get_started_btn]-Click get started button... ")

        self.driver.click("welcome_modal_get_started_btn", is_native_event=True)

    def click_sign_in_link(self):
        '''
        This is a method to click already have smart tasks sign in link on smart tasks welcome modal screen.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[click_sign_in_link]-Click already have smart tasks sign in link... ")

        self.driver.click("welcome_modal_sign_in_link", is_native_event=True)

    def click_create_a_smart_task_btn(self):
        '''
        This is a method to click create a smart task button on create smart tasks screen.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[click_create_a_smart_task_btn]-Click create a smart task button... ")

        self.driver.click("create_smart_tasks_btn", is_native_event=True)

    def click_yes_btn_on_exit_dialog(self):
        '''
        This is a method to click yes button on exit without saving changes dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[click_yes_btn_on_exit_dialog]-Click yes button... ")

        self.driver.click("exit_dialog_yes_btn", is_native_event=True)

    def click_no_btn_on_exit_dialog(self):
        '''
        This is a method to click no button on exit without saving changes dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SmartTasks]:[click_no_btn_on_exit_dialog]-Click no button... ")

        self.driver.click("exit_dialog_no_btn", is_native_event=True)

# -------------------------------Verification Methods--------------------------
