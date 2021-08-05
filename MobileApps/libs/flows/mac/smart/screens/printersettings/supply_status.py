# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the supply status screen.

@author: ten
@create_date: Jan 11, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SupplyStatus(SmartScreens):

    folder_name = "printersettings"
    flow_name = "supply_status"

    def __init__(self, driver):
        super(SupplyStatus, self).__init__(driver)

#  -------------------------------Operate Elements--------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("cartridges_text", timeout=timeout, raise_e=raise_e)

#  -------------------------------Verification Methods----------------------------------------
