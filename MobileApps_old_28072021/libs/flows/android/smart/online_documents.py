from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from datetime import datetime
import logging
import time


class OnlineDocuments(SmartFlow):
    flow_name = "online_docs"
    GOOGLE_DRIVE_TXT = "google_drive_txt"
    DROPBOX_TXT = "dropbox_txt"
    ONEDRIVE_TXT = "onedrive_txt"

    # *********************************************************************************
    #                                GENERAL FLOWS                                    *
    # *********************************************************************************

    # ---------------------     ACTION FLOWS       ------------------------------------
    def select_more_opts(self):
        """
        Click on 3 dots icon button

        End of flow: option menu displays
        """
        self.driver.wait_for_object("more_options_btn")
        layout = self.driver.find_object("nav_btns_layout")
        self.driver.find_object("more_options_btn", root_obj=layout).click()

    def select_more_options_alphabetical(self):
        """

        From Cloud screen, click on Alphabetical button on More Options
        """
        self.driver.wait_for_object("opt_alphabetical_btn")
        self.driver.click("opt_alphabetical_btn")

    def select_more_options_date(self):
        """
        From Cloud screen, click on Date button on More Options
        """
        self.driver.wait_for_object("opt_date_btn")
        self.driver.click("opt_date_btn")

    def select_file(self, target_file):
        """
        Select a target file
        :param target_file: path of target file.
                 "test_cloud/documents/1page.pdf"
        """
        file_paths = target_file.split("/")
        logging.info("fname: {} - {}".format(file_paths, len(file_paths)))
        for fname in file_paths:
            logging.info("fname: {}".format(fname))
            # Wait for files list appeared because it takes time to load files
            self.driver.wait_for_object("files_lv")
            try:
                self.driver.scroll("file_name", format_specifier=[fname], full_object=False, timeout=30, check_end=False, click_obj=True)
            except StaleElementReferenceException:
                self.driver.click("file_name", format_specifier=[fname])
            self.driver.wait_for_object("progress_icon", invisible=True, timeout=30)
            # Retry to click on fname again if first click above faile
            if not self.driver.wait_for_object("file_name", format_specifier=[fname], invisible=True, raise_e=False):
                self.driver.click("file_name", format_specifier=[fname])
        logging.info("'{}' is selected successfully !!!".format(target_file))

    # ---------------------     VERIFICATION FLOWS       --------------------------------
    def verify_displayed_file_not_supported_txt(self):
        """
        Verify "File type not supported" display
        """
        self.driver.wait_for_object("not_supported_file_txt", timeout=10)

    def verify_online_docs_screen(self, cloud_name):
        """
        Verify current screen is file screen of a cloud
        :para cloud_name: cloud name. It is one of following class variables:
                GOOGLE_DRIVE_TXT
                DROPBOX_TXT
        :return:
        """
        self.driver.wait_for_object("files_lv", timeout=30)
        self.driver.wait_for_object(cloud_name, timeout=10)

    def verify_more_opts_menu(self):
        """
        Verify current popup of More Options menu of Online Docs:
            - Date
            - Alphabetical
        """
        self.driver.wait_for_object("opt_alphabetical_btn")
        self.driver.wait_for_object("opt_date_btn")

    def verify_sort_order(self, sort_by, sort_direction="ascending", timeout=30):
        """
        Verifies that the visible items in the document list are sorted based on the sort_by and sort_direction parameters.
        :param sort_by: "alphabet" or "date" based on sort type to be verified.
        :param sort_direction: Direction of sort, "ascending" or "descending"
        :param timeout: Seconds before timing out
        """
        if sort_direction not in ["ascending", "descending"]:
            raise ValueError('sort_direction = "{}" is not valid, must be "ascending" or "descending"'.format(sort_direction))
        if sort_by is "alphabet":
            ui_obj = "file_name_txt"
        elif sort_by is "date":
            ui_obj = "file_sub_txt"
        else:
            raise ValueError('sort_by = "{}" is not valid. sort_by must be one of ["alphabet", "date"]'.format(sort_by))
        root_obj = self.driver.wait_for_object('files_lv', timeout=timeout)
        elements = self.driver.find_object(ui_obj, multiple=True, root_obj=root_obj)
        sort_values = list()
        for element in elements:
            if sort_by is "alphabet" and len(element.text) > 0:
                sort_values.append(element.text)
            elif sort_by is "date":
                date_text = element.text.strip().split(" ")[-1].strip()
                try:
                    sort_values.append(datetime.strptime(date_text, "%m/%d/%Y"))  # expects date format mm/dd/yyyy
                except ValueError:
                    continue
        assert len(sort_values) >= 3, "Should have atleast 3 values for sort verification"
        if sort_direction is "ascending":
            assert all(sort_values[i] <= sort_values[i + 1] for i in range(len(sort_values) - 1)), "Expected values to be in {} order, {}".format(sort_direction, sort_values)
        else:
            assert all(sort_values[i] >= sort_values[i + 1] for i in range(len(sort_values) - 1)), "Expected values to be in {} order, {}".format(sort_direction, sort_values)

    # *********************************************************************************
    #                                GOOGLE DRIVE FLOWS                               *
    # *********************************************************************************

    # ---------------------     ACTION FLOWS       ------------------------------------
    def select_gdrive_gmail_account(self, gmail_address):
        """
        At Choose an account popup:
            - Click on target Gmail account
            - CLick on Ok button
        :param gmail_address:
        """
        self.driver.wait_for_object("choose_account_title", timeout=10)
        self.driver.click("acc_txt", format_specifier=[gmail_address])
        self.driver.wait_for_object("choose_account_popup_ok_btn")
        self.driver.click("choose_account_popup_ok_btn")

    def select_gdrive_choose_account_cancel(self):
        """
        Select cancel on the Google Drive Choose account popup
        """
        self.driver.wait_for_object("choose_account_popup_cancel_btn", timeout=10).click()

    def allow_gdrive_access(self, raise_e=True):
        """
        Selects allow on Google Drive consent screen
        """
        self.driver.wait_for_object("access_to_google_drive_allow_btn", raise_e=raise_e)
        self.driver.click("access_to_google_drive_allow_btn", raise_e=raise_e)

    # ---------------------     VERIFICATION FLOWS       ------------------------------
    def verify_gdrive_choose_account_popup(self):
        """
        Verify that current screen is 'Choose an account' via:
            - It's title
        """
        self.driver.wait_for_object("choose_account_title", timeout=10)
        self.driver.wait_for_object("choose_account_popup_ok_btn", timeout=10)
        self.driver.wait_for_object("choose_account_popup_cancel_btn", timeout=10)