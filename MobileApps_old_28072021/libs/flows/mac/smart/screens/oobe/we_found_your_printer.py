# encoding: utf-8
'''
WeFoundYourPrinter screen

@author: ten
@create_date: Aug 6, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from selenium.common.exceptions import TimeoutException


class WeFoundYourPrinter(SmartScreens):
    folder_name = "oobe"
    flow_name = "we_found_your_printer"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WeFoundYourPrinter, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourPrinter]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("we_found_your_printer_contents", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        Click continue button
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourPrinter]:[click_continue_btn]-Click continue button... ")

        self.driver.click("continue_btn", is_native_event=True)
        if self.wait_for_screen_load(raise_e=False):
            self.driver.click("continue_btn", is_native_event=True)

    def click_change_printer_btn(self):
        '''
        Click Change printer button
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourPrinter]:[click_change_printer_btn]-Click change_printer button... ")

        self.driver.click("change_printer_btn")

    def get_value_of_we_found_your_printer_title(self):
        '''
        get_value_of_we_found_your_printer_title
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourPrinter]:[get_value_of_we_found_your_printer_title]-Get the contents of we_found_your_printer_title...  ")

        return self.driver.get_value("we_found_your_printer_title")

    def get_value_of_change_printer_btn(self):
        '''
        get_value_of_change_printer_button
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourPrinter]:[get_value_of_change_printer_btn]-Get the contents of change_printer_btn ...  ")

        return self.driver.get_title("change_printer_btn")

    def get_value_of_we_found_your_printer_contents(self):
        '''
        get_value_of_we_found_your_printer_contents
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourPrinter]:[get_value_of_we_found_your_printer_contents]-Get the contents of we_found_your_printer_contents ...  ")

        return self.driver.get_value("we_found_your_printer_contents")

    def get_value_of_continue_btn(self):
        '''
        get_value_of_continue_btn
        :parameter:
        :return:
        '''
        logging.debug("[WeFoundYourPrinter]:[get_value_of_we_found_your_printer_contents]-Get the contents of we_found_your_printer_contents ...  ")

        return self.driver.get_title("continue_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_we_found_your_printer_screen(self):
        '''
        This is a verification method to check UI strings of We found your printer screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(90)
        logging.debug("Start to verify UI string of we found your printer screen")
#         assert self.get_value_of_we_found_your_printer_title() == u"We found your printer!"
#         assert self.get_value_of_change_printer_btn()==u""
#         assert self.get_value_of_we_found_your_printer_contents()==u"Time to connect, set up, and manage your HP printer!"
#         assert self.get_value_of_continue_btn()==u""

    def verify_we_found_your_printer_title_no_existed(self, timeout=30):
        '''
        verify_we_found_your_printer_title_no_existed
        :parameter:
        :return:
        '''

        return self.driver.wait_for_object("we_found_your_printer_title", invisible=True, timeout=timeout, raise_e=False)
        

    def verify_we_found_your_printer_without_title_screen(self):
        '''
        This is a verification method to check UI strings of We found your printer without title screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(60)
        self.verify_we_found_your_printer_title_no_existed(5)
        logging.debug("Start to verify UI string of we found your printer without title screen")
#         assert self.get_value_of_change_printer_btn()==u""
#         assert self.get_value_of_we_found_your_printer_contents()==u"Add your printer to this app to connect and manage your printer."
#         assert self.get_value_of_continue_btn()==u""
