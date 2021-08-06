import pytest
import logging
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_01_Files_Photos(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Defines flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]

        # Account
        cls.gmail_addr = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]

        # Define variable 
        cls.clouds_list = [cls.files_photos.GOOGLE_DRIVE_TXT,
                          cls.files_photos.DROPBOX_TXT,
                          cls.files_photos.FACEBOOK_TXT,
                          cls.files_photos.GOOGLE_PHOTOS_TXT]
        
        def clean_up_class():
            # Log out Dropbox before
            cls.fc.flow_dropbox_logout()

        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("from_source", ["photos_tile", "doc_tiles", "view_print_nav"])
    def test_01_files_photos_screen_via(self, from_source):
        """
        Description:
            1/ Load Home screen with user onboarding account
            2/ Click on Print Photos/Print Documents/View & Print nav button

        Expected Result:
            2/ Files and Photos screen
                - title
                - PDFs, Scanned Files, and My Photos
                - Google Drive, Dropbox, and Facebook with "Log in" as sub text
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        if from_source in ["photo_tiles", "doc_tiles"]:
            tile_name = self.driver.return_str_id_value(TILE_NAMES.PRINT_PHOTOS if from_source == "photo_tiles"
                                                        else TILE_NAMES.PRINT_DOCUMENTS)
            self.home.select_tile_by_name(tile_name)
        else:
            self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.__verify_files_photos_local_storage_btns()
        self.__verify_not_login_cloud_account(self.clouds_list)

    def test_02_files_photos_screen_with_logged_in_accounts(self):
        """
        Description:
            1/ Load Home screen with user onboarding account
            2/ Click on File icon
            3/ Login Google Drive and Instagram account
        Expected Result:
            2/ Files and Photos screen
                - title
                - PDFs, Scanned Files, and My Photos
                - Google Drive, Dropbox, Instagram, and Facebook with "Log in" as sub text
            3/ Files and Photos screen
                - title
                - PDFs, Scanned Files, and My Photos
                - Dropbox and Facebook with "Log in" as sub text
                - Google Drive and Instagram with user name as sub text.
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.__verify_files_photos_local_storage_btns()
        self.__verify_not_login_cloud_account(self.clouds_list)
        self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.online_docs.select_gdrive_gmail_account(self.gmail_addr)
        self.__verify_files_photos_local_storage_btns()
        self.files_photos.verify_cloud_added_account(self.files_photos.GOOGLE_DRIVE_TXT, self.gmail_addr)
        self.clouds_list.remove(self.files_photos.GOOGLE_DRIVE_TXT)
        self.__verify_not_login_cloud_account(self.clouds_list)

    # -----------------         PRIVATE FUNCTIONS       ---------------------------------
    def __verify_files_photos_local_storage_btns(self):
        """
        Verify files photos screen with buttons for local storage (PDFs, Scanned Files, and My Photos)
        """
        self.files_photos.verify_files_photos_screen()
        self.files_photos.verify_add_acc_txt()
        self.files_photos.verify_local_files_photos_btns()

    def __verify_not_login_cloud_account(self, cloud_list):
        """
        Verify all clouds in list are not loggeg in
        :param cloud_list: list of cloud name from constant of Files Photos
        """
        for cloud in cloud_list:
            self.files_photos.verify_cloud_not_login(cloud)
