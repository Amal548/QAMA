import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from time import sleep

pytest.app_info = "JAUTH"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, ios_jauth_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jauth_setup

        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.settings = cls.fc.fd["settings"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.account_info = cls.fc.fd["account_info"]

        # Define variables
        cls.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"][
            "username"]
        cls.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"][
            "password"]
        cls.hpid_user_id = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_04"][
            "user_id"]

    def test_01_verify_network_access_disable(self):
        """
        verify network access feature disable
        """
        self.fc.go_to_home_screen()
        self.home.select_settings()
        self.settings.control_auth_token_switches([True, False, False, False, False, False])
        self.settings.select_done()
        self.home.select_add()
        assert self.home.sign_in_result() == self.home.SIGN_IN_ERROR_RESULTS.get('network')
        self.home.select_accounts()


    def test_02_verify_user_interation_disable(self):
        """
        verify user interaction feature disable
        """
        self.fc.go_to_home_screen()
        self.home.select_settings()
        self.settings.control_auth_token_switches([False, True, False, False, False, False])
        self.settings.select_done()
        self.home.select_add()
        assert self.home.sign_in_result() == self.home.SIGN_IN_ERROR_RESULTS.get('user_interaction')
        self.home.select_accounts()

    def test_03_verify_hpid_sign_in(self):
        """
        verify hpid sign in flow
        """
        self.fc.go_to_home_screen()
        if self.home.verify_empty_account_list(raise_e=False) == False:
            self.home.select_account_info(option=self.hpid_username)
            self.account_info.select_logout_button()
            self.home.select_continue()
            self.home.verify_empty_account_list()
        self.home.select_settings()
        self.settings.control_auth_token_switches([False, False, False, True, False, False])
        self.settings.select_done()
        self.home.select_add()
        self.home.select_continue()
        self.hpid.dismiss_safari_connection_not_private()
        self.home.click_visit_website_button()
        self.hpid.login(self.hpid_username,self.hpid_pwd)
        #hpid sign in takes longer time, so is the delay
        sleep(45)
        self.home.select_accounts()
        self.home.select_account_info(option=self.hpid_username)
        self.account_info.verify_email_id(id=self.hpid_username)
        self.account_info.verify_user_id(id=self.hpid_user_id)
        self.home.select_settings()
        self.settings.control_auth_token_switches([False, False, False, True, False, True])
        self.settings.select_done()
        self.account_info.select_get_token()
        token_result_1 = self.home.sign_in_result()
        assert token_result_1 != self.home.SIGN_IN_ERROR_RESULTS.get('none')
        self.account_info.select_jarvis_auto()
        self.home.select_settings()
        self.settings.control_auth_token_switches([False, False, False, True, True, False])
        self.settings.select_done()
        self.account_info.select_get_token()
        token_result_2 = self.home.sign_in_result()
        assert self.home.sign_in_result() != token_result_1
        self.account_info.select_jarvis_auto()
        self.home.select_settings()
        self.settings.control_auth_token_switches([False, False, False, True, False, True])
        self.settings.select_done()
        self.account_info.select_get_token()
        assert self.home.sign_in_result() != token_result_2
        self.account_info.select_jarvis_auto()
        self.account_info.select_logout_button()
        self.home.select_continue()
        self.home.verify_empty_account_list()

    def test_04_verify_account_creation_link(self):
        self.fc.go_to_home_screen()
        self.home.select_settings()
        self.settings.control_auth_token_switches([False, False, False, True, False, True])
        self.settings.select_done()
        self.home.select_add()
        self.home.select_continue()
        self.hpid.dismiss_safari_connection_not_private()
        self.home.click_visit_website_button()
        self.home.select_cancel()
        self.home.select_accounts()
        self.home.select_settings()
        self.settings.control_auth_token_switches([False, False, True, True, False, True])
        self.settings.select_done()
        self.home.select_add()
        self.home.select_continue()

    def test_05_verify_start_on_create_account(self):
        self.fc.go_to_home_screen()
        self.home.select_settings()
        self.settings.control_auth_token_switches([False, False, True, True, False, True])
        self.settings.select_done()
        self.home.select_add()
        self.home.select_continue()
        self.hpid.dismiss_safari_connection_not_private()
        self.home.click_visit_website_button()
        assert self.hpid.verify_create_an_account_page() == False
        self.home.select_cancel()
        self.home.select_accounts()
        self.home.select_settings()
        self.settings.control_auth_token_switches([False, False, True, False, False, True])
        self.settings.select_done()
        self.home.select_add()
        self.home.select_continue()
        #hpid takes long time to load create account page
        sleep(15)
        assert self.hpid.verify_create_an_account_page() != False
        self.home.select_cancel()
        self.home.select_accounts()