# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Mobile Fax agreement page.

@author: Ivan
@create_date: Jan 3, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class MobileFaxAgreementPage(SmartScreens):

    folder_name = "mobilefax"
    flow_name = "mobile_fax_agreement_page"

    def __init__(self, driver):
        super(MobileFaxAgreementPage, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax Agreement page screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("your_trial_starts_now_text", timeout=timeout, raise_e=raise_e)

    def click_i_agree_to_check_box(self):
        '''
        This is a method to click to select I agree to check box on Mobile Fax Agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[click_i_agree_to_check_box]-Click to select I agree to check box... ")

        self.driver.click("i_agree_to_check_box", is_native_event=True)

    def select_no_option(self):
        '''
        This is a method to select No option on Mobile Fax Agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[select_no_option]-Select no option... ")

        self.driver.click("no_option", is_native_event=True)

    def select_yes_option(self):
        '''
        This is a method to select Yes option on Mobile Fax Agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[select_yes_option]-Select yes option... ")

        self.driver.click("yes_option", is_native_event=True)

    def click_back_btn(self):
        '''
        This is a method to click Back button on Mobile Fax Agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[click_back_btn]-Click Back button... ")

        self.driver.click("back_btn", is_native_event=True)

    def click_continue_btn(self):
        '''
        This is a method to click Continue button on Mobile Fax Agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("continue_btn", is_native_event=True)

    def get_value_of_your_trial_starts_now_text(self):
        '''
        This is a method to get value of Your Trial Starts now text on Mobile Fax agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[get_value_of_your_trial_starts_now_text] - Get value of Your Trial Starts now text...  ")

        return self.driver.get_value("your_trial_starts_now_text")

    def get_value_of_i_agree_to_text(self):
        '''
        This is a method to get value of I Agree to text on Mobile Fax agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[get_value_of_i_agree_to_text] - Get value of I Agree to text...  ")

        return self.driver.get_value("i_agree_to_text")

    def get_value_of_terms_of_service_link(self):
        '''
        This is a method to get value of Terms of Service link on Mobile Fax agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[get_value_of_terms_of_service_link] - Get value of Terms of Service link...  ")

        return self.driver.get_title("terms_of_service_link")

    def get_value_of_do_you_represent_text(self):
        '''
        This is a method to get value of Do you represent text on Mobile Fax agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[get_value_of_do_you_represent_text] - Get value of Do you represent text...  ")

        return self.driver.get_value("do_you_represent_text")

    def get_value_of_usa_hipaa_regulations_link(self):
        '''
        This is a method to get value of USA HIPAA Regulations link on Mobile Fax agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[get_value_of_usa_hipaa_regulations_link] - Get value of USA HIPAA Regulations link...  ")

        return self.driver.get_value("usa_hipaa_regulations_link")

    def get_value_of_back_btn(self):
        '''
        This is a method to get value of Back button on Mobile Fax agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[get_value_of_back_btn] - Get value of Back button...  ")

        return self.driver.get_title("back_btn")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get value of Continue button on Mobile Fax agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[get_value_of_continue_btn] - Get value of Continue button...  ")

        return self.driver.get_title("continue_btn")

    def get_value_of_hp_privacy_policy_link(self):
        '''
        This is a method to get value of HP Privacy Policy link on Mobile Fax agreement page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxAgreementPage]:[get_value_of_hp_privacy_policy_link] - Get value of HP Privacy Policy link...  ")

        return self.driver.get_value("hp_privacy_policy_link")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_mobile_fax_agreement_page(self):
        '''
        This is a verification method to check UI strings of Mobile Fax agreement page.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(120)
        logging.debug("Start to check UI strings of Mobile Fax agreement page")
#         assert self.get_value_of_your_trial_starts_now_text() == u""
#         assert self.get_value_of_i_agree_to_text() == u""
#         assert self.get_value_of_terms_of_service_link() == u""
#         assert self.get_value_of_do_you_represent_text() == u""
#         assert self.get_value_of_usa_hipaa_regulations_link() == u""
#         assert self.get_value_of_back_btn() == u""
#         assert self.get_value_of_continue_btn() == u""
#         assert self.get_value_of_hp_privacy_policy_link() == u""

    def verify_continue_btn_enable(self):
        '''
        This is a verification method to verify Continue button is enable
        :parameter:
        :return:
        '''
        logging.debug("Verify Continue button's behavior")
        if self.driver.is_enable("continue_btn"):
            raise UnexpectedItemPresentException("Continue button is disabled")
        return True
