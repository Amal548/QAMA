from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class MicrosoftExcelFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "microsoft_excel"

    def __init__(self, driver):
        super(MicrosoftExcelFlow, self).__init__(driver)

