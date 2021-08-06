import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_01_ECP_Web(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]

    def test_01_go_to_ecp(self):
        self.fc.navigate(self.stack)
        self.login.verify_ecp_login()
        self.login.click_next_btn()
        self.hpid.verify_hp_id_sign_in(timeout=20)
        self.hpid.login(self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.click_home_menu_btn()
        self.home.verify_devices_menu_btn()
        self.home.click_devices_menu_btn()
        self.home.verify_users_menu_btn()
        self.home.click_users_menu_btn()
        self.home.verify_reports_menu_btn()
        self.home.click_reports_menu_btn()
        self.home.verify_support_menu_btn()
        self.home.click_support_menu_btn()
        self.home.logout()
        import pdb 
        pdb.set_trace()