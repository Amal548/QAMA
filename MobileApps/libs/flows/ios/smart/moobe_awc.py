from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
import time
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class MoobeAwc(SmartFlow):
    flow_name = "moobe_awc"

    def skip_moobe_printer_screen(self):
        self.pass_weak_bluetooth_connection()
        if self.driver.wait_for_object("skip_btn", timeout=5, raise_e=False):
            self.driver.click("skip_btn")
            return True
        self.pass_weak_bluetooth_connection()
        if self.driver.wait_for_object("cancel_btn", timeout=3, raise_e=False):
            self.driver.click("cancel_btn")

    def pass_weak_bluetooth_connection(self, timeout=5):
        if self.driver.wait_for_object("weak_bluetooth_title", timeout=timeout, raise_e=False):
            self.driver.click("need_pwd_help_popup_ok_btn")

    def check_if_select_network(self, timeout=180):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                self.driver.wait_for_object("connect_to_network_title", timeout=5)
                return True
            except TimeoutException:
                pass
            try:
                self.driver.wait_for_object("wifi_signal_img", timeout=5)
                return False
            except TimeoutException:
                pass
        raise TimeoutException("Neither path showed up")

    def connect_printer_to_network(self, ssid, timeout=60):
        if self.verify_connect_printer_to_network_screen(timeout=timeout, raise_e=False):
            self.driver.wdvr.execute_script('mobile:scroll', {'element':
                                            self.driver.find_object("connect_printer_to_network_ssid",
                                                                    format_specifier=[ssid]), "toVisible": True})
            self.driver.click("connect_printer_to_network_ssid", format_specifier=[ssid])

    def select_i_icon(self):
        """
        CLick on 'i' icon button
        End of flow: a popup for instruction
        """
        self.driver.click("i_icon_btn")

    def select_continue(self):
        """
        Click on Continue button
        It is used for all screens that have Continue button as name
        Enf of flow: next screen
        """
        self.driver.click("continue_btn")

    def select_help_popup_done(self):
        """
        Click on Done button of help (or instruction)popup
        End of flow: previous screen
        """
        self.driver.click("help_popup_done_btn")

    def select_network_not_listed(self):
        """
        Click on Network NOt Listed button on Connect printer to network screen
        End of flow: Network not list popup
        """
        self.driver.click("network_not_listed_btn")

    def select_network_not_listed_retry(self):
        """
        Click on Retry button of Network not listed popup
        End of flow: Connect printer to network
        """
        self.driver.wait_for_object("network_not_listed_popup_title", timeout=10)
        self.driver.click("popup_retry_btn")

    def select_network_name(self, ssid, wait_time=10):
        """
        Select target network from network list on Connect printer to network screen
        :param ssid:network's ssid
        :param wait_time: time for waiting network list loading.
        End of flow: Connect the printer to Wi-Fi
        """
        timeout = time.time() + wait_time
        is_displayed = False
        self.driver.wait_for_object("networks_tv")
        while time.time() < timeout:
            try:
                self.driver.click(ssid)
                is_displayed = True
                break
            except NoSuchElementException:
                logging.info("Target network '{}' has been displayed on list".format(ssid) )
                time.sleep(3)
            if not is_displayed:
                logging.info("Refreshing wifi list.")
                
                self.driver.swipe("networks_tv")
                # self.app.scroll_down_to_element_by_pair_value(
                #     self.driver.find_object(self.ui.get_name("networks_tv", "moobe_awc")),
                #     ("name", ssid),
                #     timeout=self.loading_timeout + 30,
                #     offset=30
                #     )
        if not is_displayed:
            raise NoSuchElementException("Wi-Fi {} was mot displayed on thie list.".format(ssid))
         # self.driver.click(ssid, timeout=self.loading_timeout + 30)

    def select_network_pwd_help(self):
        """
        Click on Need Password Help? link
        End of flow: Need password help popup
        """

        name = self.ui.get_object("need_pwd_help_link")
        el = self.driver.find_object(name)
        print("FOUND {} ELEMENTS WITH THE NAME [{}]".format(len(el), name))
        el[0].click()

    def select_network_pwd_help_popup_ok(self):
        """
        Click on Ok button of Need password help popup
        End of flow: Connect the printer to Wi-Fi screen
        """
        self.driver.click("need_pwd_help_popup_ok_btn")

    def enter_wifi_pwd(self, wifi_pwd, press_enter=False):
        """
        Enter password of target Wi-Fi. Then, press enter button on keyboard
        ENd of screen: Connecting the printer
        """
        self.driver.send_keys("password_tf", wifi_pwd, press_enter=press_enter)
    
    def select_reconnect_device_popup_close(self):
        """
        Click on Close button of Reconnect to mobile device popup
        End of flow: Reconnect to your device to network screen
        """
        self.driver.click("reconnect_device_popup_close_btn")
    
    def select_change_network(self):
        """
        Click on the Change network button
        :return:
        """
        name = self.ui.get_ui_object("change_network_btn")
        el = self.driver.find_object(name)
        print("FOUND {} ELEMENTS WITH THE NAME OF [{}]".format(len(el), name ))
        el[0].click()

    def check_lets_get_your_printer_connected_to_wifi_screen(self):
        if self.verify_get_your_printer_connected_to_wifi_screen(raise_e=False):
            self.select_continue()

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_connect_printer_to_wifi_instruction_screen(self):
        self.driver.wait_for_object("password_tf",timeout=5)

    def verify_connect_printer_to_wifi_popup(self):
        """
        Verify current popup is Connect the Printer to Wi-Fi via:
            - title
            - Done button
        """
        self.driver.wait_for_object("info_popup", timeout=5)
        self.driver.wait_for_object("help_popup_done_btn", timeout=5)

    def verify_visible_play_btn(self):
        """
        Verify that Play icon button displays after completing playtin
            Note: add 30 seconds to timeout for playing video
        """
        self.driver.wait_for_object("play_btn")
        self.driver.click("play_btn")
        self.driver.wait_for_object("play_btn")

    def verify_connect_printer_to_wifi_pwd_screen(self):
        """
        Verify current screen is "Connect the printer to Wi-Fi" that have password textfield via:
            - title
            - pwd tf
        """
        self.driver.wait_for_object("wifi_signal_img", timeout=30)
        self.driver.wait_for_object("password_tf")

    
    def verify_visible_process_txt(self):
        """
        Verify that Processing... text display on Connect printer
            - title
        Note: add 20 seconds to time out because sometimes, detecting printer take long time.
        """
        self.driver.wait_for_object("processing_txt")

    def verify_invisible_process_txt(self):
        """
        Verify the text "Processing..." invisible
        Note: add 20 seconds to timeout because of unstable processing time.
        """
        self.driver.wait_for_object("processing_txt")

    def verify_detecting_printer_screen(self):
        """
        Verify the text "Processing..." invisible
        Note: add 20 seconds to timeout because of unstable processing time.
        """
        time.sleep(2)
        timeout = time.time() + 300
        found = True
        while time.time() < timeout:
            try:
                progress = self.driver.find_object("progress_indicator")
                is_visible = progress.get_attribute("visible")
                logging.info("PROGRESS INDICATION WAS FOUND WITH visible as {}".format(is_visible))
                self.driver.wait_for_object("connect_to_wifi_title")
                break
            except Exception:
                logging.info("PROGRESS INDICATIOR WAS NOT FOUND BUT ITS STILL VISIBLE ON SCREEN SINCE CONNECT TO WIFI TITLE WAS NOT VISIBLE EITEHR")

    def verify_connect_printer_to_network_screen(self, timeout=30, raise_e=True):
        """
        Verify current screen is "Connect printer to network" via:
            - title
        """
        return self.driver.wait_for_object("connect_to_network_title", timeout=timeout, raise_e=raise_e)

    def verify_network_not_listed_popup_screen(self):
        """
        Click on Retry button of Network not listed popup
        End of flow: Connect printer to network
        """
        self.driver.wait_for_object("network_not_listed_popup_title", timeout=10)

    def verify_need_pwd_help_popup(self):
        """
        Verify current popup is Need password help via:
            - title
            - Ok button
        """
        self.driver.wait_for_object("need_pwd_help_popup_title")
        self.driver.wait_for_object("need_pwd_help_popup_ok_btn")

    def verify_connecting_step_1(self):
        """
        Verify 'Printer found' text of step 1 displays
        """
        self.driver.wait_for_object("connecting_step1_txt", timeout=60)

    def verify_connecting_step_2(self):
        """
        Verify 'Preparing the printer..' text of step 1 displays
        """
        self.driver.wait_for_object("connecting_step2_txt", timeout=60)

    def verify_connecting_step2_complete(self):
        """
        Verify 'Printer prepared' text displays
        Note: Add 60 seconds to timeout because of preparing time.
        """
        self.driver.wait_for_object("connecting_step2_complete_txt", timeout=60)

    def verify_connecting_step_3(self):
        """
        Verify 'Getting printer information' text of step 1 displays
        """
        self.driver.wait_for_object("connecting_step3_txt", timeout=60)

    def verify_connecting_step3_complete(self):
        """
        Verify 'Printer information obtained' text displays
        Note: Add 60 seconds to timeout because of obtaining time.
        """
        self.driver.wait_for_object("connecting_step3_complete_txt", timeout=60)

    def verify_connecting_failed(self, ga={}):
        """
        If one step fail, call this function to track event
        NOTE: this function is only used to track event for fail step in connecting.
        :param ga:
        :return:
        """
        logging.info("Failing connecting to Wi-Fi")

    def verify_reconnect_device_screen(self):
        """
        Verify that current screen is Reconnect your device to the network screen via:
            - title
        NOTE: add 60 seconds to timeout because it need to  wait for completing step4 and step 5 of Connecting screen
        """
        self.driver.wait_for_object("reconnect_device_to_network_title")

    def verify_reconnect_device_popup(self):
        """
        Verify that current popup is Reconnect to mobile device via:
            - title
            - Close button
        """
        self.driver.wait_for_object("reconnect_device_popup_title")
        self.driver.wait_for_object("reconnect_device_popup_close_btn")

    def verify_printer_connected_screen(self, timeout=180):
        """
        Verify that current screen is Printer connected to Wi-Fi screen via:
            -title
        NOTE: add 60 seconds to timeout because of Detecting printer...
        """
        self.driver.wait_for_object("connected_title", timeout=timeout)

    def did_wifi_reconnect_automatically(self, wait_time=120):
        """
        After the Moobe Conenction step the flow has two directions to go...
        Either Reconnect Iphone Network screen
        or
        Wifi network connected screen
        :return: true if wifi automatically connected
                false if needed to reconnect manually
        """
        timeout = time.time() + wait_time
        while time.time() < timeout:
            try:
                self.driver.wait_for_object("connected_title")
                return True
            except TimeoutException:
                try:
                    self.driver.wait_for_object("reconnect_device_to_network_title")
                    return False
                except TimeoutException:
                    logging.info("Still on Moobe Connection Screen")
        raise TimeoutException("Moobe Connection Screen took {} seconds to complete".format(wait_time))

    def did_network_change_screen_redirect_automatically(self):
        """
        after selecting printer form Settigns wifi list sometimes the App will redirect itsefl to the Change Network Screen from the enter password screen
        :return:
        """

        timeout = time.time() + 120
        while time.time() < timeout:
            try:
                self.driver.wait_for_object("connect_to_network_title")
                return True
            except TimeoutException:
                try:
                    self.driver.wait_for_object("connect_to_wifi_title")
                    return False
                except TimeoutException:
                    logging.info("Waiting for detecting printers to finish")
                    raise TimeoutException("Detecting printers screen did not finish within 120 seconds")

    def verify_get_your_printer_connected_to_wifi_screen(self, raise_e=True):
        return self.driver.wait_for_object("get_your_printer_connected_to_wifi_title", timeout=15, raise_e=raise_e)

    def verify_connecting_to_printer(self):
        self.driver.wait_for_object("connecting_to_wifi_txt", timeout=30)

    def select_retry_button(self, timeout=10):
        self.driver.wait_for_object("_shared_retry_btn", timeout=timeout).click()

    def verify_network_loaded(self, ssid_name):
        self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[ssid_name], timeout=90)

    def verify_reconnect_your_device_title(self, raise_e=False, timeout=60):
        return self.driver.wait_for_object("reconnect_device_to_network_title", raise_e=raise_e, timeout=timeout)

    # ----------------------------------- SECURE BLE ------------------------------------------------------------
    def verify_information_security_popup(self):
        self.driver.wait_for_object("press_info_button_header", timeout=60)
        self.driver.wait_for_object("press_button_dialog", timeout=60)

    def verify_try_again_ui(self, timeout=360):
        self.driver.wait_for_object("need_more_time_header", timeout=timeout)
        self.driver.wait_for_object("try_again_body_text", timeout=timeout)
        self.driver.wait_for_object("try_again_btn", timeout=timeout)

    def select_try_again(self):
        self.driver.wait_for_object("try_again_btn", clickable=True, timeout=10).click()

    def select_exit_setup_btn(self):
        self.driver.wait_for_object("popup_exit_setup_btn", clickable=True, timeout=10).click()

    def verify_cancel_setup_popup(self):
        self.driver.wait_for_object("want_to_cancel_body")
        self.driver.wait_for_object("want_to_cancel_title")
        self.driver.wait_for_object("try_again_btn")
        self.driver.wait_for_object("popup_exit_setup_btn")

    def verify_exit_setup_ui(self):
        self.driver.wait_for_object("exit_setup_note")
        self.driver.wait_for_object("exit_setup_message")
        self.driver.wait_for_object("popup_exit_setup_btn")
