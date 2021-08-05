import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from selenium.webdriver.support.ui import WebDriverWait
from MobileApps.libs.flows.ios.smart.printers import Printers
from MobileApps.libs.ma_misc.ma_misc import truncate_printer_model_name

pytest.app_info = "SMART"


class Test_Suite_01_Add_Printers(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.printer_info = cls.p.get_printer_information()
        cls.stack = request.config.getoption("--stack")

    def test_01_add_printer(self):
        """
        C17511080 Precondition: printers on network
        1. Tap + sign on home, tap Add Printer button, verify the Printers screen
        2. verify clicking back button goes to printer list screen
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_get_started_by_adding_a_printer()
        self.printers.select_add_printer()
        self.printers.verify_printers_setup_screen_ui()
        self.printers.select_navigate_back()
        self.printers.verify_printers_list_screen_ui()

    def test_02_setup_new_printer_btn(self):
        """
        C17511084 Precondition: printers on network
        Tap + sign on home, tap Add Printer button, tap set up new printer, verify connect to wifi screen
        tap on back button and verify previous screen
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_get_started_by_adding_a_printer()
        self.printers.select_add_printer()
        self.printers.select_set_up_a_new_printer()
        self.printers.handle_location_popup(selection="allow")
        self.fc.fd["app_settings"].verify_set_up_new_printer_ui_elements()
        self.fc.fd["app_settings"].select_navigate_back()
        self.printers.verify_printers_setup_screen_ui()

    def test_03_connect_to_previous_printer_btn(self):
        """
        C17511217 Precondition: printers on network
        Tap + sign on home, tap Add Printer button, tap set up new printer, verify connect to wifi screen
        tap on back button and verify previous screen
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_get_started_by_adding_a_printer()
        self.printers.select_add_printer()
        self.printers.select_connect_to_previously_used_printer()
        self.printers.verify_printer_connection_screen_ui()
        self.printers.select_navigate_back()
        self.printers.verify_printers_setup_screen_ui()
    
    def test_04_verify_supported_printer_list_btn(self):
        """
        C17856862 
        Tap + sign on home, tap Add Printer button, tap 'Supported printer list' button
        verify hp support page opens up in external browser
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_get_started_by_adding_a_printer()
        self.printers.select_add_printer()
        self.printers.select_supported_printers_btn()
        assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.mobilesafari") == 4)

    @pytest.mark.parametrize("yes_btn", [True, False])
    def test_05_connect_printer_using_ip(self, yes_btn):
        """
        C17854719
        Tap + sign on home, tap Add Printer button, tap Connect the printer using IP address
        Add a printer using valid ip, verify the is this your printer screen
        verify functionality of yes and no button
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_get_started_by_adding_a_printer()
        self.printers.select_add_printer()
        self.printers.select_add_printer_using_ip()
        self.printers.verify_connect_the_printer_screen()
        self.printers.search_for_printer_directly_using_ip(self.printer_info["ip address"])
        self.printers.select_is_this_your_printer(yes=yes_btn)
        if yes_btn:
            self.fc.fd["home"].close_smart_task_awareness_popup()
            self.fc.fd["home"].verify_home()
            app_printer_name = self.home.get_printer_name_from_device_carousel()
            shortened_bonjour_name = truncate_printer_model_name(self.printer_info["bonjour name"], case_sensitive=False)
            assert app_printer_name == self.printer_info["bonjour name"] or \
                   all(word in app_printer_name.lower().split() for word in shortened_bonjour_name.split())
        else:
            self.printers.verify_connect_the_printer_screen()
    
    def test_06_connect_printer_using_ip_screen(self): 
        """
        C17511241
        Tap + sign on home, tap Add Printer button, tap Connect the printer using IP address
        Verify the "connect with printer screen", tap back arrow and verify printer screen
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.select_get_started_by_adding_a_printer()
        self.printers.select_add_printer()
        self.printers.select_add_printer_using_ip()
        self.printers.verify_connect_the_printer_screen_ui()
        self.printers.select_navigate_back()
        self.printers.verify_printers_setup_screen_ui()