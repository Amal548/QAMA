from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow


class MoobeSetupComplete(SmartFlow):
    flow_name = "moobe_setup_complete"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_not_right_now(self):
        """
        Click on 'Not Right Not' button
        End of flow: Setup complete screen
        """
        self.driver.click("invite_print_not_right_now_btn")

    def select_send_link(self):
        """
        Click on Send Link on Print from other device screen
        """
        self.driver.click("invite_print_send_link_btn")

    def select_setup_complete_not_now(self):
        """
        Click on 'Not Now' button
        End of flow: Home screen
        """
        self.driver.click("setup_complete_not_now_btn")

    def select_gmail_icon(self):
        """
        Select Gmail on Send Via screen
        """
        self.driver.click("gmail")

    def select_done_btn(self):
        """
        Select Done button on Link Sent! screen
        """
        self.driver.click("done_btn")

    def select_send_another_link_btn(self):
        """
        Select Send Another Link button on Link Sent! screen
        """
        self.driver.click("sent_another_link_btn")

    def select_exit_setup_continue_btn(self):
        """
        Click on Continue button on Exit Setup screen
        """
        self.driver.click("exit_setup_continue_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_print_other_devices_screen(self, raise_e=True):
        """
        Verify current screen is "Print from other devices" screen via:
            - title
            - Send Link button
            - Not Right Now button
        """
        if self.driver.wait_for_object("print_other_devices_title", timeout=10, raise_e=raise_e):
            self.driver.wait_for_object("invite_print_send_link_btn", timeout=10)
            self.driver.wait_for_object("invite_print_not_right_now_btn", timeout=10)
            return True
        return False

    def verify_setup_complete_screen(self, raise_e=True):
        """
        Verify current screen is "Setup complete-Let'sprint!" screen via:
            - title
            - Finish button - depending on printer, text is different -> using element's id
            - Not Now button
        """
        if self.driver.wait_for_object("setup_complete_title", timeout=10, raise_e=raise_e):
            self.driver.wait_for_object("setup_complete_finish_btn", timeout=10)
            self.driver.wait_for_object("setup_complete_not_now_btn", timeout=10)
            return True
        return False

    def verify_send_via_popup(self):
        """
        Verify Send Via screen
        """
        self.driver.wait_for_object("send_via_title")

    def verify_link_sent_screen(self):
        """
        Verify Link Sent! screen
        """
        self.driver.wait_for_object("share_sent_title")
        self.driver.wait_for_object("sent_another_link_btn")
        self.driver.wait_for_object("done_btn")

    def verify_exit_setup_screen(self):
        """
        Verify current screen is Exit Setup screen via:
            - Exit Setup title
            - Continue button
        """
        self.driver.wait_for_object("exit_setup_title", timeout=10)
        self.driver.wait_for_object("exit_setup_continue_btn", timeout=10)