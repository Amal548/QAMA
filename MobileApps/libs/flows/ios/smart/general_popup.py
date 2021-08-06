from selenium.common.exceptions import TimeoutException
import logging

from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class GenerealPopup(SmartFlow):
    flow_name = "general_popup"

    def dismiss_access_your_photos_popup(self):
        """
        Dismiss popup "... Access Your Photos" popup
        """
        try:
            self.driver.wait_for_object("access_photos_popup_title")
            self.driver.click("popup_ok_btn")
        except TimeoutException:
            logging.info("'... Access Your Photos' popup is NOT displayed")
