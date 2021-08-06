# encoding: utf-8
'''
Description: It defines classes_and_methods for Printer Setup Incomplete Dialog screen

@author: ten
@create_date: July 29, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PrinterSetupIncompleteDialog(SmartScreens):
    folder_name = "oobe"
    flow_name = "printer_setup_incomplete_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterSetupIncompleteDialog, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_ok_btn(self):
        '''
        Click OK Button
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[click_ok_btn]-Click 'OK' button... ")

        self.driver.click("ok_btn_dialog", is_native_event=True)

    def click_ok_btn_for_choose_printer(self):
        '''
        Click OK Button
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[click_ok_btn_for_choose_printer]-Click 'OK' button... ")

        self.driver.click("ok_btn_dialog_2", is_native_event=True)

    def click_back_btn(self):
        '''
        Click back Button
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[click_back_btn]-Click 'Back' button... ")

        self.driver.click("back_btn_dialog", is_native_event=True)

    def get_value_of_contents_1_1(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_contents_1_1]-Get the contents of contents_1_1...  ")

        return self.driver.get_value("contents_1_1")

    def get_value_of_contents_1_2(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_contents_1_2]-Get the contents of contents_1_2...  ")

        return self.driver.get_value("contents_1_2")

    def get_value_of_contents_1_3(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_contents_1_3]-Get the contents of contents_1_3...  ")

        return self.driver.get_value("contents_1_3")

    def get_value_of_contents_1_4(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_contents_1_4]-Get the contents of contents_1_4..  ")

        return self.driver.get_value("contents_1_4")

    def get_value_of_contents_1_5(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_contents_1_5]-Get the contents of contents_1_5...  ")

        return self.driver.get_value("contents_1_5")

    def get_value_of_contents_2_1(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_contents_2_1]-Get the contents of contents_2_1...  ")

        return self.driver.get_value("contents_2_1")

    def get_value_of_contents_2_2(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_contents_2_2]-Get the contents of contents_2_2...  ")

        return self.driver.get_value("contents_2_2")

    def get_value_of_contents_2_3(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_contents_2_3]-Get the contents of contents_2_3...  ")

        return self.driver.get_value("contents_2_3")

    def get_value_of_back_btn_dialog(self):
        '''
        get_value_of_back_btn_dialog
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_back_btn_dialog]-Get the contents of back_btn_dialog...  ")

        return self.driver.get_title("back_btn_dialog")

    def get_value_of_ok_btn_dialog(self):
        '''
        get_value_of_ok_btn_dialog
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_ok_btn_dialog]-Get the contents of ok_btn_dialog...  ")

        return self.driver.get_title("ok_btn_dialog")

    def get_value_of_ok_btn_dialog_2(self):
        '''
        get_value_of_ok_btn_dialog
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupIncompleteDialog]:[get_value_of_ok_btn_dialog_2]-Get the contents of ok_btn_dialog_2...  ")

        return self.driver.get_title("ok_btn_dialog_2")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_ui_string(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.[C12797957]")
