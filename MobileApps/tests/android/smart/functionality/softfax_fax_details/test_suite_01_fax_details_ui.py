import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA, GOOGLE_PHOTOS, WEBVIEW_CONTEXT

pytest.app_info = "SMART"


class Test_Suite_01_Fax_Details_UI(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_history = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    def test_01_successful_fax_detail(self):
        """
        Description:
            1/ Load to Compose Fax with creating new account
            2/ Successfully send fax
            3/ Load Fax History and select successful record in Sent tab
        Expected Result:
            3/ Sent Fax Details:
                - title
                - Fax Delivered! text
                - Phone number
                - file name and page number
                - Started and Finished Date and Time
                - Print Confirmation and Home button
        """
        file_name, number_page, phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"], is_successful=True, check_onboarding=False)
        self.__load_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone, status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_status(is_successful=True, check_sending=False)
        self.send_fax_details.verify_phone_number(phone_number=phone)
        self.send_fax_details.verify_time_information(is_successful=True)
        self.send_fax_details.verify_file_information(file_name=file_name, number_page=number_page)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.PRINT_CONFIRMATION_BTN, self.send_fax_details.HOME_BTN])

    def test_02_unsuccessful_fax_detail(self):
        """
        Description:
            1/ Load to Compose Fax with creating new account
            2/ Unsuccessfully send fax
            3/ Load Fax History and select unsuccessful record in Sent tab
        Expected Result:
            3/ Sent Fax Details:
                - title
                - Delivery Failed! text
                - Phone number
                - file name and page number
                - Started and Failed Date and Time
                - Retry Fax and Edit Resend button
        """
        file_name, number_page, phone = self.__make_send_fax_job(recipient_phone="(858) 689-5896", is_fail=True)
        self.__load_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone, status=self.fax_history.FAILED_STATUS)
        self.send_fax_details.verify_send_fax_status(is_successful=False, check_sending=False)
        self.send_fax_details.verify_phone_number(phone_number=phone)
        self.send_fax_details.verify_time_information(is_successful=False)
        self.send_fax_details.verify_file_information(file_name=file_name, number_page=number_page)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.RETRY_FAX_BTN, self.send_fax_details.EDIT_RESEND_BTN])

    def test_03_processing_fax_detail(self):
        """
        Description:
            1/ Load to Compose Fax with creating new account
            2/ Send fax without checking status
            3/ Load Fax History and select processing record in Sent tab
        Expected Result:
            3/ Sent Fax Details:
                - title
                - Phone number
                - file name and page number
                - Started Date and Time
                - Cancel Fax and Home button
        """
        file_name, number_page, phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"])
        self.__load_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone, status=self.fax_history.PROCESSING_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.verify_phone_number(phone_number=phone)
        self.send_fax_details.verify_time_information(check_end=False)
        self.send_fax_details.verify_file_information(file_name=file_name, number_page=number_page)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.CANCEL_FAX_BTN, self.send_fax_details.HOME_BTN])

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------

    def __load_fax_history(self):
        """
        Load to Fax History screen
                - Load Compose Fax screen
                - CLick on Fax History on menu
        """
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()

    def __make_send_fax_job(self, recipient_phone, is_successful=False, is_fail=False, check_onboarding=False):
        """
        Make a successful sending fax:
            - Load Compose Fax screen
            - Enter valid information of receiver and sender
            - Add a file (from my photos)
            - Click on Send Fax
            - Verify status of job if is_successful or is_fail. Otherwise, skip this step
            - Click on Back button -> Compose screen
        :return file name, number_pages, and recipient phone number
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True, 
                                                  check_onboarding=check_onboarding)
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_album_photo_by_index(GOOGLE_PHOTOS.PNG)
        self.preview.verify_preview_nav(is_edit=True)
        self.preview.select_next()
        # There are some test cases failed by No Such context issue, so add timeout for wait_for_context for fixing this issue
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=30)
        file_name, number_pages = self.compose_fax.get_added_file_information()
        self.compose_fax.enter_recipient_information(recipient_phone)
        phone, _, code = self.compose_fax.get_recipient_information()
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_send_fax()
        # Wait for developer for timeout of sending fax
        if is_successful:
            self.send_fax_details.verify_send_fax_status(timeout=600, is_successful=True, check_sending=False)
        elif is_fail:
            self.send_fax_details.verify_send_fax_status(timeout=360, is_successful=False, check_sending=False)
        else:
            self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_back()
        return file_name, number_pages, "{} {}".format(code, phone)