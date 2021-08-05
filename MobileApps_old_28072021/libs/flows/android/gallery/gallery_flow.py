from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class GalleryFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "gallery"

    def __init__(self, driver):
        super(GalleryFlow, self).__init__(driver)
