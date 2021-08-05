from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.system_flows.base_system import BaseSystem
import logging

class PixelSystem(BaseSystem):
    manufacture = "google"


class PixelSystemOreo(PixelSystem):
    version = ["8", "9"]
