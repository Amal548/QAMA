import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
pytest.app_info = "ECP"

class Test_03_ECP_Devices_List(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.devices = self.fc.fd["devices"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]

    
    def test_01_verify_pagination(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29136330
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29136323
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_devices_menu_btn()
        self.devices.verify_all_page_size_options([25, 50, 75, 100])
        self.devices.verify_table_displaying_correctly(25, page=1)
        self.devices.verify_table_displaying_correctly(50, page=1)
        self.devices.verify_table_displaying_correctly(75, page=1)
        self.devices.verify_table_displaying_correctly(100, page=1)
  
    
    def test_02_verify_refresh(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29092858
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        cur_time = self.devices.get_sync_time_info()
        sleep(1)
        self.devices.click_refresh_button()
        new_time = self.devices.get_sync_time_info()
        assert saf_misc.compare_time_in_utc(new_time.split(": ")[1], self.driver.get_timezone(), "%d %B %Y | %I:%M:%S %p") == True
        assert new_time != cur_time

    
    def test_03_verify_default_sort(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29153765
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.verify_table_sort("status", ["Online", "Offline"])

    def test_04_verify_sort_change(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29153767
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.click_table_header_by_name("status")
        self.devices.verify_device_page()
        self.devices.verify_table_sort("status", ["Offline", "Online"])

    """
    def test_05_verify_status(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093824
        #Need to verify against real device which is a total nightmare
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_devices_menu_btn()
    """

    def test_06_verify_hero_flow_search(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29092859
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device("Laser")
        self.devices.verify_table_displaying_correctly(100, page=1)
        self.devices.verify_device_page()
        self.devices.verify_search_results("Laser")

    def test_07_verify_error_case_search(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093896
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_devices_menu_btn()
        self.devices.verify_device_page()
        self.devices.search_device("InvalidData")
        self.devices.verify_table_displaying_correctly(100, page=1)