import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.web.const import TEST_DATA as JWEB_DATA

pytest.app_info = "JWEB_DATA_COLLECTION"

class Test_Suite_01_Data_Collection(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_jweb_data_collection_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_data_collection_setup

        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.data_collection = cls.fc.fd["data_collection"]
        cls.retargeting_data = cls.fc.fd["retargeting_data"]
        cls.controlled_data = cls.fc.fd["controlled_data"]
        cls.data_collection_settings = cls.fc.fd["data_collection_settings"]

    def test_01_data_collection(self):
        """
        verify data collection test
        """
        self.fc.flow_load_home_screen()
        self.home.select_data_collection_item()
        self.data_collection.select_send_ui_event_item()
        self.data_collection.toggle_activity_btn(disable=True)
        self.data_collection.toggle_screenpath_btn(disable=True)
        self.data_collection.toggle_screenmode_btn(disable=True)
        self.driver.swipe(direction="down")
        self.data_collection.toggle_control_name_btn(disable=True)
        self.data_collection.toggle_control_detail_btn(disable=True)
        self.data_collection.select_send_item()
        sleep(5)
        assert self.data_collection.send_ui_event_result() == \
               saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.DATA_COLLECTION))["send_ui_results"]["error_2"]
        self.driver.press_key_back()
        self.driver.press_key_back()
        self.home.select_settings_item()
        self.data_collection_settings.enter_custom_printer_uuid(option="11111111-0000-0000-0000-000000000001")
        self.data_collection_settings.enter_custom_app_instance_id(option="22222222-0000-0000-0000-000000000001")
        self.data_collection_settings.select_save_btn()
        self.home.select_data_collection_item()
        self.data_collection.select_send_ui_event_item()
        self.data_collection.toggle_activity_btn(disable=False)
        self.data_collection.enter_activity_name("SendUiEventTest-v01")
        self.data_collection.toggle_screenpath_btn(disable=False)
        self.data_collection.enter_screen_path("/DataCollectionExampleApp/")
        self.data_collection.toggle_screenmode_btn(disable=False)
        self.data_collection.enter_screen_mode("Default")
        self.driver.swipe(direction="down")
        sleep(2)
        self.data_collection.toggle_control_name_btn(disable=False)
        self.data_collection.enter_control_name("SimpleUiEvent")
        self.data_collection.toggle_control_detail_btn(disable=False)
        self.data_collection.enter_control_detail("http://example.com/detail")
        sleep(2)
        self.data_collection.select_send_item()
        sleep(5)
        print(self.data_collection.send_ui_event_result())
        self.data_collection.send_ui_event_result() != \
            saf_misc.load_json(ma_misc.get_abs_path(JWEB_DATA.DATA_COLLECTION))["send_ui_results"]["error_1"]
        self.driver.press_key_back()
        self.driver.press_key_back()
        self.data_collection.select_send_sys_info_event_item()
        sleep(5)
        assert self.data_collection.send_sys_info_event_result() != False

    def test_02_retargeting_data(self):
        """
        verify retargeting tests
        """
        self.fc.flow_load_home_screen()
        self.home.select_retargeting_data_item()
        self.retargeting_data.select_open_ads_settings_item()
        self.retargeting_data.toggle_opt_out_ads_switch(disable=False)
        self.retargeting_data.select_navigate_up_btn()
        self.retargeting_data.select_client_id_availability_item()
        assert self.retargeting_data.client_id_availability_response() == \
            "Client Advertising Id User denied access!"
        self.retargeting_data.select_ok_pop_btn()
        self.retargeting_data.select_open_ads_settings_item()
        self.retargeting_data.toggle_opt_out_ads_switch(disable=True)
        self.retargeting_data.select_navigate_up_btn()
        self.retargeting_data.select_client_id_availability_item()
        self.retargeting_data.select_ok_pop_btn()
        self.retargeting_data.select_client_id_availability_item()
        assert self.retargeting_data.client_id_availability_response() == \
               "Client Advertising Id Access is granted!"
        self.retargeting_data.select_ok_pop_btn()

    def test_03_controlled_data(self):
        """
        verify auth plugin test login
        """
        self.fc.flow_load_home_screen()
        self.home.select_settings_item()
        self.data_collection_settings.select_reset_btn()
        self.home.select_controlled_data_item()
        self.controlled_data.select_data_refresh_button()
        assert self.controlled_data.get_associated_device_product_number() == "Missing Consent"
        assert self.controlled_data.get_associated_device_uuid() == "Missing Consent"
        assert self.controlled_data.get_associated_stratus_user_uuid() == "Missing Consent"
        assert self.controlled_data.get_app_caid() == "Missing Consent"
        assert self.controlled_data.get_app_name() == "Missing Consent"
        self.driver.swipe(direction="down")
        assert self.controlled_data.get_app_package_deployed_uuid() == "Missing Consent"
        assert self.controlled_data.get_app_package_id() == "Missing Consent"
        assert self.controlled_data.get_os_language() == "Missing Consent"
        self.driver.swipe(direction="up")
        self.home.select_settings_item()
        self.data_collection_settings.enter_custom_printer_uuid(option="11111111-0000-0000-0000-000000000001")
        self.data_collection_settings.enter_custom_app_instance_id(option="22222222-0000-0000-0000-000000000001")
        self.data_collection_settings.select_save_btn()
        self.home.select_controlled_data_item()
        self.controlled_data.select_data_refresh_button()
        assert self.controlled_data.get_associated_device_product_number() != "Missing Consent"
        assert self.controlled_data.get_associated_device_uuid() != "Missing Consent"
        assert self.controlled_data.get_associated_stratus_user_uuid() != "Missing Consent"
        assert self.controlled_data.get_app_caid() != "Missing Consent"
        assert self.controlled_data.get_app_name() != "Missing Consent"
        self.driver.swipe(direction="down")
        assert self.controlled_data.get_app_package_deployed_uuid() != "Missing Consent"
        assert self.controlled_data.get_app_version() != "Missing Consent"
        assert self.controlled_data.get_os_name() != "Missing Consent"
        self.driver.swipe(direction="up")