from MobileApps.libs.flows.web.jweb.home import Home
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.jweb.auth_plugin import AuthPlugin
from MobileApps.libs.flows.web.jweb.browser_plugin import BrowserPlugin
from MobileApps.libs.flows.web.jweb.security_gateway import SecurityGateway
from MobileApps.libs.flows.web.jweb.eventing_plugin import EventingPlugin
from MobileApps.libs.flows.web.jweb.security_gateway import SecurityGateway
from MobileApps.libs.flows.web.jweb.service_plugin import ServicePlugin
from MobileApps.libs.flows.web.jweb.device_plugin import DevicePlugin
from MobileApps.libs.flows.web.jweb.app_plugin import AppPlugin
from MobileApps.libs.flows.android.android_flow import android_system_ui_flow
from MobileApps.resources.const.android.const import *
from MobileApps.libs.flows.android.google_chrome.google_chrome import GoogleChrome
from time import sleep

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = { "system": android_system_ui_flow(driver),
                    "hpid": HPID(driver, context='WEBVIEW_chrome'),
                    "chrome": GoogleChrome(driver),
                    "home": Home(driver, context=WEBVIEW_CONTEXT.JWEB),
                    "browser_plugin": BrowserPlugin(driver, context=WEBVIEW_CONTEXT.JWEB),
                    "auth_plugin": AuthPlugin(driver, context=WEBVIEW_CONTEXT.JWEB),
                    "service_plugin": ServicePlugin(driver, context=WEBVIEW_CONTEXT.JWEB),
                    "event_plugin": EventingPlugin(driver, context=WEBVIEW_CONTEXT.JWEB),
                    "device_plugin": DevicePlugin(driver, context=WEBVIEW_CONTEXT.JWEB),
                    "app_plugin": AppPlugin(driver, context=WEBVIEW_CONTEXT.JWEB),
                    "security_gateway": SecurityGateway(driver, context={'url':'?redirect_to=jwebsample://auth-browser'})}

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
        self.driver.terminate_app(PACKAGE.JWEB)
        self.driver.start_activity(PACKAGE.JWEB, LAUNCH_ACTIVITY.JWEB)