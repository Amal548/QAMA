# coding: utf-8
from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import MessageCenter
import time, logging
import random


class MPMessageCenter(HPBridgeFlow):
    flow_name = "mp_message_center"

    def click_all_tab(self):
        """
        Click on all tab on message center page
        """
        self.driver.click("all_msg_tab")
        time.sleep(1)

    def click_share_tab(self):
        """
        Click on the share tab on message center page
        """
        self.driver.click("share_tab")
        time.sleep(1)

    def click_print_job_tab(self):
        """
        Click on print job tab on message center page
        """
        self.driver.click("print_job_tab")

    def click_printer_tab(self):
        """
        Click on printer tab on message center page
        """
        self.driver.wait_for_object("printer_tab").click()
        time.sleep(1)

    def click_delete_icon(self):
        """
        Click on the delete dustbin icon
        """
        if self.verify_dustin_icon_exist():
            self.driver.click("dustbin_icon", index=1)

    def click_cancel_btn(self):
        """
        Click on cancel option on message center page
        """
        self.driver.click("cancel_btn")

    def click_select_all_btn(self):
        """
        Click on select all button after clicked delete dustbin
        """
        self.driver.click("select_all_option")

    def click_delete_btn(self):
        """
        Click on delete button after clicked the delete dustbin icon
        """
        self.driver.click("delete_btn")

    def find_bottom_bolder_msg(self, time_out=180):
        """
        Find bottom bolder message on bottom of the page
        :return:
        """
        start_time = time.time()
        time_spend = 0
        if self.get_all_records_length() >= 10:
            while not self.driver.find_object("bottom_bolder_msg", raise_e=False):
                self.driver.swipe()
                if time.time() - start_time > time_out:
                    raise TimeoutError("Swipe screen to find bottom bolder message timeout in %s second" % time_out)
        else:
            logging.warning("There is no bottom bolder message if records is less than 10")

    def swipe_message_center_page(self, swipe_times=0):
        """
        Swipe the screen according to the request in test cases
        :param swipe_times: How many times you want to swipe the screen.
        """
        if self.get_all_records_length() >= 10:
            for _ in range(swipe_times):
                self.driver.swipe()
        else:
            logging.warning("The list of notifications are less than 10, no need to swipe the screen")

    def verify_no_more_msg(self):
        """
        Verify if the no more message strings appears
        """
        self.driver.wait_for_object("no_more_msg")

    def verify_dustin_icon_exist(self):
        """
        Verify if the dustin bin icon exist or not on message center page
        """
        if self.driver.wait_for_object("dustbin_icon", index=1, raise_e=False):
            return True
        else:
            raise NoSuchElementException("Failed to find the dustbin icon")

    def get_all_records_length(self):
        """
        Get the records amount in a tab
        """
        if not self.driver.wait_for_object("no_more_msg", timeout=3, raise_e=False):
            return len(self.driver.find_object("all_records", multiple=True))

    def delete_all_records(self):
        """
        Delete all records in a tab
        """
        if self.verify_dustin_icon_exist():
            self.click_delete_icon()
            self.click_select_all_btn()
            self.click_delete_btn()

    def locate_detailed_records(self, notification_order=0):
        """
        Located the detailed records in each tab, the default record is the first one which on top in a list
        :return: The object for the first record by default
        """
        if not self.driver.wait_for_object("no_more_msg", timeout=3, raise_e=False):
            return self.driver.find_object("all_records", index=notification_order)

    def get_notification_detailed_info(self, index=2, notification_order=0):  # Notes: index = 0 and 1 are empty element, not sure why
        """
        Get the notification details
        :param: index: 2: Notification title, index=3: notification body, index =4 notification time
        :param notification_order: if test the first notification, then set to 0
        :return: The strings of notification title
        """
        notification_obj = self.locate_detailed_records(notification_order=notification_order)
        return self.driver.get_text("records_details", index=index, root_obj=notification_obj)

    def verify_print_result_notification(self, passed=True):
        """
        Verify the print result from the notification title, default assert the print passed
        """
        notification_title = self.get_notification_detailed_info()
        if passed:
            assert notification_title == MessageCenter.PRINT_SUCCESS_NOTIFICATION.value
        else:
            assert notification_title == MessageCenter.PRINT_FAILED_NOTIFICATION.value

    def verify_bind_and_unbind_notification(self, bind=True, notification_order=0):
        """
        Verify the bind and unbind notifications
        :param bind: If check the bind notification, please set to True. For unbind, set to false
        :param notification_order: if test the first notification, then set to 0
        """
        notification_title = self.get_notification_detailed_info(notification_order)
        if bind:
            assert notification_title == MessageCenter.PRINTER_BINDING_NOTIFICATION.value
        else:
            assert notification_title == MessageCenter.PRINTER_UNBIND_NOTIFICATION.value

    def verify_select_all_cancel_delete_btn(self, displayed=True):
        """
        Verify the "select all", "cancel" and "Delete" button exist
        :param: displayed: if verify the button displayed, please set to True, otherwise set to False
        """
        if displayed and self.verify_dustin_icon_exist():
            self.click_delete_icon()
            self.driver.wait_for_object("select_all_option")
            self.driver.wait_for_object("cancel_btn")
            self.driver.wait_for_object("delete_btn")
        else:
            self.driver.wait_for_object("select_all_option", invisible=True)
            self.driver.wait_for_object("cancel_btn", invisible=True)
            self.driver.wait_for_object("delete_btn", invisible=True)

    def verify_records_selected(self):
        """
        Verify the records in the notification list has been selected
        :return:
        """
        root_obj = self.locate_detailed_records(notification_order=random.randint(0, self.get_all_records_length() - 1))
        assert self.driver.get_attribute("checkbox_checked", "checked", root_obj=root_obj).lower() == "true"

    def get_number_message_selected(self):
        """
        Get the number of message selected when trying to delete records
        """
        number_message = self.driver.get_text("delete_btn")
        return int(number_message[-3:-1])

    def verify_selected_number_notifications(self):
        """
        Verify the selected notifications is equal to the number beside the delete button
        """
        assert self.get_all_records_length() == self.get_number_message_selected()