from selenium.common.exceptions import *
from MobileApps.resources.const.ios.const import *

import logging
import time
from MobileApps.libs.flows.web.instant_ink.plans import Plans
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.instant_ink.shipping import Shipping
from MobileApps.libs.flows.web.instant_ink.billing import Billing
from MobileApps.libs.flows.web.instant_ink.submit_order import SubmitOrder
from MobileApps.libs.flows.web.instant_ink.connect_web_services import ConnectWebServices




class MobileFlowContainer(object):
    def __init__(self, driver):
        self.driver = driver

        self.fd = {"plans": Plans(driver=driver),
                   "hp_id_hybrid": HPID(driver=driver),
                   "shipping": Shipping(driver=driver),
                   "billing": Billing(driver=driver),
                   "submit_order": SubmitOrder(driver=driver),
                   "connect_web_services": ConnectWebServices(driver=driver)
                   }

    @property
    def flow(self):
        return self.fd

    def instant_ink_flow(self, p_object, stack, plan="100", firstname="test", lastname="test", email=None, password="123456aA"):

        self.fd["plans"].select_plan_mobile(plan=plan)
        self.driver.wdvr.switch_to.context(self.driver.wdvr.contexts[0])
        self.fd["hp_id_hybrid"].create_account(p_object, stack, firstname=firstname, lastname=lastname, email=email, password=password)
        self.fd["shipping"].enter_shipping_info()
        self.fd["billing"].enter_billing_info()
        self.fd["submit_order"].submit_order()
        self.fd["connect_web_services"].finish_connection(p_object, stack)