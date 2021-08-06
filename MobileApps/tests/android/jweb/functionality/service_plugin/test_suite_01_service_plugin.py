import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.web.const import TEST_DATA

pytest.app_info = "JWEB"

class Test_Suite_01_Service_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.service_plugin = cls.fc.fd["service_plugin"]

    def test_01_verify_get_services(self):
        """
        verify service plugin test
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_service_routing_plugin()
        self.driver.swipe(direction="up")
        self.service_plugin.select_get_services_test_btn()
        assert self.service_plugin.get_services_result() == {'services': [{'id': 'openUrl', 'supportedContainerViewTypes': ['fullScreen']}]}

    def test_02_verify_get_service_availability(self):
        """
        verify service plugin test
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_service_routing_plugin()
        self.driver.swipe(direction="up")
        self.service_plugin.select_get_service_availability_test_btn()
        assert self.service_plugin.get_service_availability_result() == {'id': 'openUrl', 'supportedContainerViewTypes': ['fullScreen']}
        self.service_plugin.enter_service_availability_id("Url")
        self.service_plugin.select_get_service_availability_test_btn()
        assert self.service_plugin.get_service_availability_result() != {'id': 'openUrl', 'supportedContainerViewTypes': ['fullScreen']}

    def test_03_verify_launch_services(self):
        """
        verify service plugin test
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_service_routing_plugin()
        self.service_plugin.enter_service_launch_data('{"https://bruce-williams.github.io"}')
        self.service_plugin.select_launch_service_test_btn()
        assert self.service_plugin.get_service_launch_result() == {'errorType': 'invalidOptions', 'message': 'url is missing from openUrl serviceOptions'}
        self.service_plugin.select_get_service_instance_test_btn()
        assert self.service_plugin.get_service_instance_result() == {'errorType': 'serviceInstanceNotFound', 'message': 'The service instance with id:  was not found'}
        for i in saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SERVICE_ROUTING))["urls"]:
            data = '{"url":"'+i+'"}'
            self.service_plugin.enter_service_launch_data(data)
            self.service_plugin.select_launch_service_test_btn()
            if all(word not in data for word in ["localhost", "chrisgeohringhp"]):
                self.driver.press_key_back()
        self.service_plugin.select_add_listener_test_btn()
        self.service_plugin.enter_service_launch_data(data)
        self.service_plugin.select_launch_service_test_btn()
        self.service_plugin.select_event_close_button(1)
        self.service_plugin.select_event_close_button(0)

    def test_04_verify_get_service_instance(self):
        """
        verify service plugin test
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_service_routing_plugin()
        self.service_plugin.enter_service_launch_data('{"url":"https://bruce-williams.github.io"}')
        self.service_plugin.select_get_service_instance_test_btn()
        svc_id = self.service_plugin.get_service_instance_svc_id()
        self.service_plugin.enter_get_service_instance_svc_id("none")
        assert self.service_plugin.get_service_instance_result() == {'errorType': 'serviceInstanceNotFound', 'message': 'The service instance with id:  was not found'}
        self.service_plugin.enter_get_service_instance_svc_id(svc_id)
        self.service_plugin.select_get_service_instance_test_btn()
        assert self.service_plugin.get_service_instance_result() != {'errorType': "serviceNotFound"}

    def test_05_verify_add_listener(self):
        """
        verify service plugin test
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_plugins_tab_from_menu()
        self.home.select_service_routing_plugin()
        self.service_plugin.enter_service_launch_data('{"url":"https://bruce-williams.github.io"}')
        self.service_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        self.service_plugin.select_add_listener_test_btn()
        self.service_plugin.enter_service_launch_data('{"url":"https://bruce-williams.github.io"}')
        self.service_plugin.select_launch_service_test_btn()
        self.driver.press_key_back()
        self.service_plugin.select_event_close_button(2)
        self.service_plugin.select_event_close_button(1)
        self.service_plugin.select_event_close_button(0)
