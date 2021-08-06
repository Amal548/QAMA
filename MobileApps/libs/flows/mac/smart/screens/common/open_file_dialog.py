# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the open file dialog.

@author: Sophia
@create_date: May 6, 2019
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class OpenFileDialog(SmartScreens):
    folder_name = "common"
    flow_name = "open_file_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(OpenFileDialog, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait open file dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[OpenFileDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("search_box", timeout=timeout, raise_e=raise_e)

    def select_file_by_coordinates(self, filename):
        '''
        This is a method to select file.
        :parameter:
        :return:
        '''
        logging.debug("[OpenFileDialog]:[selectFile]-set filename: " + filename + " to search box... ")

        self.driver.send_keys("search_box", filename)
        # if(self.driver.wait_for_object("search_contents")):
        logging.debug("file searched... ")

        sleep(6)
        position = self.driver.get_location("search_column")
        x_position = position['x'] - 440
        y_position = position['y'] - 340

        sleep(2)
        self.driver.click("search_column", is_native_event=True)
        self.driver.click_by_coordinates(x=x_position, y=y_position)
        return True
        # else:
        #    logging.debug("Failed to search file... ")
        #    raise NoSuchElementException

    def select_file_by_id(self, filename):
        '''
        This is a method to select file.
        :parameter:
        :return:
        '''
        logging.debug("[OpenFileDialog]:[selectFile]-set filename: " + filename + " to search box... ")

        self.driver.send_keys("search_box", filename, press_enter=True)
        sleep(3)
        self.driver.click("file_picker_searched_item", is_native_event=True)

    def click_open_btn(self):
        '''
        This is a method to click open button.
        :parameter:
        :return:
        '''
        logging.debug("[OpenFileDialog]:[click_open_btn]-Click 'Open' button... ")

        self.driver.click("open_btn")

# -------------------------------Verification Methods--------------------------
