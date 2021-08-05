import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc


pytest.app_info = "SMART"

class  Test_Suite_08_Softfax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, softfax_class_cleanup, record_testsuite_property):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Skip this test case for android 7 since there is an issue with file 
        if cls.driver.driver_info['platformVersion'].split(".")[0] == "7":
            pytest.skip("Skip this test suite on Android 7 as developer won't fix pdf files issue.")

        # Define flows
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]

        # Define variables
        cls.recipient = cls.fc.get_softfax_recipient_info()
        cls.sender = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device(TEST_DATA.ONE_PAGE_PDF)
        record_testsuite_property("suite_test_category", "Softfax")

        def clean_up_class():
            """
            Clean up data which is created during testing
            """
            cls.fc.clean_up_download_and_pictures_folders()
        request.addfinalizer(clean_up_class)


    def test_01_successful_sending_fax_one_page_pdf(self):
        """
        Description:
            1/ Load Compose Fax by creating account
            2/ At Compose Fax screen, enter valid information for sender and receipient
            3/ Upload one page pdf file
            4/ Click on Send Fax
            5/ Observer Send Fax Detail

        Expected:
            5/ Status of sending fax is successful
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True)
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.PDF_TXT)
        self.local_files.load_downloads_folder_screen()
        self.local_files.select_file(TEST_DATA.ONE_PAGE_PDF)
        self.preview.verify_preview_nav(is_edit=False)
        self.preview.select_next()
        self.compose_fax.verify_compose_fax_screen()
        #Files need to take10-25s to loaded, depends on the file size
        self.compose_fax.verify_uploaded_file(timeout=25)
        self.compose_fax.enter_recipient_information(self.recipient["phone"])
        self.compose_fax.enter_sender_information(self.sender["name"], self.sender["phone"])
        self.compose_fax.click_send_fax()
        # wait for developer's reply for timeout of sending fax succesfully.
        self.send_fax_details.verify_send_fax_status(timeout=200,is_successful=True, check_sending=True)
        
