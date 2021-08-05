from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, LAUNCH_ACTIVITY 
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE, WEBVIEW_CONTEXT, WEBVIEW_URL
from selenium.common.exceptions import TimeoutException , NoSuchElementException
import pytest
import time

pytest.app_info = "SMART"

class Test_Suite_Android_HPSmart(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        
        # Variables declaration
        cls.fc.hpid_username1 = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_12"]["username"]
        cls.fc.hpid_password1 = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_12"]["password"]
        cls.fc.hpid_username2 = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_12"]["username"]
        cls.fc.hpid_password2 = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_12"]["password"]
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        cls.sender_name = "sender"
        cls.sender_number = "2125551111"
        cls.receiver_name = "receiver"
        cls.receiver_number = "2125551235"

    def test_enable_tile(self):
        #import pdb ; pdb.set_trace()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        #self.fc.flow_load_home_screen()
        self.fc.fd[FLOW_NAMES.HOME].select_personalize_tiles()
        self.fc.fd[FLOW_NAMES.PERSONALIZE].toggle_tile_by_name("Print Documents")

    @pytest.mark.parametrize("permission" , ["True", "False"])
    def test_first_flow(self , permission):
        '''
          1. Launch HP Smart app
          2. Select the tile
          3. Verify OWS screen
          4. Select Sign in button
          5. Handle Chrome welcome screen
          6. Verify Sign in screen
          7. Login to HP
          8. Select My Photos folder
          9. Select a jpg image
          10. Select the fax button
        '''
        import pdb ; pdb.set_trace()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        #self.fc.flow_load_home_screen()
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Print Documents")
        #self.fc.verify_invisible_transition_screen()
        self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(tile=True, timeout=60)
        self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=1)
        #self.driver.wdvr.find_element_by_xpath("//android.widget.Button[@text = 'Sign In']").click()
        self.fc.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
        #self.driver.wdvr.find_element_by_xpath("//android.widget.Button[@resource-id = 'onetrust-accept-btn-handler']").click()
        self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
        if permission == True:
            self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username1, self.fc.hpid_password1)
        else:
            self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username2, self.fc.hpid_password2)
        try:
            self.fc.fd[FLOW_NAMES.UCDE_PRIVACY].skip_ucde_privacy_screen(timeout=30)
        #except NoSuchElementException:
        except:
            pass
        self.fc.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item("my_photos_txt")
        self.fc.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index("png")
        self.fc.fd[FLOW_NAMES.PREVIEW].select_bottom_nav_btn("fax_btn")
        time.sleep(10)
        self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].skip_get_started_screen()
        self.fc.fd[FLOW_NAMES.SOFTFAX_WELCOME].skip_welcome_screen(is_hipaa=permission)
        if permission == "True":
            #self.driver.wdvr.switch_to.context("WEBVIEW")
            #self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX_OFFER , timeout=30)
            self.driver.wait_for_context("sws/terms")
            self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].context = {"url": "sws/terms"}
            self.driver.wdvr.switch_to.context("WEBVIEW")
            self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].enroll_business_associate_agreement("test_name" , "test@testqama.com", "test_entity")
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number, self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        if self.fc.fd[FLOW_NAMES.COMPOSE_FAX].verify_file_added() == False:
            self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_add_files_option_btn("files_photos_btn")
            self.fc.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item("my_photos_txt")
            self.fc.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index("png")
            self.fc.fd[FLOW_NAMES.PREVIEW].select_next()
            time.sleep(10)
        name , page = self.fc.fd[FLOW_NAMES.COMPOSE_FAX].get_added_file_information()
        assert name != "" and page != ""
        assert self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax() != False
        self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=False , check_sending=True)
        assert self.driver.get_attribute("delivery_failed_status" , "id") == "statusTitleCalldropped" or self.driver.get_attribute("delivery_failed_status" , "id") == "statusTitleNo-answer"
        self.fc.flow_home_log_out_hpid_from_app_settings()
