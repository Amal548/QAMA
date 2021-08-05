# encoding: utf-8
'''
PrinterSetupLetsPrint screen

@author: ten
@create_date: July 26, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PrinterSetupLetsPrint(SmartScreens):
    folder_name = "oobe"
    flow_name = "printer_setup_lets_print"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterSetupLetsPrint, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_setup_lets_print_title", timeout=timeout, raise_e=raise_e)

    def wait_for_print_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Print dialog load.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint]:[wait_for_print_dialog_load]-Wait for Print Dialog loading... ")

        return self.driver.wait_for_object("print_dialog_print_btn", timeout=timeout, raise_e=raise_e)

    def click_not_now_btn(self):
        '''
        This is a method to click Not Now button on Printer setup, let's print screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint]:[click_not_now_btn]-Click Not Now button... ")

        self.driver.click("not_now_btn")

    def click_print_btn(self):
        '''
        This is a method to click Print button on Printer setup, let's print screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint]:[click_print_btn]-Click Print button.. ")

        self.driver.click("print_btn")

    def click_print_btn_on_print_dialog(self):
        '''
        This is a method to click Print button on Print dialog
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint]:[click_print_btn_dialog]-Click Print button on Print dialog.. ")

        self.driver.click("print_dialog_print_btn")

    def get_value_of_printer_setup_lets_print_title(self):
        '''
        This is a method to get value of Printer setup lets print screen title
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint]:[get_value_of_printer_setup_lets_print_title]-Get the contents of printer_setup_lets_print_title...  ")

        return self.driver.get_value("printer_setup_lets_print_title")

    def get_value_of_printer_setup_lets_print_printer_name(self):
        '''
        This is a method to get value of Printer name on Printer setup lets print screen
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint]:[get_value_of_printer_setup_lets_print_printer_name]-Get the contents of Printer name...  ")

        return self.driver.get_title("printer_setup_lets_print_printer_name")

    def get_value_of_printer_setup_lets_print_contents(self):
        '''
        This is a method to get value of Printer setup lets print screen contents
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint:[get_value_of_printer_setup_lets_print_contents]-Get the contents of Printer setup lets print screen contents...  ")

        return self.driver.get_value("printer_setup_lets_print_contents")

    def get_value_of_not_now_btn(self):
        '''
        This is a method to get value of Not now button on Printer setup lets print screen
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint]:[get_value_of_not_now_btn]-Get the contents of Not now button...  ")

        return self.driver.get_title("not_now_btn")

    def get_value_of_print_btn(self):
        '''
        This is a method to get value of Print button on Printer setup lets print screen
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSetupLetsPrint]:[get_value_of_print_btn]-Get the contents of Print button...  ")

        return self.driver.get_title("print_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_printer_setup_lets_print_screen(self):
        '''
        This is a verification method to check UI string of Printer setup let's print screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(180)
        self.driver.wait_for_object("printer_setup_lets_print_image_1", timeout=10, raise_e=True)
        self.driver.wait_for_object("printer_setup_lets_print_image_2", timeout=10, raise_e=True)
        logging.debug("Start to check UI string of Printer setup let's print screen")
#         assert self.get_value_of_printer_setup_lets_print_title() == u""
#         assert self.get_value_of_printer_setup_lets_print_printer_name() == u""
#         assert self.get_value_of_printer_setup_lets_print_contents() == u""
#         assert self.get_value_of_not_now_btn() == u""
#         assert self.get_value_of_print_btn() == u""
