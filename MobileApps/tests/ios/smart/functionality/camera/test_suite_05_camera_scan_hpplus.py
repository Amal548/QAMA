import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_05_Camera_Scan_hpplus(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.camera = cls.fc.fd["camera"]
        cls.preview = cls.fc.fd["preview"]
        cls.stack = request.config.getoption("--stack")
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.fc.go_home(stack=cls.stack, username=cls.username, password=cls.password, remove_default_printer=False)

    def test_01_verify_default_option_for_preset(self):
        """
            C28746954: Verify "Document" is default option for preset camera scan
        """
        self.fc.go_camera_screen_from_home(tile=True)
        # no element difference between other modes, only verify button
        self.camera.verify_preset_sliders(acc_type="hpplus")
        self.camera.verify_document_mode()
        self.camera.select_book_mode()
        self.driver.restart_app(BUNDLE_ID.SMART)
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_book_mode()
