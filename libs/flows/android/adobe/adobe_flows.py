from abc import  ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class AdobeFlow(AndroidFlow):
    __metaclass__ =  ABCMeta
    project = "adobe"

    def __init__(self,driver):
        super(AdobeFlow,self).__init__(driver)
