import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import logging

pytest.app_info = "SMART"


class Test_Suite_02_Google_Drive_UI(object):
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
    
    def test_01_verify_google_drive_screen(self):
        """
        Description: C11412833
         1. Launch Smart App home screen
         2. Select View & Print navbar button
         3. Sign into Google Drive
          - may already be signed in
         4. Select Google Drive
         5. Select "testdata_cloud" folder
        Expected Results:
         4. Verify Google Drive screen
          - title
          - back button
         5. Verify Google Drive screen
          - fulfills folder verification due to selecting folder in prior step
         5. Verify 3 dots icon
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT, raise_e=False):
            self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
            self.online_docs.select_gdrive_gmail_account(self.gdrive_username)
            self.online_docs.allow_gdrive_access(raise_e=False)
        self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.online_docs.verify_online_docs_screen(self.online_docs.GOOGLE_DRIVE_TXT)
        self.online_docs.select_file("testdata_cloud")
        self.online_docs.verify_online_docs_screen(self.online_docs.GOOGLE_DRIVE_TXT)
        self.online_docs.select_more_opts()

    def test_02_verify_google_drive_sorting(self):
        """
        Description: C17287516
         1. Launch Smart App home screen
         2. Select View & Print navbar button
         3. Sign into Google Drive
          - may already be signed in
         4. Select Google Drive
         5. Sort by Alphabetical(on 3 dots menu)
         6. Sort by Date(on 3 dots menu)
        Expected Results:
         5. Verify items are sorted alphabetically
         6. Verify items are sorted by date
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT, raise_e=False):
            self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
            self.online_docs.select_gdrive_gmail_account(self.gdrive_username)
            self.online_docs.allow_gdrive_access(raise_e=False)
        self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.online_docs.select_more_opts()
        self.online_docs.select_more_options_alphabetical()
        self.online_docs.verify_sort_order("alphabet", sort_direction="descending")
        # sort by date twice for descending order to bring items with dates to top
        self.online_docs.select_more_opts()
        self.online_docs.select_more_options_date()
        self.online_docs.select_more_opts()
        self.online_docs.select_more_options_date()
        self.online_docs.verify_sort_order("date", sort_direction="descending")
    
    @pytest.mark.parametrize("file_type", ["doc", "docx", "html", "ppt", "pptx", "txt", "xls", "xlsx", "bmp", "cur", "gif", "ico", "tif", "webp", "xbm"])
    def test_03_verify_file_type_not_supported(self, file_type):
        """
        Description: C11412835
         1. Launch Smart App home screen
         2. Select View & Print navbar button
         3. Sign into Google Drive
          - may already be signed in
         4. Select Google Drive
         5. Navigate to folder for specified file_type
        Expected Results:
         5. File not supported subtext appears under file of specified file_type
        """
        image_file_types = ["bmp", "cur", "tif", "gif", "ico", "webp", "xbm"]
        folder_path = ("testdata_cloud/images/" if file_type in image_file_types else "testdata_cloud/documents/") + file_type
        self.__load_view_print_with_google_drive()
        self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.online_docs.select_file(folder_path)
        self.online_docs.verify_displayed_file_not_supported_txt()

    def __load_view_print_with_google_drive(self):
        """
        Opens View and Print screen with Google Drive logged in
        1. Launch Smart app home screen
        2. Select View & Print navbar button
        3. if not already logged in sign into Google Drive account 
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT, raise_e=False):
            self.__load_google_drive_account()

    def __load_google_drive_account(self):
        """
        Signs into Google Drive account at Files & Photos screen
        """
        self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.online_docs.select_gdrive_gmail_account(self.gdrive_username)
        self.online_docs.allow_gdrive_access(raise_e=False)