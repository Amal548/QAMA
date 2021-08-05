import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_02_Google_Drive_Printing(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME] 
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        # Define variables
        cls.gdrive_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.file_paths = {
            "pdf": "testdata_cloud/documents/pdf/1page.pdf",
            "png": "testdata_cloud/images/png/hp_logo.png",
            "jpg": "testdata_cloud/images/jpg/autumn.jpg",
            "jpeg": "testdata_cloud/images/jpeg/fish.jpeg"
        }

    @pytest.mark.parametrize("file_type", ["pdf", "png", "jpg", "jpeg"])
    def test_01_google_drive_printing(self, file_type):
        """
        Description: C11412834
         1. Load Smart App home screen
         2. Select View & Print navbar button
         3. Sign into Google Drive
          - may already be signed in
         4. Select Google Drive
         5. Navigate to the folder of the file_type
         6. Select a file
         7. Print
        Verification:
         7. Print is successful on app and printer
        """
        file_path = self.file_paths[file_type]
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT, raise_e=False):
            self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT)
            self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
            self.online_docs.select_gdrive_gmail_account(self.gdrive_username)
            self.online_docs.allow_gdrive_access(raise_e=False)
        self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.online_docs.select_file(file_path)
        self.fc.flow_preview_make_printing_job(self.p, is_edit=file_type is not "pdf")
