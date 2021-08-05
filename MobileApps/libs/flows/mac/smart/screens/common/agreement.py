# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the agreement screen.

@author: Sophia
@create_date: May 9, 2019
@update_date: Aug 06, 2020 (Ivan)
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.webapp.web_app_screen import WebAppScreen
from time import sleep
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
import MobileApps.resources.const.mac.const as smart_const


class Agreement(SmartScreens):
    folder_name = "common"
    flow_name = "agreement"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(Agreement, self).__init__(driver)
        self.web_app_screen = WebAppScreen(self.driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Agreement screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[AgreementsScreen]:[wait_for_screen_load]-Wait for screen loading ...")

        return self.driver.wait_for_object("agreement_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_agreement_title(self):
        '''
        This is a method to get value of title on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[AgreementsScreen:[get_value_of_agreement_title]-Get the value of agreement_title ...  ")

        return self.driver.get_value("agreement_title")

    def get_value_of_agreement_contents(self):
        '''
        This is a method to get value of Contents on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[AgreementsScreen]:[get_value_of_agreement_contents]-Get the value of agreement_contents ...  ")

        return self.driver.get_value("agreement_contents")

    def get_value_of_hp_privacy_statement_link(self):
        '''
        This is a method to get value of HP Privacy statement link on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[AgreementsScreen]:[get_value_of_hp_privacy_statement_link]-Get the value of HP Privacy statement link ...")

        return self.driver.get_title("hp_privacy_statement_link")

    def get_value_of_google_analytics_privacy_policy_link(self):
        '''
        This is a method to get value of Google Analytics Privacy Policy link on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[AgreementsScreen]:[get_value_of_google_analytics_privacy_policy_link]-Get the value of Google Analytics Privacy Policy link ...")

        return self.driver.get_title("google_analytics_privacy_policy_link")

    def get_value_of_adobe_privacy_link(self):
        '''
        This is a method to get value of Adobe Privacy link on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[AgreementsScreen]:[get_value_of_adobe_privacy_link]-Get the value of Adobe Privacy link ...")

        return self.driver.get_title("adobe_privacy_link")

    def get_value_of_no_btn(self):
        '''
        This is a method to get value of No button on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[AgreementsScreen]:[get_value_of_no_btn]-Get the value of No button ...  ")

        return self.driver.get_title("no_btn")

    def get_value_of_yes_btn(self):
        '''
        This is a method to get value of Yes button on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[AgreementsScreen]:[get_value_of_yes_btn]-Get the value of Yes button ...  ")

        return self.driver.get_title("yes_btn")

    def click_no_btn(self):
        '''
        This is a method to click no_btn
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[click_no_btn]-Click no_btn.. ")

        self.driver.click("no_btn", is_native_event=True)

    def click_yes_btn(self):
        '''
        This is a method to click yes_btn
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[click_yes_btn]-Click yes_btn.. ")

        self.driver.click("yes_btn", is_native_event=True)

    def click_hp_privacy_statement_link(self):
        '''
        This is a method to click HP Privacy statement link on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[click_hp_privacy_statement_link]-Click HP Privacy statement link... ")

        self.driver.click("hp_privacy_statement_link")

    def click_google_analytics_privacy_policy_link(self):
        '''
        This is a method to click Google Analytics Privacy Policy link on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[click_google_analytics_privacy_policy_link]-Click Google Analytics Privacy Policy link... ")

        self.driver.click("google_analytics_privacy_policy_link")

    def click_adobe_privacy_link(self):
        '''
        This is a method to click Adobe Privacy link on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[click_adobe_privacy_link]-Click Adobe Privacy link... ")

        self.driver.click("adobe_privacy_link")

# -------------------------------Verification Methods------------------------
    def verify_agreement_screen(self):
        '''
        This is a verification method to check UI strings of Agreement screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Agreement screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='privacy_screen')
        assert self.get_value_of_agreement_title() == test_strings['agreement_title']
        assert self.get_value_of_agreement_contents() == test_strings['agreement_body']
        assert self.get_value_of_hp_privacy_statement_link() == test_strings['hp_privacy_statement_link']
        assert self.get_value_of_google_analytics_privacy_policy_link() == test_strings['google_analytics_privacy_policy_link']
        assert self.get_value_of_adobe_privacy_link() == test_strings['adobe_privacy_link']
        assert self.get_value_of_no_btn() == test_strings['no_btn']
        assert self.get_value_of_yes_btn() == test_strings['yes_btn']

    def verify_hp_privacy_statement_link(self):
        '''
        This is a verification method to check hp privacy statement link on Agreement screen.
        :parameter:
        :return:
        '''
        self.click_hp_privacy_statement_link()
        sleep(15)
        web_app_screen = WebAppScreen(self.driver)
        url = web_app_screen.get_value_of_web_browser_address()
        assert 'https://www8.hp.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_google_analytics_privacy_policy_link(self):
        '''
        This is a verification method to check google analytics privacy policy link on Agreement screen.
        :parameter:
        :return:
        '''
        self.click_google_analytics_privacy_policy_link()
        sleep(15)
        url = self.web_app_screen.get_value_of_web_browser_address()
        assert 'https://policies.google.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_adobe_privacy_link(self):
        '''
        This is a verification method to check adobe privacy link on Agreement screen.
        :parameter:
        :return:
        '''
        self.click_adobe_privacy_link()
        sleep(15)
        url = self.web_app_screen.get_value_of_web_browser_address()
        assert 'https://www.adobe.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_all_the_link(self):
        '''
        This is a verification method to check all the link on Agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("check all the link")
        self.verify_hp_privacy_statement_link()
        self.verify_google_analytics_privacy_policy_link()
        self.verify_adobe_privacy_link()
