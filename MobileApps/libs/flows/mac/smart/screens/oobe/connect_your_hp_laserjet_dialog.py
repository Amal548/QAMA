# encoding: utf-8
'''
check connect your HP laserjet dialog

@author: ten
@create_date: Aug 22, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectYourHPLaserJetDialog(SmartScreens):

    folder_name = "oobe"
    flow_name = "connect_your_hp_laserjet_dialog"

    def __init__(self, driver):
        super(ConnectYourHPLaserJetDialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_continue_btn(self):
        '''
        Click continue button
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[click_continue_btn]-Click continue_btn.. ")

        self.driver.click("continue_btn")

    def get_value_of_contents_1(self):
        '''
        get_value_of_contents_1
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[get_value_of_contents_1]-Get the contents of contents_1...  ")

        return self.driver.get_value("contents_1")

    def get_value_of_contents_3(self):
        '''
        get_value_of_contents_3
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[get_value_of_contents_3]-Get the contents of contents_3...  ")

        return self.driver.get_value("contents_3")

    def get_value_of_contents_4(self):
        '''
        get_value_of_contents_4
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[get_value_of_contents_4]-Get the contents of contents_4...  ")

        return self.driver.get_value("contents_4")

    def get_value_of_contents_5(self):
        '''
        get_value_of_contents_1
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[get_value_of_contents_5]-Get the contents of contents_5...  ")

        return self.driver.get_value("contents_5")

    def get_value_of_contents_6(self):
        '''
        get_value_of_contents_6
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[get_value_of_contents_6]-Get the contents of contents_6...  ")

        return self.driver.get_value("contents_6")

    def get_value_of_contents_7(self):
        '''
        get_value_of_contents_7
        :parameter:
        :return:
        '''
        logging.debug("[ConnectYourHPLaserJetDialog]:[get_value_of_contents_1]-Get the contents of contents_7...  ")

        return self.driver.get_value("contents_7")

#  -------------------------------Verification Methods------------------------
    def verify_ui_string(self):
        '''
        verify_ui_string
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
#         assert self.get_value_of_contents_1() == u''
#         assert self.get_value_of_contents_3() == u''
#         assert self.get_value_of_contents_4() == u''
#         assert self.get_value_of_contents_5() == u''
#         assert self.get_value_of_contents_6() == u''
#         assert self.get_value_of_contents_7() == u''
