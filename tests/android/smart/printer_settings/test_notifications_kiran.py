from selenium.common.exceptions import TimeoutException
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES , PACKAGE , LAUNCH_ACTIVITY , WEBVIEW_CONTEXT
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE
import pytest
import time
import pdb

pytest.app_info = "SMART"

class Test_Suite_Android_HPSmart(object):
    @pytest.fixture(scope="class", autouse="true")


    #def class_setup(cls, request, android_smart_setup, load_printers_session):
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        #cls.p = load_printers_session
        #cls.printer_ip = cls.p.p_obj.ipAddress

                                        # Define variables
        cls.fc.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]["username"]
        cls.fc.hpid_password = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]["password"]
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])                              
    
    def test_smart_tast_notification(self):
        #self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.fc.flow_load_home_screen()
        """
        time.sleep(5)
        self.fc.fd[FLOW_NAMES.HOME].verify_add_new_printer()
        self.fc.fd[FLOW_NAMES.HOME].select_big_add_icon()
        self.fc.fd[FLOW_NAMES.PRINTERS].select_printer(self.printer_ip, is_searched=True, keyword=self.printer_ip)
        #self.fc.fd[FLOW_NAMES.WEB_SMART_WELCOME].click_continue_btn()
        #self.fc.fd[FLOW_NAMES.WELCOME].skip_shared_usage_screen()
        #self.fc.flow_load_home_screen(skip_value_prop=True)
        #time.sleep(5)
        #self.fc.flow_app_settings_sign_in_hpid()
        #self.fc.flow_home_load_smart_task_screen()
        #self.fc.flow_smart_task_load_smart_task_create_screen("Task1")
        #self.smart_tasks.add_smart_task_for_email(to_email="tuseru2662@gmail.com")
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].select_save_btn()
        #try:
        #    self.fc.fd[FLOW_NAMES.SMART_TASKS].dismiss_smart_task_created_popup()
        #except TimeoutException:
        #    self.fc.fd[FLOW_NAMES.SMART_TASKS].select_btn_on_saved_screen(is_checked=True, btn_name="back_to_smart_tasks_btn")
        #self.driver.back()
        
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Shortcuts")
        #self.driver.wdvr.find_element_by_xpath("//android.view.View[@text = 'ContextualMenuButton']").click()
        self.driver.wdvr.find_element_by_xpath("//android.view.View[@text = 'Email tuseru2662']").click()
        self.driver.wdvr.find_element_by_xpath("//android.widget.Button[@resource-id = 'com.hp.printercontrol.debug:id/start_shortcut_files_flow']").click()
        #self.driver.wdvr.find_element_by_xpath("//android.view.View[@text = 'Start']").click()
        #self.driver.wdvr.find_element_by_xpath("//android.widget.Button[@resource-id = 'com.hp.printercontrol.debug:id/start_shortcut_files_flow']").click()
        self.fc.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item("my_photos_txt")
        self.fc.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index("png")
        self.driver.wdvr.find_element_by_xpath("//android.widget.TextView[@text = 'Start Email tuseru2662']").click()
        self.fc.fd[FLOW_NAMES.SMART_TASKS].dismiss_smart_tasks_complete_popup_screen()
        """
        import pdb ; pdb.set_trace()
        #self.fc.fd[FLOW_NAMES.HOME].select_bottom_nav_btn("nav_app_settings")
        self.fc.fd[FLOW_NAMES.HOME].select_notifications_icon()
        time.sleep(3)
        self.fc.fd[FLOW_NAMES.NOTIFICATION].select_shortcuts()
        time.sleep(5)
        self.driver.wdvr.save_screenshot("test_notification.png")
        assert self.fc.fd[FLOW_NAMES.SMART_TASKS].verify_smart_task_history_list(is_empty=True) != False

