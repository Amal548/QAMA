import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*

pytest.app_info = "SMART"

class Test_Suite_02_Ios_Smart_Set_Up_New_Printer_Screen(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_add_setup_printer_option(self):
        """
        C27654973, C27654974
        verify that the setting has been modified to 'Add / Set Up a Printer'
        Verify that user is directed to device Picker ('Printers' screen- similar to what + button on home screen does)
        """
        self.fc.go_home(stack=self.stack)
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_set_up_new_printer_cell()
        if self.fc.fd["printers"].verify_bluetooth_popup(raise_e=False):
                self.fc.fd["printers"].handle_bluetooth_popup()
        self.fc.fd["printers"].verify_printers_list_screen_ui()
