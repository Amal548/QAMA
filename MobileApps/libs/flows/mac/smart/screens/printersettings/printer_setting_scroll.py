# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the printer settings scroll area.

@author: Sophia
@create_date: Sep 18, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PrinterSettingScroll(SmartScreens):
    folder_name = "printersettings"
    flow_name = "printer_setting_scroll"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterSettingScroll, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for screen shows correctly.
        :parameter:
        :return:
        '''
        pass

    def click_print_anywhere_tab(self, claimed=False):
        '''
        This is a method to click print anywhere.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_print_anywhere_tab]-Click print anywhere... ")

        if(claimed):
            self.driver.click("print_anywhere_tab_claimed", is_native_event=True)
        else:
            self.driver.click("printer_anywhere_tab", is_native_event=True)

    def click_print_from_other_devices(self):
        '''
        This is a method to click print from other devices.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_print_from_other_devices]-Click print from other devices... ")

        self.driver.click("print_from_other_devices_tab", is_native_event=True)

    def click_network_information_tab(self):
        '''
        This is a method to click network_information_tab.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_network_information_tab]-Click network_information_tab... ")

        self.driver.click("network_information_tab", is_native_event=True)

    def click_printer_anywhere_tab(self):
        '''
        This is a method to click printer_anywhere_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_printer_anywhere_tab]-Click printer_anywhere_tab... ")

        self.driver.click("printer_anywhere_tab", is_native_event=True)

    def click_advanced_settings_tab(self):
        '''
        This is a method to click advanced_settings_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_advanced_settings_tab]-advanced_settings_tab... ")

        self.driver.click("advanced_settings_tab", is_native_event=True)

    def click_printer_reports_tab(self):
        '''
        This is a method to click printer_reports_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_printer_reports_tab]-Click printer_reports_tab... ")

        self.driver.click("printer_reports_tab", is_native_event=True)

    def click_print_quality_tools_tab(self):
        '''
        This is a method to click print from other devices.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_print_quality_tools_tab]-Click print_quality_tools_tab... ")

        self.driver.click("print_quality_tools_tab", is_native_event=True)

    def click_forget_this_printer_tab(self):
        '''
        This is a method to click forget this printer.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_forget_this_printer_tab]-Click forget_this_printer_tab... ")

        self.driver.click("forget_this_printer_tab", is_native_event=True)

    def click_supply_status_tab(self):
        '''
        This is a method to click supply status.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]:[click_supply_status_tab]-Click supply_status_tab... ")

        self.driver.click("supply_status_tab", is_native_event=True)

    def get_value_of_status_text(self):
        '''
        get_value_of_status_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_status_text-Get the contents of status_text ...  ")

        return self.driver.get_value("status_text")

    def get_value_of_printer_status_tab(self):
        '''
        get_value_of_printer_status_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_printer_status_tab-Get the contents of printer_status_tab ...  ")

        return self.driver.get_value("printer_status_tab")

    def get_value_of_supply_status_tab(self):
        '''
        get_value_of_supply_status_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_supply_status_tab-Get the contents of supply_status_tab...  ")

        return self.driver.get_value("supply_status_tab")

    def get_value_of_information_text(self):
        '''
        get_value_of_information_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_information_text-Get the contents of information_text...  ")

        return self.driver.get_value("information_text")

    def get_value_of_printer_information_tab(self):
        '''
        get_value_of_printer_information_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_printer_information_tabGet the contents ofprinter_information_tab ...  ")

        return self.driver.get_value("printer_information_tab")

    def get_value_of_network_information_tab(self):
        '''
        get_value_of_network_information_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_network_information_tab-Get the contents of network_information_tab ...  ")

        return self.driver.get_value("network_information_tab")

    def get_value_of_settings_text(self):
        '''
        get_value_of_settings_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_settings_text-Get the contents of settings_text ...  ")

        return self.driver.get_value("settings_text")

    def get_value_of_printer_anywhere_tab(self):
        '''
        get_value_of_printer_anywhere_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_printer_anywhere_tab-Get the contents of printer_anywhere_tab ...  ")

        return self.driver.get_value("printer_anywhere_tab")

    def get_value_of_advanced_settings_tab(self):
        '''
        get_value_of_advanced_settings_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_advanced_settings_tab-Get the contents of advanced_settings_tab ...  ")

        return self.driver.get_value("advanced_settings_tab")

    def get_value_of_tools_text(self):
        '''
        get_value_of_tools_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_tools_text_tab-Get the contents of tools_text...  ")

        return self.driver.get_value("tools_text")

    def get_value_of_printer_reports_tab(self):
        '''
        get_value_of_printer_reports_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_printer_reports_tab-Get the contents of printer_reports_tab ...  ")

        return self.driver.get_value("printer_reports_tab")

    def get_value_of_print_quality_tools_tab(self):
        '''
        get_value_of_print_quality_tools_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_print_quality_tools_tab-Get the contents of print_quality_tools_tab ...  ")

        return self.driver.get_value("print_quality_tools_tab")

    def get_value_of_manage_text(self):
        '''
        get_value_of_manage_text
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_manage_text-Get the contents of manage_text...  ")

        return self.driver.get_value("manage_text")

    def get_value_of_print_from_other_devices_tab(self):
        '''
        get_value_of_print_from_other_devices_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_print_from_other_devices_tab-Get the contents of print_from_other_devices_tab...  ")

        return self.driver.get_value("print_from_other_devices_tab")

    def get_value_of_forget_this_printer_tab(self):
        '''
        get_value_of_forget_this_printer_tab
        :parameter:
        :return:
        '''
        logging.debug("[PrinterSettingScroll]]:[get_value_of_forget_this_printer_tab-Get the contents of forget_this_printer_tab...  ")

        return self.driver.get_value("forget_this_printer_tab")

