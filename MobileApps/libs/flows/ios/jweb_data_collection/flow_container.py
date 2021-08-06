from MobileApps.libs.flows.ios.jweb_data_collection.home import Home
from MobileApps.libs.flows.ios.jweb_data_collection.data_collection import DataCollection
from MobileApps.libs.flows.ios.jweb_data_collection.data_collection_settings import DataCollectionSettings
from MobileApps.libs.flows.ios.jweb_data_collection.retargeting_data import RetargetingData
from MobileApps.libs.flows.ios.jweb_data_collection.controlled_data import ControlledData
from MobileApps.libs.flows.web.jweb.data_collection_plugin import DataCollectionPlugin
from MobileApps.resources.const.ios.const import *
from MobileApps.resources.const.web.const import *
from time import sleep

class FlowContainer(object):
    def __init__(self, driver, load_app_strings=False):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "data_collection": DataCollection(driver),
                   "data_collection_settings": DataCollectionSettings(driver),
                   "retargeting_data": RetargetingData(driver),
                   "controlled_data": ControlledData(driver),
                   "data_collection_plugin": DataCollectionPlugin(driver, context={"url": WEBVIEW_URL.JWEB_URL})}
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
        pkg_name = BUNDLE_ID.JWEB_DATA_COLLECTION
        self.driver.restart_app(pkg_name)
        sleep(5)

    def close_app(self):
        """
        closes App
        """
        self.driver.terminate_app(BUNDLE_ID.JWEB_DATA_COLLECTION)

    def restart_app(self):
        """
        restarts app
        """
        self.driver.restart_app(BUNDLE_ID.JWEB_DATA_COLLECTION)