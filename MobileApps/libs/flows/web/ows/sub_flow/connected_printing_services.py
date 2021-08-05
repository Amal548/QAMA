from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path



class ConnectedPrintingServices(OWSFlow):
    flow_name = "connected_printing_services"
    flow_url = "hpsmart_printer-data"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)
    
    
    def verify_connected_printing_services(self):
        self.driver.wait_for_object("connected_printing_services_continue_btn")

    def click_connected_printing_services(self):
        return self.driver.click("connected_printing_services_continue_btn", timeout=10, change_check={"wait_obj":"connected_printing_services_continue_btn","invisible": True})