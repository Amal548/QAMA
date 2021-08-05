from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.web.web_flow import WebFlow
import logging

class Plans(WebFlow):
    project = "instant_ink"
    flow_name="plans"

    
    def __init__(self,driver):
        super(Plans, self).__init__(driver)


    def verify_plans_page(self):
        self.driver.wait_for_object("plans_page_title")


    def select_plan_mobile(self, plan="100"):
        #resolve swiping issue with the swiping
        self.driver.wdvr.switch_to.context(self.driver.wdvr.contexts[-1])
        self.verify_plans_page()
        sleep(5)
        self.driver.click("plan_select_btn", format_specifier=[plan])