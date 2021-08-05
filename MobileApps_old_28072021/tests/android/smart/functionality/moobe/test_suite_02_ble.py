import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_02_BLE(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Skip test suite if printer is not supported for BLE (not secure BLE)
        if cls.fc.get_moobe_connect_wifi_type(cls.p) not in ["ble", "awc_ble"]:
            pytest.skip("{} is not supported for BLE".format(cls.p.serial))

        # Define flows
        cls.moobe_awc = cls.fc.flow[FLOW_NAMES.MOOBE_AWC]
        cls.setup_complete = cls.fc.flow[FLOW_NAMES.MOOBE_SETUP_COMPLETE]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        # Define variable
        cls.ssid, cls.password = get_wifi_info(request)
        
    def test_01_connect_to_wifi_successful_with_ble(self):
        """
        Description:
            Precondition: set printer to OOBE mode. 
            1. Load to Printers app from Home screen of HP Smart
            2. Click on Add Printer -> no popup of turning on bluetooth(Android 10)
            3. Select OOBE target printer
            4. Go through BLE process to connect printer to Wi-Fi 
               Note: To Android 7,8, and 9, no popup of turning on bluetooth during this process

        Expected Result:
            4. Printer Connected screen display
        """
        self.fc.flow_home_moobe_connect_printer_to_wifi(printer_obj=self.p,
                                                        ssid=self.ssid,
                                                        password=self.password,
                                                        is_ble=True)

    def test_02_connect_printer_to_wifi_with_incorrect_password(self):
        """
        Description:
            Precondition: set printer to OOBE mode. 
            1. Load to Printers app from Home screen of HP Smart
            2. Click on Add Printer 
            3. Select OOBE target printer
            4. Enter an invalid password. Then, click continue button
            5. Click Exit Setup button
            6. Click Continue

        Expected Result:
            4. Something might be wrong with your password

            5. Exit Setup screen
            6. Home screen
        """
        self.fc.flow_home_select_oobe_printer(self.p, self.ssid, is_ble=True)
        self.moobe_awc.verify_connect_printer_to_wifi_screen(self.ssid)
        self.moobe_awc.enter_network_password("invalid pass")
        self.moobe_awc.verify_connecting_screen(invisible=False)
        # Need to pass 2 first steps in thermometer process, so timeout should be 30 instead of 10
        self.moobe_awc.verify_wrong_password_popup(timeout=30)
        self.moobe_awc.select_wrong_password_popup_exit_setup()
        self.setup_complete.verify_exit_setup_screen()
        self.setup_complete.select_exit_setup_continue_btn()
        self.home.verify_home_nav()

    def test_03_connect_printer_to_wifi_with_incorrect_password_and_reenter_password(self):
        """
        Description:
            Precondition: set printer to OOBE mode. 
            1. Load to Printers app from Home screen of HP Smart
            2. Click on Add Printer 
            3. Select OOBE target printer
            4. Enter an invalid password. Then, click continue button
            5. Reenter valid password and continue process

        Expected Result:
            4. Something might be wrong with your password
            5. Printer connects to wifi successfully.
        """
        self.fc.flow_home_select_oobe_printer(self.p, self.ssid, is_ble=True)
        self.moobe_awc.verify_connect_printer_to_wifi_screen(self.ssid)
        self.moobe_awc.enter_network_password("invalid pass")
        self.moobe_awc.verify_connecting_screen(invisible=False)
        # Need to pass 2 first steps in thermometer process, so timeout should be 30 instead of 10
        self.moobe_awc.verify_wrong_password_popup(timeout=30)
        self.moobe_awc.reenter_network_password(self.password)
        self.moobe_awc.verify_successfully_connecting_printer_to_wifi(printer_obj=self.p)

    
    