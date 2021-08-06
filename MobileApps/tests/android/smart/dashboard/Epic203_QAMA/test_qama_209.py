from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES , LAUNCH_ACTIVITY
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE
from selenium.common.exceptions import TimeoutException
import pytest
import time

pytest.app_info = "SMART"

class Test_Suite_Android_HPSmart(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        
        # Define variables
        cls.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_10"][
            "username"]
        cls.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_10"][
                 "password"]
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        
        cls.sender_name = "sender"
        cls.sender_number = "2125551111"
        cls.receiver_name = "receiver"
        cls.receiver_number = "2125551235"

    def test_enable_tile(self):
        import pdb ; pdb.set_trace()
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.fc.fd[FLOW_NAMES.HOME].welcome_screen()
        self.fc.fd[FLOW_NAMES.WELCOME].skip_shared_usage_screen()
        self.fc.fd[FLOW_NAMES.WELCOME].skip_sign_in()
        self.driver.swipe()
        self.fc.fd[FLOW_NAMES.HOME].select_personalize_tiles()
        self.fc.fd[FLOW_NAMES.PERSONALIZE].toggle_tile_by_name("Print Documents")
        self.fc.fd[FLOW_NAMES.PERSONALIZE].select_back()

    def test_first_flow(self):
        import pdb ; pdb.set_trace()
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.driver.swipe()
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Print Documents")
        self.fc.flow_app_settings_sign_in_hpid(self.hpid_username , self.hpid_pwd)
        self.driver.back()
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Print Documents")
        self.fc.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item("my_photos_txt")
        self.fc.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index("png")
        self.fc.fd[FLOW_NAMES.PREVIEW].select_bottom_nav_btn("fax_btn")
        time.sleep(10)
        self.fc.fd[FLOW_NAMES.SOFTFAX_WELCOME].skip_get_started_screen()
        self.fc.fd[FLOW_NAMES.SOFTFAX_WELCOME].skip_welcome_screen()
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number, self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(timeout=240, is_successful=False)
        #self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].select_history_record("sent_history_record_cell", self.receiver_number)
        self.fc.flow_home_log_out_hpid_from_app_settings()
