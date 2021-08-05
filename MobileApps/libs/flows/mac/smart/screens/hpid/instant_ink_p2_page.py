# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on the instant ink sign in/up/out page.

@author: Ivan
@create_date: Sep 24, 2019
'''

import logging

from selenium.common.exceptions import TimeoutException

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class InstantInkP2Page(SmartScreens):
    folder_name = "hpid"
    flow_name = "instant_ink_p2_page"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(InstantInkP2Page, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait the Instant Ink P2 page load.
        :parameter:
        :return:
        '''
        logging.debug("[InstantInkP2Page]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("try_it_free_for_a_month_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_with_claimed_printer(self, timeout=30, raise_e=True):
        '''
        This is a method to wait DSP page load for claimed printers.
        :parameter:
        :return:
        '''
        logging.debug("[InstantInkP2Page]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("cartridge_message_text", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_in_supply_status_with_claimed_printer(self, timeout=30, raise_e=True):
        '''
        This is a method to wait DSP page load for claimed printers.
        :parameter:
        :return:
        '''
        logging.debug("[InstantInkP2Page]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("cartridge_message_text_in_supply_status", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_with_not_ii_printer(self, timeout=30, raise_e=True):
        '''
        This is a method to wait DSP page load for not support printers.
        :parameter:
        :return:
        '''
        logging.debug("[InstantInkP2Page]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("find_your_ink_text", timeout=timeout, raise_e=raise_e)

    def click_try_it_free_for_a_month_btn(self):
        '''
        This is a method to click Try it free for a month button on the Instant Ink P2 page.
        :parameter:
        :return:
        '''
        logging.debug("[InstantInkP2Page]:[try_it_free_for_a_month_btn]-Click Try it free for a month button... ")

        self.driver.click("try_it_free_for_a_month_btn", is_native_event=True)

    def get_value_of_cartridge_message_text(self):
        '''
        This is a method to get value of cartridge message text.
        :parameter:
        :return:
        '''
        logging.debug("[InstantInkP2Page]:[get_value_of_cartridge_message_text]-Get the contents of cartridge message  ...  ")

        return self.driver.get_value("cartridge_message_text")

    def get_value_of_find_your_ink_text(self):
        '''
        This is a method to get value of find your ink .
        :parameter:
        :return:
        '''
        logging.debug("[InstantInkP2Page]:[get_value_of_find_your_ink_text]-Get the contents of find your ink text  ...  ")

        return self.driver.get_value("find_your_ink_text")

# -------------------------------Verification Methods--------------------------
    def verify_dsp_page_for_claimed_printer(self):
        '''
        verify dsp page for claimed printer
        :parameter:
        :return:
        '''
        self.wait_for_screen_load_with_claimed_printer(180)
        assert self.get_value_of_cartridge_message_text() == 'Estimated Cartridge Levels'

    def verify_dsp_page_for_not_ii_printer(self):
        '''
        verify dsp page for not support printer
        :parameter:
        :return:
        '''
        self.wait_for_screen_load_with_not_ii_printer(180)
        assert self.get_value_of_find_your_ink_text() == 'Find your ink or toner cartridges'
