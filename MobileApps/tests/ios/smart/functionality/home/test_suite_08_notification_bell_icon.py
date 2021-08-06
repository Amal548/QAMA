import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc
import time
pytest.app_info = "SMART"


class Test_Suite_08_Notification_Bell_Icon(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.app_settings = cls.fc.fd["app_settings"]
    
    def test_01_verify_bell_icon_ui(self):
        """
        C27654897 - Test Bell Icon_UI
        C27654918 - Test Close Button
        C28540556 - User Onboarding from Account notifications view
        """
        login_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_02"]
        username, password = login_info["username"], login_info["password"]
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        self.home.select_close()
        self.home.verify_home()
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        self.home.verify_an_element_and_click(self.home.ACCOUNT_BTN)
        self.home.verify_an_element_and_click(self.home.SIGN_IN_BTN)
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=45)
        self.fc.fd["hpid"].verify_hp_id_sign_in()
        self.fc.fd["hpid"].login(username, password)
    
    def test_02_verify_bell_icon_ui_signed_in(self):
        """
        C27654897 - Test Bell Icon_UI
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
    
    def test_03_verify_supplies_btn(self):
        """
        C28540557 -User Onboarding from Supplies notifications view
        """
        login_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_02"]
        username, password = login_info["username"], login_info["password"]
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        self.home.verify_an_element_and_click(self.home.SUPPLIES_BTN)
        self.home.verify_an_element_and_click(self.home.SIGN_IN_BTN)
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=45)
        self.fc.fd["hpid"].verify_hp_id_sign_in()
        self.fc.fd["hpid"].login(username, password)
    
    def test_04_test_settings_btn_bell_icon_ui(self):
        """
        C27654919 - Test Settings Button on Bell Icon UI
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        self.home.select_settings_btn()
        self.fc.fd["app_settings"].verify_notifications_settings_screen()
        self.fc.fd["app_settings"].select_navigate_back()
        self.home.verify_notification_screen()
    
    @pytest.mark.parametrize("selection",["yes", "no"])
    def test_05_verify_modal_on_inbox_tab(self, selection):
        """
        C27654913 - Verify modal on "Inbox" tab
        C27654914 - Verify functionality when tap Yes on modal in Inbox tab
        C27654915 - Verify functionality when tap No on modal in Inbox tab
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        self.home.verify_an_element_and_click(self.home.INBOX_BTN)
        self.home.verify_an_element_and_click(self.home.WELCOME_TO_HP_SMART_INBOX, click=False)
        if selection == "yes":
            self.home.select_yes()
            self.home.select_settings_btn()
            assert self.app_settings.get_switch_status(self.app_settings.PROMOTIONAL_MESSAGE_SWITCH) == 1
        else:
            self.home.select_no_option()
            self.home.select_settings_btn()
            assert self.app_settings.get_switch_status(self.app_settings.PROMOTIONAL_MESSAGE_SWITCH) == 0
    
    def test_06_verify_promotional_messaging_modal_not_shown_again(self):
        """
        C27654916 - Verify promotional messaging modal not shown again
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        self.home.verify_an_element_and_click(self.home.INBOX_BTN)
        self.home.verify_an_element_and_click(self.home.WELCOME_TO_HP_SMART_INBOX, click=False)
        self.home.select_no_option()
        self.home.select_close()
        self.home.verify_home()
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        self.home.verify_an_element_and_click(self.home.INBOX_BTN)
        assert self.home.verify_an_element_and_click(self.home.WELCOME_TO_HP_SMART_INBOX, 
                                                    click=False, raise_e=False) is False
        
    def test_07_verify_print_activity_ui_no_printactivity(self):
        """
        C27654898 - Print_Activity_UI_No_PrintActivity
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        self.home.verify_an_element_and_click(self.home.NO_PRINT_ACTIVITY_TITLE, click=False)
    
    def test_08_verify_user_taps_mobile_fax_under_activity(self):
        """
        C27654920 - Test functionality when user taps Mobile Fax under Activity
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        self.home.verify_an_element_and_click(self.home.MOBILE_FAX_BTN)
        time.sleep(2)
        self.fc.fd["softfax_fax_history"].verify_fax_history_screen(timeout=10)
    
    @pytest.mark.parametrize("button",["account", "supplies"])
    def test_09_verify_tapping_on_accounts_n_supplies_btn_hp_plus(self, button):
        """
        C28475617 - Behavior by tapping on "Account" button (HP+)
        C28475618 - Behavior by tapping on "Supplies" button (HP+)
        """
        login_info = ma_misc.get_hpid_account_info(stack=self.stack, a_type="hp+")
        username, password = login_info["email"], login_info["password"]
        self.fc.go_home(reset=True, button_index=1, username=username, password=password, stack=self.stack, remove_default_printer=False)
        self.home.select_notification_bell()
        self.home.verify_notification_screen()
        if button == "account":
            self.home.verify_an_element_and_click(self.home.ACCOUNT_BTN)
        else:
            self.home.verify_an_element_and_click(self.home.SUPPLIES_BTN)
        self.home.verify_an_element_and_click(self.home.VIEW_NOTIFICATIONS_TITLE, click=False)
        self.home.verify_an_element_and_click(self.home.TOGGLE_MENU)
        self.home.verify_an_element_and_click(self.home.VIEW_NOTIFICATIONS_LINK,click=False)
    



