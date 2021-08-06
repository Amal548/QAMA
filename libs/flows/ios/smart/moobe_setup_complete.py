
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class MoobeSetupComplete(SmartFlow):
    flow_name = "moobe_setup_complete"


   # @retry((TimeoutException, NoSuchElementException), tries=2, delay=2)
    def select_remind_me(self):
        """
        At Reminder: screen, click on Remind me button
        End of flow: HP Connected screen
        """
        self.driver.click("remind_me_btn")
    
    #@MobiGA.counter(events=(EVENTS.CATEGORY_MOOBE,EVENTS.MOOBE__SETUP_COMPLETE_SCREEN))
    def select_setup_complete_skip(self):
        """
        End of flow:
        :return:
        """
        self.driver.click("not_now_btn")

    
    def select_i_icon(self):
        """
        At Invite screen, click on i icon button
        End of flow: Invite popup
        """
        self.driver.click("i_icon_btn")

    #@MobiGA.counter(events=(EVENTS.CATEGORY_MOOBE, EVENTS.MOOBE__SHARE_PRINTER_SCREEN, EVENTS.MOOBE__SHARE_PRINTER_SCREEN__INVITE))
    
    def select_invite(self):
        """
        At Invite screen, click on Invite button
        Note: This button has the same name of title -> using find_elements_by_name
        End of flow: popup displays
        """
        self.driver.wait_for_object("invite_btn")
        self.driver.find_object("invite_btn")[1].click()

    #@MobiGA.counter(events=(EVENTS.CATEGORY_MOOBE, EVENTS.MOOBE__SHARE_PRINTER_OPTIONS, EVENTS.MOOBE__SHARE_PRINTER_OPTIONS__SHARE_VIA_TEXT_MESSAGE))
    
    def select_invite_through_msg(self):
        """
        Click on Invite through text message button
        End of flow: Send Message screen
        """
        self.driver.click("invite_via_msg_btn")

    #@MobiGA.counter(events=(EVENTS.CATEGORY_MOOBE, EVENTS.MOOBE__SHARE_PRINTER_OPTIONS, EVENTS.MOOBE__SHARE_PRINTER_OPTIONS__SHARE_VIA_EMAIL))
    
    def select_invite_through_email(self):
        """
        Click on Invite through Email
        End of flow: composer of email
        """
        self.driver.click("invite_via_email_btn")

    #@MobiGA.counter(events=(EVENTS.CATEGORY_APP_USED_TO_SEND, EVENTS.APP_USED_TO_SEND__EMAIL, EVENTS.GENERAL_NO_SET))
    
    def send_share_printer_to(self, email_to):
        """
        Enter a email 'to' text field
        CLick on Send button
        :param email_to:
        """
        self.driver.send_keys("send_to_tf")
        self.driver.click("send_btn")

    #@MobiGA.counter(events=(EVENTS.CATEGORY_MOOBE, EVENTS.MOOBE__SETUP_COMPLETE_SCREEN, EVENTS.MOOBE__SETUP_COMPLETE_SCREEN__CONTINUE))
    
    def select_setup_complete_continue(self):
        """
        Click on Continue button on Setup Complete - let's print!
        End of flow: My Photos screen with permission popup
        """
        self.driver.click("continue_btn")

    def select_pop_up_yes_btn(self):
        self.driver.click("pop_up_yes_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_remind_me_title(self):
        self.driver.wait_for_object("reminder_title", timeout=5)
    
    def verify_invite_screen_from_cancelling_first_attempt(self):
        """
        Verify current screen is Invite screen via:
            - title
        """
        self.driver.wait_for_object("invite_title")

    def verify_invite_via_popup(self):
        """
        Verify current popup is Invite via popup via 3 buttons:
            - Invite through text message
            - Invite through email
            - Cancel
        """
        self.driver.wait_for_object("invite_via_msg_btn")
        self.driver.wait_for_object("invite_via_email_btn")
        self.driver.wait_for_object("cancel_btn")

    def verify_new_msg_screen(self):
        """
        Verify current screen is New Message screen via:
            - title
        """
        self.driver.wait_for_object("new_msg_title")

    def verify_email_composer_screen(self):
        """
        Verify current screen is Composer of Gmail screen via:
            - Cancel button
            - Send button
        """
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("send_btn")

    def verify_invitation_sent_screen(self, ga={}):
        """
        Verify current screen is Invitation sent! screen via:
            - title
        """
        self.driver.wait_for_object("invitation_sent_title")
    
    def verify_setup_complete_my_photos_screen(self):
        """
        Verify current screen is My Photos screen via:
            - title
        """
        self.driver.wait_for_object("my_photos_btn")
    
    def verify_setup_complete_all_photos_screen(self):
        """
        Verify current screen is All Photos screen via:
            - title
            - Select button
        """
        self.driver.wait_for_object("all_photos_btn")
        self.driver.wait_for_object("album_select_btn")

    def verify_setup_complete_print_photos_screen(self):
        """
        Verify current screen is Print Photos screen via:
            title
        """
        self.driver.wait_for_object("print_photos_title")

    def verify_document_print_preview(self):
        """
        Verify current screen is Print Photos screen via:
            title
        """
        self.driver.wait_for_object("document_print_preview_headder")

    def verify_setup_complete_printing_progress_popup(self):
        """
        Verify current popup is Printing in Progress via:
            - title
        """
        self.driver.wait_for_object("printing_progress_txt")
        self.driver.wait_for_object("printing_progress_txt")

    def is_it_photos_printing_path(self):
        """
        Determine if the next screen is print photos album or Preview Print Document
         this is determined in moobe flow if the printer that is tested is using photo paper or only plain papaer
        :return:
        """
        try:
            self.driver.wait_for_object("my_photos_btn")
            return True
        except TimeoutException:
            self.driver.wait_for_object("document_print_preview_headder")
            return False

    def select_not_right_now(self):
        """
        Select the not right now button on the Print From Other Devices Screen
        :return:
        """
        self.driver.click("not_right_now_btn")

    ###################################################
    #              Verification Flows                 #
    ###################################################

    def verify_do_you_want_to_print_this_page(self):
        self.driver.wait_for_object("print_test_page_title", timeout=5)

    ##################################################
    #       Print from Other Devices SCREEN          #
    ##################################################
    def verify_print_from_other_devices(self):
        self.driver.wait_for_object("print_from_other_devices_txt")

    def verify_print_from_other_devices_ui(self):
        self.driver.wait_for_object("print_from_other_devices_txt")
        self.driver.wait_for_object("send_link_btn")
        self.driver.wait_for_object("skip_this_step")
        self.driver.wait_for_object("print_from_other_devices_description_txt")
        self.driver.wait_for_object("send_a_link_to_download_txt")
        self.driver.wait_for_object("send_link_image", displayed=False)

    def select_skip_this_step(self):
        self.driver.wait_for_object("skip_this_step").click()

    def select_send_link(self):
        self.driver.wait_for_object("send_link_btn").click()

    ###################################################
    #              Link Sent! SCREEN                  #
    ###################################################
    def verify_link_sent_screen(self):
        self.driver.wait_for_object("link_sent_txt")

    def select_link_sent_done(self):
        self.driver.wait_for_object("done_txt").click()

    def verify_link_sent_screen_ui(self):
        self.driver.wait_for_object("link_sent_txt")
        self.driver.wait_for_object("add_new_devices_txt")
        self.driver.wait_for_object("done_txt")
        self.driver.wait_for_object("send_another_link_desc_txt")
        self.driver.wait_for_object("send_another_link_btn")
        self.driver.wait_for_object("send_link_image", displayed=False)

    def select_send_another_link(self):
        self.driver.wait_for_object("send_another_link_btn").click()

    ###################################################
    #       Setup complete!- Let's Print SCREEN       #
    ###################################################

    def verify_setup_complete_lets_print(self, timeout=30):
        self.driver.wait_for_object("setup_complete_lets_print_title", timeout=timeout)

    def verify_setup_complete_lets_print_ui(self, timeout=30):
        self.driver.wait_for_object("setup_complete_lets_print_title", timeout=timeout)
        self.driver.wait_for_object("_shared_print")
        self.driver.wait_for_object("no_thanks_btn")
        self.driver.wait_for_object("setup_complete_lets_print_image")

    def select_print(self):
        self.driver.wait_for_object("_shared_print").click()

    def select_no_thanks(self):
        self.driver.wait_for_object("no_thanks_btn").click()
    ###################################################
    #       Print Sent! SCREEN                        #
    ###################################################

    def verify_print_sent_ui(self):
        self.driver.wait_for_object("print_sent_title")
        self.driver.wait_for_object("continue_btn")

    def select_continue_btn(self):
        self.driver.wait_for_object("continue_btn").click()
    ###################################################
    #       Setup complete! SCREEN                    #
    ###################################################

    def verify_setup_complete(self, timeout=30):
        self.driver.wait_for_object("set_up_complete_page_title", timeout=timeout)

    def select_all_done_btn(self):
        self.driver.click("all_done_btn")