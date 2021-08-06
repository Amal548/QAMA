from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow

class PrinterSeries(InstantinkFlow):
    flow_name="printer_series"
    
    def select_printer(self,printer_model):
        
        model_name_list = printer_model.split(" ")
        model_name_length = len(model_name_list)-2
        model_name = "_".join(model_name_list[1:model_name_length]).lower()
        self.driver.click("printer_model_family_link", format_specifier=[model_name])
        self.driver.click("printer_model_name_btn", format_specifier=[printer_model])
        return True

    def continue_button(self):
        self.driver.click("continue_btn",timeout=10)
 
    def select_plan(self,plan = "2.99"):
        self.driver.click(plan + "_plan_select_btn")