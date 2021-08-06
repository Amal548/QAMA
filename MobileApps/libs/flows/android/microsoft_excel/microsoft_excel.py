import time
import logging

from MobileApps.libs.flows.android.microsoft_excel.microsoft_excel_flows import MicrosoftExcelFlow
from MobileApps.resources.const.android import const 
from selenium.common.exceptions import NoSuchElementException, WebDriverException

class MicrosoftExcel(MicrosoftExcelFlow):
    """
        Contains all of the elements and flows associated in Microsoft Excel
    """

    flow_name = "microsoft_excel"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################

    def open_excel(self):
        """
            Open Microsoft Excel App
        """
        try:
            self.driver.wdvr.start_activity(const.PACKAGE.MICROSOFT_EXCEL, const.LAUNCH_ACTIVITY.MICROSOFT_EXCEL, app_wait_activity = const.LAUNCH_ACTIVITY.MICROSOFT_EXCEL)
        except WebDriverException:
            self.check_run_time_permission()
        self.check_for_sign_in_screen_and_skip()
        if self.driver.wait_for_object("whats_new_in_excel_screen", timeout=5, raise_e=False):
            self.driver.click("whats_new_in_excel_screen")

    def check_for_sign_in_screen_and_skip(self, after_open_file=False):
        """
            Look for sign in screen and handle it by skipping
        """
        if not after_open_file:
            # For phones that DO NOT has any Google account signed in in android setting
            if self.driver.wait_for_object("sign_in_later_button", timeout=15, raise_e=False):
                self.driver.click("sign_in_later_button")
            elif self.driver.wait_for_object("enter_password_to_sign_in_screen", raise_e=False):
                self.driver.back()
                self.driver.wait_for_object("maybe_later_button", timeout=3).click()
            # Privacy notification
            if self.driver.wait_for_object("respect_your_privacy_screen", raise_e=False):
                self.driver.click("respect_your_privacy_screen")
                self.driver.wait_for_object("getting_better_together_screen", timeout=3).click()
                self.driver.wait_for_object("power_your_exp_screen", timeout=3).click()
        else: 
            if self.driver.wait_for_object("sign_in_screen_after_open_file", raise_e=False):
                self.driver.back()
            if self.driver.wait_for_object("add_to_home_screen_prompt", raise_e=False):
                self.driver.back()

    def look_for_excel_file_and_select(self):
        """
            Navigate to the storage of the local devices to open .xls file
        """
        self.select_open()
        self.select_this_device()
        self.select_storage()
        self.select_mobiauto()
        self.select_document()
        self.select_excel_file()
        self.agree_to_open_file_anyway()

    def select_open(self):
        """
            Select the open nav bar item in home
        """
        self.driver.click("open_nav_bar_item")

    def select_this_device(self):
        """
            Select the current device after selecting open nav bar item
        """
        self.driver.wait_for_object("this_device_option", timeout=3)
        self.driver.click("this_device_option", change_check={"wait_obj": "this_device_option", "invisible": True})

    def select_storage(self):
        """
            Select the storage of the devices after selecting this device
        """
        self.driver.wait_for_object("storage_option", timeout=3)
        self.driver.click("storage_option", change_check={"wait_obj": "documents_directory"})

    def select_mobiauto(self):
        """
            Select MobiAuto directory after selecting storage
        """
        self.driver.scroll("mobiauto_directory", direction="down")
        self.driver.click("mobiauto_directory", change_check={"wait_obj": "mobiauto_directory", "invisible": True})

    def select_document(self):
        """
            Select documents directory after selecting MobiAuto directory
        """
        self.driver.wait_for_object("documents_directory", timeout=3)
        self.driver.click("documents_directory", change_check={"wait_obj": "documents_directory", "invisible": True})

    def select_excel_file(self):
        """
            Search for excel file in the specified directory and select it
        """
        self.driver.scroll("xls_directory", direction="down")
        self.driver.wait_for_object("xls_directory", timeout=5)
        self.driver.click("xls_directory", change_check={"wait_obj": "xls_directory", "invisible": True})
        self.driver.wait_for_object("excel_file", timeout=5)
        self.driver.click("excel_file", change_check={"wait_obj": "excel_file", "invisible": True})

    def agree_to_open_file_anyway(self):
        """
            Handle if there's a warning message about unmatched file extension for the .xls file
        """
        if self.driver.wait_for_object("warning_message", timeout=5, raise_e=False):
            self.driver.click("yes_button")
        self.check_for_sign_in_screen_and_skip(after_open_file=True)

    def select_3_dot_button(self):
        """
            Select the 3 dot button after .xls is opened
        """
        self.driver.wait_for_object("3_dot_button", timeout=5).click()

    def select_print_in_3_dot_menu(self):
        """
            Select print when the menu (from selecting the 3 dot button) shows up
        """
        # Sometimes the menu disappears few seconds after the button is selected
        if self.driver.wait_for_object("print_option_in_3_dot_menu", invisible=True, timeout=5, raise_e=False):
            logging.debug("Failed to see menu after pressing the button, retrying......")
            self.driver.click("3_dot_button")
        self.driver.click("print_option_in_3_dot_menu")

    def select_print_in_print_options(self):
        """
            Select print button in the print options, which occurs after pressing the print option in 3 dot button menu
        """
        self.driver.wait_for_object("print_button_in_print_options", timeout=5)
        self.driver.click("print_button_in_print_options", change_check={"wait_obj": "print_button_in_print_options", "invisible": True})

########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_home_screen(self):
        """
            Verify for home screen of excel after skipping the sign in
        """
        self.driver.wait_for_object("open_nav_bar_item")

########################################################################################################################
#                                                                                                                      #
#                                                Guard Code                                                            #
#                                                                                                                      #
########################################################################################################################