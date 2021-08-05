from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import pytest
import time


class FailConnectingPrinterToWiFi(Exception):
    pass


class MoobeAWC(SmartFlow):
    flow_name = "moobe_awc"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def connect_printer_to_wifi(self, ssid, password, is_secure=False, printer_obj=None):
        """
        From Connect Printer screen, connect printer to Wifi
            - Enter pass word
            - Click Continue button
            - Verify successful connecting printer to wifi
        
        :param ssid: network's ssid
        :param is_secure: True -> check Press button popup for secure BLE printer. False -> ignore this popup
        :param printer_obj: SPL instance. IT is used for secure BLE printer.
        """
        self.verify_connect_printer_to_wifi_screen(ssid)
        self.enter_network_password(password)
        self.verify_successfully_connecting_printer_to_wifi(is_secure=is_secure, printer_obj=printer_obj)

    def select_continue(self):
        """
        Click on Continue button
        Note: It is used at many screens of Moobe AWC
        """
        # Have to use format spedicifier for case sensitve
        self.driver.click("continue_btn", format_specifier=[self.driver.return_str_id_value("continue_btn")])

    def enter_network_password(self, pwd):
        """
        Enter network's password to text field on Connect Printer to Wi-Fi screen
        :type pwd: str
        """
        self.driver.send_keys("password_tf", pwd)
        self.select_continue()

    def dismiss_turn_on_ble_popup(self, is_allowed=True, raise_e=True):
        """
        Dismiss Turn On Ble popup if it display
        Note: display after clicking on Continue button of Connect Printer to Wi-Fi screen
        :param is_allowed: True -> click on Allow button. False -> click on Deny
        """
        if self.driver.wait_for_object("turn_on_ble_popup_title", timeout=10, raise_e=raise_e):
            self.select_continue()
            self.check_run_time_permission(accept=is_allowed)

    def reenter_network_password(self, pwd):
        """
        On Wrong Password popup,
            - Enter valid password again
            - Click on Connect button
        :type pwd: str

        End of flow: Connecting... screen
        """
        self.driver.send_keys("wrong_password_popup_tf", pwd)
        self.driver.click("wrong_password_popup_connect_btn")

    def select_wrong_password_popup_exit_setup(self):
        """
        Click on Exit Setup button on Wrong Password popup
        """
        self.driver.click("wrong_password_popup_exit_setup_btn")

    def select_need_pwd_help_btn(self):
        """
        Click on Need Password help? link
        """
        self.driver.click("need_pwd_help_btn")

    def select_ok_btn(self):
        """
        Select OK button on Network Password Help screen
        """
        self.driver.click("ok_btn")

    def select_info_btn(self):
        """
        Click on Info icon on Connect Printer to Wi-Fi screen
        """
        self.driver.click("info_icon")

    def select_done_btn(self):
        """
        Click on Done button on Connect Printer to Wi-Fi Information screen
        """
        self.driver.click("done_btn")

    def select_change_network_btn(self):
        """
        Click on Change Network button on Connect Printer to Wi-Fi screen
        """
        self.driver.click("change_network_btn")

    def dismiss_connecting_printer_to_wifi_popup(self, is_wait=True, raise_e=True):
        """
        Dismiss Connecting printer to Wi-Fi popup by clicking on Exit Setup or Wait button
        :param is_wait: True -> click on Wait button. False -> click on Exit Setup button
        """
        button_obj = "connecting_to_wifi_popup_wait_btn" if is_wait else "connecting_to_wifi_popup_exit_setup_btn"
        return self.driver.click(button_obj, raise_e=raise_e)

    def dismiss_need_more_time_popup(self):
        """
        Click on Try Again button on Need more time? popup
        """
        self.driver.click("need_more_time_popup_try_again_btn")

    def dismiss_cancel_confirmation_popup(self, is_exit=True):
        """
        Dismiss "Are you sure you want to cancel?" popup by clicking on Try again/Exit Setup
        Note: it is for secure BLE printer

        :param is_exit: True -> click on Exit Setup button. False -> click on Try again button
        """
        button_obj = "exit_setup_btn" if is_exit else "cancel_confirmation_popup_try_again_btn"
        self.driver.click(button_obj)

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_successfully_connecting_printer_to_wifi(self, timeout=120, is_secure=False, printer_obj=None):
        """
        From Connecting screen: a loop (3 times) for handling some popup
            - Connecting screen display
            - Connecting screen is invisile: there are some cases
                + Connecting to printer popup -> dismiss this popup by clicking on Wait button
                + Connected screen display -> DONE
            - After handling the popups, go back step 1 for another in loop since Connecting screen display again.

        :param timeout: based on steps in test case
        :param is_secure: True -> check Press button popup for secure BLE printer. False -> ignore this popup
        :param printer_obj: SPL instance. IT is used for secure BLE printer.
        """
        timeout = time.time() + timeout
        self.verify_connecting_screen(invisible=False)
        while time.time() < timeout:    
            if self.verify_printer_connected_to_wifi_screen(raise_e=False):
                return True
            # Next check is for Android 10 and up
            elif int(self.driver.platform_version) > 9 and self.verify_continue_guided_setup_screen(raise_e=False):
                return True
            elif self.verify_connecting_to_printer_popup(raise_e=False):
                self.dismiss_connecting_printer_to_wifi_popup(is_wait=True, raise_e=False)
            elif is_secure and self.verify_press_information_button_popup(timeout=10, raise_e=False):
                printer_obj.press_info_btn()
        raise FailConnectingPrinterToWiFi("Connecting printer to Wi-Fi fail in 120 seconds")

    def verify_connect_printer_to_wifi_screen(self, network_ssid=None):
        """
        Verify Connect Printer to Wi-Fi screen via:
            - title
            - Continue button
        :parameter printer_ssid is for GA event  tracking
        """
        if network_ssid:
            self.driver.ga_container.insert_ga_key("Printer-ssid", network_ssid)
            self.driver.wait_for_object("ssid_txt", format_specifier=[network_ssid], timeout=10)
        self.driver.wait_for_object("connect_title", timeout=10)
        # Use it for case sensitive.
        self.driver.wait_for_object("continue_btn", format_specifier=[self.driver.return_str_id_value("continue_btn")], timeout=10)

    def verify_connecting_screen(self, invisible=False, timeout=10):
        """
        Verify Connecting screen visible/invisible via:
            - title
        Note: if using visible, timeout may be longer because of connecting process
        """
        self.driver.wait_for_object("connecting_title", invisible=invisible, timeout=timeout)

    def verify_wrong_password_popup(self, raise_e=True, timeout=10):
        """
        Verify current popup is "Something might be wrong with your password." popup via:
            - title of popup
        """
        return self.driver.wait_for_object("wrong_password_popup_title", timeout=timeout, raise_e=raise_e)

    def verify_connecting_to_printer_popup(self, raise_e=True):
        """
        Verify current popup is "Connecting to printer" popup via:
            - title of popup
        """
        return self.driver.wait_for_object("connecting_to_wifi_popup_title", timeout=10, raise_e=raise_e)

    def verify_printer_connected_to_wifi_screen(self, printer_name=None, raise_e=True, timeout=10):
        """
        Verify current screen is "Printer Connected to Wi-Fi" screen via:
            - title
        :parameter: printer_name is only for GA events tracking
        """
        if printer_name:
            self.driver.ga_container.insert_ga_key("Printer", printer_name)
        return self.driver.wait_for_object("printer_connected_title", timeout=timeout, raise_e=raise_e)

    def verify_continue_guided_setup_screen(self, raise_e=True):
        """
        Verify current screen has text "Let's contnue our guided setup"
        """
        return self.driver.wait_for_object("awc_guided_setup_txt", raise_e=raise_e)

    def verify_need_pwd_help_screen(self):
        """
        Verify Need Password Help screen
        """
        self.driver.wait_for_object("need_pwd_help_title"),
        self.driver.wait_for_object("exit_setup_btn"),
        self.driver.wait_for_object("ok_btn")

    def verify_connect_printer_to_wifi_info_screen(self):
        """
        Verify Connect Printer to Wifi Information screen
        """
        self.driver.wait_for_object("moobe_connection_info_body", timeout=20)
        self.driver.wait_for_object("done_btn")

    def verify_change_network_or_printer_screen(self):
        """
        Verify Change network or Printer screen with:
         - title
         - button: Network, Printer
        """
        self.driver.wait_for_object("change_network_or_printer_title")
        self.driver.wait_for_object("network_btn")
        self.driver.wait_for_object("printer_btn")

    def verify_press_information_button_popup(self, timeout=10, raise_e=True):
        """
        Verify "Press the flashing Information button on your printer" popup via:
            - title
        :param timeout: based on steps in the test case
        :param raise_e: True -> raise TimeoutException. False -> return True/False 
        """
        return self.driver.wait_for_object("press_information_btn_popup_title", timeout=timeout, raise_e=raise_e)

    def verify_need_more_time_popup(self, raise_e=True):
        """
        Verify "Need more time?" popup via:
            - title
        Note: this popup display if no action is perfomed in 5 minutes after press button popup displays.
              therefore, timeout for this popup 305 seconds.
        :param raise_e: True -> raise TimeoutException. False -> return True/False
        """
        return self.driver.wait_for_object("need_more_time_popup_title", timeout=305, raise_e=raise_e)

    def verify_cancel_confirmation_popup(self, raise_e=True):
        """
        Verify "Are you sure you want to cancel?" popup via:
            - title
        Note: this popup is used for secure BLE printer
        :param raise_e: True -> raise TimeoutException. False -> return True/False
        """
        return self.driver.wait_for_object("cancel_confirmation_popup_title", raise_e=raise_e)