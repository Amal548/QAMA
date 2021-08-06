import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_08_Fax_History(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.fax_history = cls.fc.fd["softfax_fax_history"]
        cls.fax_settings = cls.fc.fd["fax_settings"]
        cls.preview = cls.fc.fd["preview"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.fake_recipient = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_09"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_05"]
        cls.fc.go_home(reset=True, stack=cls.stack, button_index=2)

    def test_01_verify_fax_history_ui_when_no_faxes_sent(self):
        """
        C16023931 - fax_history_UI_when_no_faxes_sent
        """
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_mobile_fax()
        self.fc.create_account_from_tile()
        self.fc.verify_fax_welcome_screens_and_nav_compose_fax() 
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_sent_fax_history_list(is_empty=True)
    
    def test_02_verify_sent_fax_history_ui(self):
        """
        C16033024 - fax_history_sent_tab_UI
        """
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.nav_to_compose_fax()    
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_sent_fax_history_list(is_empty=False)

    def test_03_verify_unsuccessful_fax_sent_history(self):
        """
        C16033027 - Verify Unsuccessful Fax sent History
        C16033029 - fax_Retry
        """
        # phone_no = "(858) 689-5896"
        self.fc.nav_to_compose_fax()
        self.compose_fax.enter_recipient_information(self.fake_recipient["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.select_photo_from_my_photos()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_send_fax_native_btn()
        self.send_fax_details.verify_send_fax_status(timeout=360, is_successful=False, check_sending=False)
        # verify fax history screen
        self.send_fax_details.click_back()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        # verify failed fax details
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.fake_recipient["phone"], status=self.fax_history.FAILED_STATUS)
        self.send_fax_details.verify_send_fax_status(is_successful=False, check_sending=False)
        self.send_fax_details.verify_phone_number(phone_number='+1 ' + self.fake_recipient["phone"])
        self.send_fax_details.verify_time_information(is_successful=False)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.RETRY_FAX_BTN, self.send_fax_details.EDIT_RESEND_BTN])
        self.send_fax_details.click_bottom_button(self.send_fax_details.RETRY_FAX_BTN)    
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.CANCEL_FAX_BTN, self.send_fax_details.HOME_BTN])
    
    def test_04_verify_print_confirmation_successful_sent_fax(self):
        """
        C16033028 - Verify Print Confirmation for successful sent Fax
        """
        # phone_no = "(213) 531-2487"
        self.fc.nav_to_compose_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.verify_send_fax_status(is_successful=True, check_sending=False)
        self.send_fax_details.verify_phone_number(phone_number='+1 ' + self.recipient_info["phone"])
        self.send_fax_details.verify_time_information(is_successful=True)
        self.send_fax_details.verify_bottom_btn(button_names=[self.send_fax_details.PRINT_CONFIRMATION_BTN, self.send_fax_details.HOME_BTN])

    def test_06_verify_fax_edit_and_resend_failed_fax(self):
        """
        C16932588 - fax_edit_and_resend_failed_fax
        """
        # phone_no = "(858) 689-5896"
        self.fc.nav_to_compose_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], 
                                                status=self.fax_history.FAILED_STATUS)
        self.send_fax_details.verify_send_fax_status(is_successful=False, check_sending=False)
        self.send_fax_details.click_bottom_button(self.send_fax_details.RETRY_FAX_BTN)
        self.send_fax_details.click_bottom_button(self.send_fax_details.CANCEL_FAX_BTN)
    
    def test_07_verify_fax_history_draft_when_faxes_are_saved(self):
        """
        C16946925 - fax_history_draft_when_faxes_are_saved
        """
        # phone_no = "(213) 531-2487"
        self.fc.nav_to_compose_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_tab(self.fax_history.DRAFT_RECORD_CELL)
        self.fax_history.select_history_record(self.fax_history.DRAFT_RECORD_CELL, phone_number="+1 " + self.fake_recipient["phone"])
        
    
    def test_08_verify_print_confirmation_sent_fax_details(self):
        """
        C24773511 - Verify "Print confirmation" button from Sent Fax Details
        """
        # phone_no = "(858) 689-5896"
        self.fc.nav_to_compose_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.PRINT_CONFIRMATION_BTN)
        self.fc.fd["preview"].verify_preview_screen()
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_09_verify_compose_new_fax_button_sent_tab_fax_history(self, tab):
        """
        C24814559 - "Compose New Fax" button from Sent tab of "Fax History"
        C24814560 - "Compose New Fax" button from Draft tab of "Fax History"
        """
        self.fc.nav_to_compose_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.select_tab(self.fax_history.SENT_TAB)
        else:
            self.fax_history.select_tab(self.fax_history.DRAFT_RECORD_CELL)

        self.fax_history.click_compose_new_fax()
        self.compose_fax.verify_compose_fax_screen()
    
    def test_10_verify_home_btn_from_sent_fax_details_page(self):
        """
        C24814561 - Verify "Home" button from Sent Fax Details page
        """
        # phone_no = "(858) 689-5896"    
        self.fc.nav_to_compose_fax()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        self.send_fax_details.click_bottom_button(self.send_fax_details.HOME_BTN)
        self.fc.fd["home"].verify_home_tile()