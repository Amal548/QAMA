from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import logging

class About(SmartFlow):
    flow_name="about"
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_share_btn(self):
        """
        Click on Share this app on About screen
        """
        if not self.driver.click("share_btn", change_check={"wait_obj": "share_btn", "invisible": True}, raise_e=False):
            logging.info("Try to click again one more time when it failed at first time of clicking.")
            self.driver.wait_for_object("share_btn", timeout=20)
            self.driver.click("share_btn")

    def select_legal_info(self):
        """
        Click on Legal Information link
        """
        self.driver.click("legal_info_link")

    def select_ok_btn(self):
        """
        Click on OK button on Legal Information link
        """
        self.driver.click("ok_btn")

    def select_license_agreement(self):
        """
        Click on Legal Information link
        """
        self.driver.click("license_agreement_link")

    def select_hp_privacy(self):
        """
        Click on HP Online Privacy link
        """
        self.driver.click("hp_privacy_link")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_about_screen(self, invisible=False):
        """
        Verify About screen with below points:
           + Title
           + 3 links
           + Share this app button
        """
        self.driver.wait_for_object("about_title", invisible=invisible)
        self.driver.wait_for_object("hp_privacy", invisible=invisible)
        self.driver.wait_for_object("license_agreement_link", invisible=invisible)
        self.driver.wait_for_object("legal_info", invisible=invisible)
        self.driver.wait_for_object("share_btn", invisible=invisible)

    def verify_share_with_screen(self, raise_e=True):
        """
        Verify Share with screen with:
          - title
          - Gmail
        """
        return bool(self.driver.wait_for_object("share_with_title", format_specifier=[self.get_text_from_str_id("share_with_title")], raise_e=raise_e)) \
               and bool(self.driver.wait_for_object("share_gmail_btn", raise_e=raise_e))

