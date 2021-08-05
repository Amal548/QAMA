import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from time import sleep
from MobileApps.resources.const.windows.const import TEST_DATA
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA

pytest.app_info = "JWEB"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_jweb_setup

        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]

        # Define variables
        cls.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"]["username"]
        cls.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"]["password"]
        cls.hpid_user_id = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"]["user_id"]

        def clean_up_class():
            cls.fc.close_jweb_app()

        request.addfinalizer(clean_up_class)

    def test_01_verify_auth_login_logout_result(self):
        """
        verify auth plugin test login
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        if not self.auth_plugin.verify_logout_button():
            self.auth_plugin.select_auth_logout_open()
        self.auth_plugin.select_auth_logout_test()
        assert (self.auth_plugin.auth_logout_result()["error"]["code"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logout_result"]["error"]["code"]) \
               or (self.auth_plugin.auth_logout_result() == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logout_result"]["empty_string"])
        self.auth_plugin.select_auth_logout_open()
        if not self.auth_plugin.verify_logged_in_button():
            self.auth_plugin.select_auth_logged_in_open()
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logged_in_result"]["value"]
        self.auth_plugin.select_auth_logged_in_open()

    def test_02_verify_network_access_disable(self):
        """
        verify auth plugin network access disable
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        if not self.auth_plugin.verify_get_token_button():
            self.auth_plugin.select_auth_get_token_open()
        self.driver.swipe(x_offset=0, y_offset=90)
        self.auth_plugin.control_auth_token_switches([True,True,False,True,False])
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["network"]["error"]["code"]        
        self.driver.swipe(x_offset=0, y_offset=-90)
        self.auth_plugin.select_auth_get_token_open()

    def test_03_verify_user_interaction_disable(self):
        """
        verify auth plugin user interaction disable
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        if not self.auth_plugin.verify_get_token_button():
            self.auth_plugin.select_auth_get_token_open()
        self.driver.swipe(x_offset=0, y_offset=-90)
        self.auth_plugin.control_auth_token_switches([True, False, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["user_interaction"]["error"]["code"]
        self.driver.swipe(x_offset=0, y_offset=90)
        self.auth_plugin.select_auth_get_token_open()

    def test_04_verify_hpid_sign_in(self):
        """
        verify auth plugin hpid sign in
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        if not self.auth_plugin.verify_logout_button():
            self.auth_plugin.select_auth_logout_open()
        self.auth_plugin.select_auth_logout_test()
        self.driver.swipe(x_offset=0, y_offset=-90)
        self.auth_plugin.select_auth_logout_open()
        if not self.auth_plugin.verify_get_token_button():
            self.auth_plugin.select_auth_get_token_open()
        self.driver.swipe(x_offset=0, y_offset=-45)
        self.auth_plugin.control_auth_token_switches([True, False, False, True, False])
        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_sign_in_page_item()
        self.auth_plugin.select_auth_get_token_test()
        self.hpid.login(self.hpid_username, self.hpid_pwd)
        assert self.auth_plugin.auth_get_token_result()["account"]["emailAddress"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logged_in_result"]["account"]["emailAddress"]
        assert self.auth_plugin.auth_get_token_result()["account"]["accountId"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logged_in_result"]["account"]["accountId"]
        token_result_1 = self.auth_plugin.auth_get_token_result()["expiresAt"]
        assert token_result_1 != saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logged_in_result"]["value"]
        self.auth_plugin.control_auth_token_switches([False, False, False, True, True])
        self.auth_plugin.select_auth_get_token_test()
        token_result_2 = self.auth_plugin.auth_get_token_result()["expiresAt"]
        assert self.auth_plugin.auth_get_token_result()["expiresAt"] != token_result_1
        self.auth_plugin.control_auth_token_switches([True, False, False, True, False])
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["expiresAt"] != token_result_2
        self.driver.swipe(x_offset=0, y_offset=90)
        self.auth_plugin.select_auth_logout_open()
        self.home.click_close_btn()
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        self.auth_plugin.select_auth_logged_in_open()
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"] != \
               saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logged_in_result"]["value"]
        self.home.click_close_btn()

    def test_05_verify_account_creation_link(self):
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        if not self.auth_plugin.verify_logout_button():
            self.auth_plugin.select_auth_logout_open()
        self.auth_plugin.select_auth_logout_test()
        self.driver.swipe(x_offset=0, y_offset=-90)
        self.auth_plugin.select_auth_logout_open()
        if not self.auth_plugin.verify_get_token_button():
            self.auth_plugin.select_auth_get_token_open()
        self.driver.swipe(x_offset=0, y_offset=-45)
        self.auth_plugin.control_auth_token_switches([True, False, False, True, False])
        self.home.select_add()
        assert self.hpid.verify_dont_have_account_signup_link() != False
        self.home.select_cancel()
        self.home.select_accounts()
        self.home.select_settings()
        self.auth_plugin.control_auth_token_switches([True, False, False, True, True])
        self.settings.select_done()
        self.home.select_add()
        self.home.select_continue()
        assert self.hpid.verify_dont_have_account_signup_link() == False

    @pytest.mark.skip("JIRA #JWEB-480")
    def test_06_verify_start_on_create_account(self):
        self.fc.flow_load_home_screen()
        self.home.select_settings()
        self.auth_plugin.control_auth_token_switches([True, False, False, True, True])
        self.settings.select_done()
        self.home.select_add()
        self.home.select_continue()
        self.hpid.dismiss_safari_connection_permission()
        self.home.driver.click_visit_website_button()
        assert self.hpid.verify_create_an_account_page() == False
        self.home.select_cancel()
        self.home.select_accounts()
        self.home.select_settings()
        self.auth_plugin.control_auth_token_switches([True, False, False, True, False])
        self.settings.select_done()
        self.home.select_add()
        self.home.select_continue()
        assert self.hpid.verify_create_an_account_page() != False
        self.home.select_cancel()
        self.home.select_accounts()