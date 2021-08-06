# encoding: utf-8
'''
check ChooseCnnectionMethodDialog

@author: ten
@create_date: July 30, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ChooseCnnectionMethodDialog(SmartScreens):
    folder_name = "oobe"
    flow_name = "choose_a_connection_method_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ChooseCnnectionMethodDialog, self).__init__(driver)

# -----------------------------Operate Elements-------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseCnnectionMethodDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("done_btn", timeout=timeout, raise_e=raise_e)

    def click_done_btn(self):
        '''
        This is a method to click Done button on Choose a connection method dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseCnnectionMethodDialog]:[click_done_btn]-done_btn.. ")

        self.driver.click("done_btn")

    def get_value_of_choose_a_connection_method_dialog_title(self):
        '''
        This is a method to get value of Choose a connection method dialog title
        :parameter:
        :return:
        '''
        logging.debug("[ChooseCnnectionMethodDialog]:[get_value_of_choose_a_connection_method_dialog_title]-Get the contents of choose_a_connection_method_dialog_title...  ")

        return self.driver.get_value("choose_a_connection_method_dialog_title")

    def get_value_of_contents_1(self):
        '''
        This is a method to get value of contents_1 on Choose a connection method dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseCnnectionMethodDialog]:[get_value_of_contents_1]-Get the contents of contents_1...  ")

        return self.driver.get_value("contents_1")

    def get_value_of_contents_2(self):
        '''
        This is a method to get value of contents_2 on Choose a connection method dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseCnnectionMethodDialog]:[get_value_of_contents_2]-Get the contents of contents_2...  ")

        return self.driver.get_value("contents_2")

    def get_value_of_contents_3(self):
        '''
        This is a method to get value of contents_3 on Choose a connection method dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseCnnectionMethodDialog]:[get_value_of_contents_3]-Get the contents of contents_3...  ")

        return self.driver.get_value("contents_3")

    def get_value_of_contents_4(self):
        '''
        This is a method to get value of contents_4 on Choose a connection method dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseCnnectionMethodDialog]:[get_value_of_contents_4]-Get the contents of contents_4...  ")

        return self.driver.get_value("contents_4")

    def get_value_of_done_btn(self):
        '''
        This is a method to get value of Done button on Choose a connection method dialog.
        :parameter:
        :return:
        '''
        logging.debug("[ChooseCnnectionMethodDialog]:[get_value_of_done_btn]-Get the contents of Done button...  ")

        return self.driver.get_value("done_btn")

# -------------------------------Verification Methods-------------------------
    def verify_choose_a_connection_method_dialog(self):
        '''
        This is a verification method to check UI strings of Choose a connection method dialog
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        self.driver.wait_for_object("choose_a_connection_method_dialog_image", timeout=5, raise_e=True)
        logging.debug("Start to check UI String of Choose a connection method dialog")
#         assert self.get_value_of_choose_a_connection_method_dialog_title()==u""
#         assert self.get_value_of_contents_1()==u""
#         assert self.get_value_of_contents_2()==u""
#         assert self.get_value_of_contents_3()==u""
#         assert self.get_value_of_contents_4()==u""
#         assert self.get_value_of_done_btn()==u""
