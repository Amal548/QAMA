from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.system_flows.base_system import BaseSystem

import logging

class NexusSystem(BaseSystem):
    manufacture = ["nexus"]