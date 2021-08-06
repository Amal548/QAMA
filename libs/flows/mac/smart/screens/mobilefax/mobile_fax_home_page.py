# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Mobile Fax Home page.

@author: Ivan
@create_date: Jan 3, 2020
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException


class MobileFaxHomePage(SmartScreens):

    folder_name = "mobilefax"
    flow_name = "mobile_fax_home_page"

    def __init__(self, driver):
        super(MobileFaxHomePage, self).__init__(driver)

# -------------------------------Operate Elements--------------------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax Home page screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("compose_fax_menu", timeout=timeout, raise_e=raise_e)

    def wait_for_invalid_format_error_message(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Invalid format error message after input a invalid phone.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_invalid_format_error_message]-Wait for screen loading... ")

        return self.driver.wait_for_object("invalid_format_error_text", timeout=timeout, raise_e=raise_e)

    def wait_for_media_tab_file_added_successful(self, timeout=30, raise_e=True):
        '''
        This is a method to wait File name load correctly after added the file.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_media_tab_file_added_successful]-Wait for File name loading... ")

        return self.driver.wait_for_object("media_tab_added_file_name", timeout=timeout, raise_e=raise_e)

    def wait_for_compose_fax_recipient_tab_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax Recipient tab page shows correctly under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_compose_fax_recipient_tab_page_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("recipient_tab_contact_icon", timeout=timeout, raise_e=raise_e)

    def wait_for_compose_fax_sender_tab_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax Sender tab page shows correctly under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_compose_fax_sender_tab_page_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("sender_tab_business_name_text_field", timeout=timeout, raise_e=raise_e)

    def wait_for_compose_fax_media_tab_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax Media tab page shows correctly under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_compose_fax_media_tab_page_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("media_tab_add_your_files_text", timeout=timeout, raise_e=raise_e)

    def wait_for_media_tab_file_picker_dialog_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax Media tab File picker dialog shows correctly under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_media_tab_file_picker_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("media_tab_file_picker_cancel_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_compose_fax_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Compose Fax page shows correctly under Compose Fax home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_compose_fax_page_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("recipient_tab_to", timeout=timeout, raise_e=raise_e)

    def wait_for_sent_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Sent page shows correctly under Compose Fax home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_sent_page_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("empty_sent_faxes_title", timeout=timeout, raise_e=raise_e)

    def wait_for_empty_sent_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Sent page without sent history shows correctly under Compose Fax home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_empty_sent_page_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("empty_sent_faxes_title", timeout=timeout, raise_e=raise_e)

    def wait_for_fax_delivered_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Fax Delivered  page load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_fax_delivered_page_load]-Wait for Fax Delivered page loading... ")

        return self.driver.wait_for_object("fax_delivered_text", timeout=timeout, raise_e=raise_e)

    def wait_for_fax_delivered_successful_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Fax Delivered Successful page load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_fax_delivered_page_load]-Wait for Fax Delivered successful page loading... ")

        return self.driver.wait_for_object("finished_time_text", timeout=timeout, raise_e=raise_e)

    def wait_for_fax_delivered_failed_page_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Fax Delivered Failed page load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[wait_for_fax_delivered_failed_page_load]-Wait for Fax Delivered failed page loading... ")

        return self.driver.wait_for_object("fax_delivered_failed_error_message_link", timeout=timeout, raise_e=raise_e)

    def click_recipient_tab(self):
        '''
        This is a method to click Recipient tab under Compose Fax menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_recepient_tab]-Click to Recipient tab under Compose Fax menu... ")

        self.driver.click("recipient_tab_to", is_native_event=True)

    def click_compose_fax_menu(self):
        '''
        This is a method to click Compose Fax menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_compose_fax_menu]-Click Compose Fax menu... ")

        self.driver.click("compose_fax_menu", is_native_event=True)

    def click_sent_menu(self):
        '''
        This is a method to click Sent menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_sent_menu]-Click Sent menu... ")

        self.driver.click("sent_menu", is_native_event=True)

    def click_drafts_menu(self):
        '''
        This is a method to click Drafts menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_drafts_menu]-Click Drafts menu... ")

        self.driver.click("drafts_menu", is_native_event=True)

    def click_fax_settings_menu(self):
        '''
        This is a method to click Fax Settings menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_fax_settings_menu]-Click Fax Settings menu... ")

        self.driver.click("fax_settings_menu", is_native_event=True)

    def choose_country_listitems_recipient_tab(self, country_index):
        '''
        This is a method to choose any option in country DropDown list under Recipient tab.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[choose_country_dropdown_listitems]-choose any option in country drop down list... ")

#         self.driver.click("recipient_tab_selected_phone_country_name", is_native_event=True)
        self.driver.choose_combo_box_options("recipient_tab_selected_phone_country_name", "recipient_tab_phone_country_list_items", option_index=country_index, is_scroll=True)
#         self.driver.click("recipient_tab_selected_phone_country_name", is_native_event=True)
#         sleep(1)
#         returnvalue = self.driver.click("recipient_tab_phone_country_list_items", format_specifier=[country_index], is_native_event=True, raise_e=False)
#         if(not returnvalue):
#             # TODOList
#             self.driver.click("recipient_tab_phone_country_list_items", format_specifier=[country_index], is_native_event=True)

    def recipient_tab_fax_number_input(self, contents):
        '''
        This is a method to input Fax number into textfield under Recipient tab
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[recipient_tab_fax_number_input]-Input Fax Number... ")

        self.driver.send_keys("recipient_tab_fax_number_text_field", contents, press_enter=True)

    def click_recipient_tab_fax_number(self):
        '''
        This is a method to click Fax number on Recipient tab under Compose Fax menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_recipient_tab_fax_number]-Click Fax number on Recipient tab under Compose Fax menu... ")

        self.driver.click("recipient_tab_fax_number_text_field", is_native_event=True)

    def clear_recipient_tab_fax_number_input(self):
        '''
        This is a method to clear enter contents in textfield under Recipient tab
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[clear_recipient_tab_fax_number_input]-clear enter contents... ")

        self.driver.clear_text("recipient_tab_fax_number_text_field")

    def recipient_tab_name_input(self, contents):
        '''
        This is a method to input Fax Name into textfield under Recipient tab
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[recipient_tab_name_input]-Input Fax Name... ")

        self.driver.send_keys("recipient_tab_name_text_filed", contents, press_enter=True)

    def click_recipient_tab_contact_icon(self):
        '''
        This is a method to click Sender tab under Compose Fax menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_recipient_tab_contact_icon]-Click to Contact icon under Recipient tab... ")

        self.driver.click("recipient_tab_contact_icon", is_native_event=True)

    def click_sender_tab(self):
        '''
        This is a method to click Sender tab under Compose Fax menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_sender_tab]-Click to Sender tab under Compose Fax menu... ")

        self.driver.click("sender_tab_from", is_native_event=True)

    def choose_phone_country_listitems_sender_tab(self, country_index):
        '''
        This is a method to choose any option in phone country DropDown list under Sender tab.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[choose_phone_country_listitems_sender_tab]-choose any option in phone country drop down list... ")

        self.driver.choose_combo_box_options("sender_tab_selected_phone_country_name", "sender_tab_phone_country_list_items", option_index=country_index, is_scroll=True)

