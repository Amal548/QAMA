# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect Using USB screen.

@author: ten
@create_date: Aug 14, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectUsingUSB(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_using_usb"

    def __init__(self, driver):
        super(ConnectUsingUSB, self).__init__(driver)

# -------------------------------Operate Elements------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("connect_using_usb_image", timeout=timeout, raise_e=raise_e)

    def wait_for_printer_not_connected_by_usb_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Printer not connected by USB dialog load.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[wait_for_printer_not_connected_by_usb_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_not_connected_by_usb_title", timeout=timeout, raise_e=raise_e)

    def click_connect_printer_btn(self):
        '''
        This is a method to click Connect Printer button on Connect Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[click_connect_printer_btn]-Click Connect printer button.. ")

        self.driver.click("connect_using_usb_connect_printer_btn", is_native_event=True)

    def click_ok_btn(self):
        '''
        This is a method to click OK button on Printer not connected by USB dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[click_ok_btn]-Click OK button.. ")

        self.driver.click("printer_not_connected_by_usb_ok_btn")

    def get_value_of_connect_using_usb_title(self):
        '''
        This is a method to get the value of Connect Using USB screen title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_connect_using_usb_title]-Get the contents of Connect Using USB screen title...  ")

        return self.driver.get_value("connect_using_usb_title")

    def get_value_of_connect_using_usb_contents(self):
        '''
        This is a method to get the value of Connect Using USB screen contents.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_connect_using_usb_contents]-Get the contents of Connect Using USB screen contents...  ")

        return self.driver.get_title("connect_using_usb_contents")

    def get_value_of_connect_printer_btn(self):
        '''
        This is a method to get the value of Connect Printer button on Connect Using USB screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_connect_printer_btn]-Get the contents of Connect Printer button..  ")

        return self.driver.get_title("connect_using_usb_connect_printer_btn")

    def get_value_of_printer_not_connected_by_usb_title(self):
        '''
        This is a method to get the value of Printer not connected by USB dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_printer_not_connected_by_usb_title]-Get the contents of Printer not connected by USB dialog title...  ")

        return self.driver.get_value("printer_not_connected_by_usb_title")

    def get_value_of_printer_not_connected_by_usb_contents(self):
        '''
        This is a method to get the value of Printer not connected by USB dialog contents.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_printer_not_connected_by_usb_contents]-Get the contents of Printer not connected by USB dialog contents...  ")

        return self.driver.get_title("printer_not_connected_by_usb_contents")

    def get_value_of_printer_not_connected_by_usb_ok_btn(self):
        '''
        This is a method to get the value of OK button on Printer not connected by USB dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectUsingUSB]:[get_value_of_printer_not_connected_by_usb_ok_btn]-Get the contents of OK button..  ")

        return self.driver.get_title("printer_not_connected_by_usb_ok_btn")

# -------------------------------Verification Methods---------------
    def verify_connect_using_usb_screen(self):
        '''
        This is a verification method to check UI strings of Connect Using USB screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Connect Using USB screen")
#         assert self.get_value_of_connect_using_usb_title() == u""
#         assert self.get_value_of_connect_using_usb_contents() == u""
#         assert self.get_value_of_connect_printer_btn() == u""

    def verify_printer_not_connected_by_usb_dialog(self):
        '''
        This is a verification method to check UI strings of Printer not connected by USB dialog.
        :parameter:
        :return:
        '''
        self.wait_for_printer_not_connected_by_usb_dialog_load(360)
        logging.debug("Start to check UI strings of Printer not connected by USB dialog")
#         assert self.get_value_of_printer_not_connected_by_usb_title() == u""
#         assert self.get_value_of_printer_not_connected_by_usb_contents() == u""
#         assert self.get_value_of_printer_not_connected_by_usb_ok_btn() == u""
