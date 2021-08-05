# encoding: utf-8
'''
Description: It defines the operations of element and verification methods
on privacy settings screen

@author: ten
@create_date: Nov 14, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.hpwebpage.hp_webpage import HPWebPage
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class PrivacySettings(SmartScreens):

    folder_name = "menubar"
    flow_name = "privacy_settings"

    def __init__(self, driver):
        super(PrivacySettings, self).__init__(driver)

# ------------------------------Operate Elements--------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait welcome screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("data_collection_notice_btn", timeout=timeout, raise_e=raise_e)

    def click_data_collection_notice_btn(self):
        '''
        This is a method to Data Collection Notice button.
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[click_data_collection_notice_btn]-Click data_collection_notice_btn.. ")

        self.driver.click("data_collection_notice_btn", is_native_event=True)

    def click_hp_privacy_statement_btn(self):
        '''
        This is a method to HP Privacy Statement button.
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[click_hp_privacy_statement_btn]-Click hp_privacy_statement_btn.. ")

        self.driver.click("hp_privacy_statement_btn", is_native_event=True)

    def click_terms_of_use_btn(self):
        '''
        This is a method to Terms Of Use button.
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[click_terms_of_use_btn]-Click terms_of_use_btn.. ")

        self.driver.click("terms_of_use_btn", is_native_event=True)

    def click_eula_btn(self):
        '''
        This is a method to EULA button.
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[click_eula_btn]-Click eula_btn.. ")

        self.driver.click("eula_btn", is_native_event=True)

    def get_value_of_privacy_settings_title(self):
        '''
        get value of privacy Settings Title
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_privacy_settings_title]-Get the contents of privacy_settings_title")

        return self.driver.get_value("privacy_settings_title")

    def get_value_of_data_collection_notice_btn(self):
        '''
        get value of Data Collection Notice button
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_Data Collection Notice button]-Get the contents of Data Collection Notice button  ")

        return self.driver.get_title("data_collection_notice_btn")

    def get_value_of_hp_smart_services_btn(self):
        '''
        get value of hp_smart_services_btn
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_hp_smart_services_btn]-Get the contents of hp_smart_services_btn")

        return self.driver.get_title("hp_smart_services_btn")

    def get_value_of_printer_data_collection_notice_btn(self):
        '''
        get value of printer_hp_smart_data_collection_notice_btn
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_printer_hp_smart_data_collection_notice_btn]-Get the contents of printer_hp_smart_data_collection_notice_btn")

        return self.driver.get_title("printer_data_collection_notice_btn")

    def get_value_of_hp_privacy_statement_btn(self):
        '''
        get value of HP Privacy Statement button
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_HP Privacy Statement button]-Get the contents of HP Privacy Statement button  ")

        return self.driver.get_title("hp_privacy_statement_btn")

    def get_value_of_eula_btn(self):
        '''
        get value of EULA button
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_EULA button]-Get the contents of EULA button  ")

        return self.driver.get_title("eula_btn")

    def get_value_of_terms_of_use_btn(self):
        '''
        get value of Terms Of Use button.
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_Terms Of Use button.]-Get the contents of Terms Of Use button. ")

        return self.driver.get_title("terms_of_use_btn")

    def get_value_of_data_collection_title(self):
        '''
        get value of data collection title
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_HP data collection title]-Get the contents of data collection title ")

        return self.driver.get_value("data_collection_title")

    def get_value_of_data_collection_contents(self):
        '''
        get value of data collection contents
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_data collection contents]-Get the contents of data collection contents")

        return self.driver.get_value("data_collection_contents")

    def get_value_of_app_improvement_title(self):
        '''
        get value of app_improvement_title
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_app_improvement_title]-Get the contents of app_improvement_title")

        return self.driver.get_value("app_improvement_title")

    def get_value_of_app_improvement_contents(self):
        '''
        get value of app_improvement_contents
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_app_improvement_contents]-Get the contents of app_improvement_contents")

        return self.driver.get_value("app_improvement_contents")

    def get_value_of_google_analytics_btn(self):
        '''
        get value of google_analytics_btn
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_google_analytics_btn]-Get the contents of google_analytics_btn")

        return self.driver.get_title("google_analytics_btn")

    def get_value_of_adobe_privacy_btn(self):
        '''
        get value of google_analytics_btn
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_adobe_privacy_btn]-Get the contents of adobe_privacy_btn")

        return self.driver.get_title("adobe_privacy_btn")

    def get_value_of_manage_btn(self):
        '''
        get value of manage_btn
        :parameter:
        :return:
        '''
        logging.debug("[PrivacySettings]:[get_value_of_manage_btn]-Get the contents of manage_btn")

        return self.driver.get_title("manage_btn")

# -------------------------------Verification Methods------------------------------------
    def verify_ui_string(self):
        test_strings = smart_utility.get_local_strings_from_table(screen_name='privacy_settings')
        assert self.get_value_of_privacy_settings_title() == test_strings['privacy_settings_title']
        assert self.get_value_of_data_collection_title() == test_strings['data_collection_title']
        assert self.get_value_of_data_collection_contents() == test_strings['data_collection_contents']
        assert self.get_value_of_data_collection_notice_btn() == test_strings['data_collection_notice_btn']
        assert self.get_value_of_hp_smart_services_btn() == test_strings['hp_smart_services_btn']
        assert self.get_value_of_printer_data_collection_notice_btn() == test_strings['printer_data_collection_notice_btn']
        assert self.get_value_of_hp_privacy_statement_btn() == test_strings['hp_privacy_statement_btn']
        assert self.get_value_of_eula_btn() == test_strings['eula_btn']
        assert self.get_value_of_terms_of_use_btn() == test_strings['terms_of_use_btn']
        assert self.get_value_of_app_improvement_title() == test_strings['app_improvement_title']
        assert self.get_value_of_app_improvement_contents() == test_strings['app_improvement_contents']
        assert self.get_value_of_google_analytics_btn() == test_strings['google_analytics_btn']
        assert self.get_value_of_adobe_privacy_btn() == test_strings['adobe_privacy_btn']

    def verify_ui_string_without_sign_in(self):
        self.verify_ui_string()
        if self.driver.wait_for_object("manage_btn", raise_e=False):
            raise UnexpectedItemPresentException("the screen display")
        return True

    def verify_ui_string_with_sign_in(self):
        test_strings = smart_utility.get_local_strings_from_table(screen_name='privacy_settings')
        self.verify_ui_string()
        if not self.driver.wait_for_object("manage_btn", raise_e=False):
            raise UnexpectedItemPresentException("the screen not display")
        return True

        assert self.get_value_of_manage_btn() == test_strings['manage_btn']

    def verify_links_on_privacy(self):
        hp_website = HPWebPage(self.driver)

        self.click_hp_privacy_statement_btn()
        hp_website.wait_for_hp_privacy_statement_website_load()
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

        self.click_terms_of_use_btn()
        hp_website.wait_for_hp_smart_terms_of_use_website_load()
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

        self.click_eula_btn()
        hp_website.wait_for_end_user_license_agreement_website_load()
        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)
