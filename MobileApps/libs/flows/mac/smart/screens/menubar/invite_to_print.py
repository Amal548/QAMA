# encoding: utf-8
'''
check Invite to print screem

@author: ten
@create_date: July 22, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class InviteToPrint(SmartScreens):
    folder_name = "menubar"
    flow_name = "invite_to_print"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(InviteToPrint, self).__init__(driver)

    # -------------------------------Operate Elements--------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[InviteToPrintScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("invite_to_print_title", timeout=timeout, raise_e=raise_e)
