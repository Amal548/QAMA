# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Upload File Error dialog.

@author: Ivan
@create_date: Jan 13, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class UploadFileErrorDialog(SmartScreens):

    folder_name = "common"
    flow_name = "upload_file_error_dialog"

    def __init__(self, driver):
        super(UploadFileErrorDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Upload File Error dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[UploadFileErrorDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("upload_file_error_dialog_contents", timeout=timeout, raise_e=raise_e)

    def click_retry_btn(self):
        '''
        This is a method to click Retry button on Upload File Error dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UploadFileErrorDialog]:[click_retry_btn]-Click Retry button... ")

        self.driver.click("upload_file_error_dialog_retry_btn")

    def click_cancel_btn(self):
        '''
        This is a method to click Cancel button on Upload File Error dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UploadFileErrorDialog]:[click_cancel_btn]-Click Cancel button... ")

        self.driver.click("upload_file_error_dialog_cancel_btn")

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[UploadFileErrorDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("upload_file_error_dialog_title")

    def get_value_of_dialog_contents(self):
        '''
        This is a method to get value of contents_1
        :parameter:
        :return:
        '''
        logging.debug("[UploadFileErrorDialog]:[get_value_of_dialog_contents]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("upload_file_error_dialog_contents")

    def get_value_of_retry_btn(self):
        '''
        This is a method to get value of Retry button on Upload File Error dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UploadFileErrorDialog]:[get_value_of_retry_btn]-Get the value of Retry button ... ")

        return self.driver.get_title("upload_file_error_dialog_retry_btn")

    def get_value_of_cancel_btn(self):
        '''
        This is a method to get value of Cancel button on Upload File Error dialog.
        :parameter:
        :return:
        '''
        logging.debug("[UploadFileErrorDialog]:[get_value_of_cancel_btn]-Get the value of Cancel button ... ")

        return self.driver.get_title("upload_file_error_dialog_cancel_btn")

# -------------------------------Verification Methods-------------------------------
    def verify_upload_file_error_dialog(self):
        '''
        This is a verification method to check UI strings of Upload File Error dialog
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check UI strings of Upload File Error dialog")
#         assert self.get_value_of_dialog_title() == u""
#         assert self.get_value_of_dialog_contents() == u""
#         assert self.get_value_of_retry_btn() == u""
#         assert self.get_value_of_cancel_btn() == u""

    def verify_dialog_disappear(self, timeout=10):
        '''
        verify Upload File Error dialog disappear after clicking Cancel button.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("upload_file_error_dialog_contents", timeout=timeout, raise_e=False)
