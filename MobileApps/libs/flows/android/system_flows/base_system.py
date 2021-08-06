from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
import time


class BaseSystem(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "system"
    flow_name = "system_ui"
    def __init__(self, driver):
        super(BaseSystem, self).__init__(driver)

    def google_photos_select_app(self, app_name):
        """
        click on target app on Share Using:
        :param app_name:
        :return:
        """
        try:
            self.driver.click("_system_txt_place_holder", format_specifier=[app_name])
            return True
        except NoSuchElementException:
            logging.debug("Not on the default page")
        if app_name == "Print":
            object_to_scroll = "_3_dot_menu_photos_scroll_view"
        elif app_name == "HP Print Service Plugin":
            if self.driver.wait_for_object("_3_dot_more", timeout=5, raise_e=False) is not False:
                self.driver.click("_3_dot_more")
            object_to_scroll = "_system_os8_9_third_part_app_scroll_view"
        self.driver.scroll("_system_txt_place_holder", format_specifier=[app_name],scroll_object=object_to_scroll, check_end=False, swipe_duration="2500", direction="right", click_obj=True)

    def select_app(self, app_name):
        time.sleep(3)
        try:
            self.driver.wait_for_object("_system_txt_place_holder", format_specifier=[app_name], timeout=10)
            self.driver.click("_system_txt_place_holder", format_specifier=[app_name])
            return True
        except (TimeoutException, NoSuchElementException):
            logging.debug("Did not find the app on 1st page")
            self.driver.scroll("_system_txt_place_holder", direction="down", format_specifier=[app_name], timeout=30,
                               click_obj=True, full_object=False)
        if not self.driver.wait_for_object("_system_txt_place_holder", format_specifier=[app_name],
                                           invisible=True, timeout=10, raise_e=False):
            self.driver.click("_system_txt_place_holder", format_specifier=[app_name], change_check={"wait_obj":"_system_txt_place_holder", "invisible": True, "format_specifier": [app_name]})
            return True
