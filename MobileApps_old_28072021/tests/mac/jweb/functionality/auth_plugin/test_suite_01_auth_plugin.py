import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.mac.const import TEST_DATA
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA

pytest.app_info = "JWEB"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, mac_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = mac_jweb_setup

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
        self.auth_plugin.select_auth_logout_open()
        self.auth_plugin.select_auth_logout_test()
        print(self.auth_plugin.auth_logout_result())
        assert (self.auth_plugin.auth_logout_result()["error"]["code"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logout_result"]["error"]["code"]) \
               or (self.auth_plugin.auth_logout_result() == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logout_result"]["empty_string"])
        self.auth_plugin.select_auth_logout_open()
        self.auth_plugin.select_auth_logged_in_open()
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logged_in_result"]["value"]
        self.auth_plugin.select_auth_logged_in_open()
        self.home.click_close_btn()

    def test_02_verify_network_access_disable(self):
        """
        verify auth plugin network access disable
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        self.auth_plugin.select_auth_get_token_open()
        self.auth_plugin.control_auth_token_switches([True,True,False,True,False])
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["network"]["error"]["code"]
        self.home.click_close_btn()

    def test_03_verify_user_interaction_disable(self):
        """
        verify auth plugin user interaction disable
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        self.auth_plugin.select_auth_get_token_open()
        self.auth_plugin.control_auth_token_switches([True, False, True, True, False])
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["user_interaction"]["error"]["code"]
        self.home.click_close_btn()

    def test_04_verify_hpid_sign_in(self):
        """
        verify auth plugin hpid sign in
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        self.auth_plugin.select_auth_logout_open()
        self.auth_plugin.select_auth_logout_test()
        self.auth_plugin.select_auth_logout_open()
        self.auth_plugin.select_auth_get_token_open()
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
        self.home.click_close_btn()
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_plugin()
        self.auth_plugin.select_auth_logged_in_open()
        self.auth_plugin.select_auth_logged_in_test()
        assert self.auth_plugin.auth_logged_in_result()["value"] != \
               saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logged_in_result"]["value"]
        self.home.click_close_btn()