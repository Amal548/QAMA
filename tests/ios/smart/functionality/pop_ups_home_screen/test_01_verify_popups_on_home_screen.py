import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc

pytest.app_info = "SMART"


class Test_Suite_01_Popups_On_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.preview = cls.fc.fd["preview"]
        cls.photos = cls.fc.fd["photos"]
        cls.home = cls.fc.fd["home"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_allow_notifications_pop_up(self):
        """
        C28217233 - Allow notifications pop up
        C28217231 - Device connection permission pop up - iOS 14 onwards
        C28217232 - Smart Task awareness pop up on Home screen
        """
        self.go_home_local(reset=True, stack=self.stack)
        self.home.select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup(allow_access=True)
        self.fc.fd["camera"].select_close()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.select_print_button_and_verify_print_job(self.p)
        self.preview.select_navigate_back()
        self.preview.select_navigate_back()
        self.preview.select_navigate_back()
        self.preview.select_navigate_back()
        self.home.select_home_icon()
        self.home.verify_smart_task_awareness_popup(raise_e=False)

    def test_02_verify_bluetooth_popup(self):
        """
        C28279579 - Bluetooth Pop Up on Add Printer screen
        C28281910 - Location Permission Pop Up
        """
        self.go_home_local(reset=True, stack=self.stack)
        self.home.select_printer_plus_button_from_topbar()
        self.fc.fd["printers"].verify_bluetooth_popup(raise_e=True)
        self.fc.fd["printers"].handle_bluetooth_popup()
        self.fc.fd["printers"].add_printer_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.verify_allow_while_using_app(raise_e=True)
        self.home.handle_location_pop()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()

    def go_home_local(self, stack="pie", reset=False, username="", password="", share_usage_data=True):
        stack = stack.lower()
        self.fc.fd["ios_system"].clear_safari_cache()
        if reset:
            self.driver.reset(BUNDLE_ID.SMART)
        if stack != "pie":  # pie stack is default server on iOS HP Smart
            self.fc.change_stack(stack)
        self.driver.launch_app(BUNDLE_ID.SMART)
        # TEMP work around for def-#AIOI-11315
        self.fc.fd["welcome"].allow_notifications_popup(raise_e=False)
        self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME, timeout=30)
        self.fc.fd["welcome_web"].verify_welcome_screen()
        self.fc.fd["welcome_web"].click_accept_all_btn()
        self.fc.fd["welcome"].allow_notifications_popup(raise_e=False)
        self.fc.fd["welcome"].swipe_down_scrollview()
        if share_usage_data:
            self.fc.fd["welcome"].select_yes()
        else:
            self.fc.fd["welcome"].select_no_option()
        # TODO: waiting on specs for webview timeout GDG-1768
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)
        self.fc.login_value_prop_screen(tile=False, stack=self.stack, username=username, password=password,
                                        change_check={"wait_obj": "sign_in_button", "invisible": True, "timeout": 10})

        self.fc.fd["welcome"].allow_notifications_popup(timeout=15, raise_e=True)
        if self.driver.platform_version == '14':
            self.fc.fd["ios_system"].verify_hp_local_network_alert()
            self.fc.fd["ios_system"].dismiss_hp_local_network_alert(timeout=10)
        self.home.close_smart_task_awareness_popup()
        self.fc.fd["home"].dismiss_tap_account_coachmark()
        self.fc.remove_default_paired_printer()
