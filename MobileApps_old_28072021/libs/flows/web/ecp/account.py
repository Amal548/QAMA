import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class Account(ECPFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for ows
    """
    flow_name = "account"

    ###################### Account Profile Section #######################
    def verify_account_profile_page(self):
        return self.driver.wait_for_object("profile_page_title")

    def enter_username(self, username):
        #Currently this box is grayed out, not sure if that'll change in the future
        return self.driver.sent_keys("profile_username_txt_box", username)

    def enter_first_name(self, first_name):
        return self.driver.sent_keys("profile_first_name_txt_box", first_name)
    
    def enter_last_name(self, last_name):
        return self.driver.sent_keys("profile_last_name_txt_box", last_name)

    def enter_email(self, email):
        return self.driver.sent_keys("profile_email_txt_box", email)

    def select_country(self, country):
        self.driver.click("profile_country_dropdown")
        self.driver.wait_for_object("profile_country_option", format_specifier=[country])
        return self.driver.click("profile_country_option", format_specifier=[country])
    
    def select_language(self, language):
        self.driver.click("profile_language_dropdown")
        self.driver.wait_for_object("profile_language_option", format_specifier=[language])
        return self.driver.click("profile_language_option", format_specifier=[language])
    
    def click_apply_changes_btn(self):
        return self.driver.click("apply_changes_button")