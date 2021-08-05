# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Print Anywhere screen

@author: ten
@create_date: Sep 10, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_setting_scroll import PrinterSettingScroll


class Print_Anywhere(PrinterSettingScroll, SmartScreens):

    folder_name = "printersettings"
    flow_name = "print_anywhere"

    def __init__(self, driver):
        super(Print_Anywhere, self).__init__(driver)

#  ------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_anywhere_content_1", timeout=timeout, raise_e=raise_e)

    def wait_for_print_anywhere_enabled_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_in_or_enable_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_print_from_other_devices_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_from_other_devices_title", timeout=timeout, raise_e=raise_e)

    def wait_for_print_connected_another_account_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_connected_to_another_account_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_print_anywhere_title(self):
        '''
        This is a method to get value of Print anywhere screen title.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_title]-Get the contents of print_anywhere_title ...  ")

        return self.driver.get_value("print_anywhere_title")

    def get_value_of_print_anywhere_content_1(self):
        '''
        This is a method to get value of Print anywhere screen content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_content_1]-Get the contents of Print anywhere screen content - 1...  ")

        return self.driver.get_value("print_anywhere_content_1")

    def get_value_of_print_anywhere_content_2(self):
        '''
        This is a method to get value of Print anywhere screen content - 2.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_content_2]-Get the contents of Print anywhere screen content - 2...  ")

        return self.driver.get_value("print_anywhere_content_2")

    def get_value_of_print_anywhere_content_3(self):
        '''
        This is a method to get value of Print anywhere screen content - 3.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_content_3]-Get the contents of Print anywhere screen content - 3...  ")

        return self.driver.get_value("print_anywhere_content_3")

    def get_value_of_get_more_help_link(self):
        '''
        This is a method to get value of Get more help link on Print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_get_more_help_link-Get the contents of get_more_help_link ...  ")

        return self.driver.get_value("get_more_help_link")

    def get_value_of_sign_in_or_enable_btn(self):
        '''
        This is a method to get value of Sign in or Enable button on Print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_printer_anywhere_btn-Get the contents of print_anywhere_btn ...  ")

        return self.driver.get_title("sign_in_or_enable_btn")

    def get_value_of_print_anywhere_enable_content(self):
        '''
        get_value_of_printer_anywhere_enable_content
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_print_anywhere_enable_content]-Get the contents of print_anywhere_enable_content ...  ")

        return self.driver.get_title("print_anywhere_enable_content")

    def get_value_of_send_link_btn(self):
        '''
        get_value_of_send_link_btn
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[get_value_of_send_link_btn-Get the contents of send_link_btn ...  ")

        return self.driver.get_title("send_link_btn")

    def click_get_more_help_link(self):
        '''
        This is a method to click Get more help link on Print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_get_more_help_link]-Click get_more_help_link... ")

        self.driver.click("get_more_help_link")

    def click_sign_in_btn(self):
        '''
        This is a method to click Sign In button on Print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_sign in_btn]-Click sign in btn... ")

        self.driver.click("sign_in_or_enable_btn")

    def click_send_link_btn(self):
        '''
        This is a method to click print anywhere
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_send_link_btn]-Click send_link_btn... ")

        self.driver.click("send_link_btn")

    def click_enable_btn(self):
        '''
        This is a method to click Enable button after sign in on Print anywhere screen.
        :parameter:
        :return:
        '''
        logging.debug("[Print_Anywhere]:[click_enable_btn]-Click enable_btn... ")

        self.driver.click("sign_in_or_enable_btn")

#   ------------------------------Verification Methods-------------------------------------------
    def verify_screen_shows_with_sign_in_button(self):
        '''
        verify_screen_shows_with_sign_in_button
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Verify screen shows with 'sign in' button")
#         assert self.get_value_of_print_anywhere_title() == u''
#         assert self.print_anywhere_content_1() == u''
#         assert self.print_anywhere_content_2() == u''
#         assert self.print_anywhere_content_3() == u''
#         assert self.get_value_of_get_more_help_link() == u''
        assert self.get_value_of_sign_in_or_enable_btn() == 'Sign In'

    def verify_screen_shows_with_enable_button(self):
        '''
        verify_screen_shows_with_enable_button
        :parameter:
        :return:
        '''
        self.wait_for_print_anywhere_enabled_load(300)
        logging.debug("Verify screen shows with 'enable' button")
#         assert self.get_value_of_print_anywhere_title() == u''
#         assert self.print_anywhere_content_1() == u''
#         assert self.print_anywhere_content_2() == u''
#         assert self.print_anywhere_content_3() == u''
#         assert self.get_value_of_get_more_help_link() == u''
        assert self.get_value_of_sign_in_or_enable_btn() == 'Enable'

    def verify_print_anywhere_enabled_screen(self):
        '''
        verify_print_anywhere_enabled_screen
        :parameter:
        :return:
        '''
        logging.debug("verify_print_anywhere_enabled_screen")
#         assert self.get_value_of_print_anywhere_title() == u''
#         assert self.get_value_of_print_anywhere_enable_content() == u''
#         assert self.get_value_of_send_link_btn() == u''
