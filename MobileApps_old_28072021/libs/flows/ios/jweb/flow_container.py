from MobileApps.libs.flows.web.jweb.home import Home
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.jweb.auth_plugin import AuthPlugin
from MobileApps.libs.flows.web.jweb.browser_plugin import BrowserPlugin
from MobileApps.libs.flows.web.jweb.eventing_plugin import EventingPlugin
from MobileApps.libs.flows.web.jweb.security_gateway import SecurityGateway
from MobileApps.libs.flows.web.jweb.device_plugin import DevicePlugin
from MobileApps.libs.flows.ios.jauth.home import Home as System
from MobileApps.resources.const.ios.const import *
from MobileApps.resources.const.web.const import *
from time import sleep

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"auth":System(driver),
                   "home": Home(driver, context={'url':WEBVIEW_URL.JWEB}),
                   "hpid": HPID(driver, context={'url':WEBVIEW_URL.HPID}),
                   "auth_plugin": AuthPlugin(driver, context={'url':WEBVIEW_URL.JWEB}),
                   "browser_plugin": BrowserPlugin(driver, context={'url':WEBVIEW_URL.JWEB}),
                   "event_plugin": EventingPlugin(driver, context={'url':WEBVIEW_URL.JWEB}),
                   "device_plugin": DevicePlugin(driver, context={'url':WEBVIEW_URL.JWEB}),
                   "security_gateway": SecurityGateway(driver, context={'url':WEBVIEW_URL.JWEB_SECURITY})}
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
        pkg_name = BUNDLE_ID.JWEB
        self.driver.restart_app(pkg_name)
        sleep(5)

    def close_app(self):
        """
        closes App
        """
        self.driver.terminate_app(BUNDLE_ID.JWEB)