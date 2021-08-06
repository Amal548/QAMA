from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE
from selenium.common.exceptions import TimeoutException
import pytest
import base64
import os


pytest.app_info = "SMART"

class Test_Suite_01_Android_Welcome(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, record_testsuite_property):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # Define variables
        cls.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]["username"]
        cls.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]["password"]
        record_testsuite_property("suite_test_category", "Welcome")
        
    def test_01_go_home(self):
        #import pdb;pdb.set_trace()
        #Start Recording
        #self.driver.wdvr.start_recording_screen() 
        #self.driver.wdvr.save_screenshot("mycap.png")
        self.fc.flow_load_home_screen(username=self.hpid_username, password=self.hpid_pwd)
        #self.driver.wdvr.save_screenshots("mycap.png")
        #Stop Recording  
        #screen = self.driver.wdvr.stop_recording_screen()
        #file_path = os.path.join("./" , "anyname" + ".mp4")
        #with open(file_path, "wb") as sr:
		#sr.write(base64.b64decode(screen))
       
        #self.driver.wdvr.start_recording_screen()
