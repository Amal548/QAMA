# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect printer to WiFi Help Dialog.

@author: ten
@create_date: July 25, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectPrinterHelpDialog(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_printer_help_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectPrinterHelpDialog, self).__init__(driver)

# -------------------------------Operate Elements------------------------------

    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("help_dialog_contents_1", timeout=timeout, raise_e=raise_e)

    def click_help_dialog_continue_btn(self):
        '''
        This is a method to click Continue Button on Help dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[click_help_dialog_continue_btn]-Click Continue button... ")

        self.driver.click("help_dialog_continue_btn", is_native_event=True)

    def click_help_dialog_change_connection_btn(self):
        '''
        This is a method to click Change connection button on Help dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[click_help_dialog_change_connection_btn]-Click Change connection button... ")

        self.driver.click("help_dialog_change_connection_btn", is_native_event=True)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of Help dialog title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_dialog_title]-Get the value of Help dialog_title...  ")

        return self.driver.get_value("help_dialog_title")

    def get_value_of_help_dialog_contents_1(self):
        '''
        This is a method to get value of Help dialog Content - 1
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_help_dialog_contents_1]-Get the value of Help dialog Content - 1...  ")

        return self.driver.get_value("help_dialog_contents_1")

    def get_value_of_help_dialog_contents_2(self):
        '''
        This is a method to get value of Help dialog Content - 2
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_help_dialog_contents_2]-Get the value of Help dialog Content - 2...  ")

        return self.driver.get_value("help_dialog_contents_2")

    def get_value_of_help_dialog_contents_3(self):
        '''
        This is a method to get value of Help dialog Content - 3
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_help_dialog_contents_3]-Get the value of Help dialog Content - 3...  ")

        return self.driver.get_value("help_dialog_contents_3")

    def get_value_of_help_dialog_contents_link(self):
        '''
        This is a method to get value of Help dialog Content link
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_help_dialog_contents_link]-Get the value of Help dialog Content link...  ")

        return self.driver.get_title("help_dialog_contents_link")

    def get_value_of_change_connection_btn(self):
        '''
        This is a method to get value of Help dialog Change connection button
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_change_connection_btn]-Get the value of Help dialog Change connection button...  ")

        return self.driver.get_title("help_dialog_change_connection_btn")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Help dialog Continue button
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrinterHelpDialog]:[get_value_of_continue_btn]-Get the value of Help dialog Continue button...  ")

        return self.driver.get_title("help_dialog_continue_btn")

    # -------------------------------Verification Methods---------------
    def verify_connect_printer_to_wifi_help_dialog(self):
        '''
        This is a verification method to check UI strings of Connect Printer To WiFi Help Dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to verify UI string of Connect Printer To WiFi Help Dialog")
#         assert self.get_value_of_dialog_title() == u"Connect printer help"
#         assert self.get_value_of_help_dialog_contents_1() == u""
#         assert self.get_value_of_help_dialog_contents_2() == u""
#         assert self.get_value_of_help_dialog_contents_3() == u""
#         assert self.get_value_of_help_dialog_contents_link() == u""
#         assert self.get_value_of_change_connection_btn() == u""
#         assert self.get_value_of_continue_btn() == u""
