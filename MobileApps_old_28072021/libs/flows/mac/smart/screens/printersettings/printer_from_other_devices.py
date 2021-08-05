# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the printer from other devices screen.

@author: Sophia
@create_date: Sep 18, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_setting_scroll import PrinterSettingScroll


class PrinterFromOtherDevices(PrinterSettingScroll, SmartScreens):
    folder_name = "printersettings"
    flow_name = "print_from_other_devices"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterFromOtherDevices, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait print from other devices screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[PrinterFromOtherDevices]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("send_link_btn", timeout=timeout, raise_e=raise_e)

    def click_send_link_btn(self):
        '''
        This is a method to click send link button.
        :parameter:
        :return:
        '''
        logging.debug("[PrinterFromOtherDevices]:[click_send_link_btn]-Click send link button... ")

        self.driver.click("send_link_btn")

# -------------------------------Verification Methods--------------------------
