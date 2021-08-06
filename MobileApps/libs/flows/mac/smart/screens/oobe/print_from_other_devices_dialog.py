# encoding: utf-8
'''
PrintFromOtherDevicesDialog

@author: ten
@create_date: July 30, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PrintFromOtherDevicesDialog(SmartScreens):
    folder_name = "oobe"
    flow_name = "print_from_other_devices_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrintFromOtherDevicesDialog, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevicesDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("dialog_title", timeout=timeout, raise_e=raise_e)

    def click_ok_btn(self):
        '''
        Click Ok Button
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevicesDialog]:[click_ok_btn]-Click 'Ok' button... ")

        self.driver.click("ok_btn")

    def get_value_of_dialog_title(self):
        '''
        get_value_of_dialog_title
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevicesDialog]:[get_value_of_dialog_title]-Get the contents of dialog_title...  ")

        return self.driver.get_value("dialog_title")

    def get_value_of_dialog_contents_1(self):
        '''
        get_value_of_dialog_contents
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevicesDialog]:[get_value_of_dialog_contents_1]-Get the contents of dialog_contents_1...  ")

        return self.driver.get_value("dialog_contents_1")

    def get_value_of_dialog_contents_2(self):
        '''
        get_value_of_dialog_contents
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevicesDialog]:[get_value_of_dialog_contents_2]-Get the contents of dialog_contents_2...  ")

        return self.driver.get_value("dialog_contents_2")

    def get_value_of_dialog_contents_3(self):
        '''
        get_value_of_dialog_contents
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevicesDialog]:[get_value_of_dialog_contents_3]-Get the contents of dialog_contents_3...  ")

        return self.driver.get_value("dialog_contents_3")

    def get_value_of_dialog_contents_4(self):
        '''
        get_value_of_dialog_contents
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevicesDialog]:[get_value_of_dialog_contents_4]-Get the contents of dialog_contents_4...  ")

        return self.driver.get_value("dialog_contents_4")

    def get_value_of_dialog_contents_5(self):
        '''
        get_value_of_dialog_contents
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevicesDialog]:[get_value_of_dialog_contents_5]-Get the contents of dialog_contents_5...  ")

        return self.driver.get_value("dialog_contents_5")

    def get_value_of_ok_btn(self):
        '''
        get_value_of_ok_btn
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevicesDialog]:[get_value_of_ok_btn]-Get the contents of ok_btn..  ")

        return self.driver.get_title("ok_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_screen_display(self):
        '''
        verify dialog display
        :parameter:
        :return:
        '''
        logging.debug("Check 'invite' dialog, verify functionality[C12612406][C12701132][C12857916]")
        assert self.get_value_of_dialog_title() == "Print from other devices"
#         assert self.get_value_of_dialog_contents_1()==u""
#         assert self.get_value_of_dialog_contents_2()==u""
#         assert self.get_value_of_dialog_contents_3()==u""
#         assert self.get_value_of_dialog_contents_4()==u""
#         assert self.get_value_of_dialog_contents_5()==u""
#         assert self.get_value_of_ok_btn()==u""
