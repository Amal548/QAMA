import logging
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class AppSettings(SmartFlow):
    flow_name = "app_settings"

    CELL_ADD_SETUP_PRINTER = "add_set_up_a_printer"
    CELL_SEND_FEEDBACK = "send_feedback"
    CELL_ABOUT = "about"
    CELL_NOTIFICATION_N_PRIVACY = "notifications_and_privacy_cell"

    BUTTON_CLOSE = "_shared_close"
    BUTTON_CONTINUE = "continue_btn"
    BUTTON_CANCEL = "_shared_cancel"
    BUTTON_BACK = "_shared_back_arrow_btn"
    BUTTON_SUBMIT = "submit_btn"
    LINK_HP_PRIVACY = "hp_privacy_statement"

    SETUP_NEW_PRINTER_INFO_ICON = "info_icon"
    SETUP_NEW_PRINTER_PAGE_TITLE = "set_up_printer_page_title"
    SETUP_NEW_PRINTER_PAGE_NOTE = "set_up_printer_page_note"
    SETUP_NEW_PRINTER_STEP_1_MESSAGE = "set_up_printer_page_step1_message"
    SETUP_NEW_PRINTER_STEP_2_MESSAGE = "set_up_printer_page_step2_message"

    INFO_ICON_HEADER = "info_icon_page_header"
    INFO_ICON_CLOSE_BUTTON = "info_icon_page_close_button"
    INFO_ICON_PRINT_WIRELESSLY_MSG = "to_print_wirelessly_msg"
    INFO_ICON_X_BUTTON = "info_icon_page_x_button"

    NOTIFICATIONS_PRIVACY_IMPROVEMENT_SWITCH = "app_improvement_switcher"

    ABOUT_ICON = "about_icon"
    ABOUT_RATE_BUTTON = "rate_us"
    ABOUT_EULA_LINK = "eula"
    ABOUT_LEGAL_INFORMATION = "legal_information"
    ABOUT_HEADER = "HP_Smart_text"

    PROMOTIONAL_MESSAGE_SWITCH = "promotional_messaging_switch"
    SUPPLY_STATUS_SWITCH = "supply_status_switch"
    APP_IMPROVEMENT_SWITCH = "app_improvement_switch"
