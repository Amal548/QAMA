from MobileApps.libs.flows.ios.jauth.home import Home
from MobileApps.libs.flows.ios.jauth.settings import Settings
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.ios.jauth.account_info import AccountInfo
from MobileApps.resources.const.ios.const import *
from ios_settings.src.libs.ios_system_flow_factory import ios_system_flow_factory

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "settings":Settings(driver),
                   "hpid":HPID(driver, context=-1),
                   "account_info":AccountInfo(driver),
                   "ios_system": ios_system_flow_factory(driver)}

    @property
    def flow(self):
        return self.fd

    def go_to_home_screen(self):
        if not self.fd["home"].verify_home_settings():
            self.driver.restart_app(BUNDLE_ID.JAUTH)
            self.fd["home"].verify_home_settings(raise_e=True)

    def accept_self_signed_certificates(self):
        self.go_to_home_screen()
        self.fd["home"].select_settings()
        self.fd["settings"].select_app_settings()
        self.fd["settings"].toggle_self_signed_certificates(disable=True)
        self.fd["settings"].toggle_self_signed_certificates(disable=False)
        self.driver.back()

    def reinstall_app(self):
        self.driver.uninstall_app(BUNDLE_ID.JAUTH)
        self.driver.install_app()