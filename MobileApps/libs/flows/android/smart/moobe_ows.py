from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from selenium.common.exceptions import TimeoutException


class MoobeOWS(SmartFlow):
    """
    This flow is worked for Verona printer. I will update flow when I add another printer to this flow.
    """
    flow_name = "moobe_ows"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def skip_moobe_ows(self):
        """
        Skip MOOBE OWS by:
            - Click on 3 dots menu
            - Click on Skip
        """
        self.driver.wait_for_object("more_options", timeout=10).click()
        self.driver.click("skip_btn")
        self.driver.wait_for_object("are_you_sure_dialog_title", timeout=10)
        self.driver.click("are_you_sure_dialog_yes_btn")

    def select_continue(self):
        """
        Click on Continue button
        Note: Use for some screens
        """
        self.driver.click("continue_btn")

    def skip_country_language_screen(self):
        """
        Skip country and language screen
        """
        if self.driver.wait_for_object("set_country_language_txt", timeout=30, raise_e=False):
            self.select_continue()

    def skip_enjoy_hp_account_benefit_screen(self):
        """
        If this screen displays, skip it by clicking on Continue button
        """
        if self.driver.wait_for_object("enjoy_hp_acc_benefit_title", timeout=30, raise_e=False):
            self.select_continue()

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
        if self.driver.wait_for_object("let_try_something_title", timeout=30, raise_e=False):
            self.driver.click("retry_btn")

    def skip_issue_not_identified_screen(self):
        """
        Skip "Issue not identified" screen
        """
        if self.driver.wait_for_object("issue_not_identified_title", timeout=30, raise_e=False):
            self.driver.click("ok_btn")

    def skip_replace_cartridges_screen(self):
        """
        Skip 'Replace cartridges' screen by clicking on OK button
        """
        if self.driver.wait_for_object("replace_cartridges_title", timeout=30, raise_e=False):
            self.driver.click("ok_btn")

    def skip_register_instant_ink_screen(self):
        """
        Skip Register Instant Ink screen
        """
        if self.driver.wait_for_object("register_instant_ink_view", timeout=30, raise_e=False):
            self.driver.scroll("do_not_enable_ink_savings_btn", direction="right", timeout=30, check_end=False, click_obj=True)

    def skip_hp_instant_ink_screen(self):
        """
        Skip HP Instant Ink screen which is old view for gen1 printer, malbec
        """
        if self.driver.wait_for_object("hp_instant_ink_view", timeout=60, raise_e=False):
            self.driver.click("get_ink_regular_price_cb")
            self.driver.click("hp_instant_ink_continue_btn")
            if self.driver.wait_for_object("remind_me_btn", timeout=30, raise_e=False):
                self.driver.click("remind_me_btn", change_check={"wait_obj": "remind_me_btn", "invisible": True})


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_checking_printer_status_screen(self, invisible=False):
        """
        #
        Verify visible/invisible "Checking Printer Status..." via:
            - its text
            - spinner
        """
        self.driver.wait_for_object("checking_printer_status_txt", invisible=invisible, timeout=60)
        self.driver.wait_for_object("ows_wait_spinner", invisible=invisible, timeout=10)

    def verify_setup_cartridges_screen(self, invisible=False, raise_e=True):
        """
        Verify current screen is Setup cartridges screen
        """
        return self.driver.wait_for_object("setup_cartridges_view", invisible=invisible, timeout=30, raise_e=raise_e)

    def verify_load_plain_paper_screen(self, raise_e=True):
        """
        Verify current screen is for 'Let's load paper!' screen via:
            - title
            - instructions
        """
        # Using help icon button to detect the loaded page -> reduce time of waiting for 2 cases.
        try:
            self.driver.wait_for_object("help_button", timeout=30)
            if not self.driver.wait_for_object("load_paper_title", timeout=10, raise_e=False):
                self.driver.wait_for_object("load_paper_photos_title", timeout=10)
            return True
        except TimeoutException:
            if raise_e:
                raise TimeoutException("Current screen is not load paper screen (both main and photo trays)")
            else:
                return False

    def verify_print_alignment_screen(self, raise_e=True):
        """
        Verify current screen is 'Print alignment [age' screen via
            - title
        """
        return self.driver.wait_for_object("print_alignment_page_title", timeout=30, raise_e=raise_e)

    def verify_begin_calibration_screen(self, raise_e= True):
        """
        Verify current screen is 'Begin calibration"
        :param raise_e:
        """
        return self.driver.wait_for_object("begin_calibration_title", timeout=30, raise_e=raise_e)

    def verify_scan_printed_page_screen(self, raise_e=True):
        """
            Verify current screen is 'Next, scan printed page' screen via
                - title
                - instruction
        """
        return self.driver.wait_for_object("scan_printed_page_title", timeout=90, raise_e=raise_e)

    def verify_alignment_finished_screen(self, raise_e=True):
        """
        Verify current screen is Alignment Finished screen
        """
        return self.driver.wait_for_object("alignment_finished_title", timeout=60, raise_e=raise_e)

    def verify_hp_instant_ink_screen(self, raise_e=True):
        """
        Verify current screen HP Instant Ink which is old view for gen1 printer, malbec
        """
        if self.driver.wait_for_object("hp_instant_ink_view", timeout=60, raise_e=False):
            return self.driver.wait_for_object("get_ink_regular_price_cb", timeout=10, raise_e=True) is not False and\
                   self.driver.wait_for_object("hp_instant_ink_continue_btn", timeout=10, raise_e=True) is not False
        return False