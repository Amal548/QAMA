from abc import  ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class GoogleDriveFlow(AndroidFlow):
    __metaclass__ =  ABCMeta
    project = "google_drive"

    def __init__(self,driver):
        super(GoogleDriveFlow,self).__init__(driver)
