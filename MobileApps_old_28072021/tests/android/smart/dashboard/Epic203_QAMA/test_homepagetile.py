from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE
from selenium.common.exceptions import TimeoutException
#from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import pytest
import os
import base64
import time

pytest.app_info = "SMART"

class Test_Suite_01_Android_Welcome(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        # Define variables
        cls.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_06"]["username"]
        cls.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_06"]["password"]
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        
    def test_click_smarttask_tile(self):
        #import pdb;pdb.set_trace()     
        self.fc.flow_load_home_screen(username=self.hpid_username, password=self.hpid_pwd)      
        self.driver.swipe() 
        #self.driver.wdvr.save_screenshot('mycap3.png')       
        #self.fc.fd[FLOW_NAMES.HOME].ptr_tile_personalize() 
        self.fc.fd[FLOW_NAMES.HOME].select_personalize_tiles()	
        self.fc.fd[FLOW_NAMES.PERSONALIZE].select_back()
        self.driver.swipe()
        self.driver.wdvr.save_screenshot('mycap4.png')       
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].check_and_enable_tile("Mobile Fax")
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].flow_home_enable_softfax_tile()
        import pdb;pdb.set_trace()
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Smart Tasks")
        self.driver.wdvr.save_screenshot('mycap5.png')       
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].get_enabled_tiles_list()
        self.fc.fd[FLOW_NAMES.PERSONALIZE].select_back()
        self.driver.swipe()