#         self.driver.click("sender_tab_selected_phone_country_name", is_native_event=True)
#         sleep(1)
#         returnvalue = self.driver.click("sender_tab_phone_country_list_items", format_specifier=[country_index], is_native_event=True, raise_e=False)
#         if(not returnvalue):
#             # TODOList
#             self.driver.click("sender_tab_phone_country_list_items", format_specifier=[country_index], is_native_event=True)

    def click_sender_tab_fax_number(self):
        '''
        This is a method to click Fax number on Sender tab under Compose Fax menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_sender_tab_fax_number]-Click Fax number on Sender tab under Compose Fax menu... ")

        self.driver.click("sender_tab_phone_number_text_field", is_native_event=True)

    def clear_sender_tab_phone_number_input(self):
        '''
        This is a method to clear enter contents in textfield under Sender tab
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[clear_sender_tab_phone_number_input]-clear enter contents... ")

        self.driver.clear_text("sender_tab_phone_number_text_field")

    def sender_tab_phone_number_input(self, contents):
        '''
        This is a method to input Phone number into text-field under Sender tab
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[sender_tab_phone_number_input]-Input Phone Number... ")

        self.driver.send_keys("sender_tab_phone_number_text_field", contents, press_enter=True)

    def click_sender_tab_name(self):
        '''
        This is a method to click Fax name on Sender tab under Compose Fax menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_sender_tab_name]-Click Fax name on Sender tab under Compose Fax menu... ")

        self.driver.click("sender_tab_name_text_field", is_native_event=True)

    def sender_tab_name_input(self, contents):
        '''
        This is a method to input Name into text-field under Sender tab
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[sender_tab_phone_number_input]-Input Name... ")

        self.driver.send_keys("sender_tab_name_text_field", contents, press_enter=True)

    def sender_tab_business_name_input(self, contents):
        '''
        This is a method to input Business Name into text-field under Sender tab
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[sender_tab_business_name_input]-Input Business Name... ")

        self.driver.send_keys("sender_tab_business_name_text_field", contents, press_enter=True)

    def sender_tab_email_input(self, contents):
        '''
        This is a method to input Email into text-field under Sender tab
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[sender_tab_email_input]-Input Email... ")

        self.driver.send_keys("sender_tab_email_text_field", contents, press_enter=True)

    def choose_fax_country_listitems_sender_tab(self, country_index):
        '''
        This is a method to choose any option in fax country DropDown list under Sender tab.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[choose_fax_country_listitems_sender_tab]-choose any option in fax country drop down list... ")

        self.driver.click("sender_tab_selected_fax_country_name", is_native_event=True)
        sleep(1)
        returnvalue = self.driver.click("sender_tab_fax_country_list_items", format_specifier=[country_index], is_native_event=True, raise_e=False)
        if not returnvalue:
            # TODOList
            self.driver.click("sender_tab_fax_country_list_items", format_specifier=[country_index], is_native_event=True)

    def sender_tab_fax_number_input(self, contents):
        '''
        This is a method to input Fax Number into text-field under Sender tab
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[sender_tab_fax_number_input]-Input Fax Number... ")

        self.driver.send_keys("sender_tab_fax_number_text_field", contents, press_enter=True)

    def click_media_tab(self):
        '''
        This is a method to click Media tab under Compose Fax menu on Mobile Fax Home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_sender_tab]-Click to Media tab under Compose Fax menu... ")

        self.driver.click("media_tab_files_and_cover_page", is_native_event=True)

    def click_media_tab_add_a_cover_page_check_box(self):
        '''
        This is a method to click Add a cover page check-box under Media tab on Compose Fax menu.
        :parameter:
        :return:
        '''
        logging.debug("[CheckforupdatesDialog:[click_media_tab_add_a_cover_page_check_box]-Click Add a cover page check-box... ")

        self.driver.check_box("media_tab_add_a_cover_page_check_box")

    def click_media_tab_files_and_photos(self):
        '''
        This is a method to click Files & Photos item under Media tab on Compose Fax menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_media_tab_files_and_photos]-Click Files & Photos item... ")

        self.driver.click("media_tab_files_and_photos", is_native_event=True)

    def media_tab_input_searched_file_name(self, file_name):
        '''
        This is a method to input Searched file name into search text-field on File Picker dialog.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[sender_tab_fax_number_input]-Input searched file name... ")

        self.driver.send_keys("media_tab_file_picker_search_text_field", file_name, press_enter=True)

    def select_media_tab_file_picker_searched_file(self):
        '''
        This is a method to select the searched file on File Picker dialog after clicking Files and Photos option under Media tab on Compose Fax menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[select_media_tab_file_picker_searched_file]-Select the searched file... ")

        self.driver.click("media_tab_file_picker_searched_item", is_native_event=True)

    def click_media_tab_file_picker_cancel_btn(self):
        '''
        This is a method to click Cancel button on File Picker dialog after clicking Files and Photos option under Media tab on Compose Fax menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_media_tab_file_picker_cancel_btn]-Click Cancel button... ")

        self.driver.click("media_tab_file_picker_cancel_btn", is_native_event=True)

    def click_media_tab_file_picker_open_btn(self):
        '''
        This is a method to click Open button on File Picker dialog after clicking Files and Photos option under Media tab on Compose Fax menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_media_tab_file_picker_open_btn]-Click Open button... ")

        self.driver.click("media_tab_file_picker_open_btn", is_native_event=True)

    def click_media_tab_scanner(self):
        '''
        This is a method to click Scanner item under Media tab on Compose Fax menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_media_tab_scanner]-Click Scanner item... ")

        self.driver.click("media_tab_scanner", is_native_event=True)

    def click_delete_this_fax_btn(self):
        '''
        This is a method to click Delete this Fax button on Sent menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_delete_this_fax_btn]-Click Delete this Fax button... ")

        self.driver.click("delete_this_fax_btn", is_native_event=True)

    def click_export_fax_report_btn(self):
        '''
        This is a method to click Export Fax Report button on Sent menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_export_fax_report_btn]-Click Export Fax Report button... ")

        self.driver.click("export_fax_report_btn", is_native_event=True)

    def click_duplicate_and_edit_btn(self):
        '''
        This is a method to click Duplicate And Edit button on Sent menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_export_fax_report_btn]-Click Duplicate And Edit button... ")

        self.driver.click("duplicate_and_edit_btn", is_native_event=True)

    def click_send_fax_btn(self):
        '''
        This is a method to click Send Fax button on Compose Fax menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[click_send_fax_btn]-Click Send Fax button... ")

        self.driver.click("send_fax_btn", is_native_event=True)

    def get_value_of_compose_fax_menu(self):
        '''
        This is a method to get value of Compose Fax menu on Mobile Fax home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_compose_fax_menu] - Get value of Compose Fax menu...  ")

        return self.driver.get_title("compose_fax_menu")

    def get_value_of_recipient_tab_selected_country_name(self):
        '''
        This is a method to get value of Selected country name on Mobile Fax Recipient tab page under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_recipient_tab_selected_country_name] - Get value of Selected country name...  ")

        return self.driver.get_value("recipient_tab_selected_phone_country_name")

    def get_value_of_recipient_tab_fax_number(self):
        '''
        This is a method to get value of Fax number on Mobile Fax Recipient tab page under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_recipient_tab_fax_number] - Get value of Fax number...  ")

        return self.driver.get_value("recipient_tab_fax_number_text_field")

    def get_value_of_recipient_tab_invalid_format_text(self):
        '''
        This is a method to get value of Invalid format error message after input a invalid phone into Recipient phone text field.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_recipient_tab_invalid_format_text] - Get value of Invalid format error message...  ")

        return self.driver.get_value("invalid_format_error_text")

    def get_value_of_recipient_tab_name(self):
        '''
        This is a method to get value of Name on Mobile Fax Recipient tab page under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_recipient_tab_name_text] - Get value of Name...  ")

        return self.driver.get_value("recipient_tab_name_text_filed")

    def get_value_of_sender_tab_selected_phone_country_name(self):
        '''
        This is a method to get value of Selected phone country name on Mobile Fax Sender tab page under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_sender_tab_selected_phone_country_name] - Get value of Selected phone country name...  ")

        return self.driver.get_value("sender_tab_selected_phone_country_name")

    def get_value_of_sender_tab_selected_fax_country_name(self):
        '''
        This is a method to get value of Selected Fax country name on Mobile Fax Sender tab page under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_sender_tab_selected_fax_country_name] - Get value of Selected Fax country name...  ")

        return self.driver.get_value("sender_tab_selected_fax_country_name")

    def get_value_of_media_tab_add_a_cover_page_text(self):
        '''
        This is a method to get value of Add a cover page text on Mobile Fax Media tab page under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_media_tab_add_a_cover_page_text] - Get value of Add a cover page text...  ")

        return self.driver.get_value("media_tab_add_a_cover_page_text")

    def get_value_of_media_tab_add_your_files_text(self):
        '''
        This is a method to get value of Add Your Files text on Mobile Fax Media tab page under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_media_tab_add_your_files_text] - Get value of Add Your Files text...  ")

        return self.driver.get_value("media_tab_add_your_files_text")

    def get_value_of_media_tab_files_and_photos(self):
        '''
        This is a method to get value of Files & Photos text on Mobile Fax Media tab page under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_media_tab_files_and_photos] - Get value of Files & Photos text...  ")

        return self.driver.get_value("media_tab_files_and_photos")

    def get_value_of_media_tab_scanner(self):
        '''
        This is a method to get value of Scanner text on Mobile Fax Media tab page under Compose Fax Menu.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_media_tab_scanner] - Get value of Scanner text...  ")

        return self.driver.get_value("media_tab_scanner")

    def get_value_of_sent_menu(self):
        '''
        This is a method to get value of Sent menu on Mobile Fax home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_sent_menu] - Get value of Sent menu...  ")

        return self.driver.get_title("sent_menu")

    def get_value_of_drafts_menu(self):
        '''
        This is a method to get value of Drafts menu on Mobile Fax home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_drafts_menu] - Get value of Drafts menu...  ")

        return self.driver.get_title("drafts_menu")

    def get_value_of_fax_settings_menu(self):
        '''
        This is a method to get value of Fax Settings menu on Mobile Fax home page.
        :parameter:
        :return:
        '''
        logging.debug("[MobileFaxHomePage]:[get_value_of_fax_settings_menu] - Get value of Fax Settings menu...  ")

        return self.driver.get_title("fax_settings_menu")

    def input_mobile_fax_recipient_information_flow(self, recipient_phone_num):
        '''
        This is a flow to input Recipient information on Compose Fax Page.
        :parameter: recipient_phone_num - Fax number input under Recipient tab
        :return:
        '''
        self.click_recipient_tab()
        self.click_recipient_tab_fax_number()
        self.clear_recipient_tab_fax_number_input()
        self.recipient_tab_fax_number_input(recipient_phone_num)
        sleep(1)

    def input_mobile_fax_sender_information_flow(self, sender_fax_number, sender_name):
        '''
        This is a flow to input Sender information on Compose Fax Page.
        :parameter: sender_fax_number - Fax number input under Sender tab
                    sender_name - Fax name input under Sender tab
        :return:
        '''
        self.click_sender_tab()
        self.click_sender_tab_fax_number()
        self.clear_sender_tab_phone_number_input()
        self.sender_tab_phone_number_input(sender_fax_number)
        self.click_sender_tab_name()
        self.sender_tab_name_input(sender_name)

    def mobile_fax_media_tab_files_photo_flow(self, file_name):
        '''
        This is a flow to add a supported file by clicking Files&Photo option under Media tab.
        :parameter:
        :return:
        '''
        self.click_media_tab()
        sleep(1)
        #self.click_media_tab()
        #sleep(1)
        self.verify_compose_fax_media_tab_page()
        self.click_media_tab_files_and_photos()
        self.wait_for_media_tab_file_picker_dialog_load(120)
        self.media_tab_input_searched_file_name(file_name)
        sleep(1)
        self.select_media_tab_file_picker_searched_file()
        self.click_media_tab_file_picker_open_btn()

    def click_send_fax_btn_on_compose_fax_page_flow(self):
        '''
        This is a flow to click Send Fax btn to send the mobile fax.
        :parameter:
        :return:
        '''
        self.wait_for_media_tab_file_added_successful(300)
        sleep(5)
        self.click_send_fax_btn()
        self.wait_for_fax_delivered_page_load(300)

# -------------------------------Verification Methods-------------------------------------------------
    def verify_mobile_fax_home_page(self):
        '''
        This is a verification method to check UI strings of Mobile Fax Home page.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load(300)
        logging.debug("Start to check UI strings of Mobile Fax Home Page")
