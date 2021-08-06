# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the tool bar.

@author: Sophia
@create_date: May 8, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class ToolBar(SmartScreens):
    folder_name = "common"
    flow_name = "tool_bar"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ToolBar, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self):
        pass

    def wait_for_quick_reference_btn_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Quick Reference button shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]:[wait_for_quick_reference_btn_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("quick_reference_btn", timeout=timeout, raise_e=raise_e)

    def click_tool_bar(self):
        '''
        This is a method to click tool bar.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]:[click_tool_bar]-Click tool bar... ")

        self.driver.click("tool_bar")

    def click_home_btn(self):
        '''
        This is a method to click home button.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]:[click_home_btn]-Click 'Home' button... ")

        self.driver.click("home_btn", is_native_event=True)

    def click_quick_reference_btn(self):
        '''
        This is a method to click Quick Reference button.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]:[click_quick_reference_btn]-Click 'Quick Reference' button... ")

        self.driver.click("quick_reference_btn", is_native_event=True)

    def click_close_btn(self):
        '''
        This is a method to click close button.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]:[click_close_btn]-Click 'close' button... ")
        self.driver.click("close_btn")

    def click_select_printer_btn(self):
        '''
        This is a method to click select printer button.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]:[click_select_printer_btn]-Click 'Select Printer' button... ")

        self.driver.click("select_printer_btn", is_native_event=True)

    def click_back_btn(self):
        '''
        This is a method to click back button.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]]:[click_back_btn-Click 'back_btn' button... ")

        self.driver.click("back_btn", is_native_event=True)

    def click_forward_btn(self):
        '''
        This is a method to click forward button.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]]:[click_forward_btn]-Click Forward button... ")

        self.driver.click("forward_btn", is_native_event=True)

    def click_person_btn(self, is_sign_in=False):
        '''
        This is a method to click person button.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]]:[click_person_btn-Click 'person_btn' button... ")
        if(is_sign_in):
            self.driver.click("person_btn", is_native_event=True)
        else:
            self.driver.click("bell_btn", is_native_event=True)

    def click_bell_btn(self):
        '''
        This is a method to click bell button.
        :parameter:
        :return:
        '''
        logging.debug("[ToolBar]]:[click_bell_btn]-Click bell button... ")

        self.driver.click("bell_btn", is_native_event=True)

# -------------------------------Verification Methods--------------------------
    def verify_bell_icon_enable(self):
        '''
        verify bell icon is enable
        :parameter:
        :return:
        '''
        logging.debug("verify bell icon's behavior")
        if not self.driver.is_enable("bell_btn"):
            raise UnexpectedItemPresentException("Bell Icon is disabled")
        return True

    def verify_person_icon_enable(self, is_sign_in=False):
        '''
        verify person icon is enable
        :parameter:
        :return:
        '''
        logging.debug("verify person icon's behavior")
        if is_sign_in:
            if not self.driver.is_enable("person_btn"):
                raise UnexpectedItemPresentException("Person Icon is disabled")
            return True
        else:
            if not self.driver.is_enable("bell_btn"):
                raise UnexpectedItemPresentException("Person Icon is disabled")
            return True

    def verify_bell_icon_disable(self):
        '''
        verify bell icon is disable
        :parameter:
        :return:
        '''
        logging.debug("verify bell icon's behavior")
        if self.driver.is_enable("bell_btn"):
            raise UnexpectedItemPresentException("Bell Icon is enabled")
        return True

    def verify_person_icon_disable(self, is_sign_in=False):
        '''
        verify person icon is disable
        :parameter:
        :return:
        '''
        logging.debug("verify person icon's behavior")
        if is_sign_in:
            if self.driver.is_enable("person_btn"):
                raise UnexpectedItemPresentException("Person Icon is enabled")
            return True
        else:
            if self.driver.is_enable("bell_btn"):
                raise UnexpectedItemPresentException("Person Icon is enabled")
            return True
