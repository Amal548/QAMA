from selenium.common.exceptions import NoSuchElementException
from SAF.exceptions.saf_exceptions import ObjectFoundException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LocalFiles(SmartFlow):
    flow_name = "local_files"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def load_downloads_folder_screen(self):
        """
        Load Download folder screen
        """
        if not self.verify_downloads_folder_screen(raise_e=False):
            self.driver.click("drawer_menu_btn")
            self.driver.wait_for_object("drawer_layout", timeout=10)
            self.driver.click("drawer_item", format_specifier=[self.get_text_from_str_id("download_txt")],
                              change_check={"wait_obj": "drawer_item", "invisible": True,
                                            "format_specifier": [self.get_text_from_str_id("download_txt")]})
        self.verify_downloads_folder_screen()

    def select_file(self, file_name):
        """
        Select a file by file name
        :param file_name:
        """
        if not self.driver.scroll("file_name_title", format_specifier=[file_name], timeout=60, check_end=False, raise_e=False):
            self.driver.scroll("file_name_title", direction="up", format_specifier=[file_name], timeout=60, check_end=False)
        self.driver.click("file_name_title", format_specifier=[file_name], change_check={"wait_obj": "drawer_menu_btn", "invisible": True})

    def save_file_to_downloads_folder(self, file_name):
        """
        Save file to download folder:
            - Load Downloads folder
            - Change file name (including file extension, such as file_name.pdf)
            - Click on Save button
        :param file_name: file name, including file extension
        """
        self.load_downloads_folder_screen()
        self.driver.send_keys("file_name_edit_text", content=file_name)
        self.driver.click("save_btn", change_check={"wait_obj": "drawer_menu_btn", "invisible": True})

    # *********************************************************************************
    #                               VERIFICATION FLOWS                                *
    # *********************************************************************************

    def verify_downloads_folder_screen(self, invisible=False, raise_e=True):
        """
        Verify Downloads folder screen as current screen via
            - title
        """
        return self.driver.wait_for_object("title", format_specifier=[self.get_text_from_str_id("download_txt").lower()],
                                           timeout=10, raise_e=raise_e, invisible=invisible)
