# encoding: utf-8
'''
check Download Unsuccessful Dialog

@author: ten
@create_date: Sep 4, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class DownloadDialog(SmartScreens):

    folder_name = "menubar"
    flow_name = "download_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(DownloadDialog, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        logging.debug("[DownloadDialog]:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_ok_btn(self):
        '''
        Click OK Button
        :parameter:
        :return:
        '''
        logging.debug("[DownloadDialog]:[click_ok_btn]-Click 'OK' button... ")

        self.driver.click("ok_btn")

    def get_value_of_dialog_title(self):
        '''
        get value of title
        :parameter:
        :return:
        '''
        logging.debug("[DownloadDialog]:[dialog_title]-Get the contents of dialog_title")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_content(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[DownloadDialog]:[dialog_content]-Get the contents of dialog_content")

        return self.driver.get_value("dialog_content")

    def get_value_of_ok_btn(self):
        '''
        get value of ok button
        :parameter:
        :return:
        '''
        logging.debug("[DownloadDialog]:[ok_btn]-Get the contents of ok_btn")

        return self.driver.get_title("ok_btn")

# -------------------------------Verification Methods---------------------------
    def verify_download_unsuccessful_dialog_string(self):
        '''
        verify_ui_string
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
        self.wait_for_screen_load()
        assert self.get_value_of_dialog_title() == "Download Unsuccessful"
        assert self.get_value_of_dialog_content() == "A problem occurred while downloading the update. Please try again."
        assert self.get_value_of_ok_btn() == "OK"

    def verify_download_successful_dialog_string(self):
        '''
        verify_ui_string
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
        assert self.get_value_of_dialog_title() == "Download Successful"
        assert self.get_value_of_ok_btn() == "OK" 
