from MobileApps.libs.flows.web.ecp.home import Home
from MobileApps.libs.flows.web.ecp.login import Login
from MobileApps.libs.flows.web.ecp.users import Users
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ecp.devices import Devices
from MobileApps.libs.flows.web.ecp.account import Account
from MobileApps.libs.flows.web.ecp.endpoint_security import EndpointSecurity

class FlowContainer(object):
    stack_url = {
        "dev": "https://ecp.dev.portalshell.com/",
        "pie": "https://ecp.pie.portalshell.com/",
        "stage": "https://ecp.stage.portalshell.com/"
        }

    def __init__(self, driver):
        self.driver = driver
        self.fd = {"login": Login(driver),
                   "hpid": HPID(driver),
                   "home": Home(driver),
                   "users": Users(driver), 
                   "devices": Devices(driver),
                   "account": Account(driver),
                   "endpoint_security": EndpointSecurity(driver)}
    @property
    def flow(self):
        return self.fd

    def navigate(self, stack):
        return self.driver.navigate(self.stack_url[stack])

    def login(self, email, pwd):
        self.fd["login"].enter_email_login(email)
        self.fd["hpid"].verify_hp_id_sign_in()
        return self.fd["hpid"].login(email, pwd)

    def go_home(self, stack, email, pwd):
        self.navigate(stack)
        if self.fd["home"].verify_home_menu_btn(timeout=5, raise_e=False) is not False:
            pass
        else:
            self.login(email, pwd)
        self.fd["home"].verify_home_menu_btn()