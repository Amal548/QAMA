# encoding: utf-8
'''
PrintFromOtherDevices screen

@author: ten
@create_date: July 25, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class PrintFromOtherDevices(SmartScreens):
    folder_name = "oobe"
    flow_name = "print_from_other_devices"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrintFromOtherDevices, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("send_link_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_send_link_menu_items_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[wait_for_send_link_menu_items_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("send_link_menu_item_email", timeout=timeout, raise_e=raise_e)

    def click_skip_sending_this_link_btn(self):
        '''
        This is a method to click Skip sending this link button on Print from other devices screen.
        '''
        logging.debug("[PrintFromOtherDevices]:[click_skip_sending_this_link_btn]-Click Skip sending this link button... ")

        self.driver.click("skip_sending_this_link_btn", is_native_event=True)

    def click_send_link_btn(self):
        '''
        This is a method to click Send link button on Print from other devices screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[click_send_link_btn]-Click Send link button... ")

        self.driver.click("send_link_btn", is_native_event=True)

    def select_email_menu_item(self):
        '''
        This is a method to select Email menu item after clicking Send link button on Print from other devices screen.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[select_email_menu_item]-Select Email menu item... ")

        self.driver.click("send_link_menu_item_email", is_native_event=True)

    def click_quit_btn(self):
        '''
        This is a method to click Quit button on Choose a mail account provider dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[click_quit_btn]-Click Quit button... ")

        self.driver.click("choose_a_mail_account_provider_dialog_quit_btn", is_native_event=True)

    def get_value_of_print_from_other_devices_title(self):
        '''
        This is a method to get value of Print from other devices screen title.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[get_value_of_print_from_other_devices_title]-Get the contents of print_from_other_devices_title...  ")

        return self.driver.get_value("print_from_other_devices_title")

    def get_value_of_print_from_other_devices_contents_1(self):
        '''
        This is a method to get value of Print from other devices screen Content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[get_value_of_print_from_other_devices_contents_1]-Get the contents of Print from other devices screen Content - 1...  ")

        return self.driver.get_value("print_from_other_devices_contents_1")

    def get_value_of_print_from_other_devices_contents_2(self):
        '''
        This is a method to get value of Print from other devices screen Content - 2.
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[get_value_of_print_from_other_devices_contents_2]-Get the contents of Print from other devices screen Content - 1...  ")

        return self.driver.get_value("print_from_other_devices_contents_2")

    def get_value_of_skip_sending_this_link_btn(self):
        '''
        This is a method to get value of Skip sending this link button on Print from other devices screen
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[get_value_of_skip_sending_this_link_btn]-Get the contents of Skip sending this link button...  ")

        return self.driver.get_title("skip_sending_this_link_btn")

    def get_value_of_send_link_btn(self):
        '''
        This is a method to get value of Send link button on Print from other devices screen
        :parameter:
        :return:
        '''
        logging.debug("[PrintFromOtherDevices]:[get_value_of_send_link_btn]-Get the contents of Send link button...  ")

        return self.driver.get_title("send_link_btn")

# -------------------------------Verification Methods-------------------------------------------------
    def verify_print_from_other_devices_screen(self):
        '''
        This is a verification method to check UI strings of Print from other devices screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        self.driver.wait_for_object("print_from_other_devices_image", timeout=10, raise_e=True)
        logging.debug("Start to check UI strings of Print from other devices screen")
#         assert self.get_value_of_print_from_other_devices_title()==u""
#         assert self.get_value_of_print_from_other_devices_contents_1()==u""
#         assert self.get_value_of_print_from_other_devices_contents_2()==u""
#         assert self.get_value_of_skip_sending_this_link_btn()==u""
#         assert self.get_value_of_send_link_btn()==u""
