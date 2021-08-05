# encoding: utf-8
'''
SendAnotherLinkDialog screen

@author: ten
@create_date: July 25, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class SendAnotherLinkDialog(SmartScreens):
    folder_name = "oobe"
    flow_name = "send_another_link_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(SendAnotherLinkDialog, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("send_another_link_btn", timeout=timeout, raise_e=raise_e)

    def click_send_another_link_btn(self):
        '''
        This is a method to click Send Another Link button on this dialog
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[click_send_another_link_btn]-Click Send Another Link button.. ")

        self.driver.click("send_another_link_btn")

    def click_done_btn(self):
        '''
        This is a method to click Done button on this dialog
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[click_done_btn]-Click Done button.. ")

        self.driver.click("done_btn")

    def select_email_menu_item(self):
        '''
        This is a method to select Email menu item after clicking Send Another link button on the dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[select_email_menu_item]-Select Email menu item... ")

        self.driver.click("send_another_link_menu_item_email", is_native_event=True)

    def get_value_of_send_another_link_dialog_contents_1(self):
        '''
        This is a method to get_value_of Send another link dialog contents - 1
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[get_value_of_send_another_link_dialog_contents_1]-Get the contents of Send another link dialog contents - 1..  ")

        return self.driver.get_value("send_another_link_dialog_contents_1")

    def get_value_of_send_another_link_dialog_contents_2(self):
        '''
        This is a method to get_value_of Send another link dialog contents - 2
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[get_value_of_send_another_link_dialog_contents_2]-Get the contents of Send another link dialog contents - 2...  ")

        return self.driver.get_value("send_another_link_dialog_contents_2")

    def get_value_of_send_another_link_btn(self):
        '''
        This is a method to get_value_of Send another link button on this dialog
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[get_value_of_send_another_link_btn]-Get the contents of Send another link button...  ")

        return self.driver.get_title("send_another_link_btn")

    def get_value_of_done_btn(self):
        '''
        This is a method to get value of Done button on this dialog
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[get_value_of_done_btn]-Get the contents of Done button...  ")

        return self.driver.get_title("done_btn")

    def get_value_of_items_1(self):
        '''
        This is a method to get value of Send Another Link item - 1
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[get_value_of_items_1]-Get the contents of Send Another Link item - 1...  ")

        return self.driver.get_title("send_another_link_menu_item_email")

    def get_value_of_items_2(self):
        '''
        This is a method to get value of Send Another Link item - 2
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[get_value_of_items_2]-Get the contents of Send Another Link item - 2...  ")

        return self.driver.get_title("send_another_link_menu_item_messages")

    def get_value_of_items_3(self):
        '''
        This is a method to get value of Send Another Link item - 3
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[get_value_of_items_3]-Get the contents of Send Another Link item - 3...  ")

        return self.driver.get_title("send_another_link_menu_item_notes")

    def get_value_of_items_4(self):
        '''
        This is a method to get value of Send Another Link item - 4
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[get_value_of_items_4]-Get the contents of Send Another Link item - 4...  ")

        return self.driver.get_title("send_another_link_menu_item_reminders")

    def get_value_of_items_5(self):
        '''
        This is a method to get value of Send Another Link item - 5
        :parameter:
        :return:
        '''
        logging.debug("[SendAnotherLinkDialog]:[get_value_of_items_5]-Get the contents of Send Another Link item - 5...  ")

        return self.driver.get_title("send_another_link_menu_item_more")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_send_another_link_dialog(self):
        '''
        This is a verification method to check UI strings of Send Another Link dialog
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings Send Another Link dialog")
#         assert self.get_value_of_send_another_link_dialog_contents_1() == u""
#         assert self.get_value_of_send_another_link_dialog_contents_2() == u""
#         assert self.get_value_of_send_another_link_btn() == u""
#         assert self.get_value_of_done_btn() == u""

    def verify_send_another_link_items(self):
        '''
        This is a verification method to check UI strings of menu items after clicking Send Another Link button.
        :parameter:
        :return:
        '''
        self.click_send_another_link_btn()
        logging.debug("Start to check UI strings menu items after clicking Send Another Link button")
#         assert self.get_value_of_items_1() == u""
#         assert self.get_value_of_items_2() == u""
#         assert self.get_value_of_items_3() == u""
#         assert self.get_value_of_items_4() == u""
#         assert self.get_value_of_items_5() == u""
