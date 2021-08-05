# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Find the printer PIN dialog.

@author: Ivan
@create_date: Dec 09, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class FindThePrinterPINDialog(SmartScreens):

    folder_name = "common"
    flow_name = "find_the_printer_pin_dialog"

    def __init__(self, driver):
        super(FindThePrinterPINDialog, self).__init__(driver)

# -------------------------------Operate Elements-----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Find the printer PIN dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("find_the_printer_pin_content", timeout=timeout, raise_e=raise_e)

    def wait_for_incorrect_password_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Find the printer PIN dialog with incorrect password input shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("invalid_pin_code_text", timeout=timeout, raise_e=raise_e)

    def click_cancel_btn(self):
        '''
        This is a method to click Cancel button on Find the printer PIN dialog.
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[click_cancel_btn]-Click Cancel button... ")

        self.driver.click("find_the_printer_pin_cancel_btn")

    def click_submit_btn(self):
        '''
        This is a method to click Submit button on Find the printer PIN dialog.
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[click_submit_btn]-Click Submit button... ")

        self.driver.click("find_the_printer_pin_submit_btn")

    def input_password(self, password):
        '''
        This is a method to input password.
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[input_password]-Input password... ")

        self.driver.send_keys("find_the_printer_pin_inputbox", password, press_enter=True)

    def clear_enter_wifi_password_box(self):
        '''
        This is a method to clear enter contents in password box
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[enter_wifi_password_box]-clear-enter_wifi_password_box... ")

        self.driver.clear_text("find_the_printer_pin_inputbox")

    def get_value_of_find_the_printer_pin_title(self):
        '''
        This is a method to get value of dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[get_value_of_find_the_printer_pin_title]-Get the contents of dialog_title ...  ")

        return self.driver.get_value("find_the_printer_pin_title")

    def get_value_of_find_the_printer_pin_content(self):
        '''
        This is a method to get value of dialog contents
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[get_value_of_find_the_printer_pin_content]-Get the contents of dialog_contents ...  ")

        return self.driver.get_value("find_the_printer_pin_content")

    def get_value_of_find_the_printer_pin_text(self):
        '''
        This is a method to get value of dialog contents
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[get_value_of_find_the_printer_pin_text]-Get the contents of PIN text ...  ")

        return self.driver.get_value("find_the_printer_pin_text")

    def get_value_of_invalid_pin_code_text(self):
        '''
        This is a method to get value of dialog contents after invalid code input
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[get_value_of_invalid_pin_code_text]-Get the contents of Invalid code text ...  ")

        return self.driver.get_value("invalid_pin_code_text")

    def get_value_of_cancel_btn(self):
        '''
        This is a method to get value of Cancel button on Find the printer PIN dialog.
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[get_value_of_cancel_btn]-Get the contents of Cancel button ...  ")

        return self.driver.get_title("find_the_printer_pin_cancel_btn")

    def get_value_of_submit_btn(self):
        '''
        This is a method to get value of Submit button on Find the printer PIN dialog.
        :parameter:
        :return:
        '''
        logging.debug("[FindThePrinterPINDialog]:[get_value_of_submit_btn]-Get the contents of Submit button ...  ")

        return self.driver.get_title("sign_in_to_printer_submit_btn")

# -------------------------------Verification Methods-------------------------------
    def verify_find_the_printer_pin_dialog(self):
        '''
        This is a verification method to check UI strings of Find the printer PIN dialog.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        self.verify_submit_btn_disable()
#         assert self.get_value_of_find_the_printer_pin_title() == u""
#         assert self.get_value_of_find_the_printer_pin_content() == u""
#         assert self.get_value_of_find_the_printer_pin_text() == u""
#         assert self.get_value_of_cancel_btn() == u""
#         assert self.get_value_of_submit_btn() == u""

    def verify_find_the_printer_pin_dialog_with_incorrect_password(self):
        '''
        This is a verification method to check UI strings of Find the printer PIN dialog with incorrect password input.
        :parameter:
        :return:
        '''
        self.wait_for_incorrect_password_screen_load(60)
        self.verify_submit_btn_enable()
#         assert self.get_value_of_find_the_printer_pin_title() == u""
#         assert self.get_value_of_find_the_printer_pin_content() == u""
#         assert self.get_value_of_find_the_printer_pin_text() == u""
#         assert self.get_value_of_cancel_btn() == u""
#         assert self.get_value_of_submit_btn() == u""

    def verify_submit_btn_disable(self):
        '''
        This is a verification method to check Submit button is disable
        :parameter:
        :return:
        '''
        logging.debug("verify Submit button's behavior")
        if self.driver.is_enable("find_the_printer_pin_submit_btn"):
            raise UnexpectedItemPresentException("Submit button is enabled")
        return True

    def verify_submit_btn_enable(self):
        '''
        This is a verification method to check Submit button is disable
        :parameter:
        :return:
        '''
        logging.debug("verify Submit button's behavior")
        if self.driver.is_enable("find_the_printer_pin_submit_btn"):
            raise UnexpectedItemPresentException("Submit button is disabled")
        return True

    def check_submit_btn_behavior_incorrect_pin(self):
        '''
        This is a verification method to check Submit button behavior with different PIN input
        :parameter:
        :return:
        '''
        logging.debug("Enter less than 8 digits of pin on 'Find the printer PIN' dialog, verify 'Submit' button does not show enabled")
        self.input_password(123456)
        self.verify_submit_btn_disable()

        logging.debug("Enter 8 digits of pin on 'Find the printer PIN' dialog, verify 'Submit' button shows enabled")
        self.input_password(12345678)
        self.verify_submit_btn_enable()

        logging.debug('Enter incorrect pin on "Find the printer PIN" dialog, verify error message shows')
        self.click_submit_btn()
        self.verify_find_the_printer_pin_dialog_with_incorrect_password()

    def check_submit_btn_behavior_correct_pin(self, pin):
        '''
        This is a verification method to check Submit button behavior with correct PIN input
        :parameter:
        :return:
        '''
        logging.debug("Enter correct pin on 'Find the printer PIN' dialog")
        self.input_password(pin)
        self.verify_submit_btn_enable()
        self.click_submit_btn()
        self.verify_dialog_disappear(60)

    def click_cancel_btn_flow(self):
        '''
        This is a verification method to click Cancel button on "Find the printer PIN" dialog
        :parameter:
        :return:
        '''
        self.click_cancel_btn()
        self.verify_dialog_disappear()

    def verify_dialog_disappear(self, timeout=10):
        '''
        This is a verification method to verify Find the printer PIN dialog disappear after clicking cancel button.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("find_the_printer_pin_content", timeout=timeout, raise_e=False)
