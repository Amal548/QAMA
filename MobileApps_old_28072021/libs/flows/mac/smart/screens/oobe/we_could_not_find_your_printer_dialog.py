# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on "We're sorry, we could not find your printer" dialog

@author: Ivan
@create_date: Aug 28, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class WeCouldNotFindYourPrinterDialog(SmartScreens):

    folder_name = "oobe"
    flow_name = "we_could_not_find_your_printer_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WeCouldNotFindYourPrinterDialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("make_sure_your_computer_content", timeout=timeout, raise_e=raise_e)

    def click_network_btn(self):
        '''
        This is a method to click network button.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[click_network_btn]-Click network_btn.. ")

        self.driver.click("network_btn")

    def click_try_again_btn(self):
        '''
        This is a method to click try_again_btn.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[click_try_again_btn]-Click try_again_btn.. ")

        self.driver.click("try_again_btn", is_native_event=True)

    def click_exit_setup_btn(self):
        '''
        This is a method to click exit_setup_btn.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[click_exit_setup_btn]-Click exit_setup_btn.. ")

        self.driver.click("exit_setup_btn")

    def get_value_of_title(self):
        '''
        This is a method to get the value of dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_title]-Get the value of title...  ")

        return self.driver.get_value("we_could_not_find_your_printer_title")

    def get_value_of_make_sure_your_computer_content(self):
        '''
        This is a method to get the value of you_are_connected_to_content.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_make_sure_your_computer_content]-Get the contents of make_sure_your_computer_content...  ")

        return self.driver.get_value("make_sure_your_computer_content")

    def get_value_of_1_select_network_content(self):
        '''
        This is a method to get the value of 1_select_network_content.
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_1_select_network_content]-Get the contents of 1_select_network_content...  ")

        return self.driver.get_value("1_select_network_content")

    def get_value_of_network_btn(self):
        '''
        This is a method to get the value of network_btn
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_network_btn]-Get the contents of network_btn...  ")

        return self.driver.get_title("network_btn")

    def get_value_of_2_select_wifi_from_content(self):
        '''
        This is a method to get the value of 2_select_wifi_from_content
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_2_select_wifi_from_content]-Get the contents of 2_select_wifi_from_content...  ")

        return self.driver.get_value("2_select_wifi_from_content")

    def get_value_of_3_turn_wifi_on_content(self):
        '''
        This is a method to get the value of 3_turn_wifi_on_content
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_3_turn_wifi_on_content]-Get the contents of 3_turn_wifi_on_content...  ")

        return self.driver.get_value("3_turn_wifi_on_content")

    def get_value_of_4_select_network_name_content(self):
        '''
        This is a method to get the value of 4_select_network_name_content
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_4_select_network_name_content]-Get the contents of 4_select_network_name_content...  ")

        return self.driver.get_value("4_select_network_name_content")

    def get_value_of_5_once_connected_to_wifi_content(self):
        '''
        This is a method to get the value of 5_once_connected_to_wifi_content
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_5_once_connected_to_wifi_content]-Get the contents of 5_once_connected_to_wifi_content...  ")

        return self.driver.get_value("5_once_connected_to_wifi_content")

    def get_value_of_try_again_content(self):
        '''
        This is a method to get the value of try_again_content
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_try_again_content]-Get the contents of try_again_content...  ")

        return self.driver.get_value("try_again_content")

    def get_value_of_exit_setup_btn(self):
        '''
        This is a method to get the value of exit_setup_btn
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_exit_setup_btn]-Get the contents of exit_setup_btn...  ")

        return self.driver.get_title("exit_setup_btn")

    def get_value_of_try_again_btn(self):
        '''
        This is a method to get the value of try_again_btn
        :parameter:
        :return:
        '''
        logging.debug("[WeCouldNotFindYourPrinterDialog]:[get_value_of_continue_btn]-Get the contents of try_again_btn...  ")

        return self.driver.get_title("try_again_btn")

#  -------------------------------Verification Methods------------------------
    def verify_we_could_not_find_your_printer_screen(self):
        '''
        This is a verification method to check UI strings of We could not find your printer screen
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(600)
        logging.debug("Start to check UI strings of We could not find your printer screen")
#         assert self.get_value_of_title() == u''
#         assert self.get_value_of_make_sure_your_computer_content() == u''
#         assert self.get_value_of_1_select_network_content() == u''
#         assert self.get_value_of_2_select_wifi_from_content() == u''
#         assert self.get_value_of_3_turn_wifi_on_content() == u''
#         assert self.get_value_of_4_select_network_name_content() == u''
#         assert self.get_value_of_5_once_connected_to_wifi_content() == u''
#         assert self.get_value_of_try_again_content() == u''
#         assert self.get_value_of_exit_setup_btn() == u''
#         assert self.get_value_of_try_again_btn() == u''
