import pytest
import time
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_09_Verify_Edit_Fax_History(object):

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
        cls.fake_recipient = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_05"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["recipient_02"]
        cls.fc.go_home(reset=True, stack=cls.stack, button_index=2)
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_01_verify_edit_sent_faxes_ui(self, tab):
        """
        C16942941 - edit_sent_faxes_UI
        C16942942 - edit_drafted_faxes_UI (No print fax log button)
        """
        self.fc.nav_to_compose_fax() 
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.select_tab(self.fax_history.SENT_TAB)
        else:
            self.fax_history.select_tab(self.fax_history.DRAFT_RECORD_CELL)
        self.fax_history.load_edit_screen()
        self.fax_history.verify_edit_screen()
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_02_verify_edit_and_do_not_delete_sent_faxes(self, tab):
        """
        C16942945 - edit_and_do_not_delete_sent_faxes
        C16942958 - edit_and_do_not_delete_drafted_faxes
        """
        self.fc.nav_to_compose_fax() 
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()
        self.fax_history.load_edit_screen()
        self.fax_history.verify_edit_screen()
        if tab == "sent":
            self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number="+1 " + self.recipient_info["phone"], status=self.fax_history.SUCCESSFUL_STATUS)
        else:
            self.fax_history.select_history_record(self.fax_history.DRAFT_RECORD_CELL, phone_number="+1 " + self.recipient_info["phone"])
        self.fax_history.click_edit_delete()
        self.fax_history.click_edit_cancel()
        self.fax_history.verify_sent_fax_history_list(self.recipient_info["phone"])
    
    def test_03_verify_edit_and_export_multiple_faxes_from_sent_faxes(self):
        """
        C16942947 - edit_and_export_fax_log_for_multiple_faxes_from_sent_faxes 
        """
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)
        self.fc.nav_to_compose_fax(new_user=True)
        self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], no_faxes=2)
        self.fax_history.load_edit_screen()
        self.fax_history.verify_edit_screen()
        self.fax_history.select_multiple_history_records(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"],
                                                             number_records=2)
        self.fax_history.click_edit_export_fax_log()
        self.preview.verify_preview_screen()

    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_04_verify_edit_and_delete_multiple_faxes_from_sent_faxes(self, tab):
        """
        C16942943 - edit_and_delete_single_fax_from_sent_faxes
        C16942948 - edit_and_delete_multiple_faxes_from_sent_faxes
        """
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)
        self.fc.nav_to_compose_fax(new_user=True)
        if tab == "sent":
            self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], no_faxes=2)
            self.fax_history.load_edit_screen()
            self.fax_history.verify_edit_screen()
            self.fax_history.select_multiple_history_records(self.fax_history.SENT_RECORD_CELL, phone_number=self.recipient_info["phone"],
                                                             number_records=3)
        else:
            self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], option="draft", no_faxes=2)
            self.fax_history.load_edit_screen()
            self.fax_history.verify_edit_screen()
            self.fax_history.select_multiple_history_records(self.fax_history.DRAFT_RECORD_CELL, phone_number=self.recipient_info["phone"],
                                                             number_records=3)
        self.fax_history.click_edit_delete()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.verify_sent_fax_history_list(is_empty=True)
        else:
            self.fax_history.verify_draft_fax_history_list(is_empty=True)
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_05_verify_swipe_delete(self, tab):
        """
        C16942952 - swipe_left_and_delete_fax_from_sent_faxes
        C16942960 - swipe_left_and_delete_fax_from_draft_faxes
        """
        self.fc.go_home(reset=True, stack=self.stack, create_account=True)
        self.fc.nav_to_compose_fax(new_user=True)
        if tab == "sent":
            self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], no_faxes=1)
            self.fax_history.select_tab(self.fax_history.SENT_TAB)
            self.fax_history.open_record_menu_item(self.fax_history.SENT_RECORD_CELL, swipe_direction="left")
        else:
            self.send_fax_and_go_to_fax_history_screen(self.recipient_info["phone"], option = "draft", no_faxes=1)
            self.fax_history.select_tab(self.fax_history.DRAFT_TAB)
            self.fax_history.open_record_menu_item(self.fax_history.DRAFT_RECORD_CELL, swipe_direction="left")
        self.fax_history.click_record_delete_btn()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.verify_sent_fax_history_list(is_empty=True)
        else:
            self.fax_history.verify_draft_fax_history_list(is_empty=True)


    def send_fax_and_go_to_fax_history_screen(self, phone_no=None, option="sent", no_faxes=1):
        """
        option: sent = send fax
                draft = create draft
        """
        for _ in range (no_faxes):
            self.compose_fax.enter_recipient_information(phone_no)
            self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
            self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
            self.fc.select_photo_from_my_photos()
            self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
            self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
            self.compose_fax.verify_compose_fax_screen()
            if option == "sent":
                self.compose_fax.click_send_fax_native_btn()
                self.send_fax_details.verify_send_fax_status(timeout=360, is_successful=True, check_sending=False)
            else:
                self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_SAVE_DRAFT_BTN)
            self.send_fax_details.click_back()
        # verify fax history screen
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()