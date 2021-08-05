# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on the Diagnose and Fix screen.

@author: Ivan
@create_date: Jul 29, 2020
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class DiagnoseFix(SmartScreens):
    folder_name = "psdr"
    flow_name = "diagnose_fix"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(DiagnoseFix, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
# -------------------Operation on Diagnose and Fix screen-------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Diagnose and Fix screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("diagnose_and_fix_screen_printer_image", timeout=timeout, raise_e=raise_e)

    def get_value_of_diagnose_and_fix_screen_title(self):
        '''
        This is a method to get value of Diagnose and Fix screen title.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_diagnose_and_fix_screen_title]-Get value of Diagnose and Fix screen title...  ")

        return self.driver.get_value("diagnose_and_fix_screen_title")

    def get_value_of_diagnose_and_fix_screen_printer_name(self):
        '''
        This is a method to get value of Printer name on Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_diagnose_and_fix_screen_printer_name]-Get value of Printer name...  ")

        return self.driver.get_value("diagnose_and_fix_screen_printer_name")

    def get_value_of_diagnose_and_fix_screen_content(self):
        '''
        This is a method to get value of Contents on Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_diagnose_and_fix_screen_content]-Get value of Contents...  ")

        return self.driver.get_value("diagnose_and_fix_screen_content")

    def get_value_of_diagnose_and_fix_screen_start_btn(self):
        '''
        This is a method to get value of Start button on Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_diagnose_and_fix_screen_start_btn]-Get value of Start button...  ")

        return self.driver.get_title("diagnose_and_fix_screen_start_btn")

    def click_diagnose_and_fix_screen_start_btn(self):
        '''
        This is a method to click Start button on Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_diagnose_and_fix_screen_start_btn]-Click Start button... ")

        self.driver.click("diagnose_and_fix_screen_start_btn", is_native_event=True)


# -------------------Operation on Diagnosing and Fixing screen-------------------
    def wait_for_diagnosing_and_fixing_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Diagnosing and Fixing screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[wait_for_diagnosing_and_fixing_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("diagnosing_and_fixing_screen_progress_indicator", timeout=timeout, raise_e=raise_e)

    def get_value_of_diagnosing_and_fixing_screen_title(self):
        '''
        This is a method to get value of Diagnosing and Fixing screen title.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_diagnosing_and_fixing_screen_title]-Get value of Diagnosing and Fixing screen title...  ")

        return self.driver.get_value("diagnose_and_fix_screen_title")

    def get_value_of_diagnosing_and_fixing_screen_printer_name(self):
        '''
        This is a method to get value of Printer name on Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_diagnosing_and_fixing_screen_printer_name]-Get value of Printer name...  ")

        return self.driver.get_value("diagnose_and_fix_screen_printer_name")

    def get_value_of_diagnosing_and_fixing_screen_content(self):
        '''
        This is a method to get value of Contents on Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_diagnosing_and_fixing_screen_content]-Get value of Contents...  ")

        return self.driver.get_value("diagnose_and_fix_screen_content")

    def get_value_of_diagnosing_and_fixing_screen_do_not_close_text(self):
        '''
        This is a method to get value of Do not close text on Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_diagnosing_and_fixing_screen_do_not_close_text]-Get value of Do not close text...  ")

        return self.driver.get_value("diagnosing_and_fixing_screen_do_not_close_text")


# -------------------Operation on Check Diagnose Complete screen (No issue found / Still having problems)-------------------
    def wait_for_no_issue_found_or_still_having_problems_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Check Diagnose Complete screen (No issue found) shows correctly after clicking Start button on Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[wait_for_no_issue_found_or_still_having_problems_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("no_issue_found_or_still_having_problems_printer_image", timeout=timeout, raise_e=raise_e)

    def get_value_of_no_issue_found_or_still_having_problems_printer_name(self):
        '''
        This is a method to get value of Printer name on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_printer_name]-Get value of Printer name button...  ")

        return self.driver.get_value("no_issue_found_or_still_having_problems_printer_name")

    def get_value_of_no_issue_found_or_still_having_problems_diagnosis_results_btn(self):
        '''
        This is a method to get value of Diagnosis Results button on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_diagnosis_results_btn]-Get value of Diagnosis Results button...  ")

        return self.driver.get_title("no_issue_found_or_still_having_problems_diagnosis_results_btn")

    def get_value_of_no_issue_found_or_still_having_problems_title_text(self):
        '''
        This is a method to get value of Diagnosis Complete text on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_title_text]-Get value of Diagnosis Complete text...  ")

        return self.driver.get_value("no_issue_found_or_still_having_problems_title_text")

    def get_value_of_no_issue_found_or_still_having_problems_get_fast_text(self):
        '''
        This is a method to get value of Get fast text on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_get_fast_text]-Get value of Get fast text...  ")

        return self.driver.get_value("no_issue_found_or_still_having_problems_get_fast_text")

    def get_value_of_no_issue_found_or_still_having_problems_chat_with_virtual_agent_link(self):
        '''
        This is a method to get value of Chat with Virtual Agent link on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_chat_with_virtual_agent_link]-Get value of Chat with Virtual Agent link...  ")

        return self.driver.get_title("no_issue_found_or_still_having_problems_chat_with_virtual_agent_link")

    def get_value_of_no_issue_found_or_still_having_problems_online_troubleshooting_link(self):
        '''
        This is a method to get value of Online Troubleshooting link on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_online_troubleshooting_link]-Get value of Online Troubleshooting link...  ")

        return self.driver.get_title("no_issue_found_or_still_having_problems_online_troubleshooting_link")

    def get_value_of_no_issue_found_or_still_having_problems_software_and_driver_downloads_link(self):
        '''
        This is a method to get value of Software and Driver Downloads link on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_software_and_driver_downloads_link]-Get value of Software and Driver Downloads link...  ")

        return self.driver.get_title("no_issue_found_or_still_having_problems_software_and_driver_downloads_link")

    def get_value_of_no_issue_found_or_still_having_problems_hp_support_forum_link(self):
        '''
        This is a method to get value of HP Support Forum link on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_hp_support_forum_link]-Get value of HP Support Forum link...  ")

        return self.driver.get_title("no_issue_found_or_still_having_problems_hp_support_forum_link")

    def get_value_of_no_issue_found_or_still_having_problems_test_print_btn(self):
        '''
        This is a method to get value of Test Print button on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_test_print_btn]-Get value of Test Print button...  ")

        return self.driver.get_title("no_issue_found_or_still_having_problems_test_print_btn")

    def get_value_of_no_issue_found_or_still_having_problems_done_btn(self):
        '''
        This is a method to get value of Done button on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_no_issue_found_or_still_having_problems_done_btn]-Get value of Done button...  ")

        return self.driver.get_title("no_issue_found_or_still_having_problems_done_btn")

    def click_no_issue_found_or_still_having_problems_diagnosis_results_btn(self):
        '''
        This is a method to click Chat with Diagnosis Results button on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_no_issue_found_or_still_having_problems_diagnosis_results_btn]-Click Diagnosis Results button... ")

        self.driver.click("no_issue_found_or_still_having_problems_diagnosis_results_btn", is_native_event=True)

    def click_no_issue_found_or_still_having_problems_chat_with_virtual_agent_link(self):
        '''
        This is a method to click Chat with Virtual Agent link on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_no_issue_found_or_still_having_problems_chat_with_virtual_agent_link]-Click Chat with Virtual Agent link... ")

        self.driver.click("no_issue_found_or_still_having_problems_chat_with_virtual_agent_link", is_native_event=True)

    def click_no_issue_found_or_still_having_problems_online_troubleshooting_link(self):
        '''
        This is a method to click Online Troubleshooting link on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_no_issue_found_or_still_having_problems_online_troubleshooting_link]-Click Online Troubleshooting link... ")

        self.driver.click("no_issue_found_or_still_having_problems_online_troubleshooting_link", is_native_event=True)

    def click_no_issue_found_or_still_having_problems_software_and_driver_downloads_link(self):
        '''
        This is a method to click Software and Driver Downloads link on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_no_issue_found_or_still_having_problems_software_and_driver_downloads_link]-Click Software and Driver Downloads link... ")

        self.driver.click("no_issue_found_or_still_having_problems_software_and_driver_downloads_link", is_native_event=True)

    def click_no_issue_found_or_still_having_problems_hp_support_forum_link(self):
        '''
        This is a method to click HP Support Forum link on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_no_issue_found_or_still_having_problems_software_and_driver_downloads_link]-Click HP Support Forum link... ")

        self.driver.click("no_issue_found_or_still_having_problems_hp_support_forum_link", is_native_event=True)

    def click_no_issue_found_or_still_having_problems_test_print_btn(self):
        '''
        This is a method to click Test Print button on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_no_issue_found_or_still_having_problems_test_print_btn]-Click Test Print button... ")

        self.driver.click("no_issue_found_or_still_having_problems_test_print_btn", is_native_event=True)

    def click_no_issue_found_or_still_having_problems_done_btn(self):
        '''
        This is a method to click Done button on Check Diagnose complete (No issue found / Still having problems) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_no_issue_found_or_still_having_problems_done_btn]-Click Done button... ")

        self.driver.click("no_issue_found_or_still_having_problems_done_btn", is_native_event=True)


