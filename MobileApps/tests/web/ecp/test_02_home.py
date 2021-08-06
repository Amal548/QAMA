import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_02_ECP_Home(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]

    def test_01_verify_side_menu(self):
        #Test case: https://testrail.tools.cso-hp.com/index.php?/cases/view/29092660
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_home_menu_btn()
        self.home.verify_devices_menu_btn()
        self.home.verify_users_menu_btn()
        self.home.click_solutions_menu_expand_btn()
        self.home.verify_security_sub_menu_btn()
        self.home.verify_hp_room_sub_menu_btn()
        self.home.verify_reports_menu_btn()
        self.home.click_account_menu_expand_btn()
        self.home.verify_account_profile_sub_menu_btn()
        self.home.verify_support_menu_btn()

    def test_02_verify_notification_mfe_dropdown(self):
        #Test case: https://testrail.tools.cso-hp.com/index.php?/cases/view/29236612
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_notification_mfe_card()
        self.home.verify_notification_mfe_filter_dropdown()
        