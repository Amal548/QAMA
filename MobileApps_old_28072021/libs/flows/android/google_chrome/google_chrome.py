from MobileApps.libs.flows.android.google_chrome.google_chrome_flow import GoogleChromeFlow
from MobileApps.resources.const.android import const
from selenium.common.exceptions import NoSuchElementException, WebDriverException

import logging
import time

class GoogleChrome(GoogleChromeFlow):
    flow_name="google_chrome"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################
    def open_google_chrome(self):
        """
        opens the google chrome browser on mobile: Make sure chrome browser is installed on device before test starts:
        :return:
        """
        self.driver.wdvr.start_activity(const.PACKAGE.GOOGLE_CHROME, const.LAUNCH_ACTIVITY.GOOGLE_CHROME, app_wait_activity="*")
        self.handle_welcome_screen_if_present()

    def handle_welcome_screen_if_present(self):
        """
        Skip Welcome screen if it displays
        """
        if self.driver.wait_for_object("welcome_screen_accept_btn", raise_e=False):
            self.driver.click("welcome_screen_accept_btn", change_check={"wait_obj": "welcome_screen_accept_btn", "invisible": True})
            self.driver.click("ok_got_it_btn", change_check={"wait_obj": "ok_got_it_btn", "invisible": True})

    def select_search_box(self):
        """
        selects the search box to enter the url:
        :return:
        """
        try:
            self.driver.click("web_page_search_box")
        except NoSuchElementException:
            self.driver.click("search_box_for_url")

    def enter_url_and_go_to_website(self, url="https://www.wikipedia.org"):
        self.driver.send_keys("search_box_for_url", url)
        self.driver.wait_for_object("search_result", timeout=30).click()

    def select_3_dot_menu(self):
        """
        selects the three dot button on right corner:
        :return:
        """
        self.driver.wait_for_object("3_dot_menu_btn")
        self.driver.click("3_dot_menu_btn")

    def select_share_from_3_dot_menu_options(self):
        """
        selects the share button from 3 dot menu options:
        :return:
        """
        self.driver.click("share_button")

    def delete_chrome_web_cache(self):
        self.open_google_chrome()
        self.select_3_dot_menu()
        self.driver.click("settings_item")
        self.driver.swipe(direction="down", per_offset=0.5)
        self.driver.click("privacy_item")
        self.driver.click("clear_browsing_data")
        self.driver.click("basic_tab")
        self.driver.click("time_range")
        self.driver.click("all_time_text")
        clear_browser_history = self.driver.session_data["app_strings"]["google_chrome"]["clear_history_title"]
        clear_cookies = self.driver.session_data["app_strings"]["google_chrome"]["clear_cookies_and_site_data_title"]
        clear_cache = self.driver.session_data["app_strings"]["google_chrome"]["clear_cache_title"]
        self.driver.check_box("browsing_history_check_box",format_specifier=[clear_browser_history],uncheck=False)
        self.driver.check_box("cookies_check_box",format_specifier=[clear_cookies],uncheck=False)
        self.driver.check_box("cached_images_check_box",format_specifier=[clear_cache],uncheck=False)
        self.driver.click("clear_btn")
        self.driver.back()
        self.driver.back()
        self.driver.back()

    def click_webview_close_btn(self):
        """
        Click on Close button on HPID sign page
        """
        self.driver.wait_for_object("webview_close_btn", timeout=30)
        self.driver.click("webview_close_btn", change_check={"wait_obj": "webview_close_btn", "invisible": True})
########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################
    def verify_google_chrome_home_screen(self):
        """
        verifies the google chrome home screen using home button on left top corner:
        :return:
        """
        return self.driver.wait_for_object("3_dot_menu_btn", raise_e=False) is not False

    def verify_3_dot_menu_screen(self):
        """
        verifies the 3 dot menu screen using tray with some options:
        :return:
        """
        self.driver.wait_for_object("3_dot_menu_tray", timeout=5)

########################################################################################################################
#                                                                                                                      #
#                                                   Guard Code                                                         #
#                                                                                                                      #
########################################################################################################################

    def press_print_button_and_redo_share_to_print_if_needed(self, max_retry=3, flow=None):
        is_pressed = False
        for _ in range(max_retry):
            try:
                is_pressed = flow.select_app(self.driver.return_str_id_value_from_id("button_label__print", project="hpps"))
                break
            except NoSuchElementException:
                logging.debug("Failed to press the print button.")
            if not is_pressed:
                logging.debug("Something happens. Redoing the search...")
                self.driver.back()
                self.select_3_dot_menu()
                # An explicit wait rather than a verification
                self.verify_3_dot_menu_screen()
                self.select_share_from_3_dot_menu_options()
        if not is_pressed:
            raise NoSuchElementException("Print button failed to appear after " + str(max_retry + 1) + " retries")