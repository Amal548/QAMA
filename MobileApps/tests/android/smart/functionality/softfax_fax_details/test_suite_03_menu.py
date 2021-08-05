import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA, GOOGLE_PHOTOS, WEBVIEW_CONTEXT

pytest.app_info = "SMART"


class Test_Suite_03_Menu(object):

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

    def test_01_cancel_deleting_fax(self):
        """
        Description:
            1/ Load to Compose Fax with creating new account
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click 3 dots menu button -> click on Delete this fax button
            5/ Click Cancel button on Are you sure? popup
        Expected Result:
            5/ Sent Fax Details:
                - title
                - Phone number
                - file name and page number
                - Cancel Fax and Home button
        """
        phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"], check_onboarding=False)
        self.__load_fax_details_screen(phone)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=False)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.verify_phone_number(phone_number=phone)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.CANCEL_FAX_BTN, self.send_fax_details.HOME_BTN])
   
    def test_02_delete_fax(self):
        """
        Description:
            1/ Load to Compose Fax with creating new account
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click 3 dots menu button -> click on Delete this fax button
            5/ Click Delete button on Are you sure? popup
        Expected Result:
            5/ Fax History
        """
        phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"])
        self.__load_fax_details_screen(phone)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()

    def test_03_save_fax_log(self):
        """
        Description:
            1/ Load to Compose Fax with creating new account
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click 3 dots menu button
            5/ Click on Save Fax log
        Expected Result:
            5/ Save fax log is invisible
        """
        phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"])
        self.__load_fax_details_screen(phone)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_SAVE_LOG_BTN)
        self.send_fax_details.verify_menu_save_fax_log(invisible=True)

    def test_04_home(self):
        """
        Description:
            1/ Load to Compose Fax with creating new account
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click 3 dots menu button
            5/ Click on Home button
        Expected Result:
            5/ Home screen of Android Smart
        """
        phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"])
        self.__load_fax_details_screen(phone)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_HOME_BTN)
        self.home.verify_home_nav()

    def test_05_edit_forward(self):
        """
        Description:
            1/ Load to Compose Fax with creating new account
            2/ Start a sending job
            3/ Load Fax History and select processing job
            4/ Click 3 dots menu button
            5/ Click on Edit and Forward button
        Expected Result:
            5/ Compose Fax
        """
        phone = self.__make_send_fax_job(recipient_phone=self.recipient_info["phone"])
        self.__load_fax_details_screen(phone)
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_EDIT_FORWARD_BTN)
        self.compose_fax.verify_compose_fax_screen()

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __load_fax_details_screen(self, phone):
        """
        From Compose Fax, load Fax Details screen via Fax History
                - Load Compose Fax screen
                - CLick on Fax History on menu
                - Select target record
        """
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone,
                                               status=self.fax_history.PROCESSING_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()

    def __make_send_fax_job(self, recipient_phone, check_onboarding=True):
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
        #Make sure compose fax screen is empty, not affect by previous test
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
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_back()
        return "{} {}".format(code, phone)