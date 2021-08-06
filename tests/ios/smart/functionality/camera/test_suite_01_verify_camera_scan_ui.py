import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_01_Verify_Camera_Scan_Ui(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.camera = cls.fc.fd["camera"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(stack=cls.stack)
    
    def test_01_verify_camera_ui_elements(self):
        """
        C13927415, C14728105
        Precondition: fresh install
        Click camera tile and verify camera screen UI
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_ui_elements()
        self.camera.select_source_button()
        self.camera.verify_source_options()
        self.camera.select_source_option(self.camera.OPTION_CAMERA)
        self.camera.verify_preset_default_capture_mode()
        modes = [attr for attr in dir(FLASH_MODE) if not attr.startswith("__")]
        for mode in modes:
            self.camera.select_flash_mode(getattr(FLASH_MODE, mode))
            self.camera.verify_flash_mode_state(getattr(FLASH_MODE, mode))
    
    def test_02_verify_camera_ui_elements_hpplus(self):
        '''
            C28746949
            extended camera ui element for hpplus users
        '''
        login_info = ma_misc.get_hpid_account_info(stack=self.stack, a_type="hp+")
        self.username, self.password = login_info["email"], login_info["password"]
        # TODO: reset takes a long time, can log out from regular user and login with hp+ user
        self.fc.go_home(reset=True, stack=self.stack, username=self.username, password=self.password)
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_ui_elements(acc_type="hpplus")