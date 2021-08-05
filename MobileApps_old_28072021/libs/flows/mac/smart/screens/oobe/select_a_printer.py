# encoding: utf-8
'''
SelectAPrinter screen

@author: ten
@create_date: Aug 1, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SelectAPrinter(SmartScreens):
    folder_name = "oobe"
    flow_name = "select_a_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(SelectAPrinter, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("refresh_link", timeout=timeout, raise_e=raise_e)

    def wait_for_busy_icon_display(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[wait_for_busy_icon_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("busy_icon", timeout=timeout, raise_e=raise_e)

    def wait_for_busy_icon_disappear(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[wait_for_busy_icon_disappear]-Wait for screen loading... ")

        return self.driver.wait_for_object_disappear("busy_icon", timeout=timeout, raise_e=raise_e)

    def click_refresh_link(self):
        '''
        This is a method to click Refresh link on Select a printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[click_refresh_link]-Click Refresh link.. ")

        self.driver.click("refresh_link", is_native_event=True)

    def click_printer_not_listed_link(self):
        '''
        This is a method to click Printer not listed link on Select a printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[click_printer_not_listed_link]-Click Printer not listed link.. ")

        self.driver.click("printer_not_listed_link", is_native_event=True)

    def click_to_select_the_first_printer(self):
        '''
        This is a method to click the beaconing name to select the first printer in the list.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[select_the_first_printer]-click to select the first printer.. ")

        self.driver.click("beaconing_printer_name", is_native_event=True)
        if self.wait_for_screen_load(raise_e=False):
            self.driver.click("beaconing_printer_name", is_native_event=True)

    def click_to_selected_printer(self, printer_name):
        '''
        This is a method to click the beaconing name to select printer using name.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[click_to_selected_printer]-click to select printer.. ")

        self.driver.click("beaconing_printer_chosed", format_specifier=[printer_name], is_native_event=True)
        if self.wait_for_screen_load(raise_e=False):
            self.driver.click("beaconing_printer_chosed", format_specifier=[printer_name], is_native_event=True)

    def get_value_of_select_a_printer_title(self):
        '''
        This is a method to get value of Select a printer screen title.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[get_value_of_select_a_printer_title]-Get the contents of Select a printer screen title...  ")

        return self.driver.get_value("select_a_printer_title")

    def get_value_of_select_a_printer_content_1(self):
        '''
        This is a method to get value of Select a printer screen content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[get_value_of_select_a_printer_content_1]-Get the contents of Select a printer screen content - 1...  ")

        return self.driver.get_value("select_a_printer_content_1")

    def get_value_of_select_a_printer_content_2(self):
        '''
        This is a method to get value of Select a printer screen content - 2.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[get_value_of_select_a_printer_content_2]-Get the contents of Select a printer screen content - 2...  ")

        return self.driver.get_value("select_a_printer_content_2")

    def get_value_of_select_a_printer_content_3(self):
        '''
        This is a method to get value of Select a printer screen content - 3.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[get_value_of_select_a_printer_content_3]-Get the contents of Select a printer screen content - 3...  ")

        return self.driver.get_value("select_a_printer_content_3")

    def get_value_of_select_a_printer_content_4(self):
        '''
        This is a method to get value of Select a printer screen content - 4.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[get_value_of_select_a_printer_content_4]-Get the contents of Select a printer screen content - 4...  ")

        return self.driver.get_value("select_a_printer_content_4")

    def get_value_of_refresh_link(self):
        '''
        This is a method to get value of Refresh link on Select a printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[get_value_of_refresh_link]-Get the contents of Refresh link...  ")

        return self.driver.get_value("refresh_link")

    def get_value_of_printer_not_listed_link(self):
        '''
        This is a method to get value of Printer not list link on Select a printer screen.
        :parameter:
        :return:
        '''
        logging.debug("[SelectAPrinter]:[get_value_of_printer_not_listed_link]-Get the contents of Printer not list link...  ")

        return self.driver.get_value("printer_not_listed_link")

# -------------------------------Verification Methods--------------------------
    def verify_select_a_printer_screen(self):
        '''
        This is a verification method to check the string UI of Select a printer screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        logging.debug("Start to check the string UI of Select a printer screen")
#         assert self.get_value_of_select_a_printer_title() == u""
#         assert self.get_value_of_select_a_printer_content_1() == u""
#         assert self.get_value_of_select_a_printer_content_2() == u""
#         assert self.get_value_of_select_a_printer_content_3() == u""
#         assert self.get_value_of_select_a_printer_content_4() == u""
#         assert self.get_value_of_refresh_link() == u""
#         assert self.get_value_of_printer_not_listed_link() == u""
