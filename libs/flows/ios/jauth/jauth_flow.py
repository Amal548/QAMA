from abc import ABCMeta
from MobileApps.libs.flows.ios.ios_flow import IOSFlow

class JauthFlow(IOSFlow):
    __metaclass__ = ABCMeta
    project = "jauth"