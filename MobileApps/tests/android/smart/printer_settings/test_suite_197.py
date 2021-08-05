from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from SPL.driver.reg_printer import RegPrinter as reg_printer
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES , LAUNCH_ACTIVITY , TILE_NAMES 
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE, WEBVIEW_URL , WEBVIEW_CONTEXT
from selenium.common.exceptions import TimeoutException
import pytest
import time

pytest.app_info = "SMART"

class Test_Suite_Android_HPSmart(object):
    @pytest.fixture(scope="class", autouse="true")
    #def class_setup(cls, request, android_smart_setup):
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        cls.printer_ip = cls.p.p_obj.ipAddress
        #cls.claim_code = cls.p.return_claim_code()
        #cls.printer_status = cls.p.get_printer_status()

        # Define variables
        cls.fc.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_07"]["username"]
        cls.fc.hpid_password = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_07"]["password"]
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])

    #def test_claim(self):
    #    print(self.claim_code)
    #    print(self.printer_status)
 
    def test_add_printer(self):
        #import pdb ; pdb.set_trace()
        #self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        #self.fc.fd[FLOW_NAMES.WEB_SMART_WELCOME].click_continue_btn()
        #self.fc.fd[FLOW_NAMES.WELCOME].skip_shared_usage_screen()
        self.fc.flow_load_home_screen()
        #self.fc.flow_load_home_screen()
        #self.fc.skip_welcome_screen()
        self.fc.fd[FLOW_NAMES.HOME].verify_add_new_printer()
        self.fc.fd[FLOW_NAMES.HOME].select_big_add_icon()
        self.fc.fd[FLOW_NAMES.PRINTERS].select_printer(self.printer_ip, is_searched=True, keyword=self.printer_ip)
    
    def test_status_printer(self):
        #self.fc.flow_home_smart_dashboard("hp+")
        self.fc.flow_load_home_screen()
        #import pdb ; pdb.set_trace()
        #self.fc.fd[FLOW_NAMES.HOME].verify_ready_printer_status()
        self.fc.fd[FLOW_NAMES.HOME].load_printer_info()
        self.fc.fd[FLOW_NAMES.PRINTER_SETTINGS].verify_ready_status()
