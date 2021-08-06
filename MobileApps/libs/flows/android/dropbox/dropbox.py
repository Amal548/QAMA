from MobileApps.libs.flows.android.dropbox.dropbox_flow import DropboxFlow
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import WebDriverException


class Dropbox(DropboxFlow):
    flow_name = "dropbox"

    def __init__(self, driver):
        super(Dropbox, self).__init__(driver)
        self.driver.load_app_strings(self.project,
                                     ma_misc.get_apk_path("dropbox"),
                                     self.driver.session_data["language"])

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def load_app(self):
        """
        Load Dropbox (Login page/Home page app via package and activity
        """
        self.driver.wdvr.start_activity(PACKAGE.DROPBOX, LAUNCH_ACTIVITY.DROPBOX_HOME, app_wait_activity=WAIT_ACTIVITY.DROPBOX)

    def skip_choose_dropbox_plan_screen(self):
        """
        Skip Choose Your Dropbox Plan screen
        """
        if self.driver.wait_for_object("choose_plan_title", timeout=10, raise_e=False):
            self.driver.terminate_app(PACKAGE.DROPBOX)
            self.load_app()

    def unlink_devices(self):
        """
        Unlink 3 devices if this screen require displays.
        :return:
        """
        if self.driver.wait_for_object("unlink_some_devices_btn",  format_specifier=[self.get_text_from_str_id("unlink_some_devices_btn")],timeout=10, raise_e=False):
            self.driver.click("unlink_some_devices_btn", format_specifier=[self.get_text_from_str_id("unlink_some_devices_btn")])
            self.driver.wait_for_object("unlink_devices_cb", timeout=20)
            devices_cbs = self.driver.find_object("unlink_devices_cb", multiple=True)
            for cb in devices_cbs:
                cb.click()
            self.driver.click("unlink_devices_unlink_btn")
            self.driver.wait_for_object("unlink_confirmation_popup_confirm_btn", timeout=10)
            self.driver.click("unlink_confirmation_popup_confirm_btn")
            self.driver.wait_for_object("continue_btn", timeout=30)
            self.driver.click("continue_btn")
    def skip_connect_your_computer_screen(self):
        """
        "Skip Connect your computer screen
        :return:
        """
        if self.driver.wait_for_object("connect_your_computer_title", timeout=10, raise_e=False):
            self.driver.click("connect_your_computer_not_now_btn")

    def skip_how_to_backup_photos_screen(self):
        """
        Skip 'How do you want Dropbox to backup your photos" screen
        """
        if self.driver.wait_for_object("backup_photos_screen_skip_btn", raise_e=False):
            self.driver.press_key_back()

    def login(self, username, password):
        """
        Start to Welcome screen for loging in
        Login to an account
        :param username:
        :param password:
        """
        self.driver.wait_for_object("tour_sign_in_btn", timeout=10,clickable=True)
        self.driver.click("tour_sign_in_btn")
        self.driver.find_object("credential_tf", index=0).send_keys(username)
        self.driver.find_object("credential_tf", index=1).send_keys(password)
        self.driver.click("sign_in_btn")
        self.driver.wait_for_object("progress_icon", timeout=60, invisible=True)

    def logout(self):
        """
        Precondition: Dopbox is logged in to an account
        Start at Home screen by calling load_app() function
        Logout account
        """
        if self.driver.wait_for_object("nav_drawer_layout", invisible=True, timeout=10, raise_e=False):
            self.driver.click("menu_btn", format_specifier=[self.get_text_from_str_id("menu_btn")])
        self.driver.scroll("nav_settings_btn", click_obj=True, check_end=False, timeout=10)
        self.driver.wait_for_object("dropbox_settings_title", timeout=10)
        self.driver.scroll("sign_out_btn", click_obj=True, check_end=False)
        self.driver.wait_for_object("confirm_popup_sign_out_btn", timeout=10)
        self.driver.click("confirm_popup_sign_out_btn")
        self.driver.wait_for_object("tour_sign_in_btn")

    def allow_account_access_dropbox(self, username):
        """
        Allow access to Dropbox for an account
            - Verify the right screen and account via username
            - Click on Allow button
        :param username: username (email) is used to log in
        """
        self.verify_allow_access_screen()
        # Verify correct username
        self.driver.wait_for_object("allow_access_account", format_specifier=[username], timeout=5)
        self.driver.click("allow_access_btn")

    def skip_access_computer_file_screen(self):
        """
        Skip the 'Access your computer's files on this device' screen 
        """
        if self.driver.wait_for_object("set_up_btn", raise_e=False):
            self.driver.press_key_back()

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_welcome_screen(self, raise_e=True):
        """
        Verify current screen is Welcome screen
        """
        return self.driver.wait_for_object("tour_sign_in_btn", timeout=10, raise_e=raise_e)

    def verify_allow_access_screen(self, raise_e=True):
        """
        Verify current screen is Allow access screen

        Note: Allow access screen also take time for processing.
        :param raise_e:
        """
        return self.driver.wait_for_object("dropbox_title", timeout=10, raise_e=raise_e) and \
               self.driver.wait_for_object("allow_access_btn", timeout=30, raise_e=raise_e)

