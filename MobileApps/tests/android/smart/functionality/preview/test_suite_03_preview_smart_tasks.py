from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.resources.const.android.const import *

pytest.app_info = "SMART"

class Test_Suite_01_Preview_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # Android 7 has issue about read .pdf files from smart app. And won't be fixed based on comments on AIOA-7969
        if cls.driver.driver_info['platformVersion'].split(".")[0] == "7":
            pytest.skip("Skip test this test suite on Android 7 as developer won't fix pdf files issue.")

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.smart_tasks = cls.fc.flow[FLOW_NAMES.SMART_TASKS]

        # Define variables
        cls.pdf_fn = TEST_DATA.ONE_PAGE_PDF

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([cls.pdf_fn])

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

    def test_01_smart_tasks_sign_in_with_new_account(self):
        """
        Description:
        1. Load to Home screen
        2. Load to App Settings screen and login with a new HPID account
        3. Click on Print Document tile
        4. Click on PDF
        5. Select any .pdf file
        6. Click on Smart Tasks

        Expected Results:
        6. - Verify Smart Tasks screen:
             + Welcome to Smart Tasks! title
             + Sign In button is disappear
        """
        self.fc.flow_home_sign_in_hpid_account(create_acc=True)
        self.__select_file_from_home(file_name=self.pdf_fn)
        self.preview.select_bottom_nav_btn(self.preview.SMART_TASKS_BTN)
        self.smart_tasks.verify_smart_tasks_welcome_screen()

    def test_02_smart_tasks_sign_in_with_existed_account(self):
        """
        Description:
        1. Load to Home screen
        2. Load to App Settings screen and login to an existed HPID account login
        3. Click on Print Document tile
        4. Click on PDF
        5. Select any .pdf file
        6. Click on Smart Tasks

        Expected Results:
        6. Verify Smart Tasks list screen:
             + Smart Tasks list
        :param account_type:
        """
        self.fc.reset_app()
        self.fc.flow_home_sign_in_hpid_account(create_acc=False)
        self.__select_file_from_home(file_name=self.pdf_fn)
        self.preview.select_bottom_nav_btn(self.preview.SMART_TASKS_BTN)
        self.smart_tasks.verify_smart_tasks_list_screen(is_empty=False)

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __select_file_from_home(self, file_name=None):
        """
            - If current screen is not the "doc_type screen", then in Home screen:
                + CLick on Print Documents tile
                + Click on PDFs
            - Select a target file
        """
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_DOCUMENTS))
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(file_name)
        self.preview.verify_preview_nav(is_edit=False)