# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the system preferences screen.

@author: Sophia
@create_date: May 9, 2019
'''

import logging

from MobileApps.libs.flows.mac.system.screens.system_screens import SystemScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import ItemNotFoundException


class SystemPreferences(SystemScreens):
    folder_name = ""
    flow_name = "system_preferences"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(SystemPreferences, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait system preferences screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printers_sanners_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_printers_sanners_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait printer and scanner screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[wait_for_printers_sanners_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("search_field_printers", timeout=timeout, raise_e=raise_e)

    def wait_for_add_printers_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait add printer screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[wait_for_add_printers_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("add_printer_search_box", timeout=timeout, raise_e=raise_e)

    def wait_for_delete_printers_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait delete printer screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[wait_for_delete_printers_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("delete_printer_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_gather_pirnter_info_finished(self, timeout=30, raise_e=True):
        '''
        This is a method to wait gather printer information finished.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[wait_for_gather_pirnter_info_finished]-Wait for object dismiss... ")

        return self.driver.wait_for_object_disappear("gather_info_text", timeout=timeout, raise_e=raise_e)

    def wait_for_finish_to_add_printer(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for install printer done.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[wait_for_finish_to_add_printer]-Wait for object dismiss... ")

        return self.driver.wait_for_object_disappear("add_printer_sheet", timeout=timeout, raise_e=raise_e)

    def wait_for_ok_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to install usb driver
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[wait_for_ok_btn_display]-Wait for OK button... ")

        return self.driver.wait_for_object("ok_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_network_page_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait network page screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[SystemPreferences]:[wait_for_network_page_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("network_title", timeout=timeout, raise_e=raise_e)

    def wait_for_network_wifi_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait network wifi screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[SystemPreferences]:[wait_for_network_wifi_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("turn_wifi_on_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_dialog_done_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait network wifi screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[SystemPreferences]:[wait_for_dialog_done_btn_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("done_btn", timeout=timeout, raise_e=raise_e)

    def click_wifi_option(self):
        '''
        This is a method to click wifi option.
        :parameter:
        :return:
        '''
        logging.debug("[SystemPreferences]:[click_wifi_option]-Click wifi option... ")

        self.driver.click("wifi_opt", is_native_event=True)

    def click_turn_wifi_on_btn(self):
        '''
        This is a method to click turn wifi on btn on network wifi screen.
        :parameter:
        :return:
        '''
        logging.debug("[SystemPreferences]:[click_turn_wifi_on_btn]-Click turn wifi on... ")

        self.driver.click("turn_wifi_on_btn", is_native_event=True)

    def click_close_network_page_btn(self):
        '''
        This is a method to close the network page screen.
        :parameter:
        :return:
        '''
        logging.debug("[SystemPreferences]:[click_close_network_page_btn]-Click 'Close' button... ")

        self.driver.click("close_network_page_btn", is_native_event=True)

    def select_printer(self, printername):
        '''
        This is a method to select printer.
        :parameter:
        :return:
        '''
        logging.debug("[SystemPreferences]:[select_printer]-set printer: " +
                      printername + " to search box... ")

        self.driver.send_keys("add_printer_search_box", printername)
        if(self.driver.wait_for_object("printer_searched", raise_e=False)):
            logging.debug("printer searched... ")
            self.driver.click("printer_searched", is_native_event=True)
        else:
            raise ItemNotFoundException(
                "Printer: " + printername + "can't be searched...")

    def click_add_printer_button(self):
        '''
        This is a method to click add printer button.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[click_add_printer_button]-Click 'Add' button... ")

        self.driver.click("add_printer_btn", is_native_event=True)

    def click_plus_button(self):
        '''
        This is a method to click plus button on the printer and scanner screen.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[click_plus_button]-Click 'Add' button... ")

        self.driver.click("add_printer_plus_btn")

    def click_minus_button(self):
        '''
        This is a method to click minus button on the printer and scanner screen.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[click_minus_button]-Click 'Delete' button... ")

        self.driver.click("delete_printer_minus_btn")

    def click_printers_scanners_btn(self):
        '''
        This is a method to click printer and scanner button.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[click_printers_scanners_btn]-Click 'Printers and Scanners' button... ")

        self.driver.click("printers_sanners_btn")

    def click_network_btn(self):
        '''
        This is a method to click network button.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[click_network_btn]-Click 'Network' button... ")

        self.driver.click("network_btn")

    def click_close_printers_scanners_btn(self):
        '''
        This is a method to close the printer and scanner screen.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[click_close_printers_scanners_btn]-Click 'Close' button... ")

        self.driver.click("close_add_printer_btn")

    def get_printer_list_row_num(self):
        '''
        This is a method to get number of installed printer and fax.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[get_printer_list_row_num]-Get printer list rows... ")

        printer_list = self.driver.get_attribute(
            "printer_list", "AXRows").split(",")
        row_num = len(printer_list)
        return row_num

    def click_delete_printer_button(self):
        '''
        This is a method to click delete printer button.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[click_delete_printer_button]-Click 'Delete' button... ")

        self.driver.click("delete_printer_btn")

    def click_ok_btn(self):
        '''
        This is a method to click printer and scanner button.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[click_ok_btn]-Click 'ok' button... ")

        self.driver.click("ok_btn")

    def click_dialog_done_btn(self):
        '''
        This is a method to click printer and scanner button.
        :parameter:
        :return:
        '''
        logging.debug(
            "[SystemPreferences]:[click_ok_btn]-Click 'Done' button... ")
        if (self.wait_for_dialog_done_btn_display(timeout=5, raise_e=False)):
                self.driver.click("done_btn")

# -------------------------------Verification Methods--------------------------
