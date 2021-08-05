from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class PhotosFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "photos"

    def __init__(self, driver):
        super(PhotosFlow, self).__init__(driver)
