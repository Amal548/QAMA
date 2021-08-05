import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_01_Google_Drive_Account(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]

        # Define variables
        cls.gdrive_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        
    def test_01_login_google_drive_account(self):
        """
        Description: C11412831
         1. Load Smart App Home Screen
         2. Select View & Print navbar button
         3. Sign out of Google Drive account
          - there maybe no account to sign out of
         3. Sign into Google Drive account
        Expected Results:
         3. Verify Google Drive account is not signed in
         4. Verify Google Drive account is signed in
          - google drive is under All Files & Photos section
          - google drive username displayed
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if not self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT, raise_e=False):
            self.files_photos.load_logout_popup(self.files_photos.GOOGLE_DRIVE_TXT)
            self.files_photos.logout_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.online_docs.select_gdrive_gmail_account(self.gdrive_username)
        self.online_docs.allow_gdrive_access(raise_e=False)
        self.files_photos.verify_cloud_added_account(self.files_photos.GOOGLE_DRIVE_TXT, self.gdrive_username)
    
    def test_02_logout_google_drive_account(self):
        """
        Description: C11412836
         1. Load Smart App Home Screen
         2. Select View & Print navbar button
         3. Sign in to Google Drive account
          - there may already be an account signed in
         4. Logout of Google Drive account
        Expected Results:
         3. Verify Google Drive account is signed in
         4. Verify Google Drive account is not signed in
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT, raise_e=False):
            self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT)
            self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
            self.online_docs.select_gdrive_gmail_account(self.gdrive_username)
            self.online_docs.allow_gdrive_access(raise_e=False)
        self.files_photos.load_logout_popup(self.files_photos.GOOGLE_DRIVE_TXT)
        self.files_photos.logout_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT)

    def test_03_cancel_adding_google_drive_account(self):
        """
        Description: C17285939
         1. Load Smart App Home Screen
         2. Select View &  Print navbar button
         3. Sign out of Google Drive account
          - there may be no account to sign out of
         4. Select Google Drive
         5. Select cancel on "Choose Account" popup
        Expected Results:
         4. Verify "Choose Account" popup
          - title
          - ok button
          - cancel button
         5. Verify Files & Photos screen
         5. Verify no Google Drive account signed in
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if not self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT, raise_e=False):
            self.files_photos.load_logout_popup(self.files_photos.GOOGLE_DRIVE_TXT)
            self.files_photos.logout_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.online_docs.verify_gdrive_choose_account_popup()
        self.online_docs.select_gdrive_choose_account_cancel()
        self.files_photos.verify_files_photos_screen()
