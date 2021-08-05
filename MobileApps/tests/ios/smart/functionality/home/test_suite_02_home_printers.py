import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc.ma_misc import truncate_printer_model_name

pytest.app_info = "SMART"


class Test_Suite_01_Home_Printers(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup, load_printers_session, request):
        cls = cls.__class__
        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.printers = cls.fc.fd["printers"]
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.dismiss_tap_here_to_start()

    def test_01_verify_printers_screen_ui(self):
        """
        C17511081 Fresh install, go home, click on big + sign and verify printers screen
        """
        self.home.select_get_started_by_adding_a_printer()
        self.printers.verify_printers_list_screen_ui()

    def test_02_verify_back_functionality_from_printers_screen(self):
        """
        C17854792
        """
        self.home.select_get_started_by_adding_a_printer()
        self.printers.verify_printers_list_screen_ui()
        self.printers.select_navigate_back()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()

    def test_03_verify_search_field(self):
        """
        C17841934
        """
        self.home.select_get_started_by_adding_a_printer()
        self.printers.verify_printers_list_screen_ui()
        self.printers.select_search_bar()
        self.printers.verify_cancel()
        assert self.driver.wdvr.is_keyboard_shown() is True

    def test_04_cancel_button_functionality(self):
        """
        C17841944 verify that clicking cancel button clears search field and that cancel button disappears
        """
        self.home.select_get_started_by_adding_a_printer()
        self.printers.verify_printers_list_screen_ui()
        self.printers.select_search_bar()
        self.printers.verify_cancel()
        sample_text = "sample test 123"
        self.printers.find_printer_using_search_bar(sample_text)
        assert ma_misc.poll(lambda: self.printers.verify_search_bar().get_attribute("value") == sample_text, timeout=30)
        self.printers.select_cancel()
        # TODO: check if apple fixes XCTest. https://github.com/appium/appium/issues/13288#issuecomment-535745703
        assert ma_misc.poll(lambda: self.printers.verify_search_bar().get_attribute("value") == "") or \
               ma_misc.poll(lambda: self.printers.verify_search_bar().get_attribute("value") is None) or \
               ma_misc.poll(lambda: self.printers.verify_search_bar().get_attribute("value") == self.printers.get_text_from_str_id("search_txt"), timeout=30) # iOS 12
        self.printers.verify_cancel(invisible=True)

    def test_05_x_button_functionality(self):
        """
        C17841944 verify that clicking the x button clears search field
        """
        self.home.select_get_started_by_adding_a_printer()
        self.printers.verify_printers_list_screen_ui()
        self.printers.select_search_bar()
        self.printers.verify_cancel()
        sample_text = "sample test 123"
        self.printers.find_printer_using_search_bar(sample_text)
        assert ma_misc.poll(lambda: self.printers.verify_search_bar().get_attribute("value") == sample_text)
        self.printers.select_clear_text_button()
        # TODO: check if apple fixes XCTest. https://github.com/appium/appium/issues/13288#issuecomment-535745703
        assert ma_misc.poll(lambda: self.printers.verify_search_bar().get_attribute("value") == "") or \
               ma_misc.poll(lambda: self.printers.verify_search_bar().get_attribute("value") is None) or \
               ma_misc.poll(lambda: self.printers.verify_search_bar().get_attribute("value") == self.printers.get_text_from_str_id("search_txt"), timeout=30) # iOS 12

    def test_06_verify_no_search_results(self):
        """
        C17841969 verify "No Search Results" on printers list when inputting invalid printer name/ip
        """
        self.home.select_get_started_by_adding_a_printer()
        self.printers.verify_printers_list_screen_ui()
        self.printers.select_search_bar()
        self.printers.find_printer_using_search_bar("sample test 123")
        self.printers.verify_no_search_results()

    @pytest.mark.skip("test case needs to be updated and potentially removed for 8.0")
    @pytest.mark.parametrize("search_bar_input", ["ip address", "bonjour name"])
    def test_07_valid_search_functionality(self, search_bar_input):
        """
        C17841988, C17842116
        """
        self.home.select_get_started_by_adding_a_printer()
        self.printers.verify_printers_list_screen_ui()
        self.printers.select_search_bar()
        self.printers.find_printer_using_search_bar(self.printer_info[search_bar_input])
        self.printers.verify_printer_in_list(self.printer_info["bonjour name"])
        self.printers.verify_printer_in_list(self.printer_info["ip address"])
        assert ma_misc.poll(lambda: self.printers.count_number_of_printers() >= 1)
        self.printers.select_printer_in_list(self.printer_info[search_bar_input])
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].verify_home()
        # app no longer displays printer name on top bar in 8.0
        app_printer_name = self.home.get_printer_name_from_top_nav_bar()
        shortened_bonjour_name = truncate_printer_model_name(self.printer_info["bonjour name"], case_sensitive=False)
        assert app_printer_name == self.printer_info["bonjour name"] or \
                all(word in app_printer_name.lower().split() for word in shortened_bonjour_name.split())