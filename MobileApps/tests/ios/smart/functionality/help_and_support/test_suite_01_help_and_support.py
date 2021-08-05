import pytest
import time
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from selenium.webdriver.support.ui import WebDriverWait
from MobileApps.libs.ma_misc import ma_misc
from selenium.common.exceptions import TimeoutException

pytest.app_info = "SMART"


class Test_Suite_01_Help_And_Support(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.safari = cls.fc.fd["safari"]
        cls.help_center = cls.fc.fd["help_center"]
 
    def test_01_help_page(self):
        """
        C27655427 Tap on Help and Support Tile and verify help page
        """
        self.fc.go_home(reset=True)
        self.home.select_tile_by_name(HOME_TILES.TILE_HELP_AND_SUPPORT)
        try:
            self.help_center.verify_help_center_screen()
        except TimeoutException:
            self.help_center.native_verify_help_center_screen()

    def test_02_help_page_scanning(self):
        """
        C27655429 Precondition: No preexisting files 
        Tap on view & print, tap on empty photo album, tap on Learn More 
        Verify help page is opened with section 'Scanning from HP Smart'
        """
        self.fc.go_home(reset=True)
        self.fc.go_hp_smart_files_and_delete_all_files()
        self.fc.go_hp_smart_files_screen_from_home()
        self.fc.fd["files"].select_learn_more_link_on_empty_files_screen()
        try:
            self.help_center.verify_help_center_screen()
        except TimeoutException:
            self.help_center.native_verify_help_center_screen()
        # TODO: verify scanning from HP Smart is open after defect fix AIOI-10341

    def test_03_help_page_print_document(self):
        """
        C27655432 No HP Smart files
        Add a printer with a scanner, tap on Print Documents, tap on HP Smart files, tap Learn More
        Verify help page is opened with section 'Scanning from HP Smart'
        """
        self.fc.go_home(reset=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_hp_smart_files_and_delete_all_files()
        self.fc.go_hp_smart_files_screen_from_home(select_tile=True)
        self.fc.fd["files"].select_learn_more_link_on_empty_files_screen()
        try:
            self.help_center.verify_help_center_screen()
        except TimeoutException:
            self.help_center.native_verify_help_center_screen()
        # TODO: verify scanning from HP Smart is open after defect fix AIOI-10341
    
    @pytest.mark.skip("issues clicking the chat with virtual agent in both native and webview context")
    def test_04_virtual_agent(self):
        """
        C14723452 No HP Smart files
        Navigate to help center
        Tap on Chat with Virtual Agent and verify chatbot in external browser
        """
        self.fc.go_home(reset=True)
        self.home.select_tile_by_name(HOME_TILES.TILE_HELP_AND_SUPPORT)
        self.safari.verify_help_center_container(back_btn=False)
        self.help_center.verify_help_center_screen()
        self.help_center.select_accept_cookies()
        # https://github.com/appium/appium/issues/10612
        self.help_center.select_chat_with_virtual_agent()
        assert self.driver.wdvr.query_app_state("com.apple.mobilesafari") == 4
        self.help_center.verify_virtual_agent()
