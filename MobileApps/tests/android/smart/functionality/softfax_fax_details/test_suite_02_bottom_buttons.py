import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA, GOOGLE_PHOTOS, PACKAGE, WEBVIEW_CONTEXT
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "SMART"


class Test_Suite_02_Bottom_Buttons(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_history = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    def test_01_unsuccessful_fax_detail_retry_fax(self):
        """
         Description:
            1/ Load to Compose Fax 
            2/ Start a sending job - unsuccessful
            3/ Load Fax History and select unsuccessful job
            4/ Click Retry Fax button
            5/ Click Cancel Fax
        Expected Result:
            4/ Send Fax Details with processing
            5/ Send Fax Details - Uncessfull status
        """
        phone = self.__make_send_fax_job(recipient_phone="(858) 689-5896", is_fail=True,  check_onboarding=False)
        self.__select_fax_history_record(phone, self.fax_history.FAILED_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.RETRY_FAX_BTN)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.verify_bottom_btn(button_names=self.send_fax_details.CANCEL_FAX_BTN)
        self.send_fax_details.click_bottom_button(self.send_fax_details.CANCEL_FAX_BTN)
        self.send_fax_details.verify_send_fax_status(is_successful=False, check_sending=False, timeout=10)

    def test_02_unsuccessful_fax_detail_edit_resend(self):
        """
         Description:
            1/ Load to Compose Fax 
            2/ Start a sending job - unsuccessful
            3/ Load Fax History and select unsuccessful job
            4/ Click Edit and Resend button
            5/ On Compose Faxe, enter valid information
            6/ Click on Send Fax
        Expected Result:
            4/ Compose Fax screen.
            6/ Send Fax sucessfully.
        """
        phone = self.__make_send_fax_job(recipient_phone="(858) 689-5896", is_fail=True)
        self.__select_fax_history_record(phone, self.fax_history.FAILED_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.EDIT_RESEND_BTN)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.click_send_fax()
        # Wait for developer for timeout of sending fax
        self.send_fax_details.verify_send_fax_status(timeout=600, is_successful=True, check_sending=False)

    def test_03_successful_fax_detail_print_confirmation(self):
        """
         Description:
            1/ Load to Compose Fax 
            2/ Start a sending job - successful
            3/ Load Fax History and select successful job
            4/ Click Print Confirmation button
        Expected Result:
            4/ Smart app invisible (use package to verify)
        """
        phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"], is_successful=True)
        self.__select_fax_history_record(phone, self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.PRINT_CONFIRMATION_BTN)
        assert(self.driver.get_current_app_activity()[0] != PACKAGE.SMART), "Android Smart is still opened"

    def test_04_successful_fax_detail_home(self):
        """
         Description:
            1/ Load to Compose Fax 
            2/ Start a sending job - successful
            3/ Load Fax History and select successful job
            4/ Click Home button
        Expected Result:
            4/ Home screen of Android Smart app
        """
        phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"], is_successful=True)
        self.__select_fax_history_record(phone, self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.HOME_BTN)
        self.home.verify_home_nav()

    def test_05_processing_fax_detail_home(self):
        """
         Description:
            1/ Load to Compose Fax 
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click Home button
        Expected Result:
            4/ Home screen - Andnroid Smart app
        """
        phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"])
        self.__select_fax_history_record(phone, self.fax_history.PROCESSING_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.HOME_BTN)
        self.home.verify_home_nav()

    def test_06_processing_fax_detail_cancel_fax(self):
        """
        Description:
            1/ Load to Compose Fax 
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click Cancel Fax button
        Expected Result:
            4/ Compose screen displays
        """
        phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"])
        self.__select_fax_history_record(phone, self.fax_history.PROCESSING_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.CANCEL_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __select_fax_history_record(self, phone_number, status):
        """
        From Compose Fax screen, select a record on Fax History/Saved tab
                - Load Compose Fax screen
                - CLick on Fax History on menu
                - Select a record at Saved tab
                - Verify Sending Fax Details screen
        """
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number, status=status)
        self.send_fax_details.verify_send_fax_detail_screen()

    def __make_send_fax_job(self, recipient_phone, is_successful=False, is_fail=False, check_onboarding=True):
        """
        Make a successful sending fax:
            - Load Compose Fax screen
            - Enter valid information of receiver and sender
            - Add a file (from my photos)
            - Click on Send Fax
            - Verify status of job if is_successful or is_fail. Otherwise, skip this step
            - Click on Back button -> Compose screen
        :return recipient phone number
        """
        #Make sure compose fax screen is empty, not affect by previous test suite
        self.fc.reset_app()
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
        return "{} {}".format(code, phone)
