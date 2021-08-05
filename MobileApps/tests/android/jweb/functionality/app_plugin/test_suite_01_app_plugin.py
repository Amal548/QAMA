import pytest
from time import sleep

pytest.app_info = "JWEB"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.app = cls.fc.fd["app_plugin"]

    def test_01_listener_status(self):
        """
        Verify toast shows "Listener added", "Back button pressed!" and "Listener removed."

        TestRails -> C28909515, C28909517
        """
        self.fc.flow_load_home_screen()
        self.home.select_app_plugin_from_home()
        self.app.select_add_listener_btn()
        assert self.app.get_pop_up_toast_text() == "Listener added"
        self.app.close_pop_up_toast_text()
        self.driver.press_key_back()
        assert self.app.get_pop_up_toast_text() == "Back button pressed!"
        self.app.close_pop_up_toast_text()
        self.app.select_remove_listener_btn()
        assert self.app.get_pop_up_toast_text() == "Listener removed"
        self.app.close_pop_up_toast_text()
        self.driver.press_key_back()
        assert self.home.verify_main_page() != False

    def test_02_listener_stays_within_app_plugin(self):
        """
        Verify if listener is removed when leaving App plugin. 

        TestRails -> C28909519
        """
        self.fc.flow_load_home_screen()
        self.home.select_app_plugin_from_home()
        self.app.select_add_listener_btn()
        assert self.app.get_pop_up_toast_text() == "Listener added"
        self.app.close_pop_up_toast_text()
        self.home.select_menu()
        self.home.select_eventing_plugin()
        self.driver.press_key_back()
        assert self.app.verify_app_plugin() != False
        self.driver.press_key_back()
        assert self.home.verify_main_page() != False