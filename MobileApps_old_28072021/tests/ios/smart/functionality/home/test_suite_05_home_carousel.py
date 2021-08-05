import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from SPL.driver.reg_printer import PrinterNotReady
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_05_Home_Carousel(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def go_to_home(self):
        self.driver.restart_app(BUNDLE_ID.SMART)
      
    def test_01_empty_carousel(self):
        """
        C27654928 Precondition: Phone connected to wifi, fresh install
        Verify Add Your First Printer card on the carousel
        """
        self.fc.go_home(stack=self.stack, button_index=2)
        self.fc.dismiss_tap_here_to_start()
        self.home.verify_empty_carousel()

    def test_02_add_printer_second_page(self):
        """
        C27654930 verify carousel design with a printer added: 
        - left side of the card contains: printer image, printer name
        - right side of the card contains: estimated supply level
        """
        self.fc.dismiss_tap_here_to_start()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        assert not self.home.verify_add_your_first_printer(raise_e=False)
        self.home.verify_loaded_printer(self.p.get_printer_information()["bonjour name"], raise_e=False)

    def test_03_tap_on_printer(self):
        """
        C27654931 verify app is redirected to printer settings when printer icon is tapped
        """
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.click_on_printer_icon()
        self.fc.fd["printer_settings"].verify_printer_settings_screen(raise_e=True)

    def test_04_add_printer_first_page(self):
        """
        C27654930 verify carousel Add Printer card on carousel
        """
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.swipe_carousel(direction="left")
        self.home.verify_add_printer_on_carousel()

    def test_05_verify_HP_Smart_nav_bar(self):
        """
        C27654932 verify HP Smart is shown on top bar when printer is added
        """
        if self.home.verify_add_your_first_printer(raise_e=False):
            self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.home.verify_hp_smart_nav_bar()
