from MobileApps.libs.flows.web.web_flow import WebFlow


class PrivacyCentral(WebFlow):
    project = "privacy_statement"
    flow_name = "privacy_central"
    url = "https://www8.hp.com/us/en/privacy/privacy-central.html"

    def verify_url(self):
        """
        Verifying url matches
        """
        return self.driver.wdvr.current_url == self.url

    def verify_our_approach_to_privacy(self, timeout=30):
        """
        Verifying main header text "OUR APPROACH TO PRIVACY"
        """
        self.driver.wait_for_object("our_approach_to_privacy", timeout=timeout, displayed=False)
