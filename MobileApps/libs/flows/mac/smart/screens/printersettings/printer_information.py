# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on the printer information page screen.

@author: Ivan
@create_date: Sep 03, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_setting_scroll import PrinterSettingScroll
from selenium.webdriver.common.keys import Keys
from time import sleep
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class PrinterInformation(PrinterSettingScroll, SmartScreens):
    folder_name = "printersettings"
    flow_name = "printer_information"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterInformation, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait printer information screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connection_type", timeout=timeout, raise_e=raise_e)

    def wait_for_ip_address_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait IP Address item load correctly on printer information screen
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_ip_address_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("ip_address", timeout=timeout, raise_e=raise_e)

    def wait_for_preferences_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait reference notice load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_preferences_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("preferences", timeout=timeout, raise_e=raise_e)

    def wait_for_select_language_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait select language item load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_select_language_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("select_language", timeout=timeout, raise_e=raise_e)

    def wait_for_country_region_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait country/region item load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_country_region_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("country_region", timeout=timeout, raise_e=raise_e)

    def wait_for_preference_notice_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait reference notice load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_preference_notice_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("preferences_notice", timeout=timeout, raise_e=raise_e)

    def wait_for_language_dropdown_list_items_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait language DropDown load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_language_dropdown_list_items_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("language_dropdown_list_items", timeout=timeout, raise_e=raise_e)

    def wait_for_country_dropdown_list_items_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait country DropDown load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_country_dropdown_list_items_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("country_dropdown_list_items", timeout=timeout, raise_e=raise_e)

    def wait_for_set_country_language_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait set country dialog load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_set_country_language_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("set_country_language_dialog_title", timeout=timeout, raise_e=raise_e)

    def wait_unable_to_set_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait unable to set language/country dialog load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_unable_to_set_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("set_country_language_dialog_content", timeout=timeout, raise_e=raise_e)

    def wait_for_sign_in_to_printer_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait sign in to printer dialog load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_sign_in_to_printer_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_in_to_printer_username", timeout=timeout, raise_e=raise_e)

    def wait_for_sign_in_to_printer_dialog_incorrect(self, timeout=30, raise_e=True):
        '''
        This is a method to wait sign in to printer with incorrect password error dialog load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_sign_in_to_printer_dialog_incorrect]-Wait for screen loading... ")

        return self.driver.wait_for_object("sign_in_to_printer_incorrect_password_error", timeout=timeout, raise_e=raise_e)

    def wait_for_cancel_sign_in_to_printer_dialog(self, timeout=30, raise_e=True):
        '''
        This is a method to wait cancel sign in to printer dialog load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[wait_for_cancel_sign_in_to_printer_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("cancel_sign_in_to_printer_dialog_content", timeout=timeout, raise_e=raise_e)

    def get_the_string_of_name(self):
        '''
        This is a method to get the string of Name
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_name]-Get the string of Name... ")

        return self.driver.get_value("name")

    def get_the_value_of_name(self):
        '''
        This is a method to get the value of Name
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_name]-Get the value of Name... ")

        return self.driver.get_value("name_value")

    def get_the_string_of_status(self):
        '''
        This is a method to get the string of Status
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_status]-Get the string of Status... ")

        return self.driver.get_value("status")

    def get_the_value_of_status(self):
        '''
        This is a method to get the value of Status
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_status]-Get the value of Status... ")

        return self.driver.get_value("status_value")

    def get_the_string_of_modal_name(self):
        '''
        This is a method to get the string of Modal Name
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_modal_name]-Get the string of Modal Name... ")

        return self.driver.get_value("model_name")

    def get_the_value_of_modal_name(self):
        '''
        This is a method to get the value of Modal Name
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_modal_name]-Get the value of Modal Name... ")

        return self.driver.get_value("model_name_value")

    def get_the_string_of_installation_status(self):
        '''
        This is a method to get the string of Installation Status
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_installation_status]-Get the string of Installation Status... ")

        return self.driver.get_value("installation_status")

    def get_the_value_of_installation_status(self):
        '''
        This is a method to get the value of Installation Status
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_installation_status]-Get the value of Installation Status... ")

        return self.driver.get_value("installation_status_value")

    def get_the_string_of_connection_type(self):
        '''
        This is a method to get the string of Connection Type
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_connection_type]-Get the string of Connection Type... ")

        return self.driver.get_value("connection_type")

    def get_the_value_of_connection_type(self):
        '''
        This is a method to get the value of Connection Type
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_connection_type]-Get the value of Connection Type... ")

        return self.driver.get_value("connection_type_value")

    def get_the_string_of_connection_status(self):
        '''
        This is a method to get the string of Connection Status
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_connection_status]-Get the string of Connection Status... ")

        return self.driver.get_value("connection_status")

    def get_the_value_of_connection_status(self):
        '''
        This is a method to get the value of Connection Status
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_connection_status]-Get the value of Connection Status... ")

        return self.driver.get_value("connection_status_value")

    def get_the_string_of_ip_address(self):
        '''
        This is a method to get the string of IP Address
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_ip_address]-Get the string of IP Address... ")

        return self.driver.get_value("ip_address")

    def get_the_value_of_ip_address(self):
        '''
        This is a method to get the value of IP Address
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_ip_address]-Get the value of IP Address... ")

        return self.driver.get_value("ip_address_value")

    def get_the_string_of_host_name(self):
        '''
        This is a method to get the string of Host Name
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_host_name]-Get the string of Host Name... ")

        return self.driver.get_value("host_name")

    def get_the_value_of_host_name(self):
        '''
        This is a method to get the value of Host Name
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_host_name]-Get the value of Host Name... ")

        return self.driver.get_value("host_name_value")

    def get_the_string_of_mac_address(self):
        '''
        This is a method to get the string of Mac Address
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_mac_address]-Get the string of Mac Address... ")

        return self.driver.get_value("mac_address")

    def get_the_value_of_mac_address(self):
        '''
        This is a method to get the value of Mac Address
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_mac_address]-Get the value of Mac Address... ")

        return self.driver.get_value("mac_address_value")

    def get_the_string_of_product_number(self):
        '''
        This is a method to get the string of Product Number
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_product_number]-Get the string of Product Number... ")

        return self.driver.get_value("product_number")

    def get_the_value_of_product_number(self):
        '''
        This is a method to get the value of Product Number
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_product_number]-Get the value of Product Number... ")

        return self.driver.get_value("product_number_value")

    def get_the_string_of_serial_number(self):
        '''
        This is a method to get the string of Serial Number
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_serial_number]-Get the string of Serial Number... ")

        return self.driver.get_value("serial_number")

    def get_the_value_of_serial_number(self):
        '''
        This is a method to get the value of Serial Number
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_serial_number]-Get the value of Serial Number... ")

        return self.driver.get_value("serial_number_value")

    def get_the_string_of_service_id(self):
        '''
        This is a method to get the string of Service ID
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_service_id]-Get the string of Service ID... ")

        return self.driver.get_value("service_id")

    def get_the_value_of_service_id(self):
        '''
        This is a method to get the value of Service ID
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_service_id]-Get the value of Service ID... ")

        return self.driver.get_value("service_id_value")

    def get_the_string_of_tp_number(self):
        '''
        This is a method to get the string of TP Number
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_tp_number]-Get the string of TP Number... ")

        return self.driver.get_value("tp_number")

    def get_the_value_of_tp_number(self):
        '''
        This is a method to get the value of TP Number
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_tp_number]-Get the value of TP Number... ")

        return self.driver.get_value("tp_number_value")

    def get_the_string_of_firmware_version(self):
        '''
        This is a method to get the string of Firmware Version
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_firmware_version]-Get the string of Firmware Version... ")

        return self.driver.get_value("firmware_version")

    def get_the_value_of_firmware_version(self):
        '''
        This is a method to get the value of Firmware Version
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_firmware_version]-Get the value of Firmware Version... ")

        return self.driver.get_value("firmware_version_value")

    def get_the_string_of_preferences(self):
        '''
        This is a method to get the string of Preferences.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_preference]-Get the string of Preferences... ")

        return self.driver.get_value("preferences")

    def get_the_string_of_select_language(self):
        '''
        This is a method to get the string of Select Language
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_select_language]-Get the string of Select Language... ")

        return self.driver.get_value("select_language")

    def get_the_value_of_selected_language(self):
        '''
        This is a method to get the value of language item
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_select_language]-Get the value of language item... ")

        return self.driver.get_value("language_dropdown_list")

    def get_the_string_of_country_region(self):
        '''
        This is a method to get the string of Country/Region
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_country_region]-Get the string of Country/Region... ")

        return self.driver.get_value("country_region")

    def get_the_value_of_selected_country_region(self):
        '''
        This is a method to get the value of country/region item.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_value_of_selected_country_region]-Get the value of country/region item... ")

        return self.driver.get_value("country_dropdown_list")

    def get_the_string_of_preferences_notice(self):
        '''
        This is a method to get the string of Preferences Notice Content.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[get_the_string_of_reference_notice]-Get the string of Preferences Notice Content... ")

        return self.driver.get_value("preferences_notice")

    def click_status_refresh_btn(self):
        '''
        This is a method to click status refresh button.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[click_status_refresh_btn]-Click refresh_btn... ")

        self.driver.click("status_refresh_btn", is_native_event=True)

    def click_language_display(self):
        '''
        This is a method to click language display to expand the language drop list.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[click_language_display]-Click language display... ")

        self.driver.click("selected_language_value", is_native_event=True)

    def click_set_country_language_dialog_save_btn(self):
        '''
        This is a method to click save button on set country or set language dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[click_set_country_language_dialog_save_btn]-Click save button... ")

        self.driver.click("set_country_language_dialog_save_btn", is_native_event=True)

    def click_set_country_language_dialog_cancel_btn(self):
        '''
        This is a method to click cancel button on set country or set language dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[click_set_country_language_dialog_cancel_btn]-Click cancel button... ")

        self.driver.click("set_country_language_dialog_cancel_btn", is_native_event=True)

    def click_unable_to_set_dialog_close_btn(self):
        '''
        This is a method to click close button on Unable to set language/country settings dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[click_unable_to_set_dialog_close_btn]-Click close button... ")

        self.driver.click("set_country_language_dialog_save_btn", is_native_event=True)

    def close_language_country_dropdown(self):
        '''
        This is a method to close Language/Country DropDown.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[close_language_country_dropdown]-Close Language/Country DropDown... ")

        self.driver.send_keys(Keys.ESCAPE)

    def choose_language_dropdown_listitems(self, language_index):
        '''
        This is a method to choose any option in language DropDown list
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[choose_language_dropdown_listitems]-choose any option in language drop down list... ")

        self.driver.click("language_dropdown_list", is_native_event=True)
        sleep(1)
        returnvalue = self.driver.click("language_dropdown_list_items", format_specifier=[language_index], is_native_event=True, raise_e=False)
        if (not returnvalue):
            # TODOList
            self.driver.click("language_dropdown_list_items", format_specifier=[language_index], is_native_event=True)

    def choose_country_dropdown_listitems(self, country_index):
        '''
        This is a method to choose any option in country DropDown list
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[choose_country_dropdown_listitems]-choose any option in country drop down list... ")

        self.driver.click("country_dropdown_list", is_native_event=True)
        sleep(1)
        returnvalue = self.driver.click("country_dropdown_list_items", format_specifier=[country_index], is_native_event=True, raise_e=False)
        if(not returnvalue):
            # TODOList
            self.driver.click("country_dropdown_list_items", format_specifier=[country_index], is_native_event=True)

    def input_username_inputbox(self, contents):
        '''
        This is a method to input user name into UserName text box.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[input_username_inputbox]-Input username_inputbox... ")

        self.driver.send_keys("sign_in_to_printer_username_textbox", contents, press_enter=True)

    def input_password_inputbox(self, contents):
        '''
        This is a method to input password into password text box.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[input_password_inputbox]-Input password_inputbox... ")

        self.driver.send_keys("sign_in_to_printer_password_textbox", contents, press_enter=True)

    def click_sign_in_to_printer_dialog_submit_btn(self):
        '''
        This is a method to click submit button on Sign in to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[click_sign_in_to_printer_dialog_submit_btn]-Click submit button... ")

        self.driver.click("sign_in_to_printer_submit_btn", is_native_event=True)

    def click_sign_in_to_printer_dialog_cancel_btn(self):
        '''
        This is a method to click cancel button on Sign in to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[click_sign_in_to_printer_dialog_cancel_btn]-Click cancel button... ")

        self.driver.click("sign_in_to_printer_cancel_btn", is_native_event=True)

    def click_cancel_sign_in_to_printer_dialog_try_agian_btn(self):
        '''
        This is a method to click cancel button on Sign in to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[click_cancel_sign_in_to_printer_dialog_try_agian_btn]-Click Try again button... ")

        self.driver.click("cancel_sign_in_to_printer_dialog_try_again_btn", is_native_event=True)

    def click_cancel_sign_in_to_printer_dialog_exit_setup_btn(self):
        '''
        This is a method to click cancel button on Sign in to printer dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterInformation]:[click_cancel_sign_in_to_printer_dialog_exit_setup_btn]-Click Exit setup button... ")

        self.driver.click("cancel_sign_in_to_printer_dialog_exit_setup_btn", is_native_event=True)

