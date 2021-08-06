# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
screens during OWS flow.

@author: Sophia
@create_date: May 6, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class OWS(SmartScreens):
    folder_name = "oobe"
    flow_name = "ows"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(OWS, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self):
        '''
        This is a method to wait for screen loaded.
        :parameter:
        :return:
        '''
        pass

    def wait_for_enjoy_hp_account_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for enjoy hp account screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_enjoy_hp_account_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("enjoy_HP_account_title", timeout=timeout, raise_e=raise_e)

    def wait_for_time_to_install_ink_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for enjoy hp account screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_time_to_install_ink_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("time_to_install_ink_title", timeout=timeout, raise_e=raise_e)

    def wait_for_printer_connection_title_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for printer connection screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_printer_connection_title_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_connection_title", timeout=timeout, raise_e=raise_e)

    def wait_for_cartridges_install_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for cartridges installed screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_cartridges_install_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("cartridges_install_title", timeout=timeout, raise_e=raise_e)

    def wait_for_hp_instant_ink_advertisement_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for hp instant ink advertisement screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_hp_instant_ink_advertisement_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("continue_btn_instant_ink_advertisement", timeout=timeout, raise_e=raise_e)

    def wait_for_hp_instant_ink_plan_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for hp instant ink plan screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_hp_instant_ink_plan_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("no_instant_ink_radio_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_reminder_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for reminder screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_reminder_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("reminder_title", timeout=timeout, raise_e=raise_e)

    def wait_for_register_printer_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for register printer screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_register_printer_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("register_printer_title", timeout=timeout, raise_e=raise_e)

    def wait_for_almost_ready_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for almost ready screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_almost_ready_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("almost_ready_title", timeout=timeout, raise_e=raise_e)

    def wait_for_help_hp_make_better_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for help HP make better screen loaded
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_help_hp_make_better_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("postal_code", timeout=timeout, raise_e=raise_e)

    def wait_for_skip_btn_shows(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for skip button show up on install cartridges screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_skip_btn_shows]-Wait for button loading... ")

        return self.driver.wait_for_object("skip_btn_install", timeout=timeout, raise_e=raise_e)

    def wait_for_radio_btn_shows(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for radio button show up on help hp make better product screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[wait_for_radio_btn_shows]-Wait for button loading... ")

        return self.driver.wait_for_object("in_home_btn", timeout=timeout, raise_e=raise_e)

    def click_continue_btn_enjoy_hp_account(self):
        '''
        This is a method to click continue button on enjoy hp account screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_continue_btn_enjoy_hp_account]-Click 'Continue' button on enjoy hp account screen... ")

        self.driver.click("continue_btn_enjoy")

    def click_skip_btn_enjoy_hp_account(self):
        '''
        This is a method to click skip button on enjoy hp account screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_skip_btn_enjoy_hp_account]-Click 'Skip' button on enjoy hp account screen... ")

        self.driver.click("skip_btn_enjoy")

    def click_continue_btn_cartridges_install(self):
        '''
        This is a method to click continue button on cartridges installed screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_continue_btn_cartridges_install]-Click 'Continue' button on cartridges installed screen... ")

        self.driver.click("continue_btn_install")

    def click_skip_btn_cartridges_install(self):
        '''
        This is a method to click skip button on install cartridges screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_skip_btn_cartridges_install]-Click 'Skip' button on install cartridges screen... ")

        self.driver.click("skip_btn_install")

    def click_continue_btn_hp_instant_ink_advertisement(self):
        '''
        This is a method to click continue button on hp instant ink advertisement screen
        '''
        logging.debug("[OWS]:[click_continue_btn_hp_instant_ink_advertisement]-Click 'Continue' button on hp instant ink advertisement screen... ")

        self.driver.click("continue_btn_instant_ink_advertisement", is_native_event=True)

    def click_continue_btn_hp_instant_ink_plan(self):
        '''
        This is a method to click continue button on hp instant ink plan screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_continue_btn_hp_instant_ink_plan]-Click 'Continue' button on hp instant ink plan screen... ")

        self.driver.click("continue_btn_instant_ink_plan")

    def choose_first_instank_ink_plan_radio_btn(self):
        '''
        This is a method to choose the first instant ink plan button on hp instant ink plan screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[choose_first_instank_ink_plan_radio_btn]-Choose '$0.00' button on hp instant ink plan screen... ")

        self.driver.click("first_instant_ink_radio_btn")

    def choose_no_instank_ink_radio_btn(self):
        '''
        This is a method to choose no instant ink button on hp instant ink plan screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[choose_no_instank_ink_radio_btn]-Choose 'No instant ink' button on hp instant ink plan screen... ")

        self.driver.click("no_instant_ink_radio_btn")

    def click_skip_btn_reminder(self):
        '''
        This is a method to click skip button on reminder screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_skip_btn_reminder]-Click 'Skip' button on reminder screen... ")

        self.driver.click("skip_btn_reminder")

    def click_reminder_me_btn_reminder(self):
        '''
        This is a method to click Reminder me button on reminder screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_reminder_me_btn_reminder]-Click 'Reminder me' button on reminder screen... ")

        self.driver.click("reminder_me_btn_reminder")

    def click_skip_btn_register_printer(self):
        '''
        This is a method to click skip button on register printer screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_skip_btn_register_printer]-Click 'Skip' button on register printer screen... ")

        self.driver.click("skip_btn_register_printer")

    def click_continue_btn_register_printer(self):
        '''
        This is a method to click continue button on register printer screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_continue_btn_register_printer]-Click 'Continue' button on register printer screen... ")

        self.driver.click("continue_btn_register_printer")

    def click_continue_btn_almost_ready(self):
        '''
        This is a method to click continue button on almost ready screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_continue_btn_almost_ready]-Click 'Continue' button on almost ready screen... ")

        self.driver.click("continue_btn_almost_ready")

    def choose_in_home_radio_btn(self):
        '''
        This is a method to choose in a home button on help HP make better products screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[choose_in_home_radio_btn]-Choose 'In a home' button on help HP make better products screen... ")

        self.driver.click("in_home_btn")

    def click_in_home_drop_down_list(self):
        '''
        This is a method to click in a home drop down list on help HP make better products screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_in_home_drop_down_list]-Click 'In a home' drop down list on help HP make better products screen... ")

        self.driver.click("in_home_drop_down_list")

    def choose_in_home_drop_down_list_item(self):
        '''
        This is a method to choose list item on help HP make better products screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[choose_in_home_drop_down_list_item]-Choose list item on help HP make better products screen... ")

        self.driver.choose_combo_box_options("in_home_drop_down_list_item")

    def set_postal_code(self, code_value):
        '''
        This is a method to set postal code on help HP make better products screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[set_postal_code]-Click 'Continue' button on help HP make better products screen... ")

        self.driver.send_keys("postal_code", code_value)

    def click_continue_btn_help_better(self):
        '''
        This is a method to click continue button on help HP make better products screen
        :parameter:
        :return:
        '''
        logging.debug("[OWS]:[click_continue_btn_help_better]-Click 'Continue' button on help HP make better products screen... ")

        self.driver.click("continue_btn_help_better")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_collecting_your_printer_status_screen_display(self):
        '''
        verify_collecting_your_printer_status_screen_display
        :parameter:
        :return:
        '''
        self.driver.wait_for_object("collecting_your_printer_status_title")
        assert self.get_value_of_collecting_your_printer_status_title() == "Collecting your printer status"
