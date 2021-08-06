from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class WPrintTestFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "wprint_test"

    def __init__(self, driver):
        super(WPrintTestFlow, self).__init__(driver)
