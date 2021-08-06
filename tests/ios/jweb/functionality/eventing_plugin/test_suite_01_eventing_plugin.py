import pytest

pytest.app_info = "JWEB"

class Test_Suite_01_Eventing_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_setup
        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.event_plugin = cls.fc.fd["event_plugin"]
        
    def test_01_verify_event_plugin(self):
        """
        verify eventing plugin test produces 'Event Sent'

        TestRails -> C28698085
        """
        self.fc.flow_load_home_screen()
        self.home.select_eventing_plugin_from_home()
        self.event_plugin.select_eventing_plugin_test()
        assert self.event_plugin.eventing_test_result() == "Event Sent!"

    def test_02_verify_event_plugin_plugin_jarvis_event(self):
        """
        verify eventing plugin can send reserved Jarvis events

        TestRails -> C28698087
        """
        self.fc.flow_load_home_screen()
        self.home.select_eventing_plugin_from_home()
        self.event_plugin.select_jarvis_event_option_test()
        assert self.event_plugin.jarvis_event_option_test_result() == "jarvisEventFinished Event Sent!"

    def test_03_verify_event_plugin_plugin_add_listener(self):
        """
        verify event_plugin plugin add listener test

        TestRails -> C28698086, C28698088
        """
        self.fc.flow_load_home_screen()
        self.home.select_eventing_plugin_from_home()
        self.event_plugin.enter_add_listener_event(option="UpdateDeviceInfo")
        self.event_plugin.select_add_listener_test_btn()
        assert self.event_plugin.add_listener_test_result() == "Listener for UpdateDeviceInfo has been added"
        self.event_plugin.select_eventing_plugin_test()
        toast_notification_text = self.event_plugin.get_add_listener_pop_up_toast_text()
        assert toast_notification_text['main_text'] == "Event UpdateDeviceInfo Recieved from Native"
        assert toast_notification_text['sub_text'] in ['{"deviceId":"abcdef123456","status":"exploded"}', '{"status":"exploded","deviceId":"abcdef123456"}']
        self.event_plugin.select_add_listener_pop_up_close_btn()
        assert self.event_plugin.add_listener_event_result() == {"deviceId":"abcdef123456","status":"exploded"}

        self.event_plugin.enter_add_listener_event(option="jarvisEventFinished")
        assert self.event_plugin.add_listener_test_result() == "Listener for UpdateDeviceInfojarvisEventFinished has been added"
        self.event_plugin.select_eventing_plugin_test()
        toast_notification_text = self.event_plugin.get_add_listener_pop_up_toast_text()
        assert toast_notification_text['main_text'] == "Event UpdateDeviceInfo Recieved from Native"
        assert toast_notification_text['sub_text'] in ['{"deviceId":"abcdef123456","status":"exploded"}', '{"status":"exploded","deviceId":"abcdef123456"}']
        self.event_plugin.select_add_listener_pop_up_close_btn()
        # import pdb; pdb.set_trace()
        listener_results = self.event_plugin.add_listener_multiple_event_results().split('\n')
        assert listener_results[0] in ['{"status":"exploded","deviceId":"abcdef123456"}', '{"deviceId":"abcdef123456","status":"exploded"}']
        assert listener_results[1] in ['{"status":"exploded","deviceId":"abcdef123456"}', '{"deviceId":"abcdef123456","status":"exploded"}']