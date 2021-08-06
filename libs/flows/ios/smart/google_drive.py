from time import sleep

from selenium.common.exceptions import TimeoutException
import logging
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class GoogleDrive(SmartFlow):
    flow_name = "google_drive"

    ########################################################################################################################
    #                                                                                                                      #
    #                                                  Action Flows
    #                                                                                                                      #
    ########################################################################################################################

    def sign_in_to_google_drive(self, email, password):
        """
        completes the entire google Drive log in process
        :return:
        """
        try:
            self.driver.click("sign_in_email_tf")
            self.driver.send_keys("sign_in_email_tf", email, press_enter=True)

            self.driver.click("sign_in_password_tf")
            self.driver.send_keys("sign_in_password_tf", password, press_enter=True)

        except TimeoutException:
            self.driver.click("mo_appandstuff_account_btn")
            try:
                self.driver.wait_for_object("sign_in_password_tf")
                self.driver.send_keys("sign_in_password_tf", password, press_enter=True)
            except TimeoutException:
                logging.info("Google Drive was not signed out.")

    def select_back(self):
        """
        selects the back arrow
        :return:
        """
        self.driver.click("back_btn")

    def select_allow(self):
        """
        selects the allow button
        :return:
        """
        self.driver.click("allow_btn")

    def go_to_a_folder_in_test_data_folder(self, file_type):
        """
        select folder in the google_drive.
        The folder structure in google drive account is arranged in this manner:
        test_data_folder/ documents/ pdf, docx, xls, etc.
        test_data_folder/ images/ jpg,png,tif, etc.
        """
        documents_subfolders = ["pdf", "doc", "docx", "xlsx", "xls", "ppt", "pptx", "txt", "html", ""]
        images_subfolders = ["jpg", "png", "heif", "tif", "ico", "bmp", "cur", "gif", "xbm"]
        folder_name = ""

        if file_type in documents_subfolders:
            folder_name = "documents"
        elif file_type in images_subfolders:
            folder_name = "images"
        self.verify_google_drive_files()
        self.driver.scroll("testdata_cloud_folder", click_obj=True)
        sleep(1)
        self.driver.scroll("_shared_dynamic_text", format_specifier=[folder_name], click_obj=True)
        sleep(1)
        self.driver.scroll("_shared_dynamic_text", format_specifier=[file_type], click_obj=True)
        sleep(1)

    ########################################################################################################################
    #                                                                                                                      #
    #                                                  Verification Flows
    #                                                                                                                      #
    ########################################################################################################################

    def verify_google_drive_login_screen(self, raise_e=True):
        """
        verify the googledrive pop from home screen
        :return:
        """
        return self.driver.wait_for_object("google_sign_in_txt", raise_e=raise_e)

    def verify_google_drive_files(self):
        """
        verify google drive screen opened
        :return:
        """
        self.driver.wait_for_object("google_drive_txt")

    def verify_google_drive_album(self):
        """
        verify that google Drive successfully loaded into HP Smart
        :return:
        """

        self.driver.wait_for_object("google_drive_txt")

########################################################################################################################
#                                                                                                                      #
#                                                  Functionality Related sets
#                                                                                                                      #
########################################################################################################################
