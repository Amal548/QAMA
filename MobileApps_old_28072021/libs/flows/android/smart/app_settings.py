from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from SAF.decorator.saf_decorator import screenshot_capture


class AppSettings(SmartFlow):
    flow_name = "app_settings"
    HELP_CENTER = "help_center"
    NOTIFICATIONS_AND_PRIVACY = "notification_and_privacy"
    SUPPLY_STATUS = "supply_status"
    PROMOTIONAL_MESSAGING = "promotional_messaging"
    APP_IMPROVEMENT_PROGRAM = "app_improvement_program"
    MANAGEMENT_MY_PERSONALIZED_PROMOTIONS = "management_my_personlized_promotions"
    USE_5GHZ_WIFI = "use_5ghz_wifi"
    ABOUT = "about"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_sign_in_btn(self):
        """
        Click on Sign In button on App Settings screen
        """
        self.driver.wait_for_object("sign_in_btn")
        self.driver.click("sign_in_btn", change_check={"wait_obj": "sign_in_btn", "invisible": True})

    def click_sign_out_btn(self, ga=False):
        """
        Click on Sign In button on App Settings screen
        """
        if ga:
            self.driver.click("sign_out_btn_ga")
        else:
            self.driver.wait_for_object("sign_out_btn", timeout=15)
            self.driver.click("sign_out_btn", change_check={"wait_obj": "app_settings_title", "invisible": True})

    def click_create_account_btn(self):
        """
        Click on Create Account button on App Settings screen
        """
        self.driver.click("create_acc_btn", timeout=30, change_check={"wait_obj": "create_acc_btn", "invisible": True})

    def click_cancel_btn(self):
        """
        Click on Cancel button on Sign out screen
        """
        self.driver.click("cancel_btn")

    def click_refresh_btn(self):
        """
        Click on Refresh button on HPC login in screen
        """
        self.driver.click("refresh_btn")

    def sign_out_hpc_acc(self):
        """
        Sign out a HPC account
        """
        self.driver.wait_for_object("sign_out_btn", timeout=10)
        self.click_sign_out_btn()
        self.verify_sign_out_alert_dialog()
        # Click on Alert buton
        self.driver.click("sign_out_btn", index=1, format_specifier=[self.get_text_from_str_id("sign_out_btn")])
        self.driver.performance.start_timer("hpid_logout")
        self.verify_sign_in_btn(invisible=False)
        self.driver.performance.stop_timer("hpid_logout")
        
    def select_app_settings_opt(self, item_name):
        """
        click any item on app settings one by one
        :param item_name:
                HELP_CENTER
                NOTIFICATIONS_AND_PRIVACY
                ABOUT
                USE_5GHZ_WIFI
        """
        item_name = self.driver.return_str_id_value(item_name)
        self.driver.scroll("opt_item", format_specifier=[item_name], full_object=False, check_end=False)
        self.driver.click("opt_item", format_specifier=[item_name], change_check={"wait_obj":"sign_in_btn", "invisible": True})

    def toggle_on_off_btn(self, enable=True):
        """
        Enable/Disable each item after clicking each item from app settings
        :param enable:
        :param raise_e:
        """
        on_off_switch = self.driver.find_object("on_off_btn")
        if enable != (on_off_switch.get_attribute("checked").lower() =="true"):
            on_off_switch.click()
        # verify if current status of switch icon is not matched with expectation
        current_status_of_off_switch = self.driver.find_object("on_off_btn")
        if enable != (current_status_of_off_switch.get_attribute("checked").lower() =="true"):
            raise NoSuchElementException("Toggle of {} is not matched with expectation {}".format(current_status_of_off_switch, enable))

    def select_notification_privacy_opt(self, opt_name):
        """
        click any item on notification and privacy screen one by one
        :param item_name:
                SUPPLY_STATUS
                PROMOTIONAL_MESSAGING
                APP_IMPROVEMENT
                MANAGEMENT_MY_PERSONALIZED_PROMOTIONS
        """
        option_name = self.driver.return_str_id_value(opt_name)
        self.driver.scroll("opt_item", format_specifier=[option_name], full_object=False, check_end=False)
        self.driver.click("opt_item", format_specifier=[option_name], change_check={"wait_obj":"notification_and_privacy", "invisible": True})

    def dismiss_accept_cookies_popup(self):
        """
        Click on accept cookies button on privacy policy popup
        """
        self.driver.click("accept_cookies", change_check={"wait_obj":"accept_cookies", "invisible": True})

    def click_manage_my_privacy_settings(self):
        self.driver.scroll("management_my_personlized_promotions",click_obj=True)

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_app_settings(self, raise_e=True, timeout=10):
        """
        Verify app settings screen via:
            - App Settings title
        """
        return self.driver.wait_for_object("app_settings_title", timeout=timeout, raise_e=raise_e)

    def verify_sign_in_btn(self, invisible=False, raise_e=True):
        """
        Verify Sign In button
        :param is_invisible: visible or not
        """
        return self.driver.wait_for_object("sign_in_btn", timeout=15, invisible=invisible, raise_e=raise_e)

    def verify_app_settings_with_hpc_account(self, username=None, timeout=10, raise_e=True):
        """
        Verify app settings screen with HPC account login successfully:
            - Go to my HP Connected Account message
            - Sign out button
            - Verify current account match with username
        """
        if username:
            return self.driver.wait_for_object("hpc_username_txt", format_specifier=[username], timeout=timeout, raise_e=raise_e)
        return (self.verify_go_to_my_hpc_acc(raise_e=raise_e) is not False) and (self.verify_sign_out_btn(raise_e=raise_e, timeout=timeout) is not False)

    def verify_go_to_my_hpc_acc(self, raise_e=False):
        return self.driver.wait_for_object("go_to_my_hpc_acc", raise_e=raise_e)

    def verify_sign_out_btn(self, raise_e=False, timeout=3):
        return self.driver.wait_for_object("sign_out_btn", timeout=timeout, raise_e=raise_e)

    def verify_sign_out_alert_dialog(self):
        """
        Verify Sign Out alert dialog display via:
            - title
            - message
        """
        self.driver.wait_for_object("sign_out_btn", format_specifier=[self.get_text_from_str_id("sign_out_btn")],timeout=15)
        self.driver.wait_for_object("sign_out_alert_msg", timeout=15)

    def verify_notification_privacy_opt_screen(self, item_name):
        """
        Verify each item screen via:
          - Title
          - On/Off switch button
        :param item_name:
                SUPPLY_STATUS
                PROMOTIONAL_MESSAGING
                APP_IMPROVEMENT
                USE_5GHZ_WIFI
        """
        self.driver.wait_for_object("item_title", format_specifier=[self.driver.return_str_id_value(item_name)], timeout=15)
        self.driver.wait_for_object("on_off_btn", timeout=15)

    def verify_notification_privacy_screen(self):
        """
        Verify notification and privacy screen with below items:
         - Title: Notification and Privacy
         - Notification Settings
        """
        self.driver.wait_for_object("notification_and_privacy")
        self.driver.wait_for_object("notification_settings")

    @screenshot_capture(file_name="help_support.png")
    def verify_help_support_screen(self):
        """
        App direct into Help support webview screen after clicking Help & Support tile
        """
        self.driver.wait_for_object("help_support", timeout=30)

    def verify_accept_cookies_popup(self, raise_e=True):
        """
        Verify accept cookies popup
        """
        self.driver.wait_for_object("accept_cookies", timeout=20, raise_e=raise_e)