# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on the let's find your printer screen.

@author: ten
@create_date: July 24, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class FindYourPrinter(SmartScreens):
    folder_name = "oobe"
    flow_name = "let_find_your_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(FindYourPrinter, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Let's find your printer screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("make_sure_printer_content", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        This is a method to click continue button on Let's find your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[click_continue_btn]-Click continue button... ")

        self.driver.click("continue_btn")

    def get_value_of_let_find_your_printer_title(self):
        '''
        This is a method to get value of Let's find your printer screen title.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[get_value_of_let_find_your_printer_title]-Get the contents of let's find your printer title ...  ")

        return self.driver.get_value("let_find_your_printer_title")

    def get_value_of_make_sure_printer_content(self):
        '''
        This is a method to get value of make_sure_printer_content.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[get_value_of_make_sure_printer_content]-Get the contents of Make sure printer content ...  ")

        return self.driver.get_value("make_sure_printer_content")

    def get_value_of_continue_content(self):
        '''
        This is a method to get value of continue_content.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[get_value_of_continue_content]-Get the contents of continue content ...  ")

        return self.driver.get_value("continue_content")

    def get_value_of_below_content(self):
        '''
        This is a method to get value of below_content.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[get_value_of_below_content]-Get the contents of below content ...  ")

        return self.driver.get_value("below_content")

    def get_value_of_if_you_want_to_set_up_content(self):
        '''
        This is a method to get value of if_you_want_to_set_up_content.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[get_value_of_if_you_want_to_set_up_content]-Get the contents of if you want to set up content ...  ")

        return self.driver.get_value("if_you_want_to_set_up_content")

    def get_value_of_note_content(self):
        '''
        This is a method to get value of note_content.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[get_value_of_note_content]-Get the contents of note content ...  ")

        return self.driver.get_value("note_content")

    def get_value_of_if_you_are_having_trouble_content(self):
        '''
        This is a method to get value of if_you_want_to_set_up_content.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[get_value_of_if_you_are_having_trouble_content]-Get the contents of if you are having trouble content ...  ")

        return self.driver.get_value("if_you_are_having_trouble_content")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on Let's find your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[FindYourPrinter]:[get_value_of_continue_btn_find_your_printer]-Get the contents of Continue button...  ")

        return self.driver.get_value("continue_btn")

# -------------------------------Verification Methods--------------------------
    def verify_lets_find_your_printer_screen(self):
        '''
        This is a verification method to check the string UI of Let's find your printer screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check the string UI of Let's find your printer screen")
#         assert self.get_value_of_let_find_your_printer_title() == u""
#         assert self.get_value_of_make_sure_printer_content() == u""
#         assert self.get_value_of_continue_content() == u""
#         assert self.get_value_of_below_content() == u""
#         assert self.get_value_of_if_you_want_to_set_up_content() == u""
#         assert self.get_value_of_note_content() == u""
#         assert self.get_value_of_if_you_are_having_trouble_content() == u""
#         assert self.get_value_of_continue_btn() == u""
