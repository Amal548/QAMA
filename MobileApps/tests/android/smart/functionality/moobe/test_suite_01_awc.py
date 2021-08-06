import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_01_AWC(object):
    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Skip test suite if printer is not supported for awc
        if "awc" not in cls.fc.get_moobe_connect_wifi_type(cls.p):
            pytest.skip("{} is not supported for AWC".format(cls.p.serial))

        # Define variables
        cls.ssid, cls.password = get_wifi_info(request)

    def test_01_setup_successful_awc(self):
        """
        Description:
            Precondition: set printer to OOBE mode
                          turn off bluetooth of mobile device
            1. Load to Printers app from Home screen of HP Smart. 
            2. Click on Add Printer -> Dimiss "turn on bluetooth" popup if it displays for Android 10
            3. Select OOBE target printer
            4. Go through AWC process to connect printer to Wi-Fi.
                Note: Besides Android 10, dismiss "turn on bluetooth" if it displays

        Expected Result:
            4. Printer Connected screen display
        """
        self.fc.flow_home_moobe_connect_printer_to_wifi(printer_obj=self.p,
                                                        ssid=self.ssid,
                                                        password=self.password, 
                                                        is_ble=False)
