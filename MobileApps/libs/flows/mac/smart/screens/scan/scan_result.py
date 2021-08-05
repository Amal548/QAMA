# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the scan result screen.

@author: Sophia
@create_date: May 8, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ScanResult(SmartScreens):
    folder_name = "scan"
    flow_name = "scan_result"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ScanResult, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait scan result screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("save_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_scan_result_mobile_fax_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait scan result mobile fax screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[wait_for_scan_result_mobile_fax_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("continue_to_fax_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_mobile_fax_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait mobile fax button shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("mobile_fax_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_smart_task_sign_in_flyout_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait smart task sign in dialog shows correctly after clicking smart tasks button on scan result screen.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[wait_for_smart_task_sign_in_flyout_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("smart_tasks_sign_in_flyout_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_exit_without_saving_dialog(self, timeout=30, raise_e=True):
        '''
        This is a method to wait exit without saving changes dialog load.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[wait_for_exit_without_saving_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("exit_dialog_title", timeout=timeout, raise_e=raise_e)

    def click_save_btn(self):
        '''
        This is a method to click save button.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[click_save_btn]-Click 'Save' button... ")

        self.driver.click("save_btn")

    def click_print_btn(self):
        '''
        This is a method to click print button on the scan result screen.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[click_print_btn]-Click 'Print' button... ")

        self.driver.click("print_btn")

    def click_smart_tasks_btn(self):
        '''
        This is a method to click smart tasks button on the scan result screen.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[click_smart_tasks_btn]-Click 'Smart Tasks' button... ")

        self.driver.click("smart_tasks_btn", is_native_event=True)

    def click_continue_to_fax_btn(self):
        '''
        This is a method to click Continue to Fax button on the scan result mobile fax screen.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[click_continue_to_fax_btn]-Click Continue to Fax button... ")

        self.driver.click("continue_to_fax_btn", is_native_event=True)

    def click_sign_in_btn_on_flyout(self):
        '''
        This is a method to click sign in button on smart task sign in flyout dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[click_sign_in_btn_on_flyout]-Click 'Sign in' button... ")

        self.driver.click("smart_tasks_sign_in_flyout_btn", is_native_event=True)

    def click_yes_btn_on_exit_dialog(self):
        '''
        This is a method to click yes button on exit without saving dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[click_yes_btn_on_exit_dialog]-Click yes button... ")

        self.driver.click("exit_dialog_yes_btn", is_native_event=True)

    def click_no_btn_on_exit_dialog(self):
        '''
        This is a method to click no button on exit without saving dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[click_no_btn_on_exit_dialog]-Click no button... ")

        self.driver.click("exit_dialog_no_btn", is_native_event=True)

    def click_mobile_fax_btn(self):
        '''
        This is a method to click yes button on exit without saving dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[click_mobile_fax_btn]-Click mobile fax button... ")

        self.driver.click("mobile_fax_btn", is_native_event=True)

    def get_value_of_mobile_fax_btn(self):
        '''
        This is a method to get value of mobile fax button.
        :parameter:
        :return:
        '''
        logging.debug("[ScanResultScreen]:[get_value_of_mobile_fax_btn]-Get the contents of mobile_fax_btn..  ")

        return self.driver.get_title("mobile_fax_btn")

# -------------------------------Verification Methods--------------------------
    def verify_mobile_fax_button_is_load(self):
        '''
        This is a verification method to check UI strings of Mobile Fax button.
        :parameter:
        :return:
        '''
        self.wait_for_mobile_fax_btn_display()
        assert "Mobile Fax" in self.get_value_of_mobile_fax_btn()
