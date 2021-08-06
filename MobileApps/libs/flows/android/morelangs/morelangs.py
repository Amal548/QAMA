from MobileApps.libs.flows.android.android_flow import AndroidFlow
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

"""
Prerequisite:
    - App must have installed MoreLangs (manually)
    - Execute "adb shell pm grant sightidea.com.setlocale android.permission.CHANGE_CONFIGURATION" after initial install
    - Optional: In MoreLangs app Settings, set Fixed Display Language to "en"
[UI-MAP]
    mlang-android: MobileApps/resources/ui_map/android/morelangs/morelangs.json
"""
class MoreLangs(AndroidFlow):
    project = "morelangs"
    flow_name = "morelangs"

    def __init__(self, driver):
        super(MoreLangs, self).__init__(driver)

    # -------------------           USING MoreLangs APP     ------------------------------------
    def change_lang(self, language):
        """
        Change the mobile device's language
            - Launch MoreLangs app
            - Click on Search button
            - Search locale code
            - Scroll down (max 3 times) to find the target locale within search results
        :param language: target locale code to switch to. Example: en, en-rUS
        """
        lang = language.replace("-r", "_")
        self.driver.wdvr.start_activity(PACKAGE.MORELANGS, LAUNCH_ACTIVITY.MORELANGS)
        self.dismiss_rate_popup()
        self.driver.click("search_btn")
        self.driver.send_keys("search_tf", lang)

        self.driver.scroll("locale_code_txt", format_specifier=[lang], timeout=10, full_object=False, click_obj=True)

        logging.info("Successfully switched to locale: {}\n".format(lang))

        self.dismiss_rate_popup()

    def dismiss_rate_popup(self):
        """
        Dismiss rate popup if it displays
        :return:
        """
        try:
            self.driver.wait_for_object("later_btn", timeout=10)
            self.driver.click("later_btn")
        except (NoSuchElementException, TimeoutException):
            logging.info("This popup is not displayed.")
