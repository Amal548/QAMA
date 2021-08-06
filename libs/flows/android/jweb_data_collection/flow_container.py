from MobileApps.libs.flows.android.jweb_data_collection.home import Home
from MobileApps.libs.flows.android.jweb_data_collection.data_collection import DataCollection
from MobileApps.libs.flows.android.jweb_data_collection.data_collection_settings import DataCollectionSettings
from MobileApps.libs.flows.android.jweb_data_collection.retargeting_data import RetargetingData
from MobileApps.libs.flows.android.jweb_data_collection.controlled_data import ControlledData
from MobileApps.resources.const.android.const import *
from time import sleep

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "data_collection": DataCollection(driver),
                   "data_collection_settings": DataCollectionSettings(driver),
                   "retargeting_data": RetargetingData(driver),
                   "controlled_data": ControlledData(driver)}

    @property
    def flow(self):
        return self.fd

# *********************************************************************************
#                                ACTION FLOWS                                     *
# *********************************************************************************

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        self.driver.press_key_home()
        self.driver.wdvr.start_activity(PACKAGE.JWEB_DATA_COLLECTION, LAUNCH_ACTIVITY.JWEB_DATA_COLLECTION)
        sleep(5)