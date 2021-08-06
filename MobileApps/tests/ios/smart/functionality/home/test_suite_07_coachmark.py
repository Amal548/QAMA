import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*
from SAF.misc import saf_misc
import time

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_07_Coachmark(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.home = cls.fc.fd["home"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_coachmark_notification_is_invisible_second_time(self):
        """
        Coachmark notification when sign In - C28044108
        Coachmark notification is not shown when sign in for 2-nd time- C28044100
        """
        login_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_02"]
        username, password = login_info["username"], login_info["password"]
        self.fc.go_home(button_index=2, stack=self.stack)
        self.home.select_create_account_icon()
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=20)
        self.fc.fd["hpid"].verify_hp_id_sign_up()
        self.fc.fd["hpid"].click_sign_in_link_from_create_account()
        time.sleep(2)
        self.fc.fd["hpid"].login(username, password)
        self.fc.clear_popups_on_first_login(smart_task=True, coachmark=False)
        assert self.home.verify_tap_account_coachmark_popup(raise_e=False) is not False
        self.fc.fd["home"].dismiss_tap_account_coachmark()
        # start with testcase C28044100
        self.home.select_app_settings()
        self.fc.fd["app_settings"].sign_out_from_hpc()
        self.home.select_home_icon()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(HOME_TILES.TILE_PRINT_PHOTOS)
        self.fc.login_value_prop_screen(tile=True, stack=self.stack)
        self.fc.fd["photos"].select_allow_access_to_photos_popup(raise_e=True)
        assert self.home.verify_tap_account_coachmark_popup(raise_e=False) is False

    def test_02_coachmark_invisible_for_new_user_after_signout(self):
        """
        Coachmark notification for new user- C28044099
        Coachmark is not shown when sign out- C28044101
        """
        self.fc.go_home(reset=True, button_index=2, stack=self.stack)
        self.fc.fd["home"].select_create_account_icon()  
        self.fc.create_new_user_account(coachmark=False)
        self.home.verify_tap_account_coachmark_popup()
        self.home.dismiss_tap_account_coachmark()
        assert self.home.verify_tap_account_coachmark_popup(raise_e=False) is False
        self.home.select_app_settings()
        self.fc.fd["app_settings"].sign_out_from_hpc()
        self.home.select_home_icon()
        assert self.home.verify_tap_account_coachmark_popup(raise_e=False) is False
