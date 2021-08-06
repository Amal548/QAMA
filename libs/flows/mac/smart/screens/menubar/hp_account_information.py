# encoding: utf-8
'''
Description: check hp account information tab and functions

@author: ten
@create_date: July 25, 2019
'''

import logging
from selenium.common.exceptions import TimeoutException

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class Hpaccountinformation(SmartScreens):
    folder_name = "menubar"
    flow_name = "use_hp_account_information"

    def __init__(self,driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(Hpaccountinformation, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        logging.debug("[HpaccountinformationScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("hp_account_title", timeout=timeout, raise_e=raise_e)

    def click_hp_account_checkbox(self):
        '''
        Click hp account check box
        :parameter:
        :return:
        '''
        logging.debug("[hp_account_screen]:[hp_account_checkbox]-Click hp_account_checkbox.. ")

        self.driver.check_box("hp_account_checkbox")

    def click_hp_account_hpprivacystatement_link(self):
        '''
        Click hp account HPPrivacyStatement Link 
        :parameter:
        :return:
        '''
        logging.debug("[hp_account_screen]:[hp_account_checkbox]-Click hp_account_HPPrivacyStatement_Link.. ")

        self.driver.click("hp_account_hp_privacy_statement_link")

    def get_value_of_hp_account_title(self):
        '''
        get value of hp account screen title
        :parameter:
        :return:
        '''
        logging.debug("[HpaccountinformationScreen]:[get_value_of_hp_account_title]-Get the contents of hp_account_title")

        return self.driver.get_value("hp_account_title")

    def get_value_of_hp_account_contents_1(self):
        '''
        get value of hp account contents
        :parameter:
        :return:
        '''
        logging.debug("[HpaccountinformationScreen]:[get_value_of_hp_account_contents_1]-Get the contents of hp_account_contents_1")

        return self.driver.get_value("hp_account_contents_1")

    def get_value_of_hp_account_contents_2(self):
        '''
        get value of hp account contents
        :parameter:
        :return:
        '''
        logging.debug("[HpaccountinformationScreen]:[get_value_of_hp_account_contents_2]-Get the contents of hp_account_contents_2")
        return self.driver.get_value("hp_account_contents_2")

    def get_value_of_hp_account_hpprivacystatement_link(self):
        '''
        get value of hp account hp privacy statment link
        :parameter:
        :return:
        '''
        logging.debug("[HpaccountinformationScreen]:[get_value_of_hp_account_HPPrivacyStatement_Link]-Get the contents of hp_account_HPPrivacyStatement_Link  ")

        return self.driver.get_title("hp_account_hp_privacy_statement_link")

    def get_value_of_hp_account_checkbox(self):
        '''
        get value of hp account check box
        :parameter:
        :return:
        '''
        logging.debug("[HpaccountinformationScreen]:[get_value_of_hp_account_checkbox]-Get the contents of hp_account_checkbox ...  ")

        return self.driver.get_title("hp_account_checkbox")  

    # -------------------------------Verification Methods----------------------
    # def verify_hpaccountinformation(self):
    #     '''
    #     Verify strings and matching string table
    #     :parameter:
    #     :return:
    #     '''
    #     logging.debug("verify the Hp account information screen")
    #     assert self.get_value_of_hp_account_title()==""
    #     assert self.get_value_of_hp_account_contents_1()==""
    #     assert self.get_value_of_hp_account_contents_2()==""
    #     assert self.get_value_of_hp_account_hpprivacystatement_link()==""
    #     assert self.get_value_of_hp_account_checkbox()==""

    def verify_gothamappwindow_minimized(self, timeout=30):
        '''
        Verify gotham app was minimized
        :parameter:
        :return:
        '''
        logging.debug("[Gothamappwindow]:[wait_for_screen_load]-Wait for screen loading successful... ")
        assert not self.driver.wait_for_object("hp_account_hp_smart", timeout=timeout, raise_e=False)

    def verify_gothamapp_opened(self, timeout=30):
        '''
        Verify gotham app was opened
        :parameter:
        :return:
        '''
        logging.debug("[Gothamappwindow]:[wait_for_screen_load]-Wait for screen loading successful... ")

        try:
            self.driver.wait_for_object("hp_account_hp_smart",timeout=timeout)
        except TimeoutException:
            logging.debug("Screen loading failed... ")
            return False
        return True

    def verify_hp_account_checkbox_checked_out(self):
        '''
        Verify hp account checkbox was selected
        :parameter:
        :return:
        '''
        assert self.driver.get_value("hp_account_checkbox")=="1"