# -------------------Operation on Check Diagnose Complete screen (Found issues and Fixed / Found issues and not fixed / Found issue and Failed)-------------------
    def wait_for_check_diagnose_complete_found_issues_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Check Diagnose Complete screen (Found issues) shows correctly after clicking Start button on Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[wait_for_check_diagnose_complete_found_issues_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("check_diagnose_complete_found_issues_printer_image", timeout=timeout, raise_e=raise_e)

    def get_value_of_check_diagnose_complete_found_issues_printer_name(self):
        '''
        This is a method to get value of Printer name on Check Diagnose complete (Found issues) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_check_diagnose_complete_found_issues_printer_name]-Get value of Printer name...  ")

        return self.driver.get_value("check_diagnose_complete_found_issues_printer_name")

    def get_value_of_check_diagnose_complete_found_issues_title_text(self):
        '''
        This is a method to get value of Diagnosis Complete text on Check Diagnose complete (Found issues) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_check_diagnose_complete_found_issues_title_text]-Get value of Diagnosis Complete text...  ")

        return self.driver.get_value("check_diagnose_complete_found_issues_title_text")

    def get_value_of_check_diagnose_complete_found_issues_content_text(self):
        '''
        This is a method to get value of Content text on Check Diagnose complete (Found issues) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_check_diagnose_complete_found_issues_content_text]-Get value of Content text...  ")

        return self.driver.get_value("check_diagnose_complete_found_issues_content_text")

    def get_value_of_check_diagnose_complete_found_issues_status_text(self):
        '''
        This is a method to get value of Status text on Check Diagnose complete (Found issues) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_check_diagnose_complete_found_issues_status_text]-Get value of Status text...  ")

        return self.driver.get_value("check_diagnose_complete_found_issues_status_text")

    def get_value_of_check_diagnose_complete_found_issues_done_or_test_print_or_try_again_btn(self):
        '''
        This is a method to get value of Done/Test Print/Try Again button on Check Diagnose complete (Found issues) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_check_diagnose_complete_found_issues_done_or_test_print_or_try_again_btn]-Get value of Done/Test Print/Try Again button...  ")

        return self.driver.get_title("check_diagnose_complete_found_issues_done_or_test_print_or_try_again_btn")

    def get_value_of_check_diagnose_complete_found_issues_test_print_or_next_btn(self):
        '''
        This is a method to get value of Test print/Next button on Check Diagnose complete (Found issues) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[get_value_of_check_diagnose_complete_found_issues_test_print_or_next_btn]-Get value of Test print/Next button...  ")

        return self.driver.get_title("check_diagnose_complete_found_issues_test_print_or_next_btn")

    def click_check_diagnose_complete_found_issues_done_or_test_print_or_try_again_btn(self):
        '''
        This is a method to click Done(Found issue and fixed)/Test Print(Found issue and not fixed)/Try Again (Found issue and Failed) button on Check Diagnose complete (Found issues) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_check_diagnose_complete_found_issues_done_or_test_print_or_try_again_btn]-Click Done/Test Print button... ")

        self.driver.click("check_diagnose_complete_found_issues_done_or_test_print_or_try_again_btn", is_native_event=True)

    def click_check_diagnose_complete_found_issues_test_print_or_next_btn(self):
        '''
        This is a method to click Test Print(Found issue and fixed)/Next(Found issue and not fixed) button on Check Diagnose complete (Found issues) screen.
        :parameter:
        :return:
        '''
        logging.debug("[DiagnoseFix]:[click_check_diagnose_complete_found_issues_test_print_or_next_btn]-Click Test Print/Next button... ")

        self.driver.click("check_diagnose_complete_found_issues_test_print_or_next_btn", is_native_event=True)


# -------------------------------Verification Methods--------------------------
    def verify_diagnose_and_fix_screen(self):
        '''
        This is a verification method to check UI strings of Diagnose and Fix screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Diagnose and Fix screen")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='diagnose_fix')
        assert self.get_value_of_diagnose_and_fix_screen_title() == test_strings['diagnose_fix']
        assert self.get_value_of_diagnose_and_fix_screen_content() == test_strings['diagnose_and_fix_content']
        assert self.get_value_of_diagnose_and_fix_screen_start_btn() == test_strings['start_btn']

    def verify_diagnosing_and_fixing_screen(self):
        '''
        This is a verification method to check UI strings of Diagnosing and Fixing screen.
        :parameter:
        :return:
        '''
        test_strings = smart_utility.get_local_strings_from_table(screen_name='diagnose_fix')
        if self.wait_for_diagnosing_and_fixing_screen_load(raise_e=False):
            logging.debug("Start to check UI strings of Diagnosing and Fixing screen")
            assert self.get_value_of_diagnosing_and_fixing_screen_content() == test_strings['fixing_screen_content']
            assert self.get_value_of_diagnosing_and_fixing_screen_do_not_close_text() == test_strings['do_not_close_text']

    def verify_check_diagnose_complete_screen_found_issue(self):
        '''
        This is a verification method to check UI strings of Check Diagnose Complete (Found issue) screen (Including Found issue and Fixed screen, Found issue and not fixed screen and Found issues and Failed screen)
        :parameter:
        :return:
        '''
        self.wait_for_check_diagnose_complete_found_issues_load(60)
        logging.debug("Start to check UI strings of Check Diagnose Complete screen (Found issue)")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='diagnose_fix')
        assert self.get_value_of_check_diagnose_complete_found_issues_title_text() == test_strings['issues_title_text']
        assert self.get_value_of_check_diagnose_complete_found_issues_content_text() == test_strings['issues_content_text']
        assert self.get_value_of_check_diagnose_complete_found_issues_status_text() == test_strings['issues_status_text']
        assert self.get_value_of_check_diagnose_complete_found_issues_done_or_test_print_or_try_again_btn() == test_strings['issues_done_or_test_print_or_try_again_btn']
        assert self.get_value_of_check_diagnose_complete_found_issues_test_print_or_next_btn() == test_strings['issues_test_print_or_next_btn']

    def verify_check_diagnose_complete_screen_found_issue_not_install(self):
        '''
        This is a verification method to check UI strings of Check Diagnose Complete (Found issue) screen (Including Found issue and Fixed screen, Found issue and not fixed screen and Found issues and Failed screen)
        :parameter:
        :return:
        '''
        self.wait_for_check_diagnose_complete_found_issues_load(60)
        logging.debug("Start to check UI strings of Check Diagnose Complete screen (Found issue)")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='diagnose_fix')
        assert self.get_value_of_check_diagnose_complete_found_issues_title_text() == test_strings['issues_title_text']
        assert self.get_value_of_check_diagnose_complete_found_issues_content_text() == test_strings['issues_content_text_2']
        assert self.get_value_of_check_diagnose_complete_found_issues_status_text() == test_strings['issues_status_text_2']
        assert self.get_value_of_check_diagnose_complete_found_issues_done_or_test_print_or_try_again_btn() == test_strings['done_btn']
        assert self.get_value_of_check_diagnose_complete_found_issues_test_print_or_next_btn() == test_strings['test_print_btn']
        
    def verify_check_diagnose_complete_screen_no_issue_found(self):
        '''
        This is a verification method to check UI strings of Check Diagnose Complete (No issue found) screen.
        :parameter:
        :return:
        '''
        self.wait_for_no_issue_found_or_still_having_problems_load(60)
        logging.debug("Start to check UI strings of Check Diagnose Complete screen (No issue found)")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='diagnose_fix')
        assert test_strings['no_issue_title_text_1'] and test_strings['no_issue_title_text_2'] in self.get_value_of_no_issue_found_or_still_having_problems_title_text()
        assert self.get_value_of_no_issue_found_or_still_having_problems_get_fast_text() == test_strings['get_fast_text']
        assert self.get_value_of_no_issue_found_or_still_having_problems_chat_with_virtual_agent_link() == test_strings['chat_with_virtual_agent_link']
        assert self.get_value_of_no_issue_found_or_still_having_problems_online_troubleshooting_link() == test_strings['online_troubleshooting_link']
        assert self.get_value_of_no_issue_found_or_still_having_problems_software_and_driver_downloads_link() == test_strings['software_and_driver_downloads_link']
        assert self.get_value_of_no_issue_found_or_still_having_problems_hp_support_forum_link() == test_strings['hp_support_forum_link']
        assert self.get_value_of_no_issue_found_or_still_having_problems_test_print_btn() == test_strings['test_print_btn']
        assert self.get_value_of_no_issue_found_or_still_having_problems_done_btn() == test_strings['done_btn']

    def verify_check_diagnose_complete_screen_still_having_problems(self):
        '''
        This is a verification method to check UI strings of Check Diagnose Complete (Still having problems) screen after clicking Next button on Found issue and not fixed screen.
        :parameter:
        :return:
        '''
        self.wait_for_no_issue_found_or_still_having_problems_load(60)
        logging.debug("Start to check UI strings of Check Diagnose Complete screen (Still having problems)")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='diagnose_fix')
        assert self.get_value_of_no_issue_found_or_still_having_problems_diagnosis_results_btn() == test_strings['diagnosis_results_btn']
        assert self.get_value_of_no_issue_found_or_still_having_problems_title_text() == test_strings['title_text']
        assert self.get_value_of_no_issue_found_or_still_having_problems_get_fast_text() == test_strings['get_fast_text']
        assert self.get_value_of_no_issue_found_or_still_having_problems_chat_with_virtual_agent_link() == test_strings['chat_with_virtual_agent_link']
        assert self.get_value_of_no_issue_found_or_still_having_problems_online_troubleshooting_link() == test_strings['online_troubleshooting_link']
        assert self.get_value_of_no_issue_found_or_still_having_problems_software_and_driver_downloads_link() == test_strings['software_and_driver_downloads_link']
        assert self.get_value_of_no_issue_found_or_still_having_problems_hp_support_forum_link() == test_strings['hp_support_forum_link']
        assert self.get_value_of_no_issue_found_or_still_having_problems_test_print_btn() == test_strings['test_print_btn']
        assert self.get_value_of_no_issue_found_or_still_having_problems_done_btn() == test_strings['done_btn']
