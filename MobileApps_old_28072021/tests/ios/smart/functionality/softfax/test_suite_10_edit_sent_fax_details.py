import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from time import sleep

pytest.app_info = "SMART"

class Test_Suite_10_Edit_Sent_Fax_Details(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.fax_history = cls.fc.fd["softfax_fax_history"]
        cls.fax_settings = cls.fc.fd["fax_settings"]
        cls.preview = cls.fc.fd["preview"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.fake_recipient = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_09"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_03"]
        cls.fc.go_home(reset=True, stack=cls.stack, button_index=2)

    def test_01_successfully_sent_fax_detail(self):
        '''
            C16946909: successful sent fac details ui
        '''
        self.fc.nav_to_compose_fax(stack=self.stack)
        file_name, number_pages, phone = self.create_sent_fax_job(recipient_phone=self.recipient_info["phone"])
        sleep(10)
        self.go_to_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.verify_send_fax_status(is_successful=True, check_sending=False)
        self.send_fax_details.verify_phone_number(phone_number=phone)
        self.send_fax_details.verify_time_information(is_successful=True)
        self.send_fax_details.verify_file_information(file_name=file_name, number_page=number_pages)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.PRINT_CONFIRMATION_BTN, self.send_fax_details.HOME_BTN])

    def test_02_sent_fax_details_home(self):
        '''
            C16946924: sent fax details home
        '''
        self.fc.nav_to_compose_fax(stack=self.stack)
        self.go_to_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL,
                phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_HOME_BTN)
        self.home.verify_home()

    def test_03_cancel_and_delete_fax(self):
        '''
            C16946923: cancel delete fax
        '''
        self.fc.nav_to_compose_fax(stack=self.stack)
        file_name, number_pages, phone = self.create_sent_fax_job(recipient_phone=self.recipient_info["phone"])
        self.go_to_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone,
                                               status=self.fax_history.PROCESSING_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=False)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_DELETE_BTN)
        self.send_fax_details.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()

    def test_04_save_fax_log(self):
        '''
            C16946922: save fax log
        '''
        self.fc.nav_to_compose_fax(stack=self.stack)
        self.go_to_fax_history()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, self.recipient_info["phone"],
                                               status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_menu_btn(self.send_fax_details.MENU_SAVE_LOG_BTN)
        self.preview.verify_preview_screen()

    def go_to_fax_history(self):
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()

    def create_sent_fax_job(self, recipient_phone):
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        phone, _, code = self.compose_fax.get_recipient_information()
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.select_photo_from_my_photos()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        file_name, number_pages = self.compose_fax.get_added_file_information()
        # @TODO:  Webview button click did not work so using native button click
        self.compose_fax.click_send_fax_native_btn()
        self.send_fax_details.verify_send_fax_detail_screen()
        self.send_fax_details.click_back()
        return file_name, number_pages, "{} {}".format(code, phone)
