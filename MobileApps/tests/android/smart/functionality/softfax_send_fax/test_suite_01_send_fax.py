import pytest
import logging
import time
import datetime
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA, GOOGLE_PHOTOS, DROPBOX, FACEBOOK_ALBUM
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.ma_misc.excel import Excel

pytest.app_info = "SMART"


class Test_Suite_01_Send_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, get_softfax_output_file_path, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]
        cls.online_photos = cls.fc.flow[FLOW_NAMES.ONLINE_PHOTOS]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]
        cls.excel = Excel(get_softfax_output_file_path)
        cls.excel.load_sheet("Send Fax Performance")
        cls.excel.write_new_record(["Date", "File Name", "Time (seconds)", "Error Message"])

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info(request)
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.stack = request.config.getoption("--stack")
        cls.sending_time = 0
        cls.file_name = ""
        cls.error_msg = ""

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        cls.fc.transfer_test_data_to_device([TEST_DATA.ONE_PAGE_PDF, TEST_DATA.PDF_1PAGE_1MB, TEST_DATA.PDF_1PAGE_3MB,
                                             TEST_DATA.PDF_2PAGES_20MB, TEST_DATA.PDF_4PAGES_12MB, TEST_DATA.PDF_10PAGES_20MB,
                                             TEST_DATA.PDF_BIG_PDF_30MB])

        # Log out Dropbox
        cls.fc.flow_dropbox_logout()

        def clean_up_class():
            cls.fc.clean_up_download_and_pictures_folders()
            cls.fc.flow_dropbox_logout()
        request.addfinalizer(clean_up_class)

    @pytest.fixture(scope="function", autouse=True)
    def function_setup(self, request):
        """
        Setup and tear down function
        :param request:
        """
        def clean_up_func():
            if "test_00" not in request.node.name:
                self.excel.write_new_record([str(datetime.datetime.now()), self.file_name, self.sending_time, self.error_msg])
                self.excel.save()
        request.addfinalizer(clean_up_func)

    @pytest.mark.parametrize("number", [1, 3])
    def test_01_send_fax_from_camera(self, number):
        """
        Description:
            1/ Load to Compose Fax screen
            2/ In Add Files, select file via camera
            3/ Enter valid information for recipient and sender
            4/ Click on Send fax button
            5/ Click on View Status
            6/ Observe for sending fax successfully
        Expected result:
            4/ Popup "Your fax is on its way!"
            5/ Send Fax Details:
                - Processing Documents text with recipient phone number
                - Sending document
                - Send Fax again and Cancel Fax button
            6/ Same screen on step 5 with:
                - Processing Documents text with recipient phone number
                - Fax sent success
                - Send Fax again button
        """
        sending_timeouts = {1: [10, 210],
                            3: [30, 1000]}
        self.file_name = "camera/{}page".format(number)
        self.fc.flow_home_load_compose_fax_screen(stack=self.stack, create_acc=True)
        self.compose_fax.click_add_files_option_btn(self.compose_fax.CAMERA_BTN)
        self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE,
                                       number_pages=number)
        self.preview.verify_preview_nav()
        self.preview.select_next()
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=sending_timeouts[number][0])
        self.__enter_compose_fax_information()
        self.__make_send_fax_job(sending_timeouts[number][1])

    @pytest.mark.parametrize("file_names", [TEST_DATA.ONE_PAGE_PDF, TEST_DATA.PDF_1PAGE_1MB, TEST_DATA.PDF_1PAGE_3MB, TEST_DATA.PDF_2PAGES_20MB,
                                           TEST_DATA.PDF_4PAGES_12MB, TEST_DATA.PDF_10PAGES_20MB, TEST_DATA.PDF_BIG_PDF_30MB])
    def test_02_send_fax_from_file_photos_local_file(self, file_names):
        """
            Description:
                1/ Load to Compose Fax screen
                2/ In Add Files, select file from Files & Photos/Scanned Files
                3/ Enter valid information for recipient and sender
                4/ Click on Send fax button
                5/ Click on View Status
                6/ Observe for sending fax successfully
            Expected result:
                4/ Popup "Your fax is on its way!"
                6/ Same screen on step 5 with:
                    - Processing Documents text with recipient phone number
                    - Fax sent success
                    - Send Fax again button
        """
        # Timeout list: [uploading file, sending fax]
        sending_timeouts = {TEST_DATA.ONE_PAGE_PDF: [10, 180],
                            TEST_DATA.PDF_1PAGE_1MB: [10, 290],
                            TEST_DATA.PDF_1PAGE_3MB: [10, 331],
                            TEST_DATA.PDF_2PAGES_20MB: [40 , 300] ,
                            TEST_DATA.PDF_4PAGES_12MB: [30, 1750],
                            TEST_DATA.PDF_10PAGES_20MB: [40, 2550],
                            TEST_DATA.PDF_BIG_PDF_30MB: [55, 391]}
        self.file_name = "scanned file/{}".format(file_names)
        self.fc.flow_home_load_compose_fax_screen(stack=self.stack, create_acc=True)
        self.__add_file_from_file_photos(file_names, sending_timeouts[file_names][0], is_file=True)
        self.__enter_compose_fax_information()
        self.__make_send_fax_job(sending_timeouts[file_names][1])

    @pytest.mark.parametrize("album", [GOOGLE_PHOTOS.PNG, GOOGLE_PHOTOS.JPG])
    def test_03_send_fax_from_file_photos_local_photo(self, album):
        """
            Description:
                1/ Load to Compose Fax screen
                2/ In Add Files, select file from Files & Photos/My Photos
                3/ Enter valid information for recipient and sender
                4/ Click on Send fax button
                5/ Click on View Status
                6/ Observe for sending fax successfully
            Expected result:
                4/ Popup "Your fax is on its way!"
                6/ Same screen on step 5 with:
                    - Processing Documents text with recipient phone number
                    - Fax sent success
                    - Send Fax again button
        """
        # Timeout list: [uploading file, sending fax]
        sending_timeouts = {GOOGLE_PHOTOS.PNG: [10, 185],
                            GOOGLE_PHOTOS.JPG: [10, 120]}
        self.file_name = "my photos/{}".format(album)
        self.fc.flow_home_load_compose_fax_screen(stack=self.stack, create_acc=True)
        self.__add_file_from_file_photos(album, sending_timeouts[album][0], is_file=False)
        self.__enter_compose_fax_information()
        self.__make_send_fax_job(sending_timeouts[album][1])

    @pytest.mark.parametrize("file_names", [DROPBOX.PDF_1PAGE_1MB, DROPBOX.PDF_1PAGE_3MB,
                                            DROPBOX.PDF_2PAGES_20MB, DROPBOX.PDF_4PAGES_12MB,
                                            DROPBOX.PDF_10PAGES_20MB, DROPBOX.PDF_BIG_PDF_30MB,
                                            DROPBOX.JPG_BOW, DROPBOX.PNG_FISH])
    def test_04_send_fax_from_dropbox(self, file_names):
        """
            Description:
                1/ Load to Compose Fax screen
                2/ In Add Files, select file from Dropbox
                3/ Enter valid information for recipient and sender
                4/ Click on Send fax button
                5/ Click on View Status
                6/ Observe for sending fax successfully
            Expected result:
                4/ Popup "Your fax is on its way!"
                6/ Same screen on step 5 with:
                    - Processing Documents text with recipient phone number
                    - Fax sent success
                    - Send Fax again button
        """
        # Timeout list: [uploading file, sending fax]
        sending_timeouts = {DROPBOX.PDF_1PAGE_1MB: [10, 290],
                            DROPBOX.PDF_1PAGE_3MB: [10, 331],
                            DROPBOX.PDF_2PAGES_20MB: [40, 300],
                            DROPBOX.PDF_4PAGES_12MB: [30, 1750],
                            DROPBOX.PDF_10PAGES_20MB: [40, 2550],
                            DROPBOX.PDF_BIG_PDF_30MB: [55, 391],
                            DROPBOX.JPG_BOW: [10, 294],
                            DROPBOX.PNG_FISH: [10, 120]}
        self.file_name = "dropbox/{}".format(file_names)
        username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.CLOUD_ACCOUNT))["dropbox"]["account_02"]["username"]
        pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.CLOUD_ACCOUNT))["dropbox"]["account_02"]["password"]

        self.fc.flow_home_load_compose_fax_screen(stack=self.stack, create_acc=True)
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.files_photos.verify_files_photos_screen()
        if self.files_photos.verify_cloud_not_login(self.files_photos.DROPBOX_TXT, raise_e=False):
            self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
            self.fc.flow_dropbox_log_in(username, pwd)
        self.files_photos.verify_cloud_added_account(self.files_photos.DROPBOX_TXT, username)
        self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
        if file_names.split(".")[1] == "pdf":
            folder = DROPBOX.DOCUMENT_FOLDER
        else:
            folder = DROPBOX.IMAGE_FOLDER
        self.online_docs.select_file("{}/{}/{}".format(folder, file_names.split(".")[1], file_names))
        if file_names.split(".")[1] == "pdf":
            self.preview.verify_preview_nav(is_edit=False)
        else:
            self.preview.verify_preview_nav(is_edit=True)
        self.preview.select_next()
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=sending_timeouts[file_names][0])
        self.__enter_compose_fax_information()
        self.__make_send_fax_job(sending_timeouts[file_names][1])

    @pytest.mark.parametrize("number", [1, 3, 10])
    def test_05_send_fax_from_facebook(self, number):
        """
            Description:
                1/ Load to Compose Fax screen
                2/ In Add Files, select file from Facebook based on number of file
                3/ Enter valid information for recipient and sender
                4/ Click on Send fax button
                5/ Click on View Status
                6/ Observe for sending fax successfully
            Expected result:
                4/ Popup "Your fax is on its way!"
                6/ Same screen on step 5 with:
                    - Processing Documents text with recipient phone number
                    - Fax sent success
                    - Send Fax again button
        """
        # Timeout list: [uploading file, sending fax]
        sending_timeouts = {1: [10, 331],
                            3: [30, 1750],
                            10: [40, 2550]}
        self.file_name = "facebook / {} photos".format(number)
        self.fc.flow_home_load_compose_fax_screen(stack=self.stack, create_acc=True)
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.files_photos.verify_files_photos_screen()
        if self.files_photos.verify_cloud_not_login(self.files_photos.FACEBOOK_TXT, raise_e=False):
            self.files_photos.select_cloud_item(self.files_photos.FACEBOOK_TXT)
            if self.online_photos.verify_fb_login_confirmation_screen(raise_e=False):
                self.online_photos.select_fb_confirmation_continue()
        self.files_photos.verify_cloud_added_account(self.files_photos.FACEBOOK_TXT, "QA MobiAuto")
        self.files_photos.select_cloud_item(self.files_photos.FACEBOOK_TXT)
        self.online_photos.verify_fb_album_screen()
        self.online_photos.select_album(FACEBOOK_ALBUM.MOBILE_UPLOADS)
        if number == 1:
            self.online_photos.select_single_photo()
        else:
            self.online_photos.select_multiple_photos(number)
            self.online_photos.select_next()
        self.preview.verify_preview_nav(is_edit=True)
        self.preview.select_next()
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=sending_timeouts[number][0])
        self.__enter_compose_fax_information()
        self.__make_send_fax_job(sending_timeouts[number][1])

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __add_file_from_file_photos(self, file, timeout, is_file=True):
        """
        - Click on File Photos button on Compose screen
        - Select file based on from_source (pdfs, scanned files)
        - Verify compose screen with added file.
        :param file: file name for PDFs/Scanned Files or album nam for photo
        :param timeout: uploading timeout
        :param is_file: from local file (True) or my photos (False)
        """
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.files_photos.verify_files_photos_screen()
        is_edit = True
        if is_file:
            self.files_photos.select_local_item(self.files_photos.PDF_TXT)
            self.local_files.load_downloads_folder_screen()
            self.local_files.select_file(file)
            if file.split(".")[1] == "pdf":
                is_edit = False
        else:
            self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
            self.local_photos.select_album_photo_by_index(file)
        self.preview.verify_preview_nav(is_edit=is_edit)
        self.preview.select_next()
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=timeout)

    def __enter_compose_fax_information(self):
        """
        Enter required information for recipient and sender
        """
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])

    def __make_send_fax_job(self, timeout):
        """
        Start after entering information and adding file:
            - Click on Send Fax button
            - Verify Send Fax popup
            - CLick on View Status
            - Verify sending fax successfully in Send Fax Detail
        :param timeout: timeout of sending fax successfull on last step
        """
        self.compose_fax.click_send_fax()
        try:
            start = time.time()
            self.send_fax_details.verify_send_fax_status(timeout=timeout)
            self.sending_time = time.time() - start
        except (TimeoutException, NoSuchElementException) as ex:
            self.error_msg = ex.msg             # Get error message for performance record before raising exception.
            raise ex
