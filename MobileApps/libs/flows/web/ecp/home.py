import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class OptionNotFound(Exception):
    pass

class Home(ECPFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for ows
    """
    flow_name = "home"

    ############################ Main Menu verifys ############################
    def verify_user_icon(self, timeout=3, raise_e=True):
        return self.driver.wait_for_object("user_icon_top_right", timeout=timeout, raise_e=raise_e)

    def verify_logout_menu_item(self):
        return self.driver.wait_for_object("user_icon_menu_log_out_item")

    def verify_home_menu_btn(self, timeout=20, raise_e=True):
        return self.driver.wait_for_object("home_menu_btn", timeout=timeout, raise_e=raise_e)
        
    def verify_users_menu_btn(self):
        return self.driver.wait_for_object("users_menu_btn")

    def verify_devices_menu_btn(self):
        return self.driver.wait_for_object("devices_menu_btn")

    def verify_solutions_menu_expand_btn(self):
        return self.driver.wait_for_object("solutions_menu_expand_btn")

    def verify_account_menu_expand_btn(self):
        return self.driver.wait_for_object("account_menu_expand_btn")

    def verify_reports_menu_btn(self):
        return self.driver.wait_for_object("reports_menu_btn")

    def verify_support_menu_btn(self):
        return self.driver.wait_for_object("support_menu_btn")

    ############################ Main Menu Clicks ############################
    def click_home_menu_btn(self):
        return self.driver.click("home_menu_btn")

    def click_users_menu_btn(self):
        return self.driver.click("users_menu_btn")

    def click_solutions_menu_expand_btn(self):
        return self.driver.click("solutions_menu_expand_btn")

    def click_devices_menu_btn(self):
        return self.driver.click("devices_menu_btn")

    def click_account_menu_expand_btn(self):
        return self.driver.click("account_menu_expand_btn")

    def click_reports_menu_btn(self):
        return self.driver.click("reports_menu_btn")

    def click_support_menu_btn(self):
        return self.driver.click("support_menu_btn")

    ############################ Sub Menu verifys ############################
    def verify_security_sub_menu_btn(self):
        return self.driver.wait_for_object("security_sub_menu_btn")

    def verify_hp_room_sub_menu_btn(self):
        return self.driver.wait_for_object("hp_room_sub_menu_btn")

    def verify_account_profile_sub_menu_btn(self):
        return self.driver.wait_for_object("account_profile_sub_menu_btn")

    def verify_notification_settings_sub_menu_btn(self):
        return self.driver.wait_for_object("notification_settings_sub_menu_btn")

    def verify_privacy_settings_sub_menu_btn(self):
        return self.driver.wait_for_object("privacy_settings_sub_menu_btn")

    ############################ Sub Menu Clicks ############################
    def click_security_sub_menu_btn(self):
        return self.driver.click("security_sub_menu_btn")

    def click_hp_room_sub_menu_btn(self):
        return self.driver.click("hp_room_sub_menu_btn")

    def click_account_profile_sub_menu_btn(self):
        return self.driver.click("account_profile_sub_menu_btn")

    def click_notification_settings_sub_menu_btn(self):
        return self.driver.click("notification_settings_sub_menu_btn")

    def click_privacy_settings_sub_menu_btn(self):
        return self.driver.click("privacy_settings_sub_menu_btn")

    ############################ Home Page MFE Verify ############################

    def verify_notification_mfe_card(self):
        return self.driver.wait_for_object("noti_mfe_card", timeout=20)

    def verify_notification_mfe_filter_dropdown(self):
        return self.driver.wait_for_object("noti_filter_by_dropdown")

    def verify_notification_mfe_filter_options(self, option):
        all_options = self.driver.find_object("noti_filter_by_dropdown_option", multiple=True)
        for option in all_options:
            if option.text == option:
                return True
        raise OptionNotFound("Cannot find option: " + option)
    ############################ Home Page MFE Clicks ############################

    def notification_mfe_filter_dropdown(self):
        return self.driver.click("noti_filter_by_dropdown")

    ############################ Flows ############################

    def logout(self):
        #This needs to be run twice for some reason 
        for _ in range(2):
            if self.verify_user_icon(raise_e=False) is not False:
                self.driver.click("user_icon_top_right")
                self.verify_logout_menu_item()
                self.driver.click("user_icon_menu_log_out_item")
        return True