########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows
#                                                                                                                      #
########################################################################################################################

    def select_sign_in_option(self):	
        """	
        Verify the app settings screen	
        :return:	
        """	
        self.driver.click("sign_in_button")	

    def select_create_account_btn(self):	
        self.driver.click("create_account_btn")

    def select_already_have_account_sign_in(self):
        """

        :return:
        """
        self.driver.click("already_have_account_text")

    def select_goto_hpc_account(self):
        """

        :return:
        """
        self.driver.click("goto_hpc_account_link")

    def hpc_complete_sign_in(self, email="ios.mobiauto@gmail.com", password="Mobileapp123"):
        """

        :return:
        """
        self.driver.click("email_tf1")
        self.driver.send_keys("email_tf1", email, press_enter=True)
        self.driver.wait_for_object("password_tf1")
        self.driver.send_keys("password_tf1", password)
        self.driver.click("final_sign_in_button")

    def select_browser_back_to_hp_smart(self):

        self.driver.wait_for_object("browser_back_to_hp_smart_btn")
        self.driver.click("browser_back_to_hp_smart_btn")

    def select_virtual_agent(self):
        """

        :return:
        """
        self.driver.scroll("chat_virtual_agent_btn", direction="down")
        self.driver.click("chat_virtual_agent_btn")
        time.sleep(5)

    def select_contact_hp_on_fb_messenger_from_app_settings(self, direction="up" ):
        """
        Note:Fb related events are for only few countries which supports fb

        :return:
        """

        self.driver.scroll("contact_HP_on_facebook_messenger_from_app_settings", direction=direction)
        self.driver.click("contact_HP_on_facebook_messenger_from_app_settings")

    def select_contact_hp_on_fb_popup_continue(self, allow_access=True):
        """
        Note:Fb related events are for only few countries which supports fb

        :return:
        """

        try:
            if self.driver.wait_for_object("contact_us_on_fb_popup_title", timeout=5):
                if allow_access:
                    self.driver.click("continue_btn")
                else:
                    self.driver.click("cancel_btn")
        except TimeoutException:
            logging.info("Current Screen did NOT contain the contact us on FB Messenger popup")

    def select_contact_hp_on_fb_messenger(self):
        """
        Note:Fb related events are for only few countries which supports fb

        :return:
        """
        self.driver.click("contact_us_on_facebook_btn")

    def select_tweet_us_for_support(self):
        """

        :return:
        """
        self.driver.click("tweet_us_for_support_link_txt")

    def select_tweet_us_for_support_tweet_btn(self, allow_access=True):
        """

        :return:
        """
        try:
            if self.driver.wait_for_object("tweet_us_for_support_popup_title"):
                if allow_access:
                    self.driver.click("tweet_us_for_support_tweet_btn")
                else:
                    self.driver.click("tweet_us_for_support_cancel_btn")
        except TimeoutException:
            logging.warning("Current Screen did NOT contain the Tweets us for support Popup")

    def select_notifications_settings(self):

        self.driver.scroll("notifications_settings_btn", direction="up")
        self.driver.click("notifications_settings_btn")

    def select_back_notifications_settings_ga(self):
        """
         clicks the back button, so that we will back to- App settings screen:
          here we are adding GA for alert banners and special banners to a back button:
            because we need to track the GA while screen left, so i didn't find the best way to add GA on leaving screen
            [ Notification-settings, Alert-banners, ON/OFF
              Notification-settings, Special-offers, ON/OFF
            ]
        :return:
        """
        self.driver.click("notifications_back_btn_with_ga")

    def toggle_switch(self, switch_obj: str, uncheck: bool):
        """
        :param switch_obj: ui map key
        :param uncheck: True to turn off, False to turn on
        :return:
        """
        self.driver.check_box(switch_obj, uncheck=uncheck)

    def select_privacy_settings(self):
        """

        :return:
        """
        self.driver.click("privacy_settings_btn")

    def select_sign_out_hpc(self):
        """
        selects sign out button on top of the screen;
        other app settings options may be some times on top os the screen or sometimes bottom of the screen
        but sign out button is always on top right corner: so keeping scroll inside selection and giving direction up
        :return:
        """
        self.driver.scroll("sign_out_btn", direction="up")
        self.driver.click("sign_out_btn")

    def select_sign_out_on_popup(self):

        self.driver.click("pop_up_sign_out_btn")

    def select_continue_to_allow_hp_com_signin(self, allow_access=True):
        """
        Verifies the popup to allow hp.com for HP Smart signing base on allow access value:
        :param allow_access: param to change the access: Default True, do click on Continue
        :return:
        """
        try:
            if self.driver.wait_for_object("sign_in_popup_to_allow_hp_com"):
                if allow_access:
                    self.driver.click("continue_btn")
                else:
                    self.driver.click("cancel_btn")
        except TimeoutException:
            logging.warning("Current Screen did NOT contain the HP Smart wants to use hp.comto signin Popup")

    def select_accept_for_terms_of_use(self, accept=True):
        """
        Selects the accept button on terms of use popup:
        :param accept: to choose either accept or decline: Dafult True= accept
        :return:
        """
        try:
            if self.driver.wait_for_object("terms_of_use_title"):
                if accept:
                    self.driver.click("accept_btn")
                else:
                    self.driver.click("decline_btn")
        except TimeoutException:
            logging.warning("Current Screen did NOT contain the Terms of use Popup to accept")

    def send_message_on_fb_chat_window(self, message="your continuous support is awesome"):
        """
        Note:Fb related events are for only few countries which supports fb
        Trying to send some message on chat window of fb:we can come back directly using browser back button like before
        but developers are asking to complete the actions to track some events
        :return:
        """
        self.driver.wait_for_object("send_a_message_tf")
        self.driver.click("send_a_message_tf")
        self.driver.send_keys("send_message_small_box_tf", message, press_enter=True)

    def select_continue_for_sign_out(self):
        """
        selects the continue button on popup if it ask as alert some times:
        :return:
        """
        try:
            self.driver.wait_for_object("continue_btn")
            self.driver.click("continue_btn")
        except TimeoutException:
            logging.info("HPC account sign out continue confirmation popup was not visible")

    def select_send(self):
        self.driver.click("send_btn")

    def select_share_logs(self):
        """
        :return:
        """
        self.driver.scroll("share_logs_btn", scroll_object="app_settings_tv")
        self.driver.click("share_logs_btn")
        time.sleep(5)

    def select_open_in_messenger(self):
        """
        :return:
        """
        self.driver.click("open_in_messenger")

    def select_allow_access(self):
        """
        :return:
        """
        self.driver.click("allow_access")

    def select_get_the_messenger_app(self):
        """
        :return:
        """
        self.driver.click("get_the_messenger_app")

    def select_open_or_close_in_app_store_popup(self, open=True):
        """
        :return:
        """
        self.driver.wait_for_object("open_in_app_store")
        if open:
            self.driver.click("open_btn")
        else:
            self.driver.click("cancel_btn")

    def select_download_messenger_btn(self):
        """
        :return:
        """
        try:
            self.driver.click("get_app")
            time.sleep(60)
            logging.info("Downloaded FB Messenger app")
        except NoSuchElementException:
            self.driver.click("redownload_app")
            time.sleep(60)
            logging.info("Re-downloaded FB Messenger app")

    def select_open_app_button(self):
        """

        :return:
        """
        self.driver.click("open_app_btn")

    def select_turn_on_notification_popup(self, allow_access=True):
        """
        Note:

        :return:
        """

        self.driver.wait_for_object("notification_popup")
        if allow_access:
            self.driver.click("ok_btn")
        else:
            self.driver.click("not_now_btn")

    def select_messenger_send_notifications_popup(self, allow_access=True):
        """
        Note:

        :return:
        """

        self.driver.wait_for_object("messenger_send_notifications_popup")
        if allow_access:
            self.driver.click("allow_btn")
        else:
            self.driver.click("dont_allow")

    def select_not_now_skip_btn(self):
        """
        :return:
        """
        self.driver.click("not_now_skip_btn")

    def select_phone_number_added_popup(self, allow_access=True):
        """
        Note:

        :return:
        """
        self.driver.wait_for_object("phone_number_add_popup")
        if allow_access:
            self.driver.click("continue_btn")
        else:
            self.driver.click("cancel_btn")

    def select_your_contact_wont_upload_popup(self, allow_access=True):
        """
        Note:

        :return:
        """
        self.driver.wait_for_object("contact_wont_upload_popup")
        if allow_access:
            self.driver.click("continue_btn")
        else:
            self.driver.click("cancel_btn")

    def select_hp_support_chat_option(self):
        """

        :return:
        """
        self.driver.wait_for_object("hp_support", timeout=10)
        self.driver.click("hp_support")

    def select_phone_contacts_not_now_btn(self):
        """
        :return:
        """
        self.driver.click("phone_contacts_not_now_btn")

    def select_message_send_btn(self):
        """
        :return:
        """
        self.driver.click("message_send_btn")

    def enter_search_item_in_search_box(self, default_name="HP Support"):
        """
        selects the search item by searching the given  name:
        :return:
        """

        self.driver.click("search_box")
        self.driver.send_keys("search_box", default_name)

    def select_notification_n_privacy_option(self):
        self.driver.scroll(self.CELL_NOTIFICATION_N_PRIVACY, check_end=False, click_obj=True)

    def get_switch_status(self, option):
        switch_status = int(self.driver.get_attribute(option, attribute="value"))
        return switch_status

    def select_i_accept_btn(self, timeout=5, raise_e=False):
        self.driver.click("accept_btn",timeout=timeout, raise_e=raise_e)

    def select_data_collection_notice_link(self):
        self.driver.click("data_collection_notice")

    def select_hp_privacy_statement(self):
        self.driver.click("hp_privacy_statement_link")
    
    def select_x_button(self):
        self.driver.click(self.INFO_ICON_CLOSE_BUTTON)
    
    def select_terms_of_use_link(self):
        self.driver.scroll("terms_of_use_title", click_obj=True)
    
    def select_google_analytics_privacy_policy_link(self):
        self.driver.scroll("google_analytics_privacy_policy",click_obj=True, check_end=True)
    
    def select_adobe_privacy_link(self):
        self.driver.scroll("adobe_privacy_link", click_obj=True, check_end=True)
    
    def select_optimizely_link(self):
        self.driver.scroll("optimizely_link",click_obj=True, check_end=True)
    
    def select_manage_privacy_settings_option(self):
        self.driver.scroll("manage_my_privacy_settings",click_obj=True, check_end=True)
    
    def send_app_logs_via_email(self, email, subject):
        self.driver.click("mail_btn", raise_e=True)
        self.driver.send_keys("send_to_field", email)
        self.driver.send_keys("subject_field", subject)
        self.driver.click("send_btn")

    ########################################################################################################################
    #                                                                                                                      #
    #                                                  Verification Flows
    #                                                                                                                      #
    ########################################################################################################################

    def verify_app_settings_screen_via_top_nav_bar(self, raise_e=True):
        self.driver.wait_for_object("app_settings_title", timeout=20, raise_e=raise_e)

    def verify_app_settings_screen(self, raise_e=True):
        """
        Verify the app settings screen
            GA ["screen": "/app-settings"]
        :return:
        """
        self.driver.wait_for_object("app_settings_title", raise_e=raise_e)

    def scroll_top_to_app_settings_screen(self):
        """
        scroll the app settings screen to very top, where ever the current screen is:
            requires this method at some places where we need to be at top screen
            and the visibility of my account is maximum times false by normal scroll, so trying with visibility
        :return:
        """

        try:
            self.driver.scroll("my_account_text", scroll_object="app_settings_tv", direction="up")
        except TimeoutException:
            visible = self.driver.find_object("my_account_text").get_attribute("visible")
            if not visible:
                self.driver.scroll("my_account_text", scroll_object="app_settings_tv", direction="up")

    def verify_hpc_sign_in_screen(self):
        """
            here we will get the web view page with sign in options:
        :return:
        """
        time.sleep(10)
        # self.driver.wait_for_object("sign_in_btn_for_existed_acc")
        try:
            self.driver.wait_for_object("dont_have_account_txt")
            self.driver.click("dont_have_account_txt")
        except TimeoutException:
            logging.info("seeing other screen ---> to and fro changes by developers")

        self.driver.scroll("already_have_account_text")
        self.driver.wait_for_object("already_have_account_text")

    def verify_hpc_sign_in_for_old_account(self):
        """

        :return:
        """
        self.driver.wait_for_object("sign_in_hpc_title")

    def verify_main_hpc_account_webpage(self):
        """

        :return:
        """
        self.driver.wait_for_object("browser_back_to_hp_smart_btn")

    def verify_notifications_settings_screen(self):
        """
        Verify the notifications Settings screen
        :return:
        GA ["screen": "/app-settings/notification-settings"]
        """

        self.driver.wait_for_object("_shared_back_arrow_btn")
        self.driver.wait_for_object("notifications_settings_title")

    def verify_privacy_settings_screen(self):
        """
        Verify the Privacy Settings screen:
            GA ["screen": "/app-settings/privacy-settings"]
        :return:
        """
        self.driver.wait_for_object("privacy_settings_title")

    def verify_successfull_sign_in_screen(self, raise_e=True):
        """
            verifies the app settings screen with sign out button on right corner.
                by seeing sign out option we confirming that user logged in HPC successfully.

        :return:
        """
        return self.driver.wait_for_object("sign_out_btn", timeout=10, raise_e=raise_e)

    #TODO: probably depricated completely. at this screen only discussions are going to keep this popup or not. don't delete this for a while till developers confirm.
    def verify_sign_out_popup(self):
        """
        verifies the sign out popup: saying that by signing out will disable features rely on your HP account.
        :return:
        """
        self.driver.wait_for_object("sign_out_information")

    def verify_we_are_logging_out_popup_and_skip(self):
        """
        it verifies the we are logging out popup: we can wait here for invisibility of this popup::
        but just for functionality check point doing the click on skip wait time
        :return:
        """
        if self.driver.wait_for_object("we_are_logging_out_txt", interval=1, timeout=1, raise_e=False):
            self.driver.click("skip_the_wait_btn")
        else:
            logging.info("user can skip the wait time,this feature is not visible or disappear too fast")

    def verify_safari_browser_allow_access_popup(self):
        """

        :return:
        """
        self.driver.wait_for_object("safari_allow_req_popup")

    def verify_hp_support_fb_page_options(self):
        """

        :return:
        """
        self.driver.wait_for_object("open_in_messenger", timeout=50)
        self.driver.wait_for_object("get_the_messenger_app")

    def verify_get_messenger_app_options(self):
        """

        :return:
        """

        self.driver.wait_for_object("get_the_messenger_app")

    def verify_messenger_app_store_screen(self):
        """

        :return:
        """

        self.driver.wait_for_object("app_store_messenger_screen")


    def verify_messenger_login_screen(self):
        """
        :return:
        """

        self.driver.wait_for_object("messenger_login_screen")

    def handle_messenger_is_already_login(self):
        """

        :return:
        """
        try:
            self.driver.wait_for_object("messenger_login_screen")
            logging.info("messenger on login screen")
        except TimeoutException:
            self.driver.wait_for_object("welcome_to_messenger_screen")
            self.driver.click("this_isnt_me_btn")
            logging.info("messenger already login screen")

    def messenger_complete_sign_in(self, email="qamobileapps@gmail.com", password="mobileapp1"):
        """

        :return:
        """

        self.driver.click("messenger_email_field")
        self.driver.send_keys("messenger_email_field", email, press_enter=True)

        self.driver.send_keys("messenger_password_field", password)
        self.driver.click("login_btn")

    def verify_chats_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("chats_screen")

    def verify_sent_msg(self, message):
        """

        :return:
        """

        val = self.driver.get_attribute(obj_name="send_message_label", attribute="value")
        if val == message:
            logging.info("send messenger verified successfully")
            return True
        else:
            logging.info("send messenger not verified")
            return False

    def verify_virtual_agent_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("virtual_agent_screen")

    def verify_contact_hp_on_fb_popup_text(self):
        """

        :return:
        """

        self.driver.wait_for_object("fb_mess_text_on_popup")

    def verify_contact_hp_on_fb_popup_buttons(self):
        """

        :return:
        """

        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("continue_btn")

    def handle_notification_screen(self):
        """

        :return:
        """
        try:
            self.driver.wait_for_object("notification_screen")
            self.driver.click("remind_later_btn")
            logging.info("Notification screen is displayed")
        except:
            self.driver.wait_for_object("chats_screen")
            logging.info("HP chats screen is displayed")

    def verify_hp_support_chat_option(self):
        """
        :return:
        """
        self.driver.wait_for_object("hp_support")

    def verify_reply_msg(self):
        """
        here we have to  verify whether we received reply from hp agent or not ? and cant verify with exact text message,
        because every time different live agent's replies with different content in the reply.
        :return:
        """
        try:
            message="hp"
            val = self.driver.get_attribute(obj_name="hp_support_reply", attribute="value")
            if message.lower() in val.lower() :
                logging.info("send messenger verified successfully")
                return True
            else:
                logging.info("send messenger not verified")
                return False
        except NoSuchElementException:
            logging.info("HP Support replies in working hours")
            return self.driver.wait_for_object("default_delay_reply", raise_e=False)

    def verify_data_collection_notice_page(self):
        self.driver.wait_for_object("data_collection_notice")
        self.driver.wait_for_object("courtesy_translation_for_hp")
    
    def verify_promotional_message_switch(self):
        self.driver.wait_for_object(self.PROMOTIONAL_MESSAGE_SWITCH)
    
    def verify_app_improvement_switch(self):
        self.driver.scroll(self.APP_IMPROVEMENT_SWITCH, click_obj=False, check_end=True)
    
    def verify_eula_page(self):
        """
        Verify EULA page display via title "Select a location"
        """
        self.driver.wait_for_object("eula")
    
    def verify_terms_of_use_page(self):
        """
        Verify the page of "Terms of use" opened
        """
        self.driver.wait_for_object("term_use_page_page")
    
    def verify_google_analytics_privacy_policy_page(self):
        self.driver.wait_for_object("google_analytics_privacy_policy_page")
    
    def verify_adobe_privacy_policy_page(self):
        self.driver.wait_for_object("adobe_privacy_policy_title")
    
    def verify_optimizely_page(self):
        self.driver.wait_for_object("optimizely_link")
    
    def verify_sign_in_option(self, raise_e=True):
        """
        Verify the app settings screen
        :return:
        """
        return self.driver.wait_for_object("sign_in_button", raise_e=raise_e) is not False
    
    def verify_create_account_btn(self, raise_e=True):
        return self.driver.wait_for_object("create_account_btn", raise_e=raise_e) is not False	

    ########################################################################################################################
    #                                                                                                                      #
    #                                                  Functionality Related sets
    #                                                                                                                      #
    ########################################################################################################################

    def sign_in_and_verify_hpc_account(self):
        self.select_sign_in_option()
        self.select_continue_to_allow_hp_com_signin()
        self.verify_hpc_sign_in_screen()
        self.select_already_have_account_sign_in()
        self.verify_hpc_sign_in_for_old_account()
        self.hpc_complete_sign_in()
        self.select_accept_for_terms_of_use(accept=True)
        self.verify_successfull_sign_in_screen()
        self.select_goto_hpc_account()
        self.verify_main_hpc_account_webpage()
        self.select_browser_back_to_hp_smart()
        self.verify_app_settings_screen()

    def sign_out_from_hpc(self):
        self.select_sign_out_hpc()
        self.select_sign_out_on_popup()
        self.select_continue_for_sign_out()
        self.driver.performance.start_timer("hpid_logout")
        self.verify_we_are_logging_out_popup_and_skip()
        self.verify_app_settings_screen()
        self.driver.performance.stop_timer("hpid_logout")

    def contact_fb_messenger_from_app_settings(self):
        self.select_contact_hp_on_fb_messenger_from_app_settings()
        self.select_contact_hp_on_fb_popup_continue()
        self.send_message_on_fb_chat_window()
        self.select_browser_back_to_hp_smart()
        self.verify_app_settings_screen()

    ########################################################################################################################
    #                                                                                                                      #
    #                                                 Functionality
    #                                                                                                                      #
    ########################################################################################################################

    def download_and_login_messenger(self):
        """

        :return:
        """
        self.select_open_in_messenger()
        self.verify_safari_browser_allow_access_popup()
        self.select_allow_access()
        self.select_get_the_messenger_app()
        self.select_open_or_close_in_app_store_popup()
        self.verify_messenger_app_store_screen()
        self.select_download_messenger_btn()
        self.select_open_app_button()
        self.handle_messenger_is_already_login()
        self.verify_messenger_login_screen()
        self.messenger_complete_sign_in()
        self.select_turn_on_notification_popup()
        self.select_messenger_send_notifications_popup()
        self.select_not_now_skip_btn()
        self.select_phone_number_added_popup()
        #self.select_skip_phone_number_popup()
        self.select_phone_contacts_not_now_btn()
        self.select_your_contact_wont_upload_popup()

    # -----------------SET UP NEW PRINTER -----------------------------------
    def select_set_up_new_printer_cell(self):
        if not self.driver.wait_for_object(self.CELL_ADD_SETUP_PRINTER, raise_e=False):
            self.driver.scroll(self.CELL_ADD_SETUP_PRINTER, direction="down")
        self.driver.wait_for_object(self.CELL_ADD_SETUP_PRINTER, timeout=10).click()
        if self.driver.driver_info['platformVersion'].split(".")[0] == '13':
            try:
                self.driver.wait_for_object("_shared_str_ok").click()
            except TimeoutException:
                logging.info("HP Smart would like to use bluetooth popup did not occur")

    def verify_set_up_new_printer_ui_elements(self):
        names = [attr for attr in dir(AppSettings) if attr.startswith("SETUP_NEW_PRINTER_")]
        for name in names:
            self.driver.wait_for_object(getattr(AppSettings, name), timeout=5)

    def verify_info_icon_ui_elements(self):
        names = [attr for attr in dir(AppSettings) if attr.startswith("INFO_ICON_")]
        for name in names:
            self.driver.wait_for_object(getattr(AppSettings, name), timeout=5)

    def select_set_up_new_printer_info_icon(self):
        self.driver.wait_for_object(self.SETUP_NEW_PRINTER_INFO_ICON, timeout=5).click()

    # ----------------------- FEEDBACK ------------------------------------------

    def select_send_feedback_cell(self):
        if not self.driver.wait_for_object(self.CELL_SEND_FEEDBACK, raise_e=False):
            self.driver.scroll(self.CELL_SEND_FEEDBACK, direction="down")
        self.driver.wait_for_object(self.CELL_SEND_FEEDBACK).click()

    def verify_medallia_page(self):
        self.driver.wait_for_object("how_satisfied_are_you", timeout=60)

    def select_hp_privacy_link(self):
        self.driver.wait_for_object(self.LINK_HP_PRIVACY).click()

    def select_stars(self):
        """
        clicks center of star slider for "overall how satisfied are you with the HP Smart App?
        """
        self.driver.wait_for_object("star_slider").click()

    def verify_star_slider(self):
        return self.driver.wait_for_object("star_slider")

    def verify_feedback_submission_popup(self):
        self.driver.wait_for_object("feedback_submission_popup")
        self.driver.wait_for_object("_shared_str_ok")

    def select_submit_btn(self):
        if not self.driver.wait_for_object(self.BUTTON_SUBMIT, raise_e=False):
            self.driver.scroll(self.BUTTON_SUBMIT, direction="down")
        self.driver.wait_for_object(self.BUTTON_SUBMIT).click()

    # ----------------------- HELP CENTER ------------------------------------

    def select_help_center(self):
        self.driver.click("_shared_help_center")

    # ----------------------- ABOUT ------------------------------------------
    def select_about_cell(self):
        if not self.driver.wait_for_object(self.CELL_ABOUT, raise_e=False):
            self.driver.scroll(self.CELL_ABOUT, direction="down")
        self.driver.wait_for_object(self.CELL_ABOUT).click()

    def verify_about_ui_elements(self):
        names = [attr for attr in dir(AppSettings) if attr.startswith("ABOUT_")]
        for name in names:
            self.driver.wait_for_object(getattr(AppSettings, name), timeout=5)
        self.driver.wait_for_object(self.LINK_HP_PRIVACY)
        self.driver.wait_for_object(self.BUTTON_BACK)

    def select_rate_us_button(self):
        self.driver.wait_for_object(self.ABOUT_RATE_BUTTON).click()

    def select_eula_link(self):
        self.driver.wait_for_object(self.ABOUT_EULA_LINK).click()

    def select_legal_info_link(self):
        self.driver.wait_for_object(self.ABOUT_LEGAL_INFORMATION).click()

    def verify_legal_information_ui_elements(self):
        self.driver.wait_for_object(self.ABOUT_LEGAL_INFORMATION)
        self.driver.wait_for_object(self.BUTTON_BACK)

    def select_cell(self, cell_name):
        if not self.driver.wait_for_object(cell_name, raise_e=False):
            self.driver.scroll(cell_name, direction="down")
        self.driver.wait_for_object(cell_name).click()

    def verify_app_improvement(self):
        if not self.driver.wait_for_object(self.NOTIFICATIONS_PRIVACY_IMPROVEMENT_SWITCH, raise_e=False):
            self.driver.scroll(self.NOTIFICATIONS_PRIVACY_IMPROVEMENT_SWITCH, direction="down")

    def is_switch_on(self, name):
        return int(self.driver.get_attribute(name, "value"))

    # ----------------------- Backup to iCloud ------------------------------------------
    def select_backup_to_icloud_cell(self):
        if not self.driver.wait_for_object("backup_to_icloud", raise_e=False):
            self.driver.scroll("backup_to_icloud", direction="down")
        self.driver.wait_for_object("backup_to_icloud").click()

    def verify_backup_to_icloud_ui(self):
        self.driver.wait_for_object("backup_to_icloud")
        self.driver.wait_for_object("backup_icloud_switch_title")
        self.driver.wait_for_object("backup_icloud_switch")
        self.driver.wait_for_object("icloud_account_message")

    def verify_icloud_sync_popup(self):
        self.driver.wait_for_object("sync_docs_popup_title")
        self.driver.wait_for_object("_const_keep_on_my_phone")
        self.driver.wait_for_object("_const_delete_from_my_phone")
        self.driver.wait_for_object("_const_dont_disable_sync")

    def select_keep_documents(self):
        self.driver.wait_for_object("_const_keep_on_my_phone").click()

    def select_delete_documents(self):
        self.driver.wait_for_object("_const_delete_from_my_phone").click()

    def select_do_not_disable_sync(self):
        self.driver.wait_for_object("_const_dont_disable_sync").click()

    def select_mobile_fax(self):
        self.driver.click("mobile_fax_cell")
    
