from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow, Stacks
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
import logging
import time
from time import sleep


class PAHome(HPBridgeFlow):
    flow_name = "pa_home"

    def select_personal_center(self):
        """
        Click on personal center on public account page
        :return:
        """
        self.driver.wait_for_object("personal_center").click()

    def goto_mp_from_pa(self):
        """
        Click on mini program on public account page
        :return:
        """
        stack = utlitiy_misc.load_stack_info()
        if stack["stack"] == Stacks.DEV:
            self.driver.click("top_back_btn")
            self.driver.wait_for_object("address_book_button")
            self.driver.swipe(direction="up", per_offset=0.7)
            self.driver.wait_for_object("mp_icon_dev").click()
        else:
            self.driver.wait_for_object("mini_program").click()

    def click_my_printer(self):
        """
        Click on my printer on public account page which in personal center
        :return:
        """
        self.driver.wait_for_object("my_printers").click()
        self.driver.switch_to_webview(self.wechat_webview)

    def goto_wechat_from_pa(self):
        """
        Close public account page and back to wechat home page
        :return:
        """
        self.driver.switch_to_webview()
        for i in range(3):
            self.driver.click("close_pa_btn")
            if self.driver.find_object("wechat_home_btn", raise_e=False):
                break
            sleep(1)
        self.driver.wait_for_object("wechat_home_btn").click()

    def click_voice_print(self):
        """
        Click on voice print in personal center
        :return:
        """
        self.driver.click("voice_print")
        self.driver.switch_to_webview(self.wechat_webview)

    def click_print_history(self):
        """
        Click on print history in personal center
        :return:
        """
        self.driver.click("print_history")
        self.driver.switch_to_webview(self.wechat_webview)

    def click_purchase_supply(self):
        """
        Click on purchase supply in personal center
        :return:
        """
        self.driver.click("supply_purchase")
        self.driver.switch_to_webview(self.wechat_webview)

    def click_hp_supply_points(self):
        """
        Click on hp supply points in personal center
        :return:
        """
        self.driver.click("hp_supply_points")
        sleep(1)
        self.driver.switch_to_webview(self.wechat_webview)

    def verify_print_results_from_notification(self, timeout=180):
        """
        Check the print notification, if print successfully, return true, otherwise, return error code
        Clear the chat notification each time after finished checking the results, so we won't have the results from
        print out
        :return:
        """
        print_passed = False
        print_failed = False
        start_time = time.time()
        time_cost = 0
        while not print_passed and not print_failed and time_cost <= timeout:
            print_passed = self.driver.find_object("completed_notification_title", index=-1, raise_e=False)
            print_failed = self.driver.find_object("failed_notification_title", index=-1, raise_e=False)
            sleep(1)
            time_cost = time.time() - start_time

        if time_cost > timeout:
            raise TimeoutException("Wait for notification time out in %d second" % timeout)

        if print_passed:
            notification_title = print_passed.get_attribute("text")
            logging.info("printing passed, notification received, title %s, the document printed out successfully"
                        % notification_title)
            self.delete_notification_history("completed_notification_title")
            return True
        else:
            notification_title = print_failed.get_attribute("text")
            error_code = self.driver.find_object("failed_result_error_code", index=0).get_attribute("text")
            logging.info("printing failed, notification received, the document printed failed, "
                         "notification title %s Error code %s" % (notification_title, error_code))
            self.delete_notification_history("failed_notification_title")
            return False

    def delete_notification_history(self, obj_name):
        """
        Clear the chat notification
        :param obj_name: The chat history that need to be delete
        :return:
        """
        self.driver.long_press(obj_name, duration=2000)
        self.driver.wait_for_object("delete_history")
        self.driver.click("delete_history")
        self.driver.wait_for_object("confirm_delete").click()

    def click_search_help(self):
        """
        Click on search help on public account page
        :return:
        """
        self.driver.click("search_help")

    def click_new_function_introduction(self):
        """
        Click on new function introduction in search help
        :return:
        """
        self.driver.wait_for_object("new_function_intro").click()
        self.driver.switch_to_webview(self.wechat_webview)

    def click_wechat_print_notice(self):
        """
        Click on Wechat print notice in search help
        :return:
        """
        self.driver.wait_for_object("wechat_print_notice").click()
        self.driver.switch_to_webview(self.wechat_webview)

    def click_contact_support(self):
        """
        Click on contact support in search help
        :return:
        """
        self.driver.wait_for_object("contact_support").click()
        self.driver.switch_to_webview(self.wechat_webview)

    def click_suggestion_box(self):
        """
        Click on suggestion box in search help
        :return:
        """
        self.driver.wait_for_object("suggestion_box").click()
        self.driver.switch_to_webview(self.wechat_webview)

    def follow_public_account(self):
        """
        Follow the public account in Wechat
        :return:
        """
        if self.driver.wait_for_object("follow_public_account", raise_e=False):
            self.driver.click("follow_public_account")
        else:
            logging.info("User has already followed the public account")

    def unfollow_public_account(self):
        """
        Unfollow the public account in Wechat
        :return:
        """
        self.driver.wait_for_object("unfollow_public_account").click()

    def enter_public_account(self):
        """
        Enter the public account page after followed the public account
        :return:
        """
        self.driver.wait_for_object("enter_public_account").click()

    def click_3dots_menu_pa_home(self):
        """
        Click on the 3 dots menu on top right of the public account home page
        :return:
        """
        self.driver.wait_for_object("pa_home_3dots_menu").click()

    def go_to_mp_from_pa(self):
        """
        Click on '小程序' on public account home page
        :return:
        """
        self.driver.click("mini_program")