# -------------------------------Verification Methods--------------------------
    def verify_installation_status_value(self, is_installed=False):
        '''
        This is a verification method to verify Installation Status Value strings.
        :parameter:
        :return:
        '''
        logging.debug("Verify Installation Status Value strings")
        if is_installed:
            assert self.get_the_value_of_installation_status() == "Installed"
        else:
            assert self.get_the_value_of_installation_status() == "Not installed"

    def verify_connection_type_value(self, connection_type):
        '''
        This is a verification method to verify Connection Type Value strings.
        :parameter: connection_type is Network or USB
        :return:
        '''
        logging.debug("Verify Connection Type Value string")
        assert self.get_the_value_of_connection_type() == connection_type

    def verify_status_value_offline(self):
        '''
        This is a verification method to verify Status Value strings.
        :parameter:
        :return:
        '''
        logging.debug("Verify Status value string")
        assert self.get_the_value_of_status() == "Printer offline  "

    def verify_connection_status_value(self):
        '''
        This is a verification method to verify Connection Status Value strings.
        :parameter:
        :return:
        '''
        logging.debug("Verify Connection Status Value string")
        if self.get_the_value_of_status() == "Printer offline  ":
            assert self.get_the_value_of_connection_status() == "Inactive"
        else:
            assert self.get_the_value_of_connection_status() == "Active"

    def verify_language_dropdown_enable(self):
        '''
        This is a verification method to verify Language DropDown is enabled.
        :parameter:
        :return:
        '''
        logging.debug("Verify Language DropDown is enabled.")
        if self.driver.is_enable("language_dropdown_list"):
            raise UnexpectedItemPresentException("*TEST FAILED* - The Language DropDown is disabled.")
        return True

    def verify_language_dropdown_disable(self):
        '''
        This is a verification method to verify Language DropDown is disabled.
        :parameter:
        :return:
        '''
        logging.debug("Verify Language DropDown is disabled.")
        if self.driver.is_enable("language_dropdown_list"):
            raise UnexpectedItemPresentException("*TEST FAILED* - The Language DropDown is enabled.")
        return True 

    def verify_country_dropdown_enable(self):
        '''
        This is a verification method to verify Country/Region DropDown is enabled.
        :parameter:
        :return:
        '''
        logging.debug("Verify Country/Region DropDown is enabled.")
        if self.driver.is_enable("country_dropdown_list"):
            raise UnexpectedItemPresentException("*TEST FAILED* - The Country/Region DropDown is disabled.")
        return True

    def verify_country_dropdown_disable(self):
        '''
        This is a verification method to verify Country/Region DropDown is disabled.
        :parameter:
        :return:
        '''
        logging.debug("Verify Country/Region DropDown is disabled.")
        if self.driver.is_enable("country_dropdown_list"):
            raise UnexpectedItemPresentException("*TEST FAILED* - The Country/Region DropDown is enabled.")
        return True  

    def verify_dialog_disappear(self, timeout=10):
        '''
        This is a verification method to verify Set language or Set country dialog disappear after clicking Save/Cancel button.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("set_country_language_dialog_title", timeout=timeout, raise_e=False)

    def verify_preferences_section_show(self):
        '''
        This is a verification method to check Preference section shows correctly.
        :parameter:
        :return:
        '''
        self.wait_for_preferences_item_load()
        self.wait_for_select_language_item_load()
        self.wait_for_country_region_item_load()
        self.wait_for_preference_notice_item_load()

    def verify_preferences_hidden(self, timeout=10):
        '''
        This is a verification method to verify Preference does not show if printer is offline.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("preferences", timeout=timeout, raise_e=False)

    def verify_printer_information_page_items(self, is_LEDM=True, is_network_connection=True, is_designJet=False, is_offline=False, is_offSubnet=False):
        '''
        This is a verification method to check UI string of Printer Information Page.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Printer Information Page")
        assert self.get_the_string_of_name() == "Name:"
        assert self.get_the_string_of_status() == "Status:"
        assert self.get_the_string_of_modal_name() == "Model Name:"
        assert self.get_the_string_of_installation_status() == "Installation Status:"
        assert self.get_the_string_of_connection_type() == "Connection Type:"
        assert self.get_the_string_of_connection_status() == "Connection Status:"

        if not is_offline:
            if is_LEDM:
                if is_network_connection:
                    self.wait_for_ip_address_item_load()
                    assert self.get_the_string_of_ip_address() == "IP Address:"
                    assert self.get_the_string_of_host_name() == "Host Name:"
                    assert self.get_the_string_of_mac_address() == "MAC Address:"
                    assert self.get_the_string_of_product_number() == "Product Number:"
                    assert self.get_the_string_of_serial_number() == "Serial Number:"
                    assert self.get_the_string_of_service_id() == "Service ID:"
                    if not is_designJet:
                        assert self.get_the_string_of_tp_number() == "TP Number:"
                        assert self.get_the_string_of_firmware_version() == "Firmware Version:"
                    assert self.get_the_string_of_preferences() == "Preferences"
                    assert self.get_the_string_of_select_language() == "Select language"
                    assert self.get_the_string_of_country_region() == "Country/Region"
                else:
                    assert self.get_the_string_of_ip_address() == "Host Name:"
                    assert self.get_the_string_of_host_name() == "MAC Address:"
                    assert self.get_the_string_of_mac_address() == "Product Number:"
                    assert self.get_the_string_of_product_number() == "Serial Number:"
                    assert self.get_the_string_of_serial_number() == "Service ID:"
                    if not is_designJet:
                        assert self.get_the_string_of_service_id() == "TP Number:"
                        assert self.get_the_string_of_tp_number() == "Firmware Version:"
            else:
                if is_network_connection:
                    self.wait_for_ip_address_item_load()
                    assert self.get_the_string_of_ip_address() == "IP Address:"
                    if not is_offSubnet:
                        assert self.get_the_string_of_host_name() == "Host Name:"
                else:
                    assert self.get_the_string_of_ip_address() == "Host Name:"

    def change_language_flow(self, language_index_1, language_index_2):
        '''
        This is a verification method to verify change Language flow.
        :parameter:
        :return:
        '''
        self.choose_language_dropdown_listitems(language_index_1)
        if not self.wait_for_set_country_language_dialog_load(timeout=5, raise_e=False):
            self.choose_language_dropdown_listitems(language_index_2)
        self.wait_for_set_country_language_dialog_load()

    def change_country_flow(self, country_index_1, country_index_2):
        '''
        This is a verification method to verify change Country flow.
        :parameter:
        :return:
        '''
        self.choose_country_dropdown_listitems(country_index_1)
        if not self.wait_for_set_country_language_dialog_load(timeout=5, raise_e=False):
            self.choose_country_dropdown_listitems(country_index_2)
        self.wait_for_set_country_language_dialog_load()
