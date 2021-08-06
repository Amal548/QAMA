from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
import datetime

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_01_Smart_Tasks_Execution_For_Printing(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.smart_tasks = cls.fc.flow[FLOW_NAMES.SMART_TASKS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]

        # Define the variable
        cls.udid = cls.driver.driver_info["desired"]["udid"]
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

    @pytest.mark.parametrize("print_option", ["two_sided_off,from_camera,single_copies",
                                             "short_edge,from_photos,single_copies",
                                             "long_edge,from_files,single_copies",
                                             "two_sided_off,from_camera,multi_copies",
                                             "short_edge,from_photos,multi_copies",
                                             "long_edge,from_files,multi_copies"
                                             ])
    def test_01_execute_smart_tasks_with_color_print(self, print_option):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Smart Tasks screen
          4. Create a new smart task screen for single/color print with different printing settings
          5. Start a smart task from step4
          6. If print_option is two_sided_off, then click Camera from  source files
             If print_option is short_edge, then click Photos from  source files
             If print_option is long_edge, then click Files from source files
          7. - If from Camera, then click capture screenshot with manual mode
             - If from Photos, then click PDF Files, and select a .pdf file
             - If from Files, then click Dropbox and select a .jpg file
          8. Click on Start button

        Expected Result:
          8. Verify Smart Task send success screen popup:
             - Message
             - Home button
             Also verify if sending printing job success or not
        """
        print_option = print_option.split(",")
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, print_option[0], (datetime.datetime.now()))
        sides_options = {
            "two_sided_off": self.smart_tasks.TWO_SIDE_OFF,
            "short_edge": self.smart_tasks.SHORT_EDGE,
            "long_edge": self.smart_tasks.LONG_EDGE
        }
        file_sources = {
            "from_camera": self.smart_tasks.FROM_CAMERA,
            "from_photos": self.smart_tasks.FROM_PHOTOS,
            "from_files": self.smart_tasks.FROM_FILES
        }
        copies_num = {"multi_copies": 2,
                      "single_copies": 1}
        self.__load_input_smart_task_name_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_print(copies_num=copies_num[print_option[2]], 
                                                  two_sided_option=sides_options[print_option[0]], 
                                                  color_type=self.smart_tasks.COLOR_BTN)
        self.__select_a_smart_task(smart_task_name)
        self.smart_tasks.select_smart_task_source_type(file_sources[print_option[1]], is_checked=True, invisible=False)
        if print_option[0] == "two_sided_off":
            self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE)
        elif print_option[0] == "short_edge":
            # Android 7 has issue about read .pdf files from smart app. And won't be fixed based on comments on AIOA-7969
            if self.driver.driver_info['platformVersion'].split(".")[0] == "7":
                pytest.skip("Skip test this test suite on Android 7 as developer won't fix pdf files issue.")
            else:
                self.files_photos.select_local_item(self.files_photos.PDF_TXT)
                self.files.load_downloads_folder_screen()
                self.files.select_file(self.pdf_fn)
        else:
            try:
                self.files_photos.verify_cloud_added_account(self.files_photos.DROPBOX_TXT, self.dropbox_username)
            except NoSuchElementException:
                self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
                self.fc.flow_dropbox_log_in(self.dropbox_username, self.dropbox_pwd)
                self.files_photos.verify_cloud_added_account(self.files_photos.DROPBOX_TXT, self.dropbox_username)
            self.files_photos.select_local_item(self.files_photos.DROPBOX_TXT)
            self.online_docs.select_file("testdata_cloud/images/jpg/bow.jpg")
        self.fc.flow_smart_task_make_printing_job(smart_task_name, self.p, jobs=1)

    @pytest.mark.parametrize("print_option", ["two_sided_off,from_scanner,single_copies",
                                              "short_edge,from_photos,single_copies",
                                              "long_edge,from_files,single_copies",
                                              "two_sided_off,from_scanner,multi_copies",
                                              "short_edge,from_photos,multi_copies",
                                              "long_edge,from_files,multi_copies"
                                              ])
    def test_02_execute_smart_tasks_with_black_print(self, print_option):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Smart Tasks screen
          4. Create a new smart task screen for black print with different printing settings
          5. Start a smart task from step4
          6. If print_option is two_sided_off, then click Scanner from  source files
             If print_option is short_edge, then click Photos from  source files
             If print_option is long_edge, then click Files from source files
          7. - If from Scanner, then click scan button
             - If from Photos, then click My Photos and select a .jpg file
             - If from Files, then click Facebook, and select a .jpg file
          8. Click on Start button

        Expected Result:
          8. Verify Smart Task send success screen popup:
             - Message
             - Home button
             Also verify if sending printing job success or not
        """
        print_option = print_option.split(",")
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, print_option[0], (datetime.datetime.now()))
        sides_options = {
            "two_sided_off": self.smart_tasks.TWO_SIDE_OFF,
            "short_edge": self.smart_tasks.SHORT_EDGE,
            "long_edge": self.smart_tasks.LONG_EDGE
        }
        file_sources = {
            "from_scanner": self.smart_tasks.FROM_SCANNER,
            "from_photos": self.smart_tasks.FROM_PHOTOS,
            "from_files": self.smart_tasks.FROM_FILES
        }
        copies_num = {"multi_copies": 2,
                      "single_copies": 1}
        self.__load_input_smart_task_name_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_print(copies_num=copies_num[print_option[2]], 
                                                  two_sided_option=sides_options[print_option[0]], 
                                                  color_type=self.smart_tasks.GRAYSCALE_BTN)
        self.__select_a_smart_task(smart_task_name)
        self.smart_tasks.select_smart_task_source_type(file_sources[print_option[1]], is_checked=True, invisible=False)
        if print_option[0] == "two_sided_off":
            self.scan.select_scan()
            self.scan.verify_successful_scan_job()
        elif print_option[0] == "short_edge":
            self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
            self.photos.select_album_photo_by_index(album_name="jpg")
        else:
            self.files_photos.verify_files_photos_screen()
            self.files_photos.select_local_item(self.files_photos.PDF_TXT)
            self.files.load_downloads_folder_screen()
            self.files.select_file(self.pdf_fn)
        self.fc.flow_smart_task_make_printing_job(smart_task_name, self.p, jobs=1)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_input_smart_task_name_screen(self, smart_task_name):
        """
        - Load Home screen.
        - CLick on Smart Tasks tile on Home screen
        - Click on CREATE NEW SMART TASKS button or "+"
        - Input new smart task name
        - Select Email or Print or Save on Create Smart Task screen
        - Enable and Save new smart task
        :param smart_task_name
        :param for_print: True or False
        :param copies_num
        :param two_sided_option
        :param color_type
        :param acc_name
        """
        self.fc.flow_home_load_smart_task_screen(create_acc=False, printer_obj=self.p)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)

    def __select_a_smart_task(self, smart_task_name):
        """
        select a smart task from smart task lists screen or click "start this smart task" button after creating a smart task
        """
        self.smart_tasks.select_save_btn()
        try:
            self.smart_tasks.dismiss_smart_task_created_popup()
            self.smart_tasks.select_smart_task(smart_task_name)
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=False, btn_name=self.smart_tasks.START_THIS_SMART_TASK_BTN)