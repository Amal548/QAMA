from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class GoogleSheetsFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "google_sheets"

    def __init__(self, driver):
        super(GoogleSheetsFlow, self).__init__(driver)
