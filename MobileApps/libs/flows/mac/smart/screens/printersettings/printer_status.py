# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the printer status screen.

@author: Sophia
@create_date: May 21, 2019
'''

import logging

from selenium.common.exceptions import NoSuchElementException

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PrinterStatus(SmartScreens):
    folder_name = "printersettings"
    flow_name = "printer_status"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrinterStatus, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait printer status screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug(
            "[PrinterStatus]:[wait_for_screen_load]-Wait for screen loading... ")

        if(self.driver.wait_for_object("printer_image", timeout=timeout, raise_e=False) or self.driver.wait_for_object("printer_status_list", timeout=timeout, raise_e=False)):
            logging.debug("Screen loading successfully... ")
            return True
        else:
            if(raise_e):
                raise NoSuchElementException("Screen loading failed... ")
            else:
                logging.debug("Screen loading failed... ")
                return False

# -------------------------------Verification Methods--------------------------
