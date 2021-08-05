import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class EndpointSecurity(ECPFlow):
    flow_name = "endpoint_security"

    def return_section_div(self, section):
        return self.driver.wait_for_object(section + "_section")