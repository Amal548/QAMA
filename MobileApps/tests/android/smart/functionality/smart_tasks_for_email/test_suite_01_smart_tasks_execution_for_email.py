from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import TimeoutException
import datetime

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_01_Smart_Tasks_Execution_For_Email(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.smart_tasks = cls.fc.flow[FLOW_NAMES.SMART_TASKS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        # Define the variable
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        cls.dropbox_username = cls.fc.get_dropbox_acc()["username"]
        cls.dropbox_pwd = cls.fc.get_dropbox_acc()["password"]
        cls.pdf_fn = TEST_DATA.ONE_PAGE_PDF

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()
        # transfer file for testing
        cls.fc.transfer_test_data_to_device([cls.pdf_fn])

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()
            cls.fc.flow_home_delete_all_smart_tasks()

        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("file_source", ["pdf", "dropbox"])
    def test_01_execute_smart_tasks_with_single_email_through_files(self, file_source):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Click on Smart Tasks tile
          4. Create a new smart task with single email
          5. Select new smart task from step 4
          6. Select Files
          7. - If from PDFs, then select any files from PDFs screen
             - If from Dropbox, then select any files from Dropbox
          8. Click on Start button
          9. Click on HOME button on Smart Task upload complete screen

        Expected Result:
          4. Verify Smart Tasks source images or documents screen
             - Camera item
             - Files item
             - Photos item
             - Scanner item is invisible
          8. Verify Smart Task send success screen popup:
             - Message
             - Home button
          9. Verify Home screen
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, "dropbox", (datetime.datetime.now()))
        self.__load_smart_task_source_files_screen(smart_task_name, self.smart_tasks.FROM_FILES, invisible=True)
        if file_source == "pdf":
          # Android 7 has issue about read .pdf files from smart app. And won't be fixed based on comments on AIOA-7969
          if self.driver.driver_info['platformVersion'].split(".")[0] == "7":
            pytest.skip("Skip test this test suite on Android 7 as developer won't fix pdf files issue.")
          else:
            self.files_photos.select_local_item(self.files_photos.PDF_TXT)
            self.files.load_downloads_folder_screen()
            self.files.select_file(self.pdf_fn)
        else:
            self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
            self.fc.flow_dropbox_log_in(self.dropbox_username, self.dropbox_pwd)
            self.files_photos.verify_cloud_added_account(self.files_photos.DROPBOX_TXT, self.dropbox_username)
            self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
            self.online_docs.select_file("testdata_cloud/documents/pdf/1page.pdf")
        self.__verify_home_screen(smart_task_name)

    def test_02_execute_smart_tasks_with_email_through_photos(self):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Click on Smart Tasks tile
          4. Create a new smart task with single email
          5. Select new smart task from step 4
          6. Select Photo
          7. - If select images from My Photos folder
             - If select images from Instagram
          8. Click on Start button
          9. Click on HOME button on Smart Task upload complete screen

        Expected Result:
          4. Verify Smart Tasks source images or documents screen
             - Camera item
             - Files item
             - Photos item
             - Scanner item is invisible
          8. Verify Smart Task send success screen popup:
             - Message
             - Home button
          9. Verify Home screen
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, "my_photos", (datetime.datetime.now()))
        self.__load_smart_task_source_files_screen(smart_task_name, self.smart_tasks.FROM_PHOTOS, invisible=True)
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.photos.select_album_photo_by_index(album_name="jpg")
        self.__verify_home_screen(smart_task_name)

    def test_03_execute_smart_tasks_with_email_through_camera(self):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Click on Smart Tasks tile
          4. Create a new smart task with single email
          5. Select new smart task from step 4
          6. Select Camera
          7. Select Allow Access to Camera, and capture with manual mode
          8. Click on Start button
          9. Click on HOME button on Smart Task upload complete screen

        Expected Result:
          4. Verify Smart Tasks source images or documents screen
             - Camera item
             - Files item
             - Photos item
             - Scanner item is invisible
          8. Verify Smart Task send success screen popup:
             - Message
             - Home button
          9. Verify Home screen
        """
        smart_task_name = "{}_{}".format(self.udid, "camera_scan_single_email")
        self.__load_smart_task_source_files_screen(smart_task_name, self.smart_tasks.FROM_CAMERA, invisible=True)
        self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE)
        self.__verify_home_screen(smart_task_name)

    def test_04_execute_smart_tasks_with_email_through_scanner(self):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Click on Smart Tasks tile
          4. Create a new smart task with single email
          5. Select new smart task from step 4
          6. Select Scanner
          7. Select Scan button
          8. Click on Start button
          9. Click on HOME button on Smart Task upload complete screen

        Expected Result:
          8. Verify Smart Task send success screen popup:
             - Message
             - Home button
          9. Verify Home screen
        """
        smart_task_name = "{}_{}".format(self.udid, "scanner_single_email")
        self.__load_smart_task_source_files_screen(smart_task_name, self.smart_tasks.FROM_SCANNER, invisible=False, printer_obj=self.p)
        self.scan.select_scan()
        self.scan.verify_successful_scan_job()
        self.__verify_home_screen(smart_task_name)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_smart_task_source_files_screen(self, smart_task_name, source_type, invisible, printer_obj=None):
        """
        - Load Home screen.
        - CLick on Smart Tasks tile on Home screen
        - Click on CREATE NEW SMART TASKS button or "+"
        - Input new smart task name
        - Select Email on Create Smart Task screen
        - Enable and Save new smart task
        - Select this smart task
        :param smart_task_name
        :param source_type:
               - FROM_CAMERA
               - FROM_SCANNER
               - FROM_FILES
               - FROM_PHOTOS
        :param invisible: True or False for source file from Scanner
        """
        self.fc.flow_home_load_smart_task_screen(create_acc=False, printer_obj=printer_obj)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_email(to_email=self.email_address)
        self.smart_tasks.select_save_btn()
        try:
            self.smart_tasks.dismiss_smart_task_created_popup()
            self.smart_tasks.select_smart_task(smart_task_name)
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=False, btn_name=self.smart_tasks.START_THIS_SMART_TASK_BTN)
        self.smart_tasks.select_smart_task_source_type(source_type, invisible=invisible)

    def __verify_home_screen(self, smart_task_name):
        """
        - select a smart task.
        - click on start button
        - verify smart task upload complete screen
        - click on Home button
        - Verify Home screen
        """
        self.smart_tasks.check_run_time_permission()
        self.smart_tasks.verify_smart_tasks_list_screen(is_empty=False)
        self.smart_tasks.select_smart_task_from_preview_screen(smart_task_name)
        self.smart_tasks.dismiss_smart_tasks_complete_popup_screen()
        if self.home.verify_photomyne_awareness_popup(raise_e=False):
            self.home.dismiss_photomyne_awareness_popup()
        self.home.verify_home_nav()