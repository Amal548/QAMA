# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on the help & support screen.

@author: Ivan
@create_date: Sep 18, 2019
'''

import logging

from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class HelpSupport(SmartScreens):
    folder_name = "helpsupport"
    flow_name = "help_support"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(HelpSupport, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait help & support screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("about_hp_smart_app_section", timeout=timeout, raise_e=raise_e)

    def wait_for_no_internet_connection_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait no internet connection screen load correctly
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[wait_for_no_internet_connection_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("no_internet_connection_body", timeout=timeout, raise_e=raise_e)

    def wait_for_virtual_agent_image(self, timeout=30, raise_e=True):
        '''
        This is a method to wait virtual_agent_image load on help & support screen
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[wait_for_virtual_agent_image]-Wait for virtual agent image... ")

        return self.driver.wait_for_object("virtual_agent_image", timeout=timeout, raise_e=raise_e)

    def wait_for_virtual_agent_welcome_text(self, timeout=30, raise_e=True):
        '''
        This is a method to wait virtual_agent_welcome_text load on help & support screen
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[wait_for_cant_open_dialog_load]-Wait for virtual agent welcome text... ")

        return self.driver.wait_for_object("virtual_agent_welcome_text", timeout=timeout, raise_e=raise_e)

    def wait_for_virtual_agent_get_fast_text(self, timeout=30, raise_e=True):
        '''
        This is a method to wait virtual_agent_get_fast_text load on help & support screen
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[wait_for_virtual_agent_get_fast_text]-Wait for virtual agent get fast text... ")

        return self.driver.wait_for_object("virtual_agent_get_fast_text", timeout=timeout, raise_e=raise_e)

    def wait_for_virtual_agent_link(self, timeout=30, raise_e=True):
        '''
        This is a method to wait virtual_agent_btn load on help & support screen
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[wait_for_virtual_agent_btn]-Wait for virtual agent button... ")

        return self.driver.wait_for_object("virtual_agent_link", timeout=timeout, raise_e=raise_e)

    def wait_for_cookies_banner_screen(self, timeout=30, raise_e=True):
        '''
        This is a method to wait cookies banner screen load.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[wait_for_cookies_banner_screen]-Wait for cookies banner screen load... ")

        return self.driver.wait_for_object("cookies_banner_content_2", timeout=timeout, raise_e=raise_e)

    def click_chat_with_virtual_agent_link(self):
        '''
        This is a method to click chat with virtual agent link on help & support screen.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[click_chat_with_virtual_agent_link]-Click chat with virtual agent link .. ")

        self.driver.click("virtual_agent_link", is_native_event=True)

    def select_printer_support_item(self):
        '''
        This is a method to select and click printer support item on help & support screen.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[select_printer_support_item]-Select and click printer support item.. ")
        self.driver.click("printer_support", is_native_event=True)

    def select_print_anywhere_online_support_item(self):
        '''
        This is a method to select and click print anywhere online support item on help & support screen.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[select_print_anywhere_online_support_item]-Select and click print anywhere online support item.. ")
        self.driver.scroll("print_anywhere_online_support")
        self.driver.click("print_anywhere_online_support", is_native_event=True)

    def select_smart_tasks_online_support_item(self):
        '''
        This is a method to select and click smart tasks online support item on help & support screen.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[select_smart_tasks_online_support_item]-Select and click smart tasks online support item.. ")
        self.driver.scroll("smart_tasks_online_support")
        self.driver.click("smart_tasks_online_support", is_native_event=True)

    def select_hp_mobile_printing(self):
        '''
        This is a method to select and click HP mobile printing item on help & support screen.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[select_hp_mobile_printing]-Select and click HP mobile printing item.. ")
        self.driver.scroll("hp_mobile_printing")
        self.driver.click("hp_mobile_printing", is_native_event=True)

    def select_contact_hp(self):
        '''
        This is a method to select and click contact HP item on help & support screen.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[select_contact_hp]-Select and click contact hp item.. ")
        self.driver.scroll("hp_mobile_printing")
        self.driver.click("hp_mobile_printing", is_native_event=True)

    def click_ok_on_no_internet_connection_dialog(self):
        '''
        This is a method to click OK button on No Internet Connection dialog.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[click_ok_on_no_internet_connection_dialog]-Click OK button.. ")

        self.driver.click("no_internet_connection_footer", is_native_event=True)

    def click_close_on_cookies_banner(self):
        '''
        This is a method to click close button on cookies banner.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[click_close_on_cookies_banner]-Click close button.. ")

        self.driver.click("cookies_banner_close", is_native_event=True)

    def click_accept_cookies_on_cookies_banner(self):
        '''
        This is a method to click accept cookies button on cookies banner.
        :parameter:
        :return:
        '''
        logging.debug("[HelpSupport]:[click_accept_cookies_on_cookies_banner]-Click accept cookies button.. ")

        self.driver.click("cookies_banner_accept_cookies", is_native_event=True)

# -------------------------------Verification Methods--------------------------
    def verify_accept_cookies_banner_does_not_show(self, timeout=10):
        '''
        Verify accept cookies banner does not show after clicking accept cookies
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("cookies_banner_content_2", timeout=timeout, raise_e=False)

    def verify_virtual_agent_image_hidden(self, timeout=10):
        '''
        Verify virtual agent image does not show on Non-ENU language env.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("virtual_agent_image", timeout=timeout, raise_e=False)

    def verify_virtual_agent_text_hidden(self, timeout=10):
        '''
        Verify virtual agent text does not show on Non-ENU language env.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("virtual_agent_welcome_text", timeout=timeout, raise_e=False)

    def verify_virtual_agent_link_hidden(self, timeout=10):
        '''
        Verify virtual agent link does not show on Non-ENU language env.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("virtual_agent_link", timeout=timeout, raise_e=False)

    def verify_virtual_agent_information_non_enu(self):
        '''
        (Non-ENU) Check "Chat with Virtual Agent" option on list view, verify Virtual Agent option is hidden.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(120)
        self.verify_virtual_agent_image_hidden(120)
        self.verify_virtual_agent_text_hidden(120)
        self.verify_virtual_agent_link_hidden(120)

    def verify_virtual_agent_information_enu(self):
        '''
        (ENU only) Check "Chat with Virtual Agent" link on list view, verify "Chat with Virtual Agent" link shows in the help center web view
        :parameter:
        :return:
        '''
        self.wait_for_virtual_agent_link(120)
        self.wait_for_virtual_agent_image(120)
        self.wait_for_virtual_agent_welcome_text(120)
        self.wait_for_virtual_agent_get_fast_text(120)
        self.wait_for_virtual_agent_get_fast_text(120)