#         assert self.get_value_of_compose_fax_menu() == u""
#         assert self.get_value_of_sent_menu() == u""
#         assert self.get_value_of_drafts_menu() == u""
#         assert self.get_value_of_fax_settings_menu() == u""

    def verify_invalid_format_error_message(self):
        '''
        This is a verification method to check UI strings of Invalid format error message after input a invalid phone.
        :parameter:
        :return:
        '''
        self.wait_for_invalid_format_error_message()
        logging.debug("Start to check UI strings of Invalid format error message")
#         assert self.get_value_of_recipient_tab_invalid_format_text() == u"Invalid Format"

    def verify_compose_fax_recipient_tab_page(self):
        '''
        This is a verification method to check UI strings of Mobile Fax Recipient tab page under Compose Fax menu.
        :parameter:
        :return:
        '''
        self.wait_for_compose_fax_recipient_tab_page_load()
        logging.debug("Start to check UI strings of Mobile Fax Recipient Tab Page")
#         assert self.get_value_of_recipient_tab_selected_country_name() == u""
#         assert self.get_value_of_recipient_tab_fax_number() == u""
#         assert self.get_value_of_recipient_tab_name() == u""

    def verify_compose_fax_sender_tab_page(self):
        '''
        This is a verification method to check UI strings of Mobile Fax Sender tab page under Compose Fax menu.
        :parameter:
        :return:
        '''
        self.wait_for_compose_fax_sender_tab_page_load()
        logging.debug("Start to check UI strings of Mobile Fax Recipient Tab Page")
#         assert self.get_value_of_sender_tab_selected_phone_country_name() == u""
#         assert self.get_value_of_sender_tab_selected_fax_country_name() == u""

    def verify_compose_fax_media_tab_page(self):
        '''
        This is a verification method to check UI strings of Mobile Fax Media Tab (Files and Cover Page) page under Compose Fax menu.
        :parameter:
        :return:
        '''
        self.wait_for_compose_fax_media_tab_page_load()
        logging.debug("Start to check UI strings of Mobile Fax Files and Cover Page")
#         assert self.get_value_of_media_tab_add_a_cover_page_text() == u""
#         assert self.get_value_of_media_tab_add_your_files_text() == u""
#         assert self.get_value_of_media_tab_files_and_photos() == u""
#         assert self.get_value_of_media_tab_scanner() == u""
