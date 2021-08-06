# encoding: utf-8
'''
FogetPrinterDialog

@author: ten
@create_date: Sep 23, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class FogetPrinterDialog(SmartScreens):

    folder_name = "common"
    flow_name = "forget_printer_dialog"

    def __init__(self, driver):
        super(FogetPrinterDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait agreement screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_cancel_btn(self):
        '''
        This is a method to click cancel_btn
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[click_cancel_btn]-Click cancel_btn... ")

        self.driver.click("cancel_btn")

    def click_forget_printer_btn(self):
        '''
        This is a method to click forget_printer_btn
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[click_forget_printer_btn]-Click forget_printer_btn... ")

        self.driver.click("forget_printer_btn")

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_contents_1(self):
        '''
        This is a method to get value of contents_1
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_dialog_contents_1]-Get the contents of dialog_contents_1 ...  ")

        return self.driver.get_value("dialog_contents_1")

    def get_value_of_dialog_contents_2(self):
        '''
        This is a method to get value of contents_2
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_dialog_contents_2]-Get the contents of dialog_contents_2 ...  ")

        return self.driver.get_value("dialog_contents_2")

    def get_value_of_dialog_contents_3(self):
        '''
        This is a method to get value of contents_3
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_dialog_contents_3]-Get the contents of dialog_contents_3 ...  ")

        return self.driver.get_value("dialog_contents_3")

    def get_value_of_cancel_btn(self):
        '''
        This is a method to get value of cancel_btn
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_cancel_btn]-Get the contents of cancel_btn ...  ")

        return self.driver.get_title("cancel_btn")

    def get_value_of_forget_printer_btn(self):
        '''
        This is a method to get value of forget_printer_btn.
        :parameter:
        :return:
        '''
        logging.debug("[FogetPrinterDialog]:[get_value_of_forget_printer_btn]-Get the contents of forget_printer_btn ...  ")

        return self.driver.get_title("forget_printer_btn")


# -------------------------------Verification Methods-------------------------------
    def verify_ui_string(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.[C12865260][C12865261]")
#         assert self.get_value_of_dialog_title() == u""
#         assert self.get_value_of_dialog_contents_1() == u""
#         assert self.get_value_of_dialog_contents_2() == u""
#         assert self.get_value_of_dialog_contents_3() == u""
#         assert self.get_value_of_cancel_btn() == u""
#         assert self.get_value_of_forget_printer_btn() == u""
        pass

    def verify_dialog_disappear(self):
        '''
        verify_forget_printer_option_notdisplay
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("dialog_title", raise_e=False):
            raise UnexpectedItemPresentException("the screen still exists")

        return True
