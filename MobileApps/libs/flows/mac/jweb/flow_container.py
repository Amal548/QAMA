import logging
from MobileApps.libs.flows.mac.jweb.home import Home
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.mac.jweb.auth_plugin import AuthPlugin
from MobileApps.libs.flows.mac.jweb.eventing_plugin import EventingPlugin
from MobileApps.resources.const.mac.const import *


class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "hpid": HPID(driver),
                   "auth_plugin": AuthPlugin(driver),
                   "eventing_plugin": EventingPlugin(driver)}

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
        app_name = APP_NAME.JWEB
        if not self.fd['home'].verify_menu_button():
            self.driver.navigate(app_name)

    def close_jweb_app(self):
        '''
        This is a method to close jarvis reference app.
        :parameter:
        :return:
        '''
        logging.debug("Closing Jarvis App...")
        if self.fd["home"].verify_close_button():
            self.fd["home"].click_close_btn()