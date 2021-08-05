import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.resources.const.android.const import WEBVIEW_URL
from MobileApps.resources.const.android.const import WEBVIEW_CONTEXT
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA
from time import sleep

pytest.app_info = "JWEB"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # Define flows
        cls.auth = cls.fc.fd["auth"]
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.auth_plugin = cls.fc.fd["auth_plugin"]

        test_account_1 = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"]
        cls.hpid_username_1 = test_account_1["username"]
        cls.hpid_family_name_1 = test_account_1["family_name"]
        cls.hpid_given_name_1 = test_account_1["given_name"]
        cls.hpid_pwd_1 = test_account_1["password"]
        cls.hpid_user_id_1 = test_account_1["user_id"]

        test_account_2 = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.hpid_username_2 = test_account_2["username"]
        cls.hpid_family_name_2 = test_account_2["family_name"]
        cls.hpid_given_name_2 = test_account_2["given_name"]
        cls.hpid_pwd_2 = test_account_2["password"]
        cls.hpid_user_id_2 = test_account_2["user_id"]

    def test_01_verify_auth_signin_logout_result_before_after_signin(self):
        """
        verify auth plugin test signin and logout response before and after signing in
        
        TestRails -> C28698045, C28698046, C28698047, C28698048
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_auth_plugin()

        self.auth_plugin.select_auth_logged_in_test()
        assert (self.auth_plugin.auth_logged_in_result()["value"] == \
            saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT)) \
            ["logged_in_result"]["before_sign_in"]["value"])
        
        self.auth_plugin.select_auth_logout_test()
        assert (self.auth_plugin.auth_logout_result()["error"]["code"] ==
            saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT)) \
            ["logout_result"]["before_sign_in"]["error"]["code"])
        
        self.auth_plugin.control_auth_token_switches([True, True, True, False, True])
        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_sign_in_page_item()
        self.auth_plugin.select_auth_get_token_test()
        sleep(3)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)

        sleep(5)
        self.auth_plugin.select_auth_logged_in_test()
        sleep(5)
        assert (self.auth_plugin.auth_logged_in_result()["value"] == \
            saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT)) \
            ["logged_in_result"]["after_sign_in"]["value"])

        self.auth_plugin.select_auth_logout_test()
        assert self.auth_plugin.auth_logout_result() == {}


    def test_02_verify_status_token_disable_all_options(self):
        """
        verify auth plugin, token status after disabling all auth options. 
        testing sign in, create account, no option (test), invalid option
        
        TestRails -> C28714873, C28714874, C28714875, C28714876
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_auth_plugin()
        self.auth_plugin.control_auth_token_switches([False, False, False, False, False])
        network_error_code = saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["network"]["error"]["code"]
        invalid_option_code = saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["invalid_option"]["error"]["code"]
        
        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_sign_in_page_item()
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == network_error_code
        
        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_create_account_page_item()
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == network_error_code

        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_no_option_test_page_item()
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == network_error_code

        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_invalid_test_option_page_item()
        self.auth_plugin.select_auth_get_token_test()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == invalid_option_code


    def test_03_verify_closing_browser_result(self):
        """
        verify auth plugin error result after closing browser
        testing closing browser for sign in, creating account, and no option (test) 

        TestRails -> C28698051, C28698052, C28698053
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_auth_plugin()
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])
        closed_browser_error_code = saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["closed_browser"]["error"]["code"]

        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_sign_in_page_item()
        self.auth_plugin.select_auth_get_token_test()
        self.auth.select_cancel()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == closed_browser_error_code

        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_create_account_page_item()
        self.auth_plugin.select_auth_get_token_test()
        self.auth.select_cancel()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == closed_browser_error_code

        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_no_option_test_page_item()
        self.auth_plugin.select_auth_get_token_test()
        self.auth.select_cancel()
        assert self.auth_plugin.auth_get_token_result()["error"]["code"] == closed_browser_error_code

    def test_04_verify_add_listener_response(self):
        """
        verify auth plugin add listener response
        testing for when a user has signed in, loggged out.
        also testing when a user has logged into an account after already being logged in, and logged out of an account after already being logged in 

        Test -> C28698054, C28698055, C28698056, C28698057
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_auth_plugin()
        self.auth_plugin.select_auth_add_listener_btn()
        self.auth_plugin.control_auth_token_switches([True, True, True, True, True])

        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_sign_in_page_item()
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(WEBVIEW_URL.HPID)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        sleep(10)

        logged_in_listener_text_result = self.auth_plugin.auth_listener_text_result()
        assert logged_in_listener_text_result['account']['accountId'] == self.hpid_user_id_1
        assert logged_in_listener_text_result['account']['emailAddress'] == self.hpid_username_1
        assert logged_in_listener_text_result['account']['familyName'] == self.hpid_family_name_1
        assert logged_in_listener_text_result['account']['givenName'] == self.hpid_given_name_1
        assert logged_in_listener_text_result['isLoggedIn'] == True

        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        assert self.auth_plugin.auth_listener_text_result()['isLoggedIn'] == False

        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_sign_in_page_item()
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(WEBVIEW_URL.HPID)
        self.hpid.login(self.hpid_username_1, self.hpid_pwd_1)
        sleep(10)
        self.auth_plugin.select_auth_user_interaction_entry_point_selector()
        self.auth_plugin.select_auth_sign_in_page_item()
        self.auth_plugin.select_auth_get_token_test()
        self.driver.wait_for_context(WEBVIEW_URL.HPID)
        if self.hpid.verify_hp_id_sign_in(raise_e=False) == False:
            self.hpid.click_back_button()
        self.hpid.login(self.hpid_username_2, self.hpid_pwd_2)
        sleep(10)

        logged_in_listener_text_result = self.auth_plugin.auth_listener_text_result()
        assert logged_in_listener_text_result['account']['accountId'] == self.hpid_user_id_2
        assert logged_in_listener_text_result['account']['emailAddress'] == self.hpid_username_2
        assert logged_in_listener_text_result['account']['familyName'] == self.hpid_family_name_2
        assert logged_in_listener_text_result['account']['givenName'] == self.hpid_given_name_2
        assert logged_in_listener_text_result['isLoggedIn'] == True

        self.auth_plugin.select_auth_logout_test()
        sleep(5)
        assert self.auth_plugin.auth_listener_text_result()['isLoggedIn'] == False
