from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow

from MobileApps.resources.const.android import const

import logging
import time
class PrintPreference(SmartFlow):
    flow_name = "print_preference"
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_cancel(self):
        """
        Click on Cancel button of popup

        End of flow: Dismiss popup
        """
        self.driver.click("cancel_btn")

    def select_unable_print_popup_turn_on(self):
        """
        Click on Turn on button of 'You might not be able to print' popup

        End of flow: Turn on Hp Inc, Plugin screen
        """
        self.driver.wait_for_object("unable_to_print_popup_title")
        self.driver.click("unable_to_print_popup_turn_on_btn")

    def select_continue(self):
        """
        Click on Continue button on 'Turn on HP Inc. Plugin' screen

        End of flow: Printing screen in Settings of mobile device
        """
        self.driver.click("continue_btn")
    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_hpps_missing_popup(self):
        """
        Verify current popup is "HP Print Service Plugin is missing!" popup via:
            + Title
            + Cancel and Continue buttons
        """
        self.driver.wait_for_object("hpps_missing_popup_title")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("continue_btn")

    def verify_unable_to_print_popup(self):
        """
        Verify that current popup is 'You might not be able to print' via:
                + Title
                + message
                + Skip and Turn on buttons
        """
        self.driver.wait_for_object("unable_to_print_popup_title")
        self.driver.wait_for_object("unable_to_print_popup_msg")
        self.driver.wait_for_object("unable_to_print_popup_turn_on_btn")
        self.driver.wait_for_object("skip_btn")

    def verify_turn_on_hp_plugin_screen(self):
        """
        Verify that current screen is Turn on Hp inc. Plugin screen
            - title
            - Continue button
        """
        self.driver.wait_for_object("turn_on_hp_plugin_title")
        self.driver.wait_for_object("continue_btn")

    def verify_hpps_print_settings_screen(self, ga={}):
        """
        Verify current screen is Select Printer of HPPS trapdoor
            - title
        Note: This function is used to count GA screen/ event
              Don't use it for other test
        """
        self.driver.wait_for_object("hpps_print_settings_print_btn")