# -------------------------------Verification Methods--------------------------
    def verify_ui_string(self):
        '''
        Verify strings are translated correctly and matching string table.
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
        assert self.get_value_of_status_text() == "Status"
        assert self.get_value_of_printer_status_tab() == "Printer Status"
        self.assertTrue(self.driver.is_enable("printer_status_tab"))
        assert self.get_value_of_supply_status_tab() == "Supply Status"
        self.assertTrue(self.driver.is_enable("supply_status_tab"))
#         assert self.get_value_of_information_text() == u""
#         assert self.get_value_of_printer_information_tab() == u""
#         assert self.driver.find_object("printer_information_tab").is_enabled()==True
#         assert self.get_value_of_network_information_tab() == u""
#         assert self.driver.find_object("network_information_tab").is_enabled()==True
#         assert self.get_value_of_settings_text() == u""
#         assert self.get_value_of_advanced_settings_tab() == u""
#         assert self.driver.find_object("advanced_settings_tab").is_enabled()==True
#         assert self.get_value_of_tools_text() == u""
#         assert self.get_value_of_printer_reports_tab() == u""
#         assert self.driver.find_object("printer_reports_tab").is_enabled()==True
#         assert self.get_value_of_print_quality_tools_tab() == u""
#         assert self.driver.find_object("print_quality_tools_tab").is_enabled()==True
#         assert self.get_value_of_manage_text() == u""
#         assert self.get_value_of_print_from_other_devices_tab() == u""
#         assert self.driver.find_object("print_from_other_devices_tab").is_enabled()==True
#         assert self.get_value_of_forget_this_printer_tab() == u""
#         assert self.driver.find_object("forget_this_printer_tab").is_enabled()==True

    def verify_options_state_remote_printer(self):
        '''
        verify_options_state_remote_printer
        :parameter:
        :return:
        '''
        logging.debug("verify_options_state_remote_printer")
        assert self.get_value_of_status_text() == "Status"
        assert self.get_value_of_printer_status_tab() == "Supply Status"
        assert self.get_value_of_supply_status_tab() == "Information"
        assert self.get_value_of_information_text() == "Printer Information"
        assert self.get_value_of_printer_information_tab() == "Settings"
        assert self.get_value_of_network_information_tab() == "Print Anywhere"
        assert self.get_value_of_settings_text() == "Manage"
        assert self.get_value_of_printer_anywhere_tab() == "Print From Other Devices"
        assert self.get_value_of_advanced_settings_tab() == "Forget This Printer"
