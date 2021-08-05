# encoding: utf-8
'''
Check for updates Dialog 
@author: ten
@create_date: July 25, 2019
'''

import logging

from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class CheckforupdatesDialog(SmartScreens):
    folder_name = "menubar"
    flow_name = "check_for_updates_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(CheckforupdatesDialog, self).__init__(driver)
# -------------------------------Operate Elements------------------------------

    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        pass

    def wait_for_no_software_update_available_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        logging.debug("[no_software_update_available]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("no_software_update_available", timeout=timeout, raise_e=raise_e)

    def wait_for_new_software_available_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("new_software_available", timeout=timeout, raise_e=raise_e)

    def click_no_btn(self):
        '''
        Click no Button
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog:[click_no_btn]-Click 'no' button... ")

        self.driver.click("no_btn")

    def click_yes_btn(self):
        '''
        Click yes Button
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog:[click_yes_btn]-Click 'yes' button... ")

        self.driver.click("yes_btn")

    def click_checkbox_btn(self):
        '''
        Click yes Button
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog:[click_checkbox_btn]-Click checkbox button... ")

        self.driver.check_box("checkbox_btn")

    def click_ok_btn(self):
        '''
        Click OK Button
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog:[click_ok_btn]-Click 'OK' button... ")

        self.driver.click("ok_btn_dialog", is_native_event=True)

    def get_value_of_no_software_update_available(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog]:[no_software_update_available]-Get the contents of dialog_contents")

        return self.driver.get_value("no_software_update_available")

    def get_value_of_new_software_available(self):
        '''
        get value of new software available table
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog]:[dialog_contents]-Get the contents of dialog_contents")

        return self.driver.get_value("new_software_available")

    def get_value_of_ok_btn_dialog(self):
        '''
        get value of ok button
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog]:[dialog_contents]-Get the contents of ok_btn_dialog")

        return self.driver.get_title("ok_btn_dialog")

    def get_value_of_checkbox_btn(self):
        '''
        get value of checkbox button
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog]:[dialog_contents]-Get the contents of ok_btn_dialog")

        return self.driver.get_title("checkbox_btn")

    def get_value_of_no_btn(self):
        '''
        get value of no button
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog]:[dialog_contents]-Get the contents of ok_btn_dialog")

        return self.driver.get_title("no_btn")

    def get_value_of_yes_btn(self):
        '''
        get value of yes button
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog]:[dialog_contents]-Get the contents of ok_btn_dialog")

        return self.driver.get_title("yes_btn")

        # -------------------------------Verification Methods----------------
    def verify_no_software_update_available_dialog(self):
        '''
        Verify strings and matching string table
        :parameter:
        :return:
        '''
        logging.debug("verify no_software_update_available Dialog")
        self.wait_for_no_software_update_available_load()
        assert self.get_value_of_no_software_update_available() == "No software update is available.  Your version of HP Smart is up-to-date."
        assert self.get_value_of_ok_btn_dialog() == "OK"

    def verify_new_update_availabled_dialog(self):
        '''
        Verify strings and matching string table
        :parameter:
        :return:
        '''
        logging.debug("verify Checkforupdates Dialog")
        self.wait_for_new_software_available_load()
        assert self.get_value_of_new_software_available() == "New Software Available"
        assert self.get_value_of_checkbox_btn() == "Don't automatically check for updates"
        assert self.get_value_of_no_btn() == "No"
        assert self.get_value_of_yes_btn() == "Yes"

    def verify_no_software_update_available_dialog_dismissed(self, timeout=10):
        '''
        Verify no_software_update_available_dialog_dismissed
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("no_software_update_available", timeout=timeout, raise_e=False)

    def verify_new_update_availabled_dialog_no_appear(self, timeout=10):
        '''
        Verify new_update_availabled_dialog_no_appear
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("new_software_available", timeout=timeout, raise_e=False)

