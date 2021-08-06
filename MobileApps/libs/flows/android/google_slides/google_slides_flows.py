from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class GoogleSlidesFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "google_slides"

    def __init__(self,driver):
        super(GoogleSlidesFlow,self).__init__(driver)
