import logging
from abc import ABCMeta

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from MobileApps.libs.flows.ios.ios_flow import IOSFlow
from MobileApps.resources.const.ios.const import BUNDLE_ID


class SmartFlow(IOSFlow):
    __metaclass__ = ABCMeta
    project = "smart"

    def __init__(self, driver):
        super(SmartFlow, self).__init__(driver)
        self.load_smart_app_shared_ui()

    def load_smart_app_shared_ui(self):
        ui_map = self.load_ui_map(system="IOS", project="smart", flow_name="shared_obj")
        self.driver.load_ui_map("smart", "shared_obj", ui_map)
        return True

    def get_ios_device_type(self):
        return "iPhone" if "iphone" in self.driver.driver_info['deviceName'].lower() else 'iPad'

    def verify_rootbar_home_icon(self, raise_e=True):
        return self.driver.wait_for_object("home_icon_on_rootbar", raise_e=raise_e)

    def verify_rootbar_documents_icon(self, raise_e=True):
        return self.driver.wait_for_object("files_and_photos_icon_rootbar", raise_e=raise_e)

    def verify_rootbar_scan_icon(self, raise_e=True):
        return self.driver.wait_for_object("scan_icon_on_rootbar", raise_e=raise_e)

    def verify_rootbar_app_settings(self):
        return self.driver.wait_for_object("settings_icon_on_rootbar")

    def verify_rootbar_account_icon(self):
        return self.driver.wait_for_object("_shared_account")

    def verify_rootbar_create_account_icon(self):
        return self.driver.wait_for_object("_shared_create_account")

    def verify_rootbar_sign_in(self):
        return self.driver.wait_for_object("_shared_sign_in")

    def verify_bottom_navigation_bar(self):
        return self.driver.wait_for_object("bottom_rootbar")

    def verify_bottom_navigation_bar_icons(self, signed_in=True):
        self.verify_rootbar_home_icon()
        self.verify_rootbar_app_settings()
        if signed_in:
            self.verify_rootbar_documents_icon()
            self.verify_rootbar_scan_icon()
            self.verify_rootbar_account_icon()
        else:
            self.verify_rootbar_create_account_icon()
            self.verify_rootbar_sign_in()

    def verify_back_arrow_btn(self):
        return self.driver.wait_for_object("_shared_back_arrow_btn")

    def verify_cancel(self, invisible=False):
        return self.driver.wait_for_object("_shared_cancel", invisible=invisible)

    def verify_allow_while_using_app(self, raise_e=True):
        return self.driver.wait_for_object("_shared_allow_while_using_app", timeout=10, raise_e=raise_e)

    def verify_allow_once(self, raise_e=True):
        return self.driver.wait_for_object("_shared_allow_once", raise_e=raise_e)

    def verify_dont_allow(self, raise_e=True):
        return self.driver.wait_for_object("_shared_dont_allow", timeout=3, raise_e=raise_e)

    def verify_ok(self, raise_e=True):
        return self.driver.wait_for_object("_shared_str_ok", timeout=3, raise_e=raise_e)

    def verify_close(self, raise_e=True):
        return self.driver.wait_for_object("_shared_close", raise_e=raise_e)

    def handle_location_popup(self, selection="allow"):
        buttons = {
            "allow": self.verify_allow_while_using_app,
            "once": self.verify_allow_once,
            "dont_allow": self.verify_dont_allow
        }
        if self.driver.driver_info['platformVersion'].split(".")[0] != '12':
            buttons[selection]().click()

    def verify_bluetooth_popup(self, raise_e=True):
        if self.driver.driver_info['platformVersion'].split(".")[0] != '12':
            return self.driver.wait_for_object("bluetooth_alert", timeout=5, raise_e=raise_e)

    def verify_bluetooth_popup_ui(self, raise_e=True):
        return [
            self.driver.wait_for_object("bluetooth_alert", raise_e=raise_e),
            self.driver.wait_for_object("bluetooth_alert_text", raise_e=raise_e),
            self.verify_ok(raise_e=raise_e),
            self.verify_dont_allow(raise_e=raise_e)
        ]

    def handle_bluetooth_popup(self, allow=True):
        if allow:
            self.verify_ok().click()
        else:
            self.verify_dont_allow().click()

    def verify_no_internet_popup(self):
        self.driver.wait_for_object("_shared_str_check_internet")
        self.driver.wait_for_object("_shared_str_no_internet")

    def handle_no_internet_popup(self, try_again=True):
        if try_again:
            self.driver.click("_shared_try_again")
        else:
            self.driver.click("_shared_cancel")

    def get_options_listed(self, option, format_specifier=[]):
        options = []
        options_list = self.driver.find_object(option, format_specifier=format_specifier, multiple=True)
        if len(options_list) < 1:
            raise NoSuchElementException(option + "not displayed")
        for i in range(len(options_list)):
            option_name = options_list[i].get_attribute("name")
            options.append(option_name)
        logging.debug(options)
        return options

    def verify_an_element_and_click(self, element, format_specifier=[], click=True, raise_e=False):
        element_displayed = self.driver.wait_for_object(element, format_specifier=format_specifier, raise_e=raise_e)
        if element_displayed and click:
            element_displayed.click()
        return element_displayed

    def verify_static_text(self, text_option, raise_e=False):
        return self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[text_option], raise_e=raise_e)

    def select_static_text(self, text):
        self.driver.click("_shared_visible_dynamic_text", format_specifier=[text])

    def verify_array_of_elements(self, array_elements, direction="down", scroll_object=None):
        element_missing = []
        for element in array_elements:
            if not self.driver.wait_for_object(element, raise_e=False):
                if not self.driver.scroll(element, direction=direction, scroll_object=scroll_object, raise_e=False):
                    element_missing.append(element)
        if len(element_missing) > 0:
            raise NoSuchElementException("Following options {}:not displayed".format(element_missing))

    def select_navigate_back(self, index=0):
        self.driver.click("_shared_back_arrow_btn", index=index)

    def select_next(self):
        self.driver.click("next_btn")

    def select_cancel(self):
        self.driver.click("_shared_cancel")

    def select_close(self):
        self.driver.wait_for_object("_shared_close").click()

    def select_done(self):
        self.driver.wait_for_object("_shared_done").click()

    def select_ok(self):
        self.driver.wait_for_object("_shared_str_ok").click()

    def select_continue(self, timeout=10):
        self.driver.click("_shared_continue_btn", timeout=timeout)

    def verify_continue_popup(self, raise_e=False):
        return self.driver.wait_for_object("_shared_continue_btn", raise_e=raise_e)

    def select_yes(self):
        self.driver.wait_for_object("_shared_yes").click()

    def select_no_option(self):
        self.driver.click("_shared_no")

    def verify_no_search_results(self):
        self.driver.wait_for_object("_shared_no_search_results", displayed=False)

    def allow_notifications_popup(self, timeout=5, allow=True, raise_e=True):
        """
        Check if the current screen contains the notification popup
        :return:
        """
        if self.driver.wait_for_object("notifications_alert", timeout=timeout, raise_e=raise_e) is not False:
            self.driver.performance.stop_timer("hpid_login")
            if allow:
                self.driver.click("allow_btn")
            else:
                self.driver.click("do_not_allow_access_btn")

    def verify_adjust_scan_coach_mark(self, raise_e=False):
        return self.driver.wait_for_object("adjust_scan_coach_mark", timeout=5, raise_e=raise_e)

    def select_second_close_btn(self):
        self.driver.click("_shared_close", index=1)

    def verify_second_close_btn(self, raise_e=False):
        return self.driver.wait_for_object("_shared_close", index=1, timeout=5, raise_e=raise_e)

    def verify_sign_in_btn(self, raise_e=True):
        return self.driver.wait_for_object("_shared_sign_in", raise_e=raise_e) is not False

    def verify_create_account_btn(self, raise_e=True):
        return self.driver.wait_for_object("_shared_create_account", raise_e=raise_e) is not False

    def select_sign_in_btn(self):
        self.driver.click("_shared_sign_in")

    def select_create_account_btn(self):
        self.driver.click("_shared_create_account")
    
    def select_on_my_iphone(self):
        self.driver.click("on_my_iphone")
    
    def rename_file(self, obj, file_name):
        self.driver.click("_shared_clear_text_btn")
        self.driver.send_keys(obj, file_name)
