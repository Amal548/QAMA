from time import sleep
from selenium.common.exceptions import *

from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class MoobeOws(SmartFlow):
    flow_name = "moobe_ows"

    def select_continue(self, timeout=10):
        """
        Click on Continue button
        End o flow: next screen (depends on current screens and selected option on this screen)
        """
        self.driver.wait_for_object("continue_btn", timeout=timeout).click()

    def select_sign_up_button(self):
        self.driver.wait_for_object("sign_up_btn").click()

    def handle_ios_popup(self, timeout=20, cancel=False):
        self.driver.wait_for_object("popup_alert", timeout=timeout)
        if cancel:
            self.driver.wait_for_object("_shared_cancel").click()
        else:
            self.select_continue()

    def skip_country_language_screen(self):
        """
        Skip country and language screen
        """
        pass

    def select_get_ink_at_regular_price(self):
        self.driver.click("get_ink_at_regular_price_title")

    #@MobiGA.counter(events=(EVENTS.CATEGORY_MOOBE, EVENTS.MOOBE__INSTALL_INK_PAPER, EVENTS.MOOBE__INSTALL_INK_PAPER__DO_NOT_ENABLE))
    
    def select_do_not_enable(self):
        """
        Click on Do not enable button on HP Printer Web Services screen
        End of flow: Reminder: screen
        """
        self.driver.click("do_not_enable_btn")

    def select_skip_popup_yes(self):
        """
        Click on Yes button of Skip popup
        End of flow: Invite screen
        """
        self.driver.click("skip_popup_yes_btn")

    def test_page_select_no_thanks(self):
        self.driver.click("print_test_page_no_thanks_btn")

    def select_remind_me_btn(self):
        self.driver.click("remind_me_btn")

    def select_skip_this_step(self):
        self.driver.click("skip_this_step_btn")

    def select_align_btn(self):
        self.driver.click("align_btn")

    def select_next_btn(self):
        self.driver.click("next_btn")

    def select_continue_with_setup(self):
        if self.verify_printer_not_connected_to_account():
            self.driver.click("continue_with_setup_btn")

    def ignore_activation_problem(self):
        sleep(3)
        if self.driver.find_object("activation_problem_screen", raise_e=False):
            self.select_continue()

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************

    def verify_set_country_region_screen(self):
        #work around due to unable to use wait_for_object as appium does not see
        #objects from "hybrid views" as visible
        self.driver.wait_by_find("set_country_region_title", timeout=20)

    def verify_load_plain_paper_screen(self, raise_e=True):
        """
               Verify current screen is for 'Let's load paper!' screen via:
                   - title
        """
        return self.driver.wait_for_object("lets_load_paper", raise_e=raise_e)

    def verify_print_alignment_screen(self, raise_e=True):
        """
        Verify current screen is 'Print alignment page' screen via
            - title
        """
        return self.driver.wait_for_object("print_alignment_page_title", timeout=30, raise_e=raise_e)

    def verify_scan_printed_page_screen(self, raise_e=True):
        """
            Verify current screen is 'Next, scan printed page' screen via
                - title
        """
        return self.driver.wait_for_object("scan_printed_page_title", timeout=90, raise_e=raise_e)

    def verify_alignment_finished_screen(self, raise_e=True):
        """
        Verify current screen is Alignment Finished screen
        """
        return self.driver.wait_for_object("alignment_finished_title", timeout=60, raise_e=raise_e)

    def verify_print_from_other_device_screen(self):
        self.driver.wait_for_object("print_from_other_device_title", timeout=5)

    def verify_do_you_want_to_print_test_page(self):
        self.driver.wait_for_object("do_you_want_to_print_test_page_title", timeout=5)

    def verify_remind_me_screen(self):
        self.driver.wait_for_object("remind_me_btn", timeout=5)

    #@MobiGA.counter(screens=SCREENS.MOOBE_START_OWS)
    
    def verify_checking_printer(self):
        """
        Verify that current screen is Checking printer... via:
            - title text
        """
        self.driver.wait_for_object("checking_printer_txt")

    
    def verify_are_you_sure_pop_up(self):
        self.driver.wait_for_object("not_right_now_skip_msg")

    def verify_hp_instant_ink_screen(self):
        """
        Verify current screen is HP Instant Ink via:
            - title
        """
        self.driver.wait_for_object("get_ink_at_regular_price_title", timeout=60)
    
    def verify_printer_web_services_screen(self):
        """
        Verify current screen is HP Printer Web Services: screen via:
            - title
        Note: Add 60 seconds to timeout because it is web view -> take time to load screen
        """
        self.driver.wait_by_find("printer_web_services_title", timeout=10)

    def verify_continue_button(self, timeout=60):
        self.driver.wait_for_object("continue_btn", timeout=timeout)
    
    def verify_create_hp_connected_acc_screen(self):
        """
        Verify current screen is HP connected account screen via:
            - title
        Note: Add 60 seconds to timeout because it is web view -> loading web page
        """
        self.driver.wait_for_object("hp_connected_create_acc_txt")

    def verify_skip_popup(self):
        """
        Verify current popup is Skip popup via:
            - title
            - yes button
        """
        self.driver.wait_for_object("skip_msg")
        self.driver.wait_for_object("skip_popup_yes_btn")

    def select_skip(self):
        """
        Click on SKip button of Create HP Connected account
        End of flow: Skip popup
        """
        self.driver.click("more_icon_btn")
        self.driver.click("skip_btn")

    def verify_cartridges_installed_and_paper_loaded_title(self):
        self.driver.wait_by_find("cartridges_installed_and_paper_loaded_title", timeout=40)

    def verify_printer_not_connected_to_account(self):
        self.driver.wait_by_find("continue_with_setup_btn", timeout=30)

    def verify_enjoy_hp_account_benefits(self):
        self.driver.wait_for_object("enjoy_hp_account_benefit_title", timeout=60)

    def verify_setup_cartridges_screen(self, invisible=False, raise_e=True):
        """
        Verify current screen is "Use SETUP cartridges" screen
        """
        return self.driver.wait_for_object("use_setup_cartridges", invisible=invisible, timeout=30, raise_e=raise_e)

    def skip_something_unexpected_happened_screen(self):
        """
        Skip 'Something unexpected happened' screen by clicking retry button
        :return:
        """
        if self.driver.wait_for_object("something_unexpected_title", timeout=30, raise_e=False):
            return self.driver.click("retry_btn")
        return False

    def skip_let_try_something_screen(self):
        """
        Skip "Let's try something else" if it display
        """
        raise NotImplementedError

    def skip_issue_not_identified_screen(self):
        """
        Skip "Issue not identified" screen
        """
        raise NotImplementedError

    def skip_replace_cartridges_screen(self):
        """
        Skip 'Replace cartridges' screen by clicking on OK button
        """
        if self.driver.wait_for_object("replace_cartridges_title", timeout=30, raise_e=False):
            self.driver.click("_shared_str_ok")

    def skip_register_instant_ink_screen(self):
        """
        Skip Register Instant Ink screen
        """
        if self.driver.wait_for_object("sign_up_hp_instant_ink_txt", timeout=30, raise_e=False):
            self.driver.scroll("do_not_enable_ink_savings_btn", direction="right", timeout=30, check_end=False, click_obj=True)
