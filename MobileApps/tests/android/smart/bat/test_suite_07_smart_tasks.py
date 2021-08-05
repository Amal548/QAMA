from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import TimeoutException
import logging
import datetime


pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}

class Test_Suite_07_Smart_Tasks(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session, record_testsuite_property):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.smart_tasks = cls.fc.flow[FLOW_NAMES.SMART_TASKS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]

        # Define the variable
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        cls.dropbox_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.CLOUD_ACCOUNT))["dropbox"]["account_01"]["username"]
        cls.dropbox_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.CLOUD_ACCOUNT))["dropbox"]["account_01"]["password"]
        record_testsuite_property("suite_test_category", "SmartTask")

        def clean_up_class():
            cls.fc.flow_home_delete_all_smart_tasks()

        request.addfinalizer(clean_up_class)

    def test_01_smart_task_for_print_photos(self):
        """
        Description:
          1. Load to Home screen
          2. Select a target printer from Printer lists
          3. Login in HPID in App Settings
          4. Click on Smart Tasks tile on Home screen (Enable Smart Task file from Personalize if Smart Tasks tile not on Home screen)
          5. Click on "CREATE NEW SMART TASKS" or "+" button
          6, Type a smart tasks name
          7. Click on Print
          8. Turn on Smart task for printing
          9. Click on Back button
          10. Click on Save button
          11. Click on OK button if popup "You just created a Smart task" displays
          12. Click on 3 dot icon for the smart task just created
          13. Click on Start button
          14. Click on Photos, then go to below steps:
              - Click on My Photos
              - Select a photo from any album
              - Click on Next button
          15. Click on Start button
          16. Allow access to HPPS, and Make a printing job via HPPS trapdoor ui

        Expected Result:
          16. Verify Printing job on:
              - Printer
              - HPPS app via trapdoor ui
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], "print_photos", (datetime.datetime.now()))
        self.__load_input_smart_task_name_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_print(two_sided_option=self.smart_tasks.TWO_SIDE_OFF,color_type=self.smart_tasks.COLOR_BTN)
        self.smart_tasks.select_save_btn()
        self.__load_smart_task_source_files_screen(smart_task_name, source_type=self.smart_tasks.FROM_PHOTOS)
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_album_photo_by_index(album_name="png")
        self.fc.flow_smart_task_make_printing_job(smart_task_name, self.p, jobs=1)

    def test_02_smart_task_for_print_document(self):
        """
        Description:
          1. Load to Home screen
          2. Select a target printer from Printer lists
          3. Login in HPID in App Settings
          4. Click on Smart Tasks tile on Home screen (Enable Smart Task file from Personalize if Smart Tasks tile not on Home screen)
          5. Click on "CREATE NEW SMART TASKS" or "+" button
          6, Type a smart tasks name
          7. Click on Print
          8. Turn on Smart task for printing
          9. Click on Back button
          10. Click on Save button
          11. Click on Start this smart task button
          12. Click on Scanner, then go to below steps:
               - Click on Scan button
               - Select Start button
               - Click on Next button
          13. Click on Start button
          14. Allow access to HPPS, and Make a printing job via HPPS trapdoor ui

        Expected Result:
          14. Verify Printing job on:
              - Printer
              - HPPS app via trapdoor ui
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], "print_documents", (datetime.datetime.now()))
        self.__load_input_smart_task_name_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_print(two_sided_option=self.smart_tasks.SHORT_EDGE, color_type=self.smart_tasks.GRAYSCALE_BTN)
        self.smart_tasks.select_save_btn()
        self.__load_smart_task_source_files_screen(smart_task_name, source_type=self.smart_tasks.FROM_SCANNER)
        self.scan.verify_scan_screen()
        self.scan.select_scan()
        self.scan.verify_successful_scan_job()
        self.fc.flow_smart_task_make_printing_job(smart_task_name, self.p, jobs=1)

    def test_03_smart_task_for_email(self):
        """
        Description:
          1. Load to Home screen
          2. Select a target printer from Printer Lists
          3. Login HPID in App Settings
          4. Click on Smart Tasks tile on Home screen (Go to personalize tile to enable Smart Tasks tile if not on Home screen)
          5. Click on "CREATE NEW SMART TASKS" or "+" button
          6, Type a smart tasks name
          7. Click on Email
          8. Turn on Smart task for email
          9. Type email address we need Email
          10. Click on Back button
          11. Click on Save button
          12. Click on Start this smart task button
          13. Click on Photos
          14. Click on Start button

        Expected Result:
          14. Verify Your Smart Task is on its way screen:
              - Completed icon
              - HOME button
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], "email", (datetime.datetime.now()))
        self.__load_input_smart_task_name_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_email(to_email=self.email_address)
        self.smart_tasks.select_save_btn()
        self.__load_smart_task_source_files_screen(smart_task_name, source_type=self.smart_tasks.FROM_PHOTOS)
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_album_photo_by_index(album_name="png")
        self.smart_tasks.verify_smart_tasks_list_screen(is_empty=False)
        self.smart_tasks.select_smart_task_from_preview_screen(smart_task_name)
        self.smart_tasks.dismiss_smart_tasks_complete_popup_screen()

    def test_04_smart_task_for_save_to_dropbox(self):
        """
        Description:
          1. Load to Home screen
          2. Select a target printer from Printer Lists
          3. Login HPID in App Settings
          4. Click on Smart Tasks tile on Home screen (Go to personalize tile to enable Smart Tasks tile if not on Home screen)
          5. Click on "CREATE NEW SMART TASKS" or "+" button
          6, Type a smart tasks name
          7. Click on Save
          8. Enable Dropbox for saving
          10. Click on Back button
          11. Click on Save button
          12. Click on Start this smart task button
          13. Click on Scanner
          14. Click on Start button

        Expected Result:
          14. Verify Your Smart Task is on its way screen:
              - Completed icon
              - HOME button
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], "dropbox", (datetime.datetime.now()))
        self.__load_input_smart_task_name_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_saving(self.smart_tasks.SAVE_TO_DROPBOX)
        self.smart_tasks.select_save_btn()
        self.__load_smart_task_source_files_screen(smart_task_name, source_type=self.smart_tasks.FROM_CAMERA)
        self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE)     
        self.smart_tasks.verify_smart_tasks_list_screen(is_empty=False)
        self.smart_tasks.select_smart_task_from_preview_screen(smart_task_name)
        self.smart_tasks.dismiss_smart_tasks_complete_popup_screen()

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
        self.fc.flow_home_load_smart_task_screen(printer_obj=self.p)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)

    def __load_smart_task_source_files_screen(self, smart_task_name, source_type):
        """
        - Select this smart task
        - Select a type from source files
        :param smart_task_name:
        :param source_type:
               - FROM_CAMERA
               - FROM_SCANNER
               - FROM_PHOTOS
        """
        try:
            self.smart_tasks.dismiss_smart_task_created_popup()
            self.smart_tasks.select_smart_task(smart_task_name)
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=False, btn_name=self.smart_tasks.START_THIS_SMART_TASK_BTN)
        self.smart_tasks.select_smart_task_source_type(source_type, invisible=False)