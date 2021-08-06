from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow


class WPrintDebugEnablerFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "wprint_debug_enabler"

    def __init__(self, driver):
        super(WPrintDebugEnablerFlow, self).__init__(driver)
