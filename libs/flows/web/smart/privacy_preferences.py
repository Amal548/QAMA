from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
class PrivacyPreferences(SmartFlow):
    flow_name = "privacy_preferences"

    TERM_USE_LINK = "terms_of_use_link"
    EULA_LINK = "eula_link"
    HP_PRIVACY_STATEMENT = "hp_privacy_statement_link"
    APP_ANALYTICS = "app_analytics_toggle"
    ADVERTISING = "advertising_toggle"
    PERSONALIZED_SUGGESTIONS = "personalized_suggestions_toggle"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def click_continue(self,timeout=3):
        """
        Click on "Continue" button
        """
        self.driver.click("continue_btn",timeout=timeout)
    
    def toggle_switch(self, switch_obj: str, uncheck: bool):
        """
        @param switch_obj:
        To toggle privacy options on manage options page 
            1. APP_ANALYTICS
            2. ADVERTISING
            3. PERSONALIZED_SUGGESTIONS
        @param uncheck: True to turn off, False to turn on
        @return:
        """
        self.driver.check_box(switch_obj, uncheck=uncheck)
    
    def click_link(self, link):
        """
        Click on a link
        :param link: use class constants:
                TERM_USE_LINK 
                EULA_LINK
        """
        self.driver.click(link)
    
    def click_back_btn(self):
        """
        CLick on Back button on privacy preferences screen
        """
        self.driver.click("back_button")

    def toggle_privacy_options(self, switch_obj: str, state: bool):
        """
        @param switch_obj:
        To toggle privacy options on manage options page 
            1. APP_ANALYTICS
            2. ADVERTISING
            3. PERSONALIZED_SUGGESTIONS
        @param state: True to turn on, False to turn off
        """
        self.driver.selenium.check_box(switch_obj,state=state)
    
    def get_switch_status(self, option, state=True):
        """
        Get the status of toggle btn:
        @param:
            1. APP_ANALYTICS
            2. ADVERTISING
            3. PERSONALIZED_SUGGESTIONS
        """
        return self.driver.check_box(option,uncheck=state)

        
    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_privacy_preference_screen(self, timeout=10):
        """
        Verifying "Manage your HP Smart privacy preferences" screen
        """
        self.driver.wait_for_object("manage_your_hp_smart_privacy_preference", timeout=timeout)
        self.driver.wait_for_object("privacy_consents_items")

    def verify_continue_btn(self):
        """
        Verify continue button on manage privacy preference screen
        """
        self.driver.wait_for_object("continue_btn")

    def verify_back_btn(self):
        """
        Verify back button on manage privacy prefference screen
        """
        self.driver.wait_for_object("back_button")

    def verify_toggles(self, switch):
        """
        Verify APP_ANALYTICS on manage privacy preference screen
        @param:
            1. APP_ANALYTICS
            2. ADVERTISING
            3. PERSONALIZED_SUGGESTIONS
        """
        self.driver.wait_for_object(switch)