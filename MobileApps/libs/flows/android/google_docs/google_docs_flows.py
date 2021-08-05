from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class GoogleDocsFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "google_docs"

    def __init__(self, driver):
        super(GoogleDocsFlow, self).__init__(driver)
