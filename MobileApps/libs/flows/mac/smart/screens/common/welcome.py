# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on welcome screen
the welcome screen.

@author:
@create_date: May 1, 2019
@update_date: Aug 06, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.webapp.web_app_screen import WebAppScreen
from time import sleep
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class Welcome(SmartScreens):
    folder_name = "common"
    flow_name = "welcome"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(Welcome, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Welcome to HP Smart screen load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("welcome_to_hp_smart_title", timeout=timeout, raise_e=raise_e)

    def get_value_of_welcome_to_hp_smart_title(self):
        '''
        This is a method to get value of Welcome to HP Smart screen title.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[get_value_of_welcome_to_hp_smart_title]-Get the value of Welcome to HP Smart screen title ...")

        return self.driver.get_title("welcome_to_hp_smart_title")

    def get_value_of_welcome_to_hp_smart_content(self):
        '''
        This is a method to get value of contents on Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[get_value_of_welcome_to_hp_smart_content]-Get the value of screen contents ...")

        return self.driver.get_value("welcome_to_hp_smart_content")

    def get_value_of_welcome_to_hp_smart_learn_more_link(self):
        '''
        This is a method to get value of Learn More link on Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[get_value_of_welcome_to_hp_smart_learn_more_link]-Get the value of Learn More link ...")

        return self.driver.get_title("welcome_to_hp_smart_learn_more_link")

    def get_value_of_welcome_to_hp_smart_term_of_use_link(self):
        '''
        This is a method to get value of term_of_use link on Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[get_value_of_welcome_to_hp_smart_learn_more_link]-Get the value of Learn More link ...")

        return self.driver.get_title("welcome_to_hp_smart_term_of_use_link")

    def get_value_of_welcome_to_hp_smart_end_user_license_agreement_link(self):
        '''
        This is a method to get value of end_user_license_agreement link on Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[get_value_of_welcome_to_hp_smart_learn_more_link]-Get the value of Learn More link ...")

        return self.driver.get_title("welcome_to_hp_smart_end_user_license_agreement_link")

    def get_value_of_welcome_to_hp_smart_continue_btn(self):
        '''
        This is a method to get value of Continue button on Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[get_value_of_welcome_to_hp_smart_continue_btn]-Get the value of Continue button ...")

        return self.driver.get_title("welcome_to_hp_smart_continue_btn")

    def click_welcome_to_hp_smart_learn_more_link(self):
        '''
        This is a method to click Learn More link on Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[click_welcome_to_hp_smart_learn_more_link]-Click Learn More link.. ")

        self.driver.click("welcome_to_hp_smart_learn_more_link")

    def click_welcome_to_hp_smart_term_of_use_link(self):
        '''
        This is a method to click welcome_to_hp_smart_term_of_use_linkon Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[click_welcome_to_hp_smart_term_of_use_link]-Click welcome_to_hp_smart_term_of_use_link.. ")

        self.driver.click("welcome_to_hp_smart_term_of_use_link")

    def click_welcome_to_hp_smart_end_user_license_agreement_link(self):
        '''
        This is a method to click welcome_to_hp_smart_end_user_license_agreement_linkon Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[click_welcome_to_hp_smart_end_user_license_agreement_link]-Click welcome_to_hp_smart_end_user_license_agreement_link.. ")

        self.driver.click("welcome_to_hp_smart_end_user_license_agreement_link")

    def click_welcome_to_hp_smart_continue_btn(self):
        '''
        This is a method to click Continue button on Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("[WelcomeScreen]:[click_welcome_to_hp_smart_continue_btn]-Click Continue button ...")

        self.driver.click("welcome_to_hp_smart_continue_btn", is_native_event=True)

# -------------------------------Verification Methods--------------------------
    def verify_gothamappwindow_minimized(self):
        '''
        This is a verification method to check app is minimized.
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("welcome_to_hp_smart_title", raise_e=False):
            raise UnexpectedItemPresentException("the screen still exists")
        return True

    def verify_welcome_to_hp_smart_screen(self):
        '''
        This is a verification method to check UI strings of Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(120)
        logging.debug("Start to check UI strings of Welcome to HP Smart screen")

        test_strings = smart_utility.get_local_strings_from_table(screen_name='welcome_screen')
        assert self.get_value_of_welcome_to_hp_smart_title() == test_strings['welcome_title']
        assert self.get_value_of_welcome_to_hp_smart_content() == test_strings['welcome_body']
        assert self.get_value_of_welcome_to_hp_smart_learn_more_link() == test_strings['learn_more_link']
        assert self.get_value_of_welcome_to_hp_smart_continue_btn() == test_strings['continue_btn']
        assert self.get_value_of_welcome_to_hp_smart_term_of_use_link() == test_strings['term_of_use_link']
        assert self.get_value_of_welcome_to_hp_smart_end_user_license_agreement_link() == test_strings['end_user_license_agreement_link']

    def check_learn_more_link(self):
        '''
        This is a verification method to check learn more link on HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("check_learn_more_link")
        self.click_welcome_to_hp_smart_learn_more_link()
        sleep(15)
        web_app_screen = WebAppScreen(self.driver)
        url = web_app_screen.get_value_of_web_browser_address()
        assert 'https://www8.hp.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def check_term_of_use_link(self):
        '''
        This is a verification method to check term of ues link on Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("check_term_of_use_link")
        self.click_welcome_to_hp_smart_term_of_use_link()
        sleep(15)
        web_app_screen = WebAppScreen(self.driver)
        url = web_app_screen.get_value_of_web_browser_address()
        assert 'https://www.hpsmart.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def check_welcome_to_hp_smart_end_user_license_agreement_link(self):
        '''
        This is a verification method to check welcome_to_hp_smart_end_user_license_agreement_link on Welcome to HP Smart screen.
        :parameter:
        :return:
        '''
        logging.debug("welcome_to_hp_smart_end_user_license_agreement_link")
        self.click_welcome_to_hp_smart_end_user_license_agreement_link()
        sleep(15)
        web_app_screen = WebAppScreen(self.driver)
        url = web_app_screen.get_value_of_web_browser_address()
        assert 'https://support.hp.com' in url
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def verify_all_the_link(self):
        self.check_learn_more_link()
        self.check_term_of_use_link()
        self.check_welcome_to_hp_smart_end_user_license_agreement_link()

    def verify_welcome_back_screen_display(self):
        '''
        This is a verification method to check UI strings of Welcome Back screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(120)
        logging.debug("Start to check UI strings of Welcome to HP Smart screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='welcome_screen')
        assert self.get_value_of_welcome_to_hp_smart_title() == test_strings['welcome_back_title']
