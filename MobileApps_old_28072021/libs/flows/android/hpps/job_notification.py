from MobileApps.libs.flows.android.hpps.hpps_flow import hppsFlow
from time import sleep
from time import time
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

class TrapDoorJobNotFinished(Exception):
    pass
class SystemUIJobNotFinished(Exception):
    pass


class Job_Notification(hppsFlow):
    """
        Job_Notifications - All Elements associated with HPPs notifications
    """
    # Flow_name - Title of the ui map used in this class
    flow_name = "job_notification"
    
########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################

    def select_print_notification_by_printer_name(self, printer_name):
        """
        selects the job notification by pritner name
        :param printer_name:
        :return:
        """
        self.driver.wait_for_object("print_job_title", format_specifier=[printer_name])
        els = self.driver.find_object("notif_main_column", multiple=True)
        for el in els:
            title = self.driver.find_object("print_job_title", root_obj=el)
            logging.warning(u"ELEMENT TEXT: {}".format(title.get_attribute("text")))
            if printer_name in title.get_attribute("text"):
                logging.warning("Found element")
                el.click()
                break

    def get_printing_results_trap_door(self, timeout=120):
        """
        waits for both the printing state in the notification and the printer itself to return the results of the print
        :param printer_con:
        :return:
        """
        cells = self.driver.find_object("job_cell", multiple=True)
        finished_state = self.get_text_from_str_id("finished_txt")

        for cell in cells:
            els = self.driver.find_object("file_name_as_job_description", root_obj=cell).text
            job_timeout = time() + timeout
            job_state = printer_status = None
            while time() < job_timeout:
                job_state = self.driver.find_object("job_state", root_obj=cell).text
                if job_state == finished_state:
                    printer_status = self.driver.find_object("job_status", root_obj=cell).text
                    break
                else:
                    sleep(5)
            logging.info(u"Print job ('{}') success with:\n\t- State: {}\n\t-Status: {}".format(els, job_state, printer_status))
        return True

    def select_print_job_from_trap_door_print_spooler(self):
        """
        select the first print job in the list on the trapdoor print spooler
        :return:
        """
        try:
            self.driver.wait_for_object("job_select_cb").click()
        except StaleElementReferenceException:
            logging.error("Cannot select the job to cancel, the job is probably finished")
            raise

    def cancel_selected_jobs(self):
        """
        click the "X" button to cancel the jobs that are selected
        """
        try:
            self.driver.wait_for_object("cancel_btn", timeout=5).click()
        except StaleElementReferenceException:
            logging.error("Cannot cancel job, all of the selected job are probably finished")
            raise

    def get_printing_results_system_ui(self, printer_con=None):
        """
        Only talks to the printer to find the result of the print job
        :param printer_con:
        :return:
        """
        pass



    ########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_print_jobs_screen(self):
        """
        verify print jobs screen is displayed
        :return:
        """
        self.driver.wait_for_object("print_job_txt")