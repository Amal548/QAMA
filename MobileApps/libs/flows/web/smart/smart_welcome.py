from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow
from selenium.common.exceptions import NoSuchElementException
from SAF.decorator.saf_decorator import screenshot_capture

class SmartWelcome(SmartFlow):
    flow_name = "smart_welcome"

    TERM_USE_LINK = "terms_of_use_link"
    EULA_LINK = "eula_link"
    HP_PRIVACY_STATEMENT = "hp_privacy_statement_link"
    APP_ANALYTICS = "app_analytics_toggle"
    ADVERTISING = "advertising_toggle"
    PERSONALIZED_SUGGESTIONS = "personalized_suggestions_toggle"

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    @screenshot_capture(file_name="welcome_screen.png")
    def verify_welcome_screen(self, raise_e=True, invisible=False):
        """
        Verify current screen is Welcome screen
        """
        #There are 2 contents should be shows on welcome screen, but it doesn't show at same speed, one shows up later. 
        # Developer is woking on this one to improve the screen's loading experience
        return self.driver.wait_for_object("welcome_title", timeout=15, raise_e=raise_e, invisible=invisible) is not False and \
        self.driver.wait_for_object("welcome_message", timeout=20, raise_e=raise_e, invisible=invisible) is not False

    def verify_click_btn(self):
        """
        Verify Accept All button on Welcome screen
        :return:
        """
        #Legacy method call still used in IOS 13
        #Swaping the definition to the new stuff
        self.driver.wait_for_object("accept_all_btn")

    def verify_manage_options_btn(self):
        """
        Verify More Options Button on Welcome screen
        Currently this function verified only for Android
        """
        self.driver.wait_for_object("manage_options_btn")
        
    def verify_learn_more_link(self):
        """
        #Legacy method from old welcome flow still used by IOS
        #Locator the same as privacy_statement_link
        """
        self.verify_hp_privacy_statement_link()

    def verify_hp_privacy_statement_link(self, raise_e=True):
        """
        Verify HP Privacy Statement link on Welcome screen
        :return:
        """
        return self.driver.wait_for_object("hp_privacy_statement_link", raise_e=raise_e)


    def verify_terms_of_use_link(self):
        self.driver.wait_for_object("terms_of_use_link")

    def verify_eula_link(self):
        self.driver.wait_for_object("eula_link")

    #-----------------      SOME SCREENS AFTER CLICKING ANY LINK ---------------------
    def verify_terms_of_use_page(self):
        """
        Verify the page of "Terms of use" opened
        """
        self.driver.wait_for_object("term_use_page_title")

    def verify_eula_page(self):
        """
        Verify EULA page display via title "Select a location"
        """
        self.driver.wait_for_object("select_location_title")

    def verify_privacy_statement_page(self):
        """
        Verify 'Our Approach to Privacy" page
        """
        self.driver.wait_for_object("privacy_statement_title")
    
    def verify_manage_options(self, raise_e=True):
        return self.driver.wait_for_object("manage_options", raise_e=raise_e)

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_accept_all_btn(self, timeout=10, change_check=None):
        """
        Click on "Accept All" button on the welcome screen
        """
        self.driver.click("accept_all_btn", timeout=timeout, retry=4, change_check=change_check)	

    def click_manage_options(self, timeout=10):
        """
        Click on "Manage Options" button on the welcome screen
        """
        self.driver.click("manage_options", timeout=timeout)
    def click_link(self, link):
        """
        Click on a link
        :param link: use class constants:
                TERM_USE_LINK 
                EULA_LINK
                HP_PRIVACY_STATEMENT
                LEARN_MORE_LINK
        """
        self.driver.click(link)

class AndroidSmartWelcome(SmartWelcome):
    context = "NATIVE_APP"