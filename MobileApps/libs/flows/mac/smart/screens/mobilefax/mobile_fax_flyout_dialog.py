# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Mobile Fax flyout dialog screen.

@author: ten
@create_date: Jan 6, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class MobileFaxFlyoutDialog(SmartScreens):

    folder_name = "mobilefax"
    flow_name = "mobile_fax_flyout_dialog"

    def __init__(self, driver):
        super(MobileFaxFlyoutDialog, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax flyout dialog screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxFlyoutDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_learn_more_btn(self):
        '''
        This is a method to click Get Started button on Mobile Fax value prop screen.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxFlyoutDialog:[click_learn_more_btn]-Click learn more button... ")

        self.driver.click("learn_more_btn", is_native_event=True)

    def get_value_of_dialog_title(self):
        '''
        This is a method to get value of screen title of Mobile Fax flyout dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxFlyoutDialog]:[get_value_of_mobile_fax_title] - Get value of screen title...  ")

        return self.driver.get_value("mobile_fax_title")

    def get_value_of_dialog_content(self):
        '''
        This is a method to get value of screen title of Mobile Fax flyout dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxFlyoutDialog]:[get_value_of_dialog_content] - Get value of screen content...  ")

        return self.driver.get_value("dialog_content")

    def get_value_of_learn_more_btn(self):
        '''
        This is a method to get value of screen title of Mobile Fax flyout dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxFlyoutDialog]:[get_value_of_learn_more_btn] - Get value of learn more button...  ")

        return self.driver.get_title("learn_more_btn")

    # -------------------------------Verification Methods----------------------------------------
    def verify_mobile_fax_flyout_dialog(self):
        '''
        This is a verification method to check UI strings of Mobile Fax flyout dialog.
        :parameter:
        :return:
        '''
        logging.debug("Start to check UI strings of Mobile Fax flyout dialog")
#         assert self.get_value_of_dialog_title() == u""
#         assert self.get_value_of_dialog_content() == u""
#         assert self.get_value_of_learn_more_btn() == u""
  