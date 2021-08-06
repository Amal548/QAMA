from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE
from selenium.common.exceptions import TimeoutException
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_Android_Welcome(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, record_testsuite_property):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # Define variables
        record_testsuite_property("suite_test_category", "Welcome")
        
    def test_01_go_home(self):
        self.fc.flow_load_home_screen()