import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_01_ECP_Login(object):

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

    def test_01_hero_flow_login(self):
        #Test case https://testrail.tools.cso-hp.com/index.php?/cases/view/29236562
        #Verfy can log in with a valid account
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_notification_mfe_card()
        sleep(2)
        
    def test_02_logout(self):
        #Test case https://testrail.tools.cso-hp.com/index.php?/cases/view/29236606
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.logout()
        self.login.verify_ecp_login()
        self.login.enter_email_address(self.hpid_username)
        self.login.click_next_btn()
        self.hpid.verify_hp_id_sign_in()