from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import pytest
import os

pytest.app_info = "SMART"


class Test_Suite_03_PDF_Printing(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        # Android 7 has issue about read .pdf files from smart app. And won't be fixed based on comments on AIOA-7969
        if cls.driver.driver_info['platformVersion'].split(".")[0] == "7":
            pytest.skip("Skip test this test suite on Android 7 as developer won't fix pdf files issue.")

        # Defines flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([TEST_DATA.PDF_3PAGES_WORD_IMAGE,
                                             TEST_DATA.PDF_5PAGES_EMAIL,
                                             TEST_DATA.PDF_6PAGES_FORMATTED_DOC])

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("file_name", [TEST_DATA.PDF_3PAGES_WORD_IMAGE,
                                           TEST_DATA.PDF_5PAGES_EMAIL,
                                           TEST_DATA.PDF_6PAGES_FORMATTED_DOC])
    def test_01_printing(self, file_name):
        """
        Descriptions:
            1/ Load Home screen
            2/ Connect to target printer
            3/ At Home screen, click on View and Print button on bottom navigation
            4/ Click on PDF's button on Files screen. 
            5/ select  <file_name.pdf> 
            6/ click on Print button
            7/ Go through Print flow in PSP 

        Expected Result:
            7/ Verify printing job successfully
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        self.fc.flow_home_select_network_printer(self.p)
        self.fc.flow_home_verify_ready_printer(self.p.get_printer_information()["bonjour name"])
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(file_name)
        if "novelli" in self.p.p_obj.projectName:
            self.preview.verify_print_size_screen()
            self.preview.select_print_size_btn(self.preview.PRINT_SIZE_4x6_STANDARD)
        self.fc.flow_preview_make_printing_job(self.p, jobs=1, is_edit=False)