from abc import ABCMeta
from MobileApps.libs.flows.web.web_flow import WebFlow


class HPConnectFlow(WebFlow):
    __metaclass__ = ABCMeta
    project = "hp_connect"