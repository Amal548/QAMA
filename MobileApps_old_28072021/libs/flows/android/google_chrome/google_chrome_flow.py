from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow
from MobileApps.resources.const.android import const

class GoogleChromeFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "google_chrome"

    def __init__(self, driver, load_app_strings=False):
        super(GoogleChromeFlow, self).__init__(driver)
        if load_app_strings:
            self.driver.load_app_strings(self.project, self.driver.pull_package_from_device(const.PACKAGE.GOOGLE_CHROME),
                                         self.driver.session_data["language"], append=True, add_array=True)