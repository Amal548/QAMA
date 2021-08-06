from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.ma_misc import ma_misc

class HPConnect(HPConnectFlow):
    flow_name="hp_connect_home"
    root_url = {"pie": "https://www.hpsmartpie.com/us/en",
                "stage": "https://www.hpsmartstage.com/us/en"}
    

    HELP_SUPPORT_LINK = "help_support_link"
    ENDER_USER_LICENSE_AGREEMENT_LINK = "end_user_license_agreement_link"
    HP_PRIVACY_LINK = "hp_privacy_link"
    HP_SMART_TERMS_OF_USE_LINK = "hp_smart_terms_of_use_link"
    
    def __init__(self, driver, context=None):
        super(HPConnect, self).__init__(driver, context=context)
        self.hp_id_web = HPID(driver, context=context)

    def navigate(self, stack):
        self.driver.navigate(self.root_url[stack])

    ###############################################################################
    #                             Home page flows
    ###############################################################################
    def accept_privacy_popup(self):
        self.driver.click("privacy_popup_accept_btn", timeout=5, raise_e=False)

    def sign_in_from_home_page(self, username, password):
        self.verify_sign_in_btn()
        self.click_sign_in_btn()
        self.hp_id_web.login(username, password)
        self.driver.current_project = self.project
        self.driver.current_flow = self.flow_name
        self.driver.wait_for_object("my_printer_link")
        return True

    def verify_sign_up_btn(self):
        self.driver.wait_for_object("sign_up_btn")

    def click_sign_up_btn(self):
        self.driver.click("sign_up_btn")

    def verify_sign_in_btn(self):
        self.driver.wait_for_object("sign_in_link")

    def click_sign_in_btn(self):
        self.driver.click("sign_in_link")

    ###############################################################################
    #                             UCDE account flows
    ###############################################################################
    def click_menu_toggle(self):
        #This button is for mobile only
        self.driver.click("menu_toggle_btn")

    def verify_account_profile_screen(self, timeout=10):
        """
        Verify Account Profile screen  via:
        - Account Profile title
        - Profile form
        """
        self.driver.wait_for_object("account_profile_title", timeout=timeout)
        self.driver.wait_for_object("profile_form")

    ###############################################################################
    #                            HP+ account flows
    ###############################################################################
    
    def verify_account_summary(self, timeout=10):
        """
        Verify HP Plus account status on Account Summary screen via:
        - Account & HP+Memeber
        """
        self.driver.wait_for_object("account_summary_title", timeout=timeout)
        self.driver.wait_for_object("account_hp_plus_member")
    
    def click_close_btn(self):
        """
        Click on Close button on Account Summary screen
        """
        self.driver.click("close_btn")
    
    def click_help_center_btn(self):
        """
        Click on Help Center on HP Smart menu screen
        :return:
        """
        self.driver.click("help_center_btn")

    def click_users_btn(self):
        """
        Click on Users button on HP Smart menu screen
        :return:
        """
        self.driver.click("users_btn")
    
    def click_link(self, link, timeout=15):
        """
        Click on a link
        :param link: use class constants:
                HELP_SUPPORT_LINK 
                ENDER_USER_LICENSE_AGREEMENT_LINK 
                HP_PRIVACY_LINK
                HP_SMART_TERMS_OF_USE_LINK  
        """
        self.driver.click(link, timeout=timeout)

    def verify_smart_dashboard_menu_screen(self, timeout=15, invisible=False):
        """
        Verify Smart Dashboard menu screen via:
        - Account Dashboard (This item only shows for HP+ account)
        - HP+ Print Plans
        - Printers
        - Features
        - Account
        - Help Center
        """
        self.driver.wait_for_object("account_dashboard_btn", timeout=timeout, invisible=invisible)
        self.driver.wait_for_object("hp_instant_ink_btn")
        self.driver.wait_for_object("printers_btn")
        self.driver.wait_for_object("features_btn")
        self.driver.wait_for_object("account_btn")
        self.driver.wait_for_object("help_center_btn")

    ###############################################################################
    #                             Virtual Agent 
    ###############################################################################
    
    def verify_virtual_chat_popup(self, timeout=10):
        """
        Verify virtual chat pop up message is shown with 'Cancel' and 'Start Chat' buttons 
        """
        self.driver.wait_for_object("va_icon", timeout=timeout)
        self.driver.wait_for_object("va_cancel_btn")
        self.driver.wait_for_object("va_start_chat_btn")
    
    def select_start_chat(self):
        self.driver.click("va_start_chat_btn")
    
    def select_virtual_agent_cancel(self):
        self.driver.click("va_cancel_btn")
    
    def select_chat_with_virtual_agent(self):
        self.driver.click("chat_with_virtual_agent")