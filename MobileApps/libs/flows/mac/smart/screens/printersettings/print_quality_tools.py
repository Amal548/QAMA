# encoding: utf-8
'''
Description: print quality tools screen

@author: ten
@create_date: Oct 29, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_setting_scroll import PrinterSettingScroll
# from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import ItemNotFoundException


class PrintQualityTools(PrinterSettingScroll, SmartScreens):

    folder_name = "printersettings"
    flow_name = "print_quality_tools"

    def __init__(self, driver):
        super(PrintQualityTools, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("print_quality_tools_title", timeout=timeout, raise_e=raise_e)

    def wait_for_align_printheads_dialog_title_display(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("align_printheads_dialog_title", timeout=timeout, raise_e=raise_e)

    def wait_for_unable_to_align_title_display(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("unable_to_align_title", timeout=timeout, raise_e=raise_e)

    def wait_for_busy_icon_display(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("busy_icon", timeout=timeout, raise_e=raise_e)

    def wait_for_alignment_complete_title_display(self, timeout=240, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("alignment_complete_title", timeout=timeout, raise_e=raise_e)

    def click_align_printheads_image(self):
        '''
        This is a method to click align_printheads_image
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[click_align_printheads_image]-Click align_printheads_image.. ")

        self.driver.click("align_printheads_image", is_native_event=True)

    def click_clean_printheads_image(self):
        '''
        This is a method to click clean_printheads_image
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[Click clean_printheads_image.. ")

        self.driver.click("clean_printheads_image", is_native_event=True)

    def click_print_scan_alignment_page_btn(self):
        '''
        This is a method to click print_scan_alignment_page_btn
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[-Click print_scan_alignment_page_btn.. ")

        self.driver.click("print_scan_alignment_page_btn")

    def click_close_btn(self):
        '''
        This is a method to click print_scan_alignment_page_btn
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[Click close_btn. ")

        self.driver.click("close_btn")

    def click_cancel_btn(self):
        '''
        This is a method to click cancel_btn
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[Click cancel_btn ")

        self.driver.click("cancel_btn")

    def click_next_btn(self):
        '''
        This is a method to click next_btn
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[-Click next_btn ")

        self.driver.click("next_btn")

    def click_back_arrow(self):
        '''
        This is a method to click back_btn
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[-Click back_btn ")

        self.driver.click("back_arrow")

    def click_back_btn(self):
        '''
        This is a method to click back_btn
        :parameter:
        :return:
        '''
        logging.debug("[print_quality_tools]:[-Click back_btn ")

        self.driver.click("back_btn")

    def get_value_of_close_btn_value(self):
        '''
        get_value_of_close_btn_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_close_btn_value-Get the contents of close_btn_value ...  ")

        return self.driver.get_title("close_btn")

    def get_value_of_align_printheads_dialog_title_value(self):
        '''
        get_value_of_align_printheads_dialog_title_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_align_printheads_dialog_title_value-Get the contents of align_printheads_dialog_title_value ...  ")

        return self.driver.get_value("align_printheads_dialog_title")

    def get_value_of_content_text_value(self):
        '''
        get_value_of_content_text_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_content_textvalue-Get the contents of content_text_value ...  ")

        return self.driver.get_value("content_text")

    def get_value_of_print_scan_alignment_page_btn_value(self):
        '''
        get_value_of_print_scan_alignment_page_btn_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_print_scan_alignment_page_btn_value-Get the contents of print_scan_alignment_page_btn_value ...  ")

        return self.driver.get_title("print_scan_alignment_page_btn")

    def get_value_of_next_btn_value(self):
        '''
        get_value_of_next_btn_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_next_btn_value-Get the contents of next_btn_value ...  ")

        return self.driver.get_title("next_btn")

    def get_value_of_scanning_title_value(self):
        '''
        get_value_of_scanning_title_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_scanning_title_value-Get the contents of scanning_title_value ...  ")

        return self.driver.get_value("scanning_title")

    def get_value_of_scanning_content_text_value(self):
        '''
        get_value_of_scanning_content_text_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_scanning_content_text_value-Get the contents of scanning_content_text_value ...  ")

        return self.driver.get_value("scanning_content_text")

    def get_value_of_no_available_text_value(self):
        '''
        get_value_of_no_available_text_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_no_available_text_value-Get the contents of no_available_text_value ...  ")

        return self.driver.get_value("no_available_text")

    def get_value_of_unable_to_align_title_value(self):
        '''
        get_value_of_unable_to_align_title_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_unable_to_align_title_value-Get the contents of unable_to_align_title_value ...  ")

        return self.driver.get_value("unable_to_align_title")

    def get_value_of_back_btn_value(self):
        '''
        get_value_of_back_btn_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_back_btn_value-Get the contents of back_btn_value ...  ")

        return self.driver.get_title("back_btn")

    def get_value_of_unable_to_align_content_value(self):
        '''
        get_value_of_unable_to_align_content_value
        :parameter:
        :return:
        '''
        logging.debug("[Alignment_Pattern_Choices_Dialog]:[get_value_of_unable_to_align_content_value-Get the contents of unable_to_align_content_value ...  ")

        return self.driver.get_value("unable_to_align_content")

#   -------------------------------Verification Methods------------------------------------
    def verify_alignment_complete_dialogue_disappear(self):
        '''
        verify_alignment_complete_dialogue_disappear
        :parameter:
        :return:
        '''
        logging.debug("verify_alignment_complete_dialogue_disappear")
        if self.driver.wait_for_object("alignment_complete_title", raise_e=False):
            raise UnexpectedItemPresentException("the screen still exists")
        return True   

    def verify_busy_disappear(self):
        '''
        verify_busy_disappear
        :parameter:
        :return:
        '''
        logging.debug("verify_busy_disappear")
        if self.driver.wait_for_object("busy_icon", raise_e=False):
            raise UnexpectedItemPresentException("the screen still exists")
        return True

    def verify_align_printheads_page1_ui_string(self):
        '''
        verify_align_printheads_page1_ui_string
        :parameter:
        :return:
        '''
        logging.debug("verify_align_printheads_page1__ui_string")
#         assert self.get_value_of_align_printheads_dialog_title_value() == u""
#         assert self.get_value_of_content_text_value() == u""
#         assert self.get_value_of_print_scan_alignment_page_btn_value() == u""
#         assert self.get_value_of_next_btn_value() == u""

    def verify_align_printheads_page2_ui_string(self):
        '''
        verify_align_printheads_page2_ui_string
        :parameter:
        :return:
        '''
        logging.debug("verify_align_printheads_page1__ui_string")
#         assert self.get_value_of_align_printheads_dialog_title_value() == u""
#         assert self.get_value_of_content_text_value() == u""
#         assert self.get_value_of_print_scan_alignment_page_btn_value() == u""
#         assert self.get_value_of_next_btn_value() == u""

    def verify_scanning_ui_string(self):
        '''
        verify_scanning_ui_string
        :parameter:
        :return:
        '''
        logging.debug("verify_scanning_ui_string")
#         assert self.get_value_of_scanning_title_value() == u""
#         assert self.get_value_of_scanning_content_text_value() == u""
        assert self.get_value_of_print_scan_alignment_page_btn_value() == "Cancel"

    def verify_alignment_complete_ui_string(self):
        '''
        verify_alignment_complete_ui_string
        :parameter:
        :return:
        '''
        logging.debug("verify_alignment_complete_ui_string")
        assert self.get_value_of_scanning_title_value() == "Alignment complete"
        assert self.get_value_of_scanning_content_text_value() == "Alignment completed successfully. This will help to ensure the best possible print quality."
        assert self.get_value_of_close_btn_value() == "Close"

    def verify_no_available_ui_string(self):
        '''
        verify_no_available_ui_string
        :parameter:
        :return:
        '''
        logging.debug("verify_no_available_ui_string")
        assert self.get_value_of_no_available_text_value() == "This feature is not available for your selected printer through the HP Smart App. To perform print quality actions, use the full featured software, or see the printer's control panel."

    def verify_unable_to_align_screen(self):
        '''
        verify_alignment_pattern_choices_dialog_with_text_content
        :parameter:
        :return:
        '''
        logging.debug("verify_alignment_pattern_choices_dialog_with_text_content")
#         assert self.get_value_of_unable_to_align_title_value() == u""
#         assert self.get_value_of_unable_to_align_content_value() == u""
#         assert self.get_value_of_back_btn_value() == u""
    