# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the Would you like to save this password dialog

@author: ten
@create_date: May 22, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class Savethispassworddialog(SmartScreens):

    folder_name = "common"
    flow_name = "save_this_password_dialog"

    def __init__(self, driver):
        super(Savethispassworddialog, self).__init__(driver)

    # -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[ClassName]:[wait_for_to_save_this_password_dialog]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_not_now_btn(self):
        '''
        This is a method to click not now btn
        :parameter:
        :return:
        '''
        logging.debug("[SigninDialog]:[click_not_now_btn-Click 'not now' button... ")

        self.driver.click("not_now_btn")

    def click_save_password_btn(self):
        '''
        This is a method to click save password btn
        :parameter:
        :return:
        '''
        logging.debug("[SigninDialog]:[click_save_password_btn-Click 'save password' button... ")

        self.driver.click("save_password_btn")

    # -------------------------------Verification Methods-----------------------------------

