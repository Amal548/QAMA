# encoding: utf-8
'''
developer tools dialog

@author: ten
@create_date: Sep 3, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class DeveloperToolsDialog(SmartScreens):

    folder_name = "menubar"
    flow_name = "developer_tools_dialog"

    def __init__(self, driver):
        super(DeveloperToolsDialog, self).__init__(driver)

# -------------------------------Operate Elements---------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        '''
        logging.debug("[DeveloperToolsDialog:[wait_for_screen_load]-Wait for screen loading... ")
        return self.driver.wait_for_object("override_app_version", timeout=timeout, raise_e=raise_e)

    def input_override_app_version(self, contents):
        '''
        input text in override app version
        :parameter:
        :return:
        '''
        logging.debug("[DeveloperToolsDialog]:[override_app_version]input-override_app_version... ")

        self.driver.send_keys("override_app_version", contents, press_enter=True)

    def click_ok_btn(self):
        '''
        click ok button
        :parameter:
        :return:
        '''
        logging.debug("[DeveloperToolsDialog]:[click ok button]click ok button... ")

        self.driver.click("ok_btn")

#  -------------------------------Verification Methods-----------------------------
