# encoding: utf-8
'''
SetupIsAlmostFinished screen

@author: ten
@create_date: July 25, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SetupIsAlmostFinished(SmartScreens):
    folder_name = "oobe"
    flow_name = "setup_is_almost_finished"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(SetupIsAlmostFinished, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("setup_is_almost_finished_title", timeout=timeout, raise_e=raise_e)

    def click_printers_scanners_btn(self):
        '''
        Click printers&scanners button
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[click_printers_scanners_btn]-printers_scanners_btn... ")

        self.driver.click("printers_scanners_btn")

    def click_printers_scanners_close_btn(self):
        '''
        Click printers&scanners close button
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[click_printers_scanners_close_btn]-printers_scanners_close_btn... ")

        self.driver.click("printers_scanners_close_btn")

    def get_value_of_setup_is_almost_finished_title(self):
        '''
        get_value_of_setup_is_almost_finished_title
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_setup_is_almost_finished_title]-Get the contents of setup_is_almost_finished_title..  ")

        return self.driver.get_value("setup_is_almost_finished_title")

    def get_value_of_contents_1(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_contents_1]-Get the contents of contents_1...  ")

        return self.driver.get_value("contents_1")

    def get_value_of_contents_2_1(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_contents_2_1]-Get the contents of contents_2_1...  ")

        return self.driver.get_value("contents_2_1")

    def get_value_of_contents_2_2(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_contents_2_2]-Get the contents of contents_2_2...  ")

        return self.driver.get_value("contents_2_2")

    def get_value_of_contents_2_3(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_contents_2_3]-Get the contents of contents_2_3...  ")

        return self.driver.get_value("contents_2_3")

    def get_value_of_contents_3(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_contents_3]-Get the contents of contents_3...  ")

        return self.driver.get_value("contents_3")

    def get_value_of_contents_4(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_contents_4]-Get the contents of contents_4...  ")

        return self.driver.get_value("contents_4")

    def get_value_of_contents_5_1(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_contents_5_1-Get the contents of contents_5_1..  ")

        return self.driver.get_value("contents_5_1")

    def get_value_of_contents_5_2(self):
        '''
        get value of contents
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_contents_5_2]-Get the contents of contents_5_2...  ")

        return self.driver.get_value("contents_5_2")

    def get_value_of_printers_scanners_btn(self):
        '''
        get value of printers_scanners button
        :parameter:
        :return:
        '''
        logging.debug("[SetupIsAlmostFinished]:[get_value_of_printers_scanners_btn]-Get the contents of printers_scanners_btn...  ")

        return self.driver.get_title("printers_scanners_btn")

# -------------------------------Verification Methods-------------------------------------------------
    # def verify_ui_string(self):
    #     '''
    #     Verify strings are translated correctly and matching string table.
    #     :parameter:
    #     :return:
    #     '''
    #     logging.debug("Verify strings are translated correctly and matching string table.[C12865260][C12865261]")
    #     assert self.get_value_of_setup_is_almost_finished_title() == u""
    #     assert self.get_value_of_contents_1() == u""
    #     assert self.get_value_of_contents_2() == u""
    #     assert self.get_value_of_contents_2_1() == u""
    #     assert self.get_value_of_contents_2_2() == u""
    #     assert self.get_value_of_contents_2_3() == u""
    #     assert self.get_value_of_contents_3() == u""
    #     assert self.get_value_of_contents_4() == u""
    #     assert self.get_value_of_contents_5_1() == u""
    #     assert self.get_value_of_contents_5_2() == u""
    #     assert self.get_value_of_printers_scanners_btn() == u""
