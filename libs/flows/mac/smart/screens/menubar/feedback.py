# encoding: utf-8
'''
Description: check send feedback screen

@author: ten
@create_date: July 22, 2019
'''

import logging
from selenium.common.exceptions import TimeoutException

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class Feedback(SmartScreens):
    folder_name = "menubar"
    flow_name = "feedback"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(Feedback, self).__init__(driver)

    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker
        :parameter:
        :return:
        '''
        logging.debug("[FeedbackScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("feedback_title", timeout=timeout, raise_e=raise_e)

    def click_dropdown_btn(self):
        '''
        click drop down button on feedback screen
        :parameter:
        :return:
        '''
        logging.debug("[feedbackScreen]:[feedback_dropdown_btn]click-feedback_dropdown_btnbutton... ")

        self.driver.click("feedback_dropdown_btn")

    def click_selectoption_combobox(self):
        '''
        choose select option in combobox
        :parameter:
        :return:
        '''
        logging.debug("[feedbackScreen]:[feedback_dropdown_btn]click-feedback_dropdown_btnbutton... ")

        self.driver.click("feedback_selectoption_combobox")

    def choose_dropdown_listitem_1(self):
        '''
        choose very Easy in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[feedbackScreen]:[feedback_dropdown_listitem_1]click-feedback_dropdown_listitem_1button... ")

        self.driver.choose_combo_box_options("feedback_dropdown_listitem_1")

    def choose_dropdown_listitems(self, index):
        '''
        choose any option in drop down list
        :parameter:
        :return:
        '''
        logging.debug("[feedbackScreen]:[feedback_dropdown_listitem_1]click-feedback_dropdown_listitem_1button... ")

        self.driver.choose_combo_box_options("feedback_dropdown_listitems", index)

    def input_textbox(self, contents):
        '''
        input text in textbox
        :parameter:
        :return:
        '''
        logging.debug("[feedbackScreen]:[feedback_textbox]input-feedback_textbox... ")

        self.driver.send_keys("feedback_textbox", contents, press_enter=True)

    def click_sendfeedback_btn(self):
        '''
        click_feedback_sendfeedback_button
        :parameter:
        :return:
        '''
        logging.debug("[feedbackScreen]:[ffeedback_sendfeedback_btn]click-feedback_sendfeedback_btn... ")

        self.driver.click("feedback_sendfeedback_btn")

    def click_likely_item_10_button(self):
        '''
        choose '10'
        :parameter:
        :return:
        '''
        logging.debug("[feedbackScreen]:[feedback_likely_item_10_btn]click-feedback_likely_item_10.. ")

        self.driver.click("feedback_likely_item_10")

# -------------------------------Verification Methods--------------------------
    def verify_thankyou_title_enabled(self, timeout=30):
        '''
        verify thank you screen display
        :parameter:
        :return:
        '''
        logging.debug("[feedbackScreen]:[wait_for_screen_load]-Wait for screen loading successful... ")
        assert self.driver.wait_for_object("feedback_thankyou_title", timeout=timeout)
