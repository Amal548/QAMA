import pytest
import time
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_03_Secure_BLE(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Skip test suite if printer is not supported for BLE (not secure BLE)
        if cls.fc.get_moobe_connect_wifi_type(cls.p) != "secure_ble":
            pytest.skip("{} is not supported for secure BLE".format(cls.p.serial))

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.moobe_awc = cls.fc.flow[FLOW_NAMES.MOOBE_AWC]
        cls.moobe_setup_complete = cls.fc.flow[FLOW_NAMES.MOOBE_SETUP_COMPLETE]

        # Define variables
        cls.ssid, cls.password = get_wifi_info(request)

    def test_01_successfully_connect_printer_to_wifi(self):
        """
        Description:
            Precondition: set printer to OOBE mode. 
            1. From Home screen, process to Add Printer screen, then select OOBE printer
            2. At Connect Wi-Fi screen, enter valid password, then click on OK button
            3. Press on information button on printer
            4. Continue process

        Expected Result:
            2. A push button popup display
            3. Pop up disappear 
            4. Connected screen display
        """
        self.fc.flow_home_moobe_connect_printer_to_wifi(printer_obj=self.p,
                                                        ssid=self.ssid,
                                                        password=self.password,
                                                        is_ble=True,
                                                        is_secure=True)

    @pytest.mark.parametrize("times", [1, 3])
    def test_02_successfully_connect_printer_to_wifi_after_retry(self, times):
        """
        Description:
            Precondition: set printer to OOBE mode. 
            1. From Home screen, process to Add Printer screen, then select OOBE printer
            2. At Connect Wi-Fi screen, enter valid password, then click on OK button.
            3. The following steps is in loop based on times variale:
                - Push button popup display -> Wait for 5 minutes -> Retry popup display
                - Click on Retry button
            4. Press on information button on printer -> Continue process

        Expected Result:
            2. A push button popup display
            4. Connected screen display.
        """
        self.__load_connecting_screen()
        for _ in range(times):
            self.moobe_awc.verify_press_information_button_popup()
            self.moobe_awc.verify_need_more_time_popup()
            self.moobe_awc.dismiss_need_more_time_popup()
        self.moobe_awc.verify_press_information_button_popup()
        self.p.press_info_btn()
        self.moobe_awc.verify_successfully_connecting_printer_to_wifi(is_secure=True, printer_obj=self.p)

    def test_03_cancel_connecting_printer_to_wifi(self):
        """
        Description:
            Precondition: set printer to OOBE mode. 
            1. From Home screen, process to Add Printer screen, then select OOBE printer
            2. At Connect Wi-Fi screen, enter valid password, then click on OK button
            3. Press cancel button on printer when press button popup displays
            4. Click on Exit Setup button
            5. Click on Continue button
            6. From Home screen, select this OOBE printer again in Add Printer screen
        Expected Result:
            2. A push button popup display
            3. Confirmation of Cancel popup
            4. Exit Setup screen
            5. Home screen
            6. Connect Wi-Fi screen display
        """
        self.__load_connecting_screen()
        self.p.press_cancel_btn()
        self.moobe_awc.verify_cancel_confirmation_popup()
        self.moobe_awc.dismiss_cancel_confirmation_popup(is_exit=True)
        self.moobe_setup_complete.verify_exit_setup_screen()
        self.moobe_setup_complete.select_exit_setup_continue_btn()
        self.home.verify_home_nav()
        self.fc.flow_home_select_oobe_printer(printer_obj=self.p, 
                                              ssid=self.ssid, 
                                              is_ble=True)
        self.moobe_awc.verify_connect_printer_to_wifi_screen(self.ssid)

    def test_04_successfully_connect_printer_to_wifi_after_try_again_from_cancel(self):
        """
        Description:
            Precondition: set printer to OOBE mode. 
            1. From Home screen, process to Add Printer screen, then select OOBE printer
            2. At Connect Wi-Fi screen, enter valid password, then click on OK button
            3. Press cancel button on printer when press button popup displays
            4. Click on Try Again button
            5. Press information button on printer -> continue process
        Expected Result:
            2. A push button popup display
            3. Confirmation of Cancel popup
            4. Push button popup display
            5. Connected screen display.
        """
        self.__load_connecting_screen()
        self.p.press_cancel_btn()
        self.moobe_awc.verify_cancel_confirmation_popup()
        self.moobe_awc.dismiss_cancel_confirmation_popup(is_exit=False)
        self.moobe_awc.verify_press_information_button_popup()
        self.p.press_info_btn()
        self.moobe_awc.verify_successfully_connecting_printer_to_wifi(is_secure=True, printer_obj=self.p)

    def test_05_successful_connect_printer_to_wifi_with_putting_app_background_before_taping(self):
        """
        Description:
            Precondition: set printer to OOBE mode. 
            1. From Home screen, process to Add Printer screen, then select OOBE printer
            2. At Connect Wi-Fi screen, enter valid password, then click on OK button
            3. Putting app background when press button popup displays
            4. Open app again, then press i button of printer
            5. Continue process
        Expected Result:
            5. Connected screen display
        """
        self.__load_connecting_screen()
        self.fc.run_app_background(3)
        self.moobe_awc.verify_press_information_button_popup()
        self.p.press_info_btn()
        self.moobe_awc.verify_successfully_connecting_printer_to_wifi(is_secure=True, printer_obj=self.p)

    def test_06_successful_connect_printer_to_wifi_with_putting_app_background_after_taping(self):
        """
        Description:
            Precondition: set printer to OOBE mode. 
            1. From Home screen, process to Add Printer screen, then select OOBE printer
            2. At Connect Wi-Fi screen, enter valid password, then click on OK button
            3. Press push button when press button popup displays
            4. Push app in background. Then, open app again
            5. Continue process
        Expected Result:
            5. Connected screen display
        """
        self.__load_connecting_screen()
        self.p.press_info_btn()
        self.fc.run_app_background(3)
        self.moobe_awc.verify_successfully_connecting_printer_to_wifi(is_secure=True, printer_obj=self.p)

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __load_connecting_screen(self):
        """
        From Home screen:
            - Select oobe printer
            - Enter valid password
            - Click on Continue button
            - Wait for ppopup for requesting click on i button
        End of flow: popup displays
        """
        self.fc.flow_home_select_oobe_printer(printer_obj=self.p, 
                                              ssid=self.ssid,
                                              is_ble=True)
        self.moobe_awc.verify_connect_printer_to_wifi_screen(self.ssid)
        self.moobe_awc.enter_network_password(self.password)
        self.moobe_awc.verify_connecting_screen(invisible=False)
        # Depend on printer, step 1&2 in thermometer screens are finished in 15-20 seconds.
        # Therefore, using 20 seconds timout for all printers in Chamber.
        self.moobe_awc.verify_press_information_button_popup(timeout=20)