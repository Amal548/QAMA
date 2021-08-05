from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE
from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.web.hp_connect.hp_connect import HPConnect
import pytest

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}

class Test_Suite_01_HPID_Android(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, record_testsuite_property):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define variables
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        record_testsuite_property("suite_test_category", "HPID")
    
    def test_01_hpid_sign_in(self):
        self.fc.flow_load_home_screen()

    def test_02_hpid_sign_out(self):
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_APP_SETTINGS_BTN)
        self.app_settings.sign_out_hpc_acc()

    def test_03_hpid_sign_up(self):
        self.driver.clear_app_cache(PACKAGE.SMART.get(self.driver.session_data["pkg_type"], PACKAGE.SMART["default"]))
        self.fc.flow_load_home_screen(create_acc=True)