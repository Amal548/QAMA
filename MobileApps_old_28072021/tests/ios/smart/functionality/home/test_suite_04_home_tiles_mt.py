import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": False}


class Test_Suite_04_Home_Tiles_MT(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_info = cls.p.get_printer_information()

    def test_01_feature_unavailable_no_support(self):
        """
        C17153604 Printer without scanner
        Add printer without scanner, tap on printer scan tile
        Verify the Feature Unavailable popup, dismiss popup and verify home screen
        """
        self.fc.go_home(reset=True)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.select_tile_by_name(HOME_TILES.TILE_SCAN)
        self.home.verify_feature_unavailable_popup("not_supported_msg")
        self.fc.select_ok_btn()
        self.home.verify_home()

    def test_02_feature_unavailable_printer_offline(self):
        """
        C17153604 Printer without scanner
        Without adding any printer, tap on Copy tile and verify 'Feature Unavailable'
        Add a printer and make it go offline, tap on Copy tile and verify 'Feature Unavailable'
        """
        self.fc.go_home(reset=True)
        self.home.select_tile_by_name(HOME_TILES.TILE_COPY)
        self.home.verify_feature_unavailable_popup("no_printer_msg")
        self.fc.select_ok_btn()
        self.home.verify_home()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.p.toggle_wifi(on=False)
        self.home.select_tile_by_name(HOME_TILES.TILE_COPY)
        self.home.verify_feature_unavailable_popup("no_printer_msg")  
        