from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.system_flows.base_system import BaseSystem
import logging

class SamsungSystem(BaseSystem):
    manufacture = "samsung"


class SamsungSystemNougate(SamsungSystem):
    version = ["7"]

    def select_app(self, app_name):
        try:
            self.driver.wait_for_object("_system_samsung_select_app_page_area", timeout=10)
            self.driver.click("_system_txt_place_holder", format_specifier=[app_name])
            return True
        except NoSuchElementException:
            logging.debug("Not on the default page")

        total_page = len(self.driver.find_object("_system_samsung_select_app_page_area_nav_dots", multiple=True))
        for index in range(total_page):
            try:
                self.driver.click("_system_txt_place_holder", format_specifier=[app_name])
                return True
            except NoSuchElementException:
                logging.debug("Did not find the app on page: " + str(index))
                self.driver.swipe(swipe_object="_system_samsung_select_app_page_area", direction="right")
        raise NoSuchElementException("Did not find the app with the name: " + app_name)


class SamsungSystemOreo(SamsungSystem):
    version = ["8", "9"]

