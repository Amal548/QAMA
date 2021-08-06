import logging
from time import sleep
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path

class OptionsNotUnselected(Exception):
    pass

class Osprey(OWSFlow):
    """
        Contains all of the elements and flows associated in the "Confirmation and Big
            Data - Help HP Make Better Products" page for ows
    """
    flow_name = "osprey"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

#########################################################################################
#                                                                                       #
#                                     Action Flows                                      #
#                                                                                       #
#########################################################################################

    def select_continue_button(self):
        self.driver.click("continue_button")

    def select_in_a_home_radio_button(self):
        self.driver.click("in_a_home_label")

    def select_in_a_business_radio_button(self):
        self.driver.click("in_a_business_label")

    def select_dropdown_toggle(self, dropdown_type):
        if dropdown_type == "home":
            self.driver.click("in_a_home_dropdown_toggle")
        elif dropdown_type == "business":
            self.driver.click("in_a_business_dropdown_toggle")

    def return_dropdown_list(self, dropdown_type):
        if dropdown_type == "home":
            return self.driver.find_object("list_of_home_dropdown_options", multiple=True)
        elif dropdown_type == "business":
            return self.driver.find_object("list_of_business_dropdown_options", multiple=True)

    def enter_code_into_postal_code_text_field(self, code, clear_text=False):
        self.driver.wait_for_object("postal_code_text_field")
        self.driver.send_keys("postal_code_text_field", code, clear_text=clear_text)
        sleep(1)
    def get_value_from_postal_code_text_field(self):
        return self.driver.wait_for_object("postal_code_text_field").get_attribute("value")

    def check_any_option(self):
        self.select_in_a_home_radio_button()
        self.select_dropdown_toggle("home")
        self.driver.wait_for_object("list_of_home_dropdown_options").click()

#########################################################################################
#                                                                                       #
#                                  Verification Flows                                   #
#                                                                                       #
#########################################################################################

    def verify_radio_button_status(self, dropdown_type, checked=True):
        # Wait for the DOM to fully rendered
        # Using wait_for_object(invisible=True) instead of sleep + find_object() won't
        #   work in this case since we are looking for custom <input> radio field
        sleep(2)
        if dropdown_type == "home":
            return self.driver.find_object("in_a_home_radio_button", raise_e=False).is_selected() == checked
        elif dropdown_type == "business":
            return self.driver.find_object("in_a_business_radio_button", raise_e=False).is_selected() == checked

    def verify_both_home_and_business_option_are_not_selected(self):
        self.driver.check_box("in_a_home_radio_button", state=False)
        self.driver.check_box("in_a_business_radio_button", state=False)

    def verify_help_hp_make_better_products_page(self):
        self.driver.wait_for_object("help_hp_make_better_products_page")

    def check_continue_button_state(self, check_enabled=True):
        self.driver.wait_for_object("continue_button", clickable=check_enabled)

    def verify_home_dropdown_toggle_is_displayed(self):
        self.driver.wait_for_object("in_a_home_dropdown_toggle")

    def verify_business_dropdown_toggle_is_displayed(self):
       self.driver.wait_for_object("in_a_business_dropdown_toggle")

    def verify_each_option_in_dropdown_list_is_selectable(self, dropdown_type):
        self.select_dropdown_toggle(dropdown_type)
        dropdown_list = self.return_dropdown_list(dropdown_type)
        for item in dropdown_list:
            sleep(1)
            item.click()
            self.select_dropdown_toggle(dropdown_type)
        self.select_dropdown_toggle(dropdown_type)

    def verify_edit_button_is_not_displayed(self):
        self.driver.wait_for_object("edit_button", invisible=True)

    def verify_no_error_message_displayed(self):
        self.driver.wait_for_object("invalid_postal_code_message", invisible=True)

    def verify_option_unselected_in_the_section(self):
        """
            Make sure "home" or "business" section has not been selected, not the
                section that was selected and isn't anymore.
        """
        if self.verify_radio_button_status("home", checked=False) and self.verify_radio_button_status("business", checked=False):
            return True
        if self.verify_radio_button_status("home", checked=True) and self.driver.wait_for_object("please_specify_text_in_home_dropdown", timeout=3, raise_e=False):
            return True
        if self.verify_radio_button_status("business", checked=True) and self.driver.wait_for_object("please_specify_text_in_business_dropdown", timeout=3, raise_e=False):
            return True
        raise OptionsNotUnselected("Home or business section have options selected")

    def verify_dropdown_list_is_folded(self, dropdown_type):
        if dropdown_type == "home":
            self.driver.wait_for_object("home_dropdown_menu_list", invisible=True)
        elif dropdown_type == "business":
            self.driver.wait_for_object("business_dropdown_menu_list", invisible=True)
