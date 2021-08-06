# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Sign in to [printer] dialog.

@author: Ivan
@create_date: Nov 27, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_information import PrinterInformation


class SignInToPrinterDialog(SmartScreens):

    folder_name = "common"
    flow_name = "sign_in_to_printer_dialog"

    def __init__(self, driver):
        super(SignInToPrinterDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Sign in to printer dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_in_to_printer_password_textbox", timeout=timeout, raise_e=raise_e)

    def wait_for_incorrect_password_message_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Sign in to printer dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("incorrect_password_message", timeout=timeout, raise_e=raise_e)

    def wait_for_dialog_disappear(self, timeout=30, raise_e=True):
        '''
        This is a method to wait windows security dialog disappear.
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[wait_for_security_dialog_disappear]-Wait for screen disappear... ")

        return self.driver.wait_for_object_disappear("sign_in_to_printer_cancel_btn", timeout=timeout, raise_e=raise_e)

    def click_cancel_btn(self):
        '''
        This is a method to click Cancel button on Sign in to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[click_cancel_btn]-Click Cancel button... ")

        self.driver.click("sign_in_to_printer_cancel_btn")

    def click_submit_btn(self):
        '''
        This is a method to click Submit button on Sign in to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[click_submit_btn]-Click Submit button... ")

        self.driver.click("sign_in_to_printer_submit_btn")

    def input_password(self, password):
        '''
        This is a method to input password.
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[input_password]-Input password... ")

        self.driver.send_keys("sign_in_to_printer_password_textbox", password, press_enter=True)

    def get_value_of_sign_in_to_printer_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[get_value_of_sign_in_to_printer_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("sign_in_to_printer_title")

    def get_value_of_sign_in_to_printer_content(self):
        '''
        This is a method to get value of dialog contents
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[get_value_of_sign_in_to_printer_content]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("sign_in_to_printer_content")

    def get_value_of_cancel_btn(self):
        '''
        This is a method to get value of Cancel button on Sign in to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[get_value_of_cancel_btn]-Get the contents of Cancel button ...  ")

        return self.driver.get_title("sign_in_to_printer_cancel_btn")

    def get_value_of_submit_btn(self):
        '''
        This is a method to get value of Submit button on Sign in to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[get_value_of_submit_btn]-Get the contents of Submit button ...  ")

        return self.driver.get_title("sign_in_to_printer_submit_btn")

    def get_value_of_incorrect_password_message(self):
        '''
        This is a method to get value of incorrect password message on Sign in to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[SignInToPrinterDialog]:[get_value_of_incorrect_password_message]-Get the contents of incorrect_password_message ...  ")

        return self.driver.get_value("incorrect_password_message")

# -------------------------------Verification Methods-------------------------------
    def verify_sign_in_to_printer_dialog(self):
        '''
        This is a verification method to check UI strings of Sign in to printer dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(120)
        printer_information_screen = PrinterInformation(self.driver)
        logging.debug("Start to check UI strings of Sign in to printer dialog")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='sign_in_to_printer_dialog')
        assert self.get_value_of_sign_in_to_printer_title() == test_strings['sign_in_to_printer_title'] + str(printer_information_screen.get_the_value_of_name()) + "."
        assert self.get_value_of_sign_in_to_printer_content() == test_strings['sign_in_to_printer_body']
        assert self.get_value_of_cancel_btn() == test_strings['sign_in_to_printer_cancel_btn']
        assert self.get_value_of_submit_btn() == test_strings['sign_in_to_printer_Submit_btn']

    def verify_submit_button_disabled(self):
        '''
        This is a verification method to check Submit button disabled
        :parameter:
        :return:
        '''
        if self.driver.is_enable("sign_in_to_printer_submit_btn"):
            raise UnexpectedItemPresentException("the option can be clicked")
        return True

    def verify_submit_button_enabled(self):
        '''
        This is a verification method to check Submit button enabled
        :parameter:
        :return:
        '''
        if not self.driver.is_enable("sign_in_to_printer_submit_btn"):
            raise UnexpectedItemPresentException("the option can not be clicked")
        return True

    def verify_incorrect_password_message_display(self):
        '''
        This is a verification method to check incorrect password message display
        :parameter:
        :return:
        '''
        self.wait_for_incorrect_password_message_display()
#         assert self.get_value_of_incorrect_password_message == ""

    def some_operations_on_sign_in_to_printer_dialog(self, password, incorrectpassword):
        '''
        This is a verification method to check some screen
        :parameter:
        :return:
        '''
        logging.debug("enter at least 1 character verify 'Submit' button does show enabled")
        self.input_password(password)
        self.verify_submit_button_enabled()
        self.driver.clear_text("sign_in_to_printer_password_textbox")
        self.input_password(incorrectpassword)
        self.click_submit_btn()
        self.verify_incorrect_password_message_display()
        self.click_cancel_btn()
        self.wait_for_dialog_disappear()

    def enter_correct_password_flow(self, password):
        '''
        This is a flow to enter the correct password on sign in to [printer name] dialog.
        :parameter:
        :return:
        '''
        self.input_password(password)
        self.click_submit_btn()
        self.wait_for_dialog_disappear()

    def verify_sign_in_to_printer_dialog_does_not_show(self, timeout=10):
        '''
        This is a verification method to check Sign in to printer dialog does not show.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("sign_in_to_printer_title", timeout=timeout, raise_e=False)
