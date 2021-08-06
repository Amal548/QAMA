import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA

pytest.app_info = "JWEB_DATA_COLLECTION"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_data_collection_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_data_collection_setup

        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.data_collection = cls.fc.fd["data_collection"]
        cls.retargeting_data = cls.fc.fd["retargeting_data"]
        cls.controlled_data = cls.fc.fd["controlled_data"]
        cls.data_collection_settings = cls.fc.fd["data_collection_settings"]
        cls.data_collection_plugin = cls.fc.fd["data_collection_plugin"]

        def clean_up_class():
            cls.fc.close_app()

        request.addfinalizer(clean_up_class)

    def test_01_data_collection(self):
        """
        verify data collection test
        """
        self.fc.flow_load_home_screen()
        self.home.select_retargeting_data_item()
        self.retargeting_data.select_request_client_id_access_item()
        sleep(3)
        self.data_collection_settings.select_allow_btn()
        self.retargeting_data.select_goto_application_settings_item()
        self.data_collection_settings.toggle_allow_tracking_btn(disable=True)
        self.fc.restart_app()
        self.home.select_data_collection_item()
        self.data_collection.select_send_ui_event_item()
        self.data_collection.toggle_activity_btn(disable=True)
        self.data_collection.toggle_screenpath_btn(disable=True)
        self.data_collection.toggle_screenmode_btn(disable=True)
        self.data_collection.toggle_control_name_btn(disable=True)
        self.data_collection.toggle_control_detail_btn(disable=True)
        self.data_collection.select_send_item()
        sleep(5)
        assert self.data_collection.send_ui_event_result() == saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.DATA_COLLECTION))["send_ui_results"]["error_1"]
        self.data_collection.select_send_ui_event_item()
        self.home.select_retargeting_data_item()
        self.retargeting_data.select_goto_application_settings_item()
        self.data_collection_settings.toggle_allow_tracking_btn(disable=False)
        self.driver.swipe(direction="down")
        sleep(3)
        self.data_collection_settings.toggle_printer_uuid_custom_btn(disable=False)
        self.data_collection_settings.toggle_app_instance_id_custom_btn(disable=False)
        self.fc.restart_app()
        self.home.select_data_collection_item()
        self.data_collection.select_send_ui_event_item()
        self.data_collection.toggle_activity_btn(disable=False)
        sleep(2)
        self.data_collection.toggle_screenpath_btn(disable=False)
        sleep(2)
        self.data_collection.toggle_screenmode_btn(disable=False)
        sleep(2)
        self.data_collection.toggle_control_name_btn(disable=False)
        sleep(2)
        self.data_collection.toggle_control_detail_btn(disable=False)
        sleep(2)
        self.data_collection.enter_activity_name("SendUiEventTest-v01")
        self.data_collection.enter_screen_path("/DataCollectionExampleApp/")
        self.data_collection.enter_screen_mode("Default")
        self.data_collection.enter_control_name("Send UI Event")
        self.data_collection.enter_control_detail("http://example.com/detail")
        self.data_collection.select_send_item()
        sleep(10)
        self.data_collection.send_ui_event_result() != saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.DATA_COLLECTION))["send_ui_results"]["error_1"]
        self.data_collection.select_send_ui_event_item()
        self.data_collection.select_data_collection_services_item()
        self.data_collection.select_send_sys_info_event_item()
        sleep(5)
        assert self.data_collection.send_sys_info_event_result() != False

    def test_02_retargeting_data(self):
        """
        verify retargeting tests
        """
        self.fc.flow_load_home_screen()
        self.home.select_retargeting_data_item()
        self.retargeting_data.select_request_client_id_access_item()
        sleep(3)
        self.data_collection_settings.select_allow_btn()
        self.retargeting_data.select_ok_pop_up_item()
        self.retargeting_data.select_goto_application_settings_item()
        self.data_collection_settings.toggle_allow_tracking_btn(disable=True)
        sleep(3)
        self.fc.restart_app()
        self.home.select_retargeting_data_item()
        self.retargeting_data.select_client_id_availability_item()
        assert self.retargeting_data.client_id_availability_response() == 'User Denied Access'
        self.retargeting_data.select_ok_pop_up_item()
        self.retargeting_data.select_request_client_id_access_item()
        assert self.retargeting_data.client_id_availability_response() == 'User Denied Access\n\nGo to the App Settings to manually enable access.'
        self.retargeting_data.select_ok_pop_up_item()
        self.retargeting_data.select_goto_application_settings_item()
        self.data_collection_settings.select_data_ingress_stack()
        self.data_collection_settings.select_dev_stack()
        self.data_collection_settings.select_data_collection_settings()
        self.data_collection_settings.toggle_printer_uuid_custom_btn(disable=False)
        self.driver.swipe(direction="down")
        self.data_collection_settings.toggle_app_instance_id_custom_btn(disable=False)
        self.driver.swipe(direction="up")
        self.data_collection_settings.toggle_allow_tracking_btn(disable=False)
        self.data_collection_settings.select_allow_btn()
        sleep(5)
        self.fc.flow_load_home_screen()
        self.home.select_retargeting_data_item()
        self.retargeting_data.select_client_id_availability_item()
        assert self.retargeting_data.client_id_availability_response() == 'Access is granted.'
        self.retargeting_data.select_ok_pop_up_item()
        self.retargeting_data.select_request_client_id_access_item()
        assert self.retargeting_data.client_id_availability_response() == 'Access is granted.'
        self.retargeting_data.select_ok_pop_up_item()

    def test_03_controlled_data(self):
        """
        verify auth plugin test login
        """
        self.fc.flow_load_home_screen()
        self.home.select_retargeting_data_item()
        self.retargeting_data.select_request_client_id_access_item()
        sleep(3)
        self.data_collection_settings.select_allow_btn()
        self.retargeting_data.select_ok_pop_up_item()
        self.retargeting_data.select_goto_application_settings_item()
        self.data_collection_settings.toggle_printer_uuid_custom_btn(disable=True)
        self.driver.swipe(direction="down")
        self.data_collection_settings.toggle_app_instance_id_custom_btn(disable=True)
        self.driver.swipe(direction="up")
        self.data_collection_settings.toggle_allow_tracking_btn(disable=True)
        self.fc.restart_app()
        self.home.select_controlled_data_item()
        self.controlled_data.select_data_refresh_button()
        sleep(5)
        assert self.controlled_data.get_associated_device_product_number() == "Missing Consent"
        assert self.controlled_data.get_associated_device_uuid() == "Missing Consent"
        assert self.controlled_data.get_associated_stratus_user_uuid() == "Missing Consent"
        assert self.controlled_data.get_app_caid() == "Missing Consent"
        assert self.controlled_data.get_app_name() == "Missing Consent"
        assert self.controlled_data.get_app_package_deployed_uuid() == "Missing Consent"
        assert self.controlled_data.get_app_package_id() == "Missing Consent"
        assert self.controlled_data.get_os_language() == "Missing Consent"
        self.home.select_retargeting_data_item()
        self.retargeting_data.select_goto_application_settings_item()
        self.data_collection_settings.toggle_printer_uuid_custom_btn(disable=False)
        self.driver.swipe(direction="down")
        self.data_collection_settings.toggle_app_instance_id_custom_btn(disable=False)
        self.driver.swipe(direction="up")
        self.data_collection_settings.toggle_allow_tracking_btn(disable=False)
        self.data_collection_settings.select_allow_btn()
        self.fc.restart_app()
        self.home.select_controlled_data_item()
        self.controlled_data.select_data_refresh_button()
        sleep(6)
        assert self.controlled_data.get_associated_device_product_number() != "Missing Consent"
        assert self.controlled_data.get_associated_device_uuid() != "Missing Consent"
        # assert self.controlled_data.get_associated_stratus_user_uuid() != "Missing Consent"
        assert self.controlled_data.get_app_caid() != "Missing Consent"
        assert self.controlled_data.get_app_name() != "Missing Consent"
        assert self.controlled_data.get_app_package_deployed_uuid() != "Missing Consent"
        assert self.controlled_data.get_app_package_id() != "Missing Consent"
        assert self.controlled_data.get_os_language() != "Missing Consent"


    def test_04_verify_data_collection_plugin(self):
        """
        verify data collection plugin
        """
        self.fc.flow_load_home_screen()
        self.home.select_retargeting_data_item()
        self.retargeting_data.select_request_client_id_access_item()
        sleep(3)
        self.data_collection_settings.select_allow_btn()
        self.retargeting_data.select_ok_pop_up_item()
        self.retargeting_data.select_goto_application_settings_item()
        self.data_collection_settings.toggle_printer_uuid_custom_btn(disable=False)
        self.driver.swipe(direction="down")
        self.data_collection_settings.toggle_app_instance_id_custom_btn(disable=False)
        self.driver.swipe(direction="up")
        self.data_collection_settings.toggle_allow_tracking_btn(disable=False)
        self.fc.restart_app()
        self.home.select_weblet_item()
        self.data_collection_plugin.select_send_ui_event_test()
        assert self.data_collection_plugin.get_send_ui_event_result() == "Error: sendEventFailed"
        self.data_collection_plugin.select_send_collection_profile_test_btn()
        assert self.data_collection_plugin.get_send_collection_profile_result() == "Refresh Collection Profile Sent!"
        self.data_collection_plugin.enter_activity_name(option='SendUiEventTest-v01')
        self.data_collection_plugin.enter_screen_name(option='DataCollectionTab')
        self.data_collection_plugin.enter_screen_path(option='/DataCollectionExampleApp/')
        self.data_collection_plugin.enter_screen_mode(option='Default')
        self.data_collection_plugin.enter_control_name(option='Send UI Event')
        self.data_collection_plugin.enter_control_detail(option='http://example.com/detail')
        self.data_collection_plugin.select_send_ui_event_test()
        sleep(7)
        assert self.data_collection_plugin.get_send_ui_event_result() != "Error: sendEventFailed"
        print(self.data_collection_plugin.get_send_ui_event_result())
        self.data_collection_plugin.select_send_collection_profile_test_btn()
        assert self.data_collection_plugin.get_send_collection_profile_result() == "Refresh Collection Profile Sent!"