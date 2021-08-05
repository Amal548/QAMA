from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import TimeoutException
import datetime
import time

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_01_Smart_Tasks_Execution_For_Saving(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.smart_tasks = cls.fc.flow[FLOW_NAMES.SMART_TASKS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]

        # Define the variable
        cls.udid = cls.driver.driver_info["desired"]["udid"]
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

    def test_01_execute_smart_tasks_with_saving_for_dropbox(self):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Smart Tasks screen
          4. Create a new smart task screen for saving with dropbox
          5. Start a smart task from step4
          6. Click Files, then select PDFs, and select a .pdf file from PDFs
          7. Click on Start button

        Expected Result:
          7. Verify the Smart Task complete popup
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, "from_photos", (datetime.datetime.now()))
        self.__load_smart_task_source_type_screen(smart_task_name, self.smart_tasks.SAVE_TO_DROPBOX, self.smart_tasks.FROM_FILES)
        # Android 7 has issue about read .pdf files from smart app. And won't be fixed based on comments on AIOA-7969
        if self.driver.driver_info['platformVersion'].split(".")[0] == "7":
            pytest.skip("Skip test this test suite on Android 7 as developer won't fix pdf files issue.")
        else:
            self.files_photos.select_local_item(self.files_photos.PDF_TXT)
            self.files.load_downloads_folder_screen()
            self.files.select_file(self.pdf_fn)
            self.__verify_home_screen(smart_task_name)

    @pytest.mark.parametrize("file_source", ["from_scanner", "from_photo"])
    def test_02_execute_smart_tasks_with_saving_for_googledrive(self, file_source):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Smart Tasks screen
          4. Create a new smart task screen for saving with dropbox
          5. Start a smart task from step4
          6. - Click Scanner, then select Scan
             - Click Photos, then select My Photo, and select a photo
          7. Click on Start button

        Expected Result:
          7. Verify the Smart Task complete popup
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, file_source, (datetime.datetime.now()))
        file_sources = {
            "from_scanner": self.smart_tasks.FROM_SCANNER,
            "from_photo": self.smart_tasks.FROM_PHOTOS
        }
        self.__load_smart_task_source_type_screen(smart_task_name, self.smart_tasks.SAVE_TO_GGDRIVE, file_sources[file_source])
        if file_source == "from_scanner":
            self.scan.select_scan()
            self.scan.verify_successful_scan_job()
        else:
            self.files_photos.verify_files_photos_screen()
            self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
            self.photos.select_album_photo_by_index(album_name="jpg")
        self.__verify_home_screen(smart_task_name)


    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_smart_task_source_type_screen(self,smart_task_name, acc_name, source_type):
        """
        - Load Home screen.
        - Select a printer to connect
        - Load to Smart Task screen with HPID connected
        - Create a smart task for saving with Dropbox or GoogleDrive
        - Select a file source type
        :param smart_task_name
        :param acc_name
           - SAVE_TO_GGDRIVE
           - SAVE_TO_DROPBOX
        :param source_type
           - FROM_SCANNER
           - FROM_PHOTOS
           - FROM_FILES
        """
        
        self.fc.flow_home_load_smart_task_screen(create_acc=False, printer_obj=self.p)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_saving(acc_name)
        self.smart_tasks.select_save_btn()
        try:
            self.smart_tasks.dismiss_smart_task_created_popup()
            self.smart_tasks.select_smart_task(smart_task_name)
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=False, btn_name=self.smart_tasks.START_THIS_SMART_TASK_BTN)
        self.smart_tasks.select_smart_task_source_type(source_type, invisible=False)

    def __verify_home_screen(self, smart_task_name):
        """
        - select a smart task.
        - click on start button
        - verify smart task upload complete screen
        - click on Home button
        - Verify Home screen
        """
        self.smart_tasks.verify_smart_tasks_list_screen(is_empty=False)
        self.smart_tasks.select_smart_task_from_preview_screen(smart_task_name)
        self.smart_tasks.dismiss_smart_tasks_complete_popup_screen()
        if self.home.verify_photomyne_awareness_popup(raise_e=False):
            self.home.dismiss_photomyne_awareness_popup()
        self.home.verify_home_nav()