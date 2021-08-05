from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow
from MobileApps.libs.ma_misc import ma_misc

class HPConnectBasicAccount(HPConnectFlow):
    flow_name="hp_connect_basic_account"
    root_url = {"pie": "https://www.hpsmartpie.com/us/en",
                "stage": "https://www.hpsmartstage.com/us/en"}
    

    def __init__(self, driver, context=None):
        super(HPConnectBasicAccount, self).__init__(driver, context=context)

    ###############################################################################
    #                             Basic account flows
    ###############################################################################

    def verify_new_printer_page(self, timeout=30):
        self.driver.wait_for_object("claim_code_direction", timeout=timeout)

    def  basic_sign_out(self, raise_e=False):
        if self.driver.wait_for_object("settings_btn", interval=1, timeout=15, raise_e=raise_e):
            self.driver.click("settings_btn")
            self.driver.click("sign_out_btn")
            self.driver.performance.start_timer("hpid_logout")
            return True
        else:
            return False

    def delete_printer(self, printer_obj, stack, raise_e=True):
        try:
            if self.driver.wait_for_object("personalize_email_address_close_btn", timeout=90, raise_e=False):
                self.driver.click("personalize_email_address_close_btn", change_check={"wait_obj": "personalize_email_address_close_btn", "invisible": True})
            self.driver.wait_for_object("remove_printer_link")
            self.driver.click("remove_printer_link")
            self.driver.wait_for_object("remove_printer_modal_remove_btn", timeout=10)
            self.driver.click("remove_printer_modal_remove_btn")
            self.driver.wait_for_object("claim_code_txt_box", timeout=120)
            system_cfg = ma_misc.load_system_config_file()
            if system_cfg["printer_power_config"]["type"] != "manual":
                printer_obj.db_object.update_HPC_is_associated(printer_obj.serial, stack, associated=False)
            return True
        except (TimeoutException, NoSuchElementException) as ex:
            if raise_e:
                raise ex
            else:
                return False