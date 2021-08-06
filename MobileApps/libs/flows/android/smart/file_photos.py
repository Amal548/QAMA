import logging
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from SAF.decorator.saf_decorator import screenshot_capture


class FilePhotos(SmartFlow):
    flow_name = "files_photos"

    PDF_TXT = "pdfs_txt"
    MY_PHOTOS_TXT = "my_photos_txt"
    GOOGLE_DRIVE_TXT = "google_drive_txt"
    DROPBOX_TXT = "dropbox_txt"
    FACEBOOK_TXT = "facebook_txt"
    INSTAGRAM_TXT = "instagram_txt"
    GOOGLE_PHOTOS_TXT = "google_photos_txt"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_local_item(self, item_name):
        """
        Click on PDFs/Scanned Files/My Photos
        :param item_name: local item's name. Use class constant:
            - PDF_TXT
            - MY_PHOTOS_TXT
        """
        item_name = self.get_text_from_str_id(item_name)
        self.driver.wait_for_object("item_name",
                                    format_specifier=[item_name],
                                    timeout=10, clickable=True)
        self.driver.click("item_name", format_specifier=[item_name], change_check={"wait_obj": "title", "invisible": True})

    #Todo: After updating GA, if it is not used by GA, merge it with select_local_item()
    def select_cloud_item(self, item_name):
        """
        Click on Google Drive/ Dropbox/Facebook/Instagram
        :param item_name: cloud item's name. Use class constant:
            - GOOGLE_DRIVE_TXT
            - DROPBOX_TXT
            - FACEBOOK_TXT
            - INSTAGRAM_TXT
            - GOOGLE_PHOTOS_TXT
        """
        item_name = self.get_text_from_str_id(item_name)
        self.driver.scroll("item_name", format_specifier=[item_name], full_object=False, check_end=False)
        self.driver.click("item_name", format_specifier=[item_name], change_check={"wait_obj": "title", "invisible": True})

    def load_logout_popup(self, cloud_item_name):
        """
        Load logout popup for cloud item
        :param cloud_item_name: cloud item's name. Use class constant:
            - GOOGLE_DRIVE_TXT
            - DROPBOX_TXT
            - FACEBOOK_TXT
            - INSTAGRAM_TXT
            - GOOGLE_PHOTOS_TXT
        """
        self.driver.scroll(cloud_item_name, full_object=False,  click_obj=False)
        self.driver.long_press(cloud_item_name)

    def logout_cloud_item(self, cloud_item_name):
        """
        Pre-condition: log out popup should be displayed
        Log out cloud's item name
        :param cloud_item_name: cloud item's name. Use class constant:
            - GOOGLE_DRIVE_TXT
            - DROPBOX_TXT
            - FACEBOOK_TXT
            - INSTAGRAM_TXT
            - GOOGLE_PHOTOS_TXT
        """
        self.driver.wait_for_object("logout_btn", timeout=10, clickable=True)
        self.driver.click("logout_btn")
        self.driver.wait_for_object("removed_acc_toast_msg",
                                    format_specifier=["{} {}".format(self.driver.return_str_id_value(cloud_item_name),
                                                                     self.driver.return_str_id_value(
                                                                         "successfully_remove_txt"))],
                                    timeout=10, raise_e=False)


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    @screenshot_capture(file_name="photos_screen.png")
    def verify_files_photos_screen(self, raise_e=True):
        """
        Verify current screen is Files and Photos screen via:
            - Title
            - Text of 2 headers of each group buttons
        :return:
        """
        return self.driver.wait_for_object("title", raise_e=raise_e) is not False \
               and self.driver.scroll("all_files_photos_txt", "up", timeout=10, full_object=False, raise_e=raise_e) is not False


    def verify_add_acc_txt(self, invisible=False):
        """
        Verify "Add Account" text invisible/visible
        :param invisible:
        """
        self.driver.wait_for_object("add_accounts_txt", timeout=10, invisible=invisible)

    def verify_local_files_photos_btns(self):
        """
        Verify displayed PDFs, and My Photos buttons
        """
        self.driver.wait_for_object("pdfs_txt", timeout=10)
        self.driver.wait_for_object("my_photos_txt", timeout=10)

    def verify_cloud_added_account(self, cloud_name, acc_name):
        """
        Verify the account of cloud  is added
        :param cloud_name: cloud name. Use class constant variable
                            - GOOGLE_DRIVE_TXT
                            - DROPBOX_TXT
                            - FACEBOOK_TXT
                            - INSTAGRAM_TXT
                            - GOOGLE_PHOTOS_TXT
        :param acc_name: account name (usually, it is user name, except Facebook - use name)
        """
        target_item_name = self.driver.return_str_id_value(cloud_name)
        acc_name = u"{}".format(acc_name)
        self.driver.wait_for_object("title")
        # order of dynamic value for item acc _name is [acc name, cloud name]
        self.driver.scroll("item_acc_name", format_specifier=[acc_name, target_item_name], timeout=10, full_object=False, check_end=False)

    def verify_cloud_not_login(self, cloud_name, raise_e=True):
        """
        Verify a cloud item is not logged in. "Log in" text under cloud name
        :param cloud_name: cloud name. Use class constant variable
                            - GOOGLE_DRIVE_TXT
                            - DROPBOX_TXT
                            - FACEBOOK_TXT
                            - INSTAGRAM_TXT
                            - GOOGLE_PHOTOS_TXT
        """
        try:
            self.verify_cloud_added_account(cloud_name, self.driver.return_str_id_value("login_txt"))
            return True
        except NoSuchElementException as ex:
            if raise_e:
                raise ex
            return False

    def verify_logout_popup(self):
        """
        Verify current popup is for logout of a cloud item
        """
        self.driver.wait_for_object("logout_btn")
