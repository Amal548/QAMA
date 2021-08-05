import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA


pytest.app_info = "JWEB"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.browser_plugin = cls.fc.fd["browser_plugin"]
        cls.security_gateway = cls.fc.fd["security_gateway"]
        cls.system = cls.fc.fd["auth"]

        def clean_up_class():
            cls.fc.close_app()

        request.addfinalizer(clean_up_class)

    def test_01_verify_browser_test_plugin_service_login(self):
        """
        verify browser plugin test
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_auth_browser_plugin()
        self.browser_plugin.select_browser_open()
        self.browser_plugin.select_browser_test()
        self.system.select_continue()
        self.security_gateway.select_redirect_me()
        assert self.browser_plugin.browser_sign_in_result() == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.JWEB_ACCOUNT))["logged_in_result"]["browser_token"]