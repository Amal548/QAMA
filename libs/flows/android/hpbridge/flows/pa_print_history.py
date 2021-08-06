# coding: utf-8
from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrintJobStatus
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
import logging
from time import sleep


class PAPrintHistory(HPBridgeFlow):
    flow_name = "pa_print_history"

    def get_print_history_list(self):
        """
        Get the print history list from print history list page
        :return:
        """
        return self.driver.find_object("notification_list", index=0)

    def get_print_job_file_name(self):
        """
        Get the printed file name from the print history, could be a customized name
        :return: print_job_file_name
        """
        return self.driver.get_text("notification_title", root_obj=self.get_print_history_list())

    def get_printer_name(self):
        """
        Get the printer name from the print history, could be a customized name
        :return: printer_name
        """
        return self.driver.get_text("notification_content", index=0, root_obj=self.get_print_history_list())

    def get_print_job_completed_time(self):
        """
        Get the print job completed time from print history
        :return: completed_time
        """
        return self.driver.get_text("notification_content", index=1, root_obj=self.get_print_history_list())

    def get_print_job_status(self):
        """
        Get the printed status by the icon in printed history
        :return: print_status
        """
        self.driver.wait_for_object("notification_list")
        return self.driver.get_attribute("print_status", "class", root_obj=self.get_print_history_list())

    def verify_print_status_from_print_history(self, retries=20):
        """
        Check the print job completed status from print history
        :param retries:
        :return:
        """
        print_status = self.get_print_job_status()
        retry = 0
        while print_status == PrintJobStatus.PRINT_INPROGRESS.value and retry <= retries:
            self.driver.press_key_back()
            self.driver.switch_to_webview()
            self.driver.click("personal_center")
            self.driver.click("print_history")
            self.driver.switch_to_webview(webview_name=self.wechat_webview)
            print_status = self.get_print_job_status()
            retry += 1
        if retry > retries:
            raise TimeoutException("Unable to get the print job status in %d times retry" % retries)
        if print_status == PrintJobStatus.PRINT_PASSED.value:
            logging.info("print job %s printed with %s on %s successfully" %
                        (self.get_print_job_file_name(), self.get_printer_name(), self.get_print_job_completed_time()))
            return True
        else:
            logging.info("print job %s failed on printer %s, Error icon %s" %
                        (self.get_print_job_file_name(), self.get_printer_name(), print_status))
            return False

    def close_print_history_page(self):
        """
        Change back to native view(since the print history page is a webview) then click close the current print history
         page
        """
        self.driver.switch_to_webview()
        self.driver.click("print_history_page_close_btn")
