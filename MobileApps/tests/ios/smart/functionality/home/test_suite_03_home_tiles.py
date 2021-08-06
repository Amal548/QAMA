import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc

pytest.app_info = "SMART"


class Test_Suite_03_Home_Tiles_Without_Onboarding(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.personalize = cls.fc.fd["personalize"]
        cls.stack = request.config.getoption("--stack")
        cls.login_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.username, cls.password = cls.login_info["username"], cls.login_info["password"]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, request):
        self.driver.restart_app(BUNDLE_ID.SMART)
        if not self.fc.fd["home"].verify_home_tile(raise_e=False):
            self.fc.go_home(reset=True, button_index=2, stack=self.stack)
            self.fc.dismiss_tap_here_to_start()

    def test_01_verify_locked_tile(self):
        """
        C27654941 select Explore HP Smart during OWS Value prop and select a locked tile
        Verify value prop screen
        """
        self.home.select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(tile=True, timeout=60)
    
    def test_02_verify_locked_tile_without_printer(self):
        """
        C27654937 select Explore HP Smart during OWS Value prop and select a Printer Scan or Copy tile
        Verify "Feature Unavailable" pop-up shows up with "OK" button
        """
        self.home.select_tile_by_name(HOME_TILES.TILE_SCAN)
        self.home.verify_feature_unavailable_popup("no_printer_msg")  
    
    def test_03_login_on_locked_tiles(self):
        """
        C27654935
        """
        self.home.select_tile_by_name(HOME_TILES.TILE_SMART_TASK)
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(tile=True, timeout=60)
        self.fc.fd["ows_value_prop"].select_value_prop_buttons(1)
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=45)
        self.fc.fd["hpid"].verify_hp_id_sign_in()
        self.fc.fd["hpid"].login(self.username, self.password, change_check={"wait_obj":"smart_tasks_title", "timeout":60,
                                                                "flow_change":"smart_tasks", "project_change":"smart"}) 
