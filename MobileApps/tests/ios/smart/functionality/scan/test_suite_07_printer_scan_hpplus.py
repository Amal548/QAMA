import pytest
import time
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_07_Printer_Scan_Hpplus(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup,load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.camera = cls.fc.fd["camera"]
        cls.preview = cls.fc.fd["preview"]
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        login_info = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="hp+")
        cls.username, cls.password = login_info["email"], login_info["password"]
        cls.fc.go_home(reset=True, stack=cls.stack, username=cls.username, password=cls.password, remove_default_printer=False)
    
    def test_01_verify_gear_btn_functionality_hpplus(self):
        """
        C28761385 - Verify 'Gear' button functionality from top bar
        C28761350 - Printer Scan UI (HP+ user)
        """
        self.fc.go_scan_screen_from_home(self.p)
        if self.fc.fd["scan"].verify_second_close_btn() is not False:
            self.fc.fd["scan"].select_second_close_btn()
        # verify Modes
        self.fc.fd["scan"].verify_an_element_and_click(self.fc.fd["scan"].PHOTO_MODE, click=False, raise_e=True)
        self.fc.fd["scan"].verify_an_element_and_click(self.fc.fd["scan"].DOCUMENT_MODE, click=False, raise_e=True)
        self.fc.fd["scan"].verify_an_element_and_click(self.fc.fd["scan"].BATCH_MODE, click=False, raise_e=True)
        self.fc.fd["scan"].verify_an_element_and_click(self.fc.fd["scan"].MULTI_ITEM_MODE, click=False, raise_e=True)
        self.fc.fd["scan"].verify_an_element_and_click(self.fc.fd["scan"].BOOK_MODE, click=False, raise_e=True)
        # verify gear btn ui
        self.fc.fd["scan"].select_gear_setting_btn()
        self.fc.fd["scan"].verify_an_element_and_click(self.fc.fd["scan"].AUTO_ENHANCEMENT_SWITCH, click=False, raise_e=True)
        self.fc.fd["scan"].verify_an_element_and_click(self.fc.fd["scan"].AUTO_ORIENTATION_SWITCH, click=False, raise_e=True)
        self.fc.fd["scan"].verify_an_element_and_click(self.fc.fd["scan"].AUTO_HEAL_SWITCH, click=False, raise_e=True)
        self.fc.fd["scan"].verify_an_element_and_click(self.fc.fd["scan"].FLATTEN_PAGES_SWITCH, click=False, raise_e=True)