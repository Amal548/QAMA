from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES , LAUNCH_ACTIVITY , TILE_NAMES 
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE, WEBVIEW_CONTEXT
from selenium.common.exceptions import TimeoutException , InvalidSessionIdException , WebDriverException
import pytest
import time

pytest.app_info = "SMART"

class Test_Suite_Android_HPSmart(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
    #def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        cls.printer_ip = cls.p.p_obj.ipAddress


        # Define variables
        cls.fc.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_07"][
            "username"]
        cls.fc.hpid_password = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_07"][
                 "password"]
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        cls.sender_name = "sender" 
        cls.receiver_name = "receiver"
        cls.sender_number = "2125551111"
        cls.receiver_number = "2083739237"
        cls.receiver_fake_number = "2125551235"

    @pytest.mark.steps
    def test_add_printer(self):
        self.fc.flow_load_home_screen()
        #self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.fd[FLOW_NAMES.HOME].verify_add_new_printer()
        self.fc.fd[FLOW_NAMES.HOME].select_big_add_icon()
        self.fc.fd[FLOW_NAMES.PRINTERS].select_printer(self.printer_ip, is_searched=True, keyword=self.printer_ip)
        self.fc.flow_home_log_out_hpid_from_app_settings()

    @pytest.mark.steps 
    def test_enable_tiles(self):
        #import pdb ; pdb.set_trace()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.fd[FLOW_NAMES.HOME].select_personalize_tiles()
        #self.driver.wdvr.find_element_by_xpath("//android.widget.Switch[@resource-id='com.hp.printercontrol.debug:id/generic_switch' and ../android.widget.TextView[@text='Mobile Fax']]").click()
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].toggle_tile_by_name(self.driver.return_str_id_value(TILE_NAMES.FAX), on=True)
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].toggle_tile_by_name(self.driver.return_str_id_value(TILE_NAMES.PRINT_DOCUMENTS), on=True)
        self.fc.fd[FLOW_NAMES.PERSONALIZE].toggle_tile_by_name("Mobile Fax")
        self.fc.fd[FLOW_NAMES.PERSONALIZE].toggle_tile_by_name("Printer Scan")

    #@pytest.mark.steps
    def test_first_flow(self):
        #self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Mobile Fax")
        #self.fc.verify_invisible_transition_screen()
        try:
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(tile=True, timeout=60)
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=1)
            self.fc.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
            self.driver.wait_for_context("WEBVIEW_chrome")
            #self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
            #self.fc.fd[FLOW_NAMES.HP_CONNECT].accept_privacy_popup()
            self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username,self.fc.hpid_password)
            time.sleep(5)
            if self.fc.fd[FLOW_NAMES.UCDE_PRIVACY].verify_ucde_privacy_screen():
                self.fc.fd[FLOW_NAMES.UCDE_PRIVACY].skip_ucde_privacy_screen(timeout=30)
            self.fc.fd[FLOW_NAMES.HOME].check_run_time_permission_photo_ga()
            self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].select_accept_cookies()
        except:
            pass
        self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].skip_get_started_screen()
        self.fc.fd[FLOW_NAMES.SOFTFAX_WELCOME].skip_welcome_screen(is_hipaa=True)
        time.sleep(5)
        self.driver.wait_for_context("sws/terms")
        self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].context = {"url": "sws/terms"}
        self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].enroll_business_associate_agreement("test_name" , "test@testqama.com", "test_entity", "03/5/2021")
        self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].click_compose_new_fax()
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_menu_option_btn("menu_clear_fields")
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number, self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_add_files_option_btn("files_photos_btn")
        self.fc.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item("my_photos_txt")
        self.fc.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index("png")
        self.fc.fd[FLOW_NAMES.PREVIEW].select_next()
        name , page = self.fc.fd[FLOW_NAMES.COMPOSE_FAX].get_added_file_information()
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        #self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=True , check_sending=False)
        self.fc.flow_home_log_out_hpid_from_app_settings()

    #@pytest.mark.steps
    @pytest.mark.parametrize("file_type" , ["png" , "jpg"])
    def test_files(self , file_type ):
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Mobile Fax")
        #import pdb ; pdb.set_trace()
        try: 
            #self.fc.verify_invisible_transition_screen()
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(tile=True, timeout=60)
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=1)
            self.fc.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
            self.driver.wait_for_context("WEBVIEW_chrome")
            #self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
            self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username,self.fc.hpid_password)
            self.driver.wait_for_context("sws/terms")
            self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].context = {"url": "sws/terms"}
            self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].select_accept_cookies()
            self.fc.fd[FLOW_NAMES.SOFTFAX_OFFER].skip_get_started_screen()
            self.fc.fd[FLOW_NAMES.SOFTFAX_WELCOME].skip_welcome_screen(is_hipaa=False)
            self.fc.fd[FLOW_NAMES.HOME].check_run_time_permission_photo_ga()
        except:
            pass
        try:
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].verify_fax_history_screen(timeout=15)
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].click_compose_new_fax()
        except TimeoutException:
            pass
        #time.sleep(5)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_menu_option_btn("menu_clear_fields")
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number, self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_add_files_option_btn("files_photos_btn")
        self.fc.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item("my_photos_txt")
        self.fc.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index(file_type)
        #self.fc.fd[FLOW_NAMES.PREVIEW].select_edit()
        self.fc.fd[FLOW_NAMES.PREVIEW].select_preview_image_opts_btn("edit_btn")
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_main_option("edit_options_crop_txt")
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_main_option("square_txt")
        self.fc.fd[FLOW_NAMES.EDIT].apply_crop_rotate()
        self.fc.fd[FLOW_NAMES.EDIT].apply_crop_flip()
        self.fc.fd[FLOW_NAMES.EDIT].apply_crop_scale_picker()
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_done()
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_main_option("edit_options_text_txt")
        self.fc.fd[FLOW_NAMES.EDIT].add_txt_string("THIS IS EDITED")
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_done()
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_main_option("edit_options_filters_txt")
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_main_option("light_blue_color")
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_done()
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_main_option("edit_options_adjust_txt")
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_main_option("concert_option")
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_done()
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_done()
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_done()
        time.sleep(5)
        self.fc.fd[FLOW_NAMES.PREVIEW].select_next()
        time.sleep(5)
        #self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        #self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=True , check_sending=False)
        self.driver.wdvr.save_screenshot("test_qama_success.png")
        self.fc.flow_home_log_out_hpid_from_app_settings()

    #@pytest.mark.steps
    def test_camera_scan(self):     
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Mobile Fax")
        #self.fc.verify_invisible_transition_screen()
        try:
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(tile=True, timeout=60)
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=1)
            self.fc.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
            #time.sleep(5)
            self.driver.wait_for_context("WEBVIEW_chrome")
            #self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
            self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username,self.fc.hpid_password)
            time.sleep(5)
            self.fc.fd[FLOW_NAMES.HOME].check_run_time_permission_photo_ga()
        except:
            pass
        try:
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].verify_fax_history_screen(timeout=15)
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].click_compose_new_fax()
        except TimeoutException:
            pass
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_menu_option_btn("menu_clear_fields")
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number, self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        #import pdb ; pdb.set_trace()
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_add_files_option_btn("camera_btn")
        #self.fc.fd[FLOW_NAMES.CAMERA_SCAN].select_camera_access_allow()
        #self.fc.fd[FLOW_NAMES.CAMERA_SCAN].select_camera_permission_allow_btn()
        #self.driver.wdvr.find_element_by_xpath("//android.widget.Button[@text = 'ALLOW']").click()
        #self.fc.fd[FLOW_NAMES.CAMERA_SCAN].take_picture()
        self.fc.fd[FLOW_NAMES.CAMERA_SCAN].capture_photo(mode="photo_btn")
        self.fc.fd[FLOW_NAMES.CAMERA_SCAN].select_adjust_full_option_btn()
        self.fc.fd[FLOW_NAMES.CAMERA_SCAN].select_adjust_next_btn()
        #self.fc.fd[FLOW_NAMES.PREVIEW].select_edit()
        self.fc.fd[FLOW_NAMES.PREVIEW].select_preview_image_opts_btn("edit_btn")
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_main_option("edit_options_crop_txt")
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_main_option("square_txt")
        self.fc.fd[FLOW_NAMES.EDIT].apply_crop_rotate()
        self.fc.fd[FLOW_NAMES.EDIT].apply_crop_flip()
        self.fc.fd[FLOW_NAMES.EDIT].apply_crop_scale_picker()
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_done()
        self.fc.fd[FLOW_NAMES.EDIT].select_edit_done()
        time.sleep(5)
        self.fc.fd[FLOW_NAMES.PREVIEW].select_next()
        #self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        #self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=True , check_sending=False)
        self.fc.flow_home_log_out_hpid_from_app_settings()

    #@pytest.mark.steps
    def test_printer_scan(self):
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Printer Scan")
        #self.fc.verify_invisible_transition_screen()
        time.sleep(5)
        try:
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(tile=True, timeout=60)
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=1)
            self.fc.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
            #time.sleep(5)
            self.driver.wait_for_context("WEBVIEW_chrome")
            #self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
            self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username,self.fc.hpid_password)
            time.sleep(5)
            self.fc.fd[FLOW_NAMES.HOME].check_run_time_permission_photo_ga()
        except:
            pass
        time.sleep(5)
        self.fc.fd[FLOW_NAMES.SCAN].select_scan()
        self.fc.fd[FLOW_NAMES.PREVIEW].select_bottom_nav_btn("fax_btn")
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number , self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        #self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        #self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=True , check_sending=False)
        self.driver.wdvr.save_screenshot("test_qama_fax.png")
        self.fc.flow_home_log_out_hpid_from_app_settings()

    
    #@pytest.mark.steps
    def test_contention(self):
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Mobile Fax")
        #self.fc.verify_invisible_transition_screen()
        try:
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(tile=True, timeout=60)
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=1)
            self.fc.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
            self.driver.wait_for_context("WEBVIEW_chrome")
            #self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
            self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username,self.fc.hpid_password)
            time.sleep(10)
            self.fc.fd[FLOW_NAMES.HOME].check_run_time_permission_photo_ga()
        except:
            pass
        try:  
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].verify_fax_history_screen(timeout=15)
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].click_compose_new_fax()
        except TimeoutException:
            pass
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_menu_option_btn("menu_clear_fields")
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number, self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_add_files_option_btn("files_photos_btn")
        self.fc.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item("my_photos_txt")
        self.fc.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index("png")
        self.fc.fd[FLOW_NAMES.PREVIEW].select_next()
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_menu_option_btn("menu_home")
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Printer Scan")
        self.fc.fd[FLOW_NAMES.SCAN].select_scan()
        self.fc.fd[FLOW_NAMES.PREVIEW].select_bottom_nav_btn("fax_btn")
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number, self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        #self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        #self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=True , check_sending=False)
        self.fc.flow_home_log_out_hpid_from_app_settings()

 
    #@pytest.mark.steps
    def test_scanner(self):    
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Mobile Fax")
        #self.fc.verify_invisible_transition_screen()
        time.sleep(5)
        try:
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(tile=True, timeout=60)
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=1)
            self.fc.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
            self.driver.wait_for_context("WEBVIEW_chrome")
            #self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
            self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username,self.fc.hpid_password)
            time.sleep(5)
            self.fc.fd[FLOW_NAMES.HOME].check_run_time_permission_photo_ga()
        except:
            pass
        try:
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].verify_fax_history_screen(timeout=15)
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].click_compose_new_fax()
        except TimeoutException:
            pass
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_menu_option_btn("menu_clear_fields")
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number, self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_add_files_option_btn("scanner_btn")
        time.sleep(5)
        self.fc.fd[FLOW_NAMES.SCAN].select_scan()
        time.sleep(10)
        self.fc.fd[FLOW_NAMES.PREVIEW].select_next()
        #self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        #self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=True , check_sending=False)
        self.fc.flow_home_log_out_hpid_from_app_settings()

    @pytest.mark.steps
    def test_retry_fax(self):
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Mobile Fax")
        #self.fc.verify_invisible_transition_screen()
        time.sleep(5)
        try:
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(tile=True, timeout=60)
            self.fc.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=1)
            self.fc.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
            self.driver.wait_for_context("WEBVIEW_chrome")
            #self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
            self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username,self.fc.hpid_password)
            time.sleep(5)
            self.fc.fd[FLOW_NAMES.HOME].check_run_time_permission_photo_ga()
        except:
            pass
        import pdb ; pdb.set_trace()
        try:
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].verify_fax_history_screen(timeout=20)
            self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].click_compose_new_fax()
        except TimeoutException:
            pass
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_menu_option_btn("menu_clear_fields")
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_number, self.receiver_name)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(self.sender_name , self.sender_number)
        phone , name, code = self.fc.fd[FLOW_NAMES.COMPOSE_FAX].get_recipient_information()
        print(phone,name,code)
        """
        phone_number='{} {}'.format(code,phone)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(self.receiver_fake_number, self.receiver_name)
        phone_number_fake='{} {}'.format(code,phone)
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_add_files_option_btn("files_photos_btn")
        self.fc.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item("my_photos_txt")
        self.fc.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index("png")
        self.fc.fd[FLOW_NAMES.PREVIEW].select_next()
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        #self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=False , check_sending=False)
        self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].click_back()
        self.fc.fd[FLOW_NAMES.COMPOSE_FAX].click_menu_option_btn("menu_fax_history")
        self.fc.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].select_history_record("sent_history_record_cell" , phone_number_fake , "failed_icon")
        #self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=False , check_sending=False)
        self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_phone_number(phone_number=phone_number)
        self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_bottom_btn(["retry_fax_btn" , "edit_resend_btn"])
        self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].click_bottom_button("retry_fax_btn")
        #self.fc.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_status(is_successful=True , check_sending=False)
        self.fc.flow_home_log_out_hpid_from_app_settings()
        """
    #@pytest.mark.steps
    @pytest.mark.parametrize("opt_name" , ["supply_status" , "promotional_messaging"])
    def test_enable_notifications(self , opt_name):
        self.fc.flow_load_home_screen(skip_value_prop=True)
        #import pdb ; pdb.set_trace()
        self.fc.fd[FLOW_NAMES.HOME].verify_home_nav()
        self.fc.fd[FLOW_NAMES.HOME].select_bottom_nav_btn("nav_app_settings")
        self.fc.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings()
        time.sleep(5)
        self.fc.fd[FLOW_NAMES.APP_SETTINGS].click_sign_in_btn()
        self.fc.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
        time.sleep(5)
        self.fc.fd[FLOW_NAMES.HPID].login(self.fc.hpid_username,self.fc.hpid_password)
        self.fc.fd[FLOW_NAMES.APP_SETTINGS].select_app_settings_opt("notification_and_privacy")
        self.fc.fd[FLOW_NAMES.APP_SETTINGS].select_notification_privacy_opt(opt_name)
        self.fc.fd[FLOW_NAMES.APP_SETTINGS].verify_notification_privacy_opt_screen(opt_name)
        self.fc.fd[FLOW_NAMES.APP_SETTINGS].toggle_on_off_btn()
        self.fc.flow_home_log_out_hpid_from_app_settings()
