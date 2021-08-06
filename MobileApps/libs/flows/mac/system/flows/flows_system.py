# encoding: utf-8
'''
Description: It defines system flows in the MAC OS.

@author: Sophia
@create_date: May 9, 2019
'''

import logging
from time import sleep

from selenium.common.exceptions import WebDriverException

from MobileApps.libs.flows.mac.system.screens.system_preferences import SystemPreferences


class SystemFlows(object):

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        self.driver = driver

    def install_printer_using_printer_name(self, printer_name, raise_e=True):
        '''
        This is a method to install printer using printer BONJOUR name.
        :parameter:
        :return:
        '''
        logging.debug(
            "[Utilities]:[install_printer_using_printer_name]-Install printer using printer bonjour name: " + printer_name)

        try:
            self.driver.open_app("System Preferences")
            sleep(1)

            add_printer_screen = SystemPreferences(self.driver)
            add_printer_screen.click_printers_scanners_btn()
            add_printer_screen.wait_for_printers_sanners_screen_load()

            add_printer_screen.click_plus_button()
            add_printer_screen.wait_for_add_printers_screen_load()

            add_printer_screen.select_printer(printer_name)
            add_printer_screen.wait_for_gather_pirnter_info_finished(90)
            sleep(1)
            add_printer_screen.click_add_printer_button()
            if add_printer_screen.wait_for_ok_btn_display(timeout=5, raise_e=False):
                add_printer_screen.click_ok_btn()
            add_printer_screen.wait_for_finish_to_add_printer(600)

        except WebDriverException:
            if raise_e:
                raise WebDriverException(
                    "Error happened during add printer process...")
            else:
                return False
        finally:
            add_printer_screen.click_close_printers_scanners_btn()

    def delete_all_printers_and_fax(self, raise_e=True):
        '''
        This is a method to delete all installed printers in the MAC system.
        :parameter:
        :return:
        '''
        logging.debug(
            "[Utilities]:[delete_all_printers_and_fax]-Delete all printers...")

        try:
            self.driver.open_app("System Preferences")
            sleep(1)

            printer_screen = SystemPreferences(self.driver)
            printer_screen.click_printers_scanners_btn()
            printer_screen.wait_for_printers_sanners_screen_load()

            printer_rows = printer_screen.get_printer_list_row_num()
            while (printer_rows > 1):
                printer_screen.click_minus_button()
                printer_screen.wait_for_delete_printers_screen_load()

                printer_screen.click_delete_printer_button()

                sleep(1)
                printer_rows = printer_screen.get_printer_list_row_num()

        except WebDriverException:
            if raise_e:
                raise WebDriverException(
                    "Error happened during delete printer process...")
            else:
                return False
        finally:
            printer_screen.click_close_printers_scanners_btn()

    def turn_off_computer_wifi_connection(self, raise_e=True):
        '''
        This is a method to turn off the WiFi connection in the MAC system.
        :parameter:
        :return:
        '''
        logging.debug("[Utilities]:[turn_off_computer_wifi_connection]-Turn off WiFi connection...")

        try:
            self.driver.open_app("System Preferences")
            sleep(1)

            network_page = SystemPreferences(self.driver)
            network_page.click_network_btn()
            network_page.wait_for_network_wifi_screen_load()
            network_page.click_turn_wifi_on_btn()

        except WebDriverException:
            if raise_e:
                raise WebDriverException("Error happened during turn off wifi process...")
            else:
                return False
        finally:
            network_page.click_close_network_page_btn()

    def turn_on_computer_wifi_connection(self, raise_e=True):
        '''
        This is a method to turn on the WiFi connection in the MAC system.
        :parameter:
        :return:
        '''
        logging.debug("[Utilities]:[turn_off_computer_wifi_connection]-Turn off WiFi connection...")

        try:
            self.driver.open_app("System Preferences")
            sleep(1)

            network_page = SystemPreferences(self.driver)
            network_page.click_network_btn()
            network_page.wait_for_network_page_screen_load()
            network_page.click_wifi_option()
            network_page.wait_for_network_wifi_screen_load()
            network_page.click_turn_wifi_on_btn()

        except WebDriverException:
            if raise_e:
                raise WebDriverException("Error happened during turn on wifi process...")
            else:
                return False
        finally:
            network_page.click_close_network_page_btn()
