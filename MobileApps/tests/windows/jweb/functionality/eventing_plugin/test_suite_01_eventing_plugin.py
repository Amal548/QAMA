import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.windows.const import TEST_DATA

pytest.app_info = "JWEB"

class Test_Suite_01_Eventing_Plugin(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_jweb_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_jweb_setup

        # Define flows
        cls.home = cls.fc.fd["home"]
        cls.hpid = cls.fc.fd["hpid"]
        cls.eventing = cls.fc.fd["eventing_plugin"]

        def clean_up_class():
            cls.fc.close_jweb_app()

        request.addfinalizer(clean_up_class)

    def test_01_verify_eventing_plugin(self):
        """
        verify eventing plugin test
        """
        self.fc.flow_load_home_screen()
        self.home.select_menu()
        self.home.select_eventing_plugin()
        if not self.eventing.verify_eventing_plugin_test():
            self.eventing.select_eventing_dispatch_open()
        assert self.eventing.eventing_test_result() == False
        self.eventing.enter_name_field("RandomInfo")
        self.eventing.enter_data_field("{'deviceId':'abcdef654321', 'status':'sent'}")
        self.eventing.select_eventing_plugin_test()
        assert self.eventing.eventing_test_result() == False
        self.eventing.enter_data_field('{"deviceId":"abcdef654321", "status":"sent"}')
        self.eventing.select_eventing_plugin_test()
        assert self.eventing.eventing_test_result() == False
        self.eventing.select_eventing_dispatch_close()