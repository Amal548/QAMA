from abc import ABCMeta
from MobileApps.libs.flows.mac.mac_flow import MACFlow


class SystemScreens(MACFlow):
    __metaclass__ = ABCMeta
    project = "system"

    def __init__(self, driver):
        super(SystemScreens, self).__init__(driver)
