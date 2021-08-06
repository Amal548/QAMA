import logging

from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow
from pytz import timezone
from selenium.webdriver.common.action_chains import ActionChains

class UserSearchException(Exception):
    pass

class SuccessMessageException(Exception):
    pass

class StringMismatchException(Exception):
    pass

class ReloadDataException(Exception):
    pass

class Users(ECPFlow):
    """
        Contains all of the elements and flows associated in Users section for ECP
    """
    flow_name = "users"

    def verify_userspage_title(self, timeout=20):
        #Verify Users page/section title
        expected_user_title_text = "Users"
        self.driver.wait_for_object("users_title", timeout=timeout)
        actual_user_title_text = self.driver.get_text("users_title")
        if expected_user_title_text == actual_user_title_text:
            logging.info("Users section title: "+actual_user_title_text)
            return True
        else:
            raise StringMismatchException("Users section title does not match: "+actual_user_title_text)

    def verify_userspage_desc(self):
        #verify users section descriion 
        expected_users_scection_desc="View, manage, and modify user privileges, and user access to solutions."
        actual_users_scection_desc = self.driver.get_text("users_section_desc")
        if expected_users_scection_desc == actual_users_scection_desc:
            logging.info("expected_desc: "+ expected_users_scection_desc+",  actual_users_scection_desc: "+actual_users_scection_desc)
            return True
        else:
            raise StringMismatchException("Does not match expected_desc: "+ expected_users_scection_desc+",  actual_users_scection_desc: "+actual_users_scection_desc)
        

    def search_users(self, usr_info, raise_e=True, timeout=10):
        """
            Search users in user table by using either user name or Email id 
            Should display list of users based on search string, if search string match
            else should display No items foumd message.
        """
        self.driver.wait_for_object("search_user_inputbox",timeout=timeout, raise_e=raise_e)
        self.driver.send_keys("search_user_inputbox", usr_info)
        
        if self.driver.find_object("table_entry_noitemsfound",raise_e=False) is not False:
            table_entry_users=self.driver.find_object("table_entry_noitemsfound")
            logging.info(table_entry_users.text)
            return False
        else:
            table_entry_users = self.driver.find_object("table_entry_username",multiple=True)
            table_entry_emails = self.driver.find_object("table_entry_email",multiple=True)

            for i in range(len(table_entry_users)):
                if usr_info in table_entry_users[i].text or usr_info in table_entry_emails[i].text:
                    logging.info("Username: " + table_entry_users[i].text+ " or  email: " + table_entry_emails[i].text + " contains the searched string: " + usr_info)
                    continue
                else:
                    raise UserSearchException("Username: " + table_entry_users[i].text+ " or email: " + table_entry_emails[i].text + " does not contain the searched string: " + usr_info)
        return True

    def verify_refresh_button(self,timeout=10):
        """
            - Verify Refresh button and click on it:
            - Verify refresh date and time
            - Note: Currently client's time is hard code, need find right solution to get clients's time zone and update client_time
        """
        self.driver.wait_for_object("reload_btn",timeout=timeout)
        self.driver.click("reload_btn")
        format = "%-d %b %Y | %I:%M:"
        now_utc = datetime.now(timezone('UTC'))
        client_time = now_utc.astimezone(timezone('US/Pacific'))
        expected_time="Last Updated: "+client_time.strftime(format)
        actual_time = self.driver.find_object("table_reload_date_and_time_text")
        if expected_time in actual_time.text:
            logging.info("Data load actual_time : "+actual_time.text+ " match with expected_time : "+expected_time)
            return True
        else:
            raise ReloadDataException("Data load actual_time : "+actual_time.text+ " does not match with expected_time : "+expected_time)

    def click_search_clear_button(self):
        return self.driver.click("search_clear_btn")
    
    def click_floating_button(self, timeout=20):
        return self.driver.click("user_floating_btn", timeout=timeout)

    def click_remove_user(self):
        return self.driver.click("remove_user_btn")

    def verify_remove_user_success_notification(self, no_of_users):
        #verify positive  toast notification alert message 
        expected_text = "Sucessfully removed {} users" 
        expected_alert_message= expected_text.format(no_of_users)
        #self.driver.wait_for_object("success_alert")
        actual_alert_message = self.get_toast_notification_text()
        if expected_alert_message == actual_alert_message:
            logging.info(actual_alert_message)
            return True
        else:
            raise SuccessMessageException("Success message does not matach. expected_alert_message: "+expected_alert_message+" actual_alert_message: "+actual_alert_message)

    def verify_email_invitation_sent_message(self):
        expected_alert_message = "Email Invitation was sent successfully." 
        actual_alert_message = self.get_toast_notification_text()
        if expected_alert_message == actual_alert_message:
            logging.info(actual_alert_message)
            return True
        else:
            raise SuccessMessageException("Success message does not matach. expected_alert_message: "+expected_alert_message+" actual_alert_message: "+actual_alert_message)

        
    def get_toast_notification_text(self):
        self.driver.wait_for_object("success_alert")
        return self.driver.get_text("success_alert")

    def verify_remove_single_user(self, usr_info, timeout=10):
        """
            - This is method used to remove a specific user
            - If user doed not found it returns False
        """
        if self.search_users(usr_info, timeout=timeout):
            self.select_user_click_mouse_right_button()
            self.click_remove_user()
            self.click_removeuser_popup_remove_button()
            self.verify_remove_user_success_notification(1)
            if self.search_users(usr_info, timeout=timeout):
                raise UserSearchException("User is not  deleted: "+usr_info)
            else:
                logging.info("User successfully deleted: "+usr_info)
                return True
        else:
            logging.info("User does not found: "+usr_info)
            return False

    def select_user_click_mouse_right_button(self):
        #This method is used for Mouse right button click
        ac = ActionChains(self.wdvr)
        obj = self.driver.find_object("table_entry_username")
        ac.context_click(obj).perform()
        return True
    
    #######################    Contextual footer    ###############################
    def verify_select_all_items_checkbox(self):
        return self.driver.wait_for_object("table_select_all_items_checkbox")

    def click_select_all_items_checkbox(self):
        return self.driver.click("table_entry_checkbox")

    def verify_contextual_footer(self):
        return self.driver.wait_for_object("contextual_footer")
    
    def verify_contextual_footer_cancel_button(self):
        return self.driver.wait_for_object("contextual_footer_cancel_btn")

    def click_contextual_footer_cancel_button(self):
        return self.driver.click("contextual_footer_cancel_btn")

    def verify_contextual_footer_delete_button(self):
        return self.driver.wait_for_object("contextual_footer_delete_btn")

    def click_contextual_footer_delete_button(self):
        return self.driver.click("contextual_footer_delete_btn")

    def verify_contextual_footer_remove_user_dropdown(self):
        return self.driver.wait_for_object("contextual_footer_remove_user_dropdown")

    def click_contextual_footer_remove_user_dropdown(self):
        return self.driver.click("contextual_footer_remove_user_dropdown")


    ################ Remove user popup ##############################################
    def verify_removeuser_popup_title(self, timeout=20):
        return self.driver.wait_for_object("removeuser_popup_title", timeout=timeout)

    def verify_removeuser_popup_cancel_button(self):
        return self.driver.wait_for_object("removeuser_popup_cancel_btn")

    def verify_removeuser_popup_remove_button(self):
        return self.driver.wait_for_object("removeuser_popup_remove_btn")

    def click_removeuser_popup_cancel_button(self):
        return self.driver.click("removeuser_popup_cancel_btn")

    def click_removeuser_popup_remove_button(self):
        return self.driver.click("removeuser_popup_remove_btn")

    ########################### Invite Page ###########################
    #Will split these out info a different flow if needed 
    def select_option_from_role_dropdown(self, option):
        #Option is a number that matches the drop down in order (starting from 1)
        self.driver.click("invite_select_role_drop_down")
        self.driver.wait_for_object("invite_select_role_drop_down_option", format_specifier=[option])
        return self.driver.click("invite_select_role_drop_down_option", format_specifier=[option])

    def enter_emails_to_invite_txt_box(self, emails):
        return self.driver.send_keys("invite_email_address_text_box", emails)

    def click_send_invitation_button(self):
        return self.driver.click("invite_send_invitations_btn")

    def click_invite_button(self, timeout=30): 
        return self.driver.click("invite_btn", timeout=timeout)

    def verify_invite_user_tab(self):
        return self.driver.wait_for_object("invite_user_tab")

    def click_invite_add_button(self):
        return self.driver.click("invite_user_add_btn")

    def click_all_users_tab(self):
        return self.driver.click("invite_all_users_breadcrumb")
