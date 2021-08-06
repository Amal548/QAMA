import os
import time
import logging

from SPL.decorator import SPL_decorator
from SPL.driver.reg_printer import PrinterNotReady

from MobileApps.libs.flows.android.hpps.system_ui import System_UI
from MobileApps.libs.flows.android.hpps.trap_door import Trap_Door
from MobileApps.libs.flows.android.hpps.more_options import More_Options
from MobileApps.libs.flows.android.hpps.all_printers import All_Printers
from MobileApps.libs.flows.android.hpps.hpps_settings import HPPS_Settings
from MobileApps.libs.flows.android.hpps.hp_print_service import HP_Print_Service
from MobileApps.libs.flows.android.hpps.job_notification import Job_Notification
from android_settings.src.libs.android_system_flow_factory import android_system_flow_factory
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.android.system_flows.sys_flow_factory import system_flow_factory


class Flow_Container(object):

    def __init__(self, driver):
        self.driver = driver

        # Initializing Flows
        self.fd = {
            "android_system": android_system_flow_factory(self.driver),
            "hp_print_service": HP_Print_Service(self.driver),
            "hpps_settings": HPPS_Settings(self.driver),
            "trap_door": Trap_Door(self.driver),
            "more_options": More_Options(self.driver),
            "system_ui": System_UI(self.driver),
            "all_printers" : All_Printers(self.driver),
            "job_notifications": Job_Notification(self.driver),
            "intermediate_flow": system_flow_factory(self.driver)
        }

    def turn_on_hpps(self):
        self.flow["android_system"].toggle_print_plugin(on=True)
        #self.flow["hp_print_service"].accept_ok_for_document_passing()

    def set_protocol(self, protocol=None):
        _protocol = self.driver.session_data["test_params"].hpps_protocol if protocol is None else protocol
        if _protocol != 'Default':
            logging.info("Setting Protocol to [{}]".format(_protocol))
            self.flow["android_system"].navigate_to_hp_print_plugin_page()
            self.flow["android_system"].select_more_options()
            self.flow["android_system"].verify_more_options()

            self.flow["android_system"].select_settings()
            self.flow["hp_print_service"].agree_and_accept_terms_and_condition_if_present()
            self.flow["hp_print_service"].turn_off_wifi_direct_notification_on_android_10_11_if_present()
            self.flow["hpps_settings"].verify_hpps_settings_screen()
            self.flow["hpps_settings"].select_advanced_settings()
            self.flow["hpps_settings"].select_print_protocol_type(_protocol)
            self.flow["hpps_settings"].select_back_arrow()
        else:
            logging.info("Leaving Protocol to Default settings")
        return True

    @property
    def flow(self):
        return self.fd

    #
    #   System UI Helper Methods
    #

    def open_and_select_printer_via_system_ui(self, bonjour_name, is_searched=True, timeout=120):
        self.flow["hp_print_service"].handle_hpps_t_and_c_notification_on_android_10_11_if_present()
        toc = self.flow["hp_print_service"].agree_and_accept_terms_and_condition_if_present()
        self.flow["hp_print_service"].turn_off_wifi_direct_notification_on_android_10_11_if_present()
        self.flow["system_ui"].check_run_time_permission()
        self.flow["system_ui"].verify_system_ui_screen()
        self.flow["system_ui"].select_all_printers()

        #Sometimes the list is dynamic so 
        if not self.flow["all_printers"].verify_all_printers_screen(raise_e=False):
            self.flow["system_ui"].select_all_printers()
            self.flow["all_printers"].verify_all_printers_screen(raise_e=True)

        self.flow["all_printers"].select_printer(bonjour_name, is_searched=is_searched, timeout=timeout)
        if not toc:
            self.flow["hp_print_service"].handle_hpps_t_and_c_notification_on_android_10_11_if_present()
            self.flow["hp_print_service"].agree_and_accept_terms_and_condition_if_present()
            self.flow["hp_print_service"].turn_off_wifi_direct_notification_on_android_10_11_if_present()
            self.flow["system_ui"].check_run_time_permission()

        #Sometimes for android 8 the preview/print button doesn't show up 
        #Developers don't know how to fix it. So we bandage it by changing the orientation one time
        if self.flow["system_ui"].verify_system_ui_preview_screen_with_print_button(raise_e=False) is False:
            self.flow["system_ui"].select_collapse_button()
            time.sleep(5)
            self.flow["system_ui"].change_orientation("landscape")
            time.sleep(5)
            self.flow["system_ui"].change_orientation("portrait")
            self.driver.wdvr.back()

        self.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()        

    def set_printer_options_in_system_ui(self, file_type):
        copies = self.driver.session_data["test_params"].hpps_copies
        color_mode = self.driver.session_data["test_params"].hpps_color
        paper_size = self.driver.session_data["test_params"].hpps_paper_size
        orientation = self.driver.session_data["test_params"].hpps_orientation
        two_sided = self.driver.session_data["test_params"].hpps_two_sided

        if copies != 'Default':
            logging.debug("Changing copies to [{}]".format(str(copies)))
            self.flow["system_ui"].change_copies(copies)
        else:
            logging.debug("Leaving Copies to Default Settings")
        if color_mode != 'Default':
            logging.debug("Color mode [{}]".format(color_mode))
            self.flow["system_ui"].change_color(color_mode)
        else:
            logging.debug("Leaving Color Mode to Default Settings")
        if paper_size != 'Default':
            logging.debug("Paper Size [{}]".format(paper_size))
            self.flow["system_ui"].change_paper_size(paper_size)
        else:
            logging.debug("Leaving Paper Size to Default Settings")
        if orientation != 'Default':
            logging.debug("Orientation [{}]".format(orientation))
            self.flow["system_ui"].change_orientation(orientation)
        else:
            logging.debug("Leaving Orientation to Default Settings")

        if two_sided != 'Default':
            logging.debug("Two Sided [{}]".format(two_sided))
            self.flow["system_ui"].change_two_sided(two_sided)
        else:
            logging.debug("Leaving Two Sided to Default Settings")

    @SPL_decorator.print_job_decorator()
    def select_print_and_verify_results_for_system_ui(self, printer_obj, cancel_job=False):
        self.select_print_in_system_ui_to_send_job(printer_obj)
        # Give extra time for print job to start
        time.sleep(2)
        if not cancel_job:
            self.verify_print_result_for_system_ui()
        else:
            self.cancel_print_job_in_system_ui_print_spooler()

    def select_print_in_system_ui_to_send_job(self, printer_obj):
        if printer_obj.is_printer_status_ready():
            self.flow["system_ui"].select_print()
            self.flow["hp_print_service"].accept_ok_for_document_passing()
            # Sometime the print_btn doesn't register on the first click
            self.make_sure_print_button_registered_in_system_ui()
        else:
            raise PrinterNotReady("Printer Status was not ready at this time.")

    def make_sure_print_button_registered_in_system_ui(self):
        is_triggered = False
        for _ in range(3):
            if not self.flow["system_ui"].does_print_button_disappear():
                logging.debug("Print btn doesn't seem to be registered. Retrying...")
                self.flow["system_ui"].select_print()
            else:
                is_triggered = True
                break
        if not is_triggered and not self.flow["system_ui"].does_print_button_disappear():
            raise TimeoutException("Failed to trigger print job after pressing the print_btn 3 times.")

    def verify_print_result_for_system_ui(self):
        self.driver.wdvr.open_notifications()
        try: 
            # Sometimes, print job takes longer than expected so the dev team requests
            # the timeout to be between 300 to 600 seconds
            self.flow["android_system"].open_print_spooler_from_notifications(timeout=300)
            self.flow["job_notifications"].get_printing_results_system_ui()
        except NoSuchElementException:
            logging.warning("Could not verify job through notifications (Probably because it finished too fast)")

    def cancel_print_job_in_system_ui_print_spooler(self):
        self.driver.wdvr.open_notifications()
        self.flow["android_system"].open_print_spooler_from_notifications(cancel_job=True)

    #
    #   Trap Door Helper Methods
    #
    def open_and_select_printer_via_trapdoor(self, printer_info, is_searched=True, timeout=120):
        """
        Select a printer on Select Printer screen
        :param printer_info: ip address or bonjour name
        :param is_searched: using searching or scrolling on printer list
        :return:
        """
        self.flow["hp_print_service"].agree_and_accept_terms_and_condition_if_present()
        self.flow["hp_print_service"].turn_off_wifi_direct_notification_on_android_10_11_if_present()
        self.flow["trap_door"].check_run_time_permission()
        self.flow["trap_door"].verify_select_printer_screen()
        self.flow["trap_door"].select_printer(printer_info, is_searched=is_searched, timeout=timeout)
        self.flow["trap_door"].verify_printer_preview_screen()

    def set_printer_options_in_trap_door(self, file_type):
        copies = self.driver.session_data["test_params"].hpps_copies
        color_mode = self.driver.session_data["test_params"].hpps_color
        paper_size = self.driver.session_data["test_params"].hpps_paper_size
        orientation = self.driver.session_data["test_params"].hpps_orientation
        two_sided = self.driver.session_data["test_params"].hpps_two_sided

        logging.debug("Copies: {}".format(copies))

        if copies != 'Default':
            logging.debug("Changing copies to [{}]".format(str(copies)))
            self.flow["trap_door"].change_number_of_copies_to(copies)
        else:
            logging.debug("Leaving Copies to Default Settings")
        if color_mode != 'Default':
            logging.debug("Color mode [{}]".format(color_mode))
            self.flow["trap_door"].change_color_mode(color_mode)
        else:
            logging.debug("Leaving Color Mode to Default Settings")
        if paper_size != 'Default':
            logging.debug("Paper Size [{}]".format(paper_size))
            self.flow["trap_door"].change_paper_size(paper_size)
        else:
            logging.debug("Leaving Paper Size to Default Settings")
        if orientation != 'Default' and file_type!="image":
            logging.debug("Orientation [{}]".format(orientation))
            self.flow["trap_door"].change_orientation(orientation)
        else:
            logging.debug("Leaving Orientation to Default Settings")
            
        if two_sided != 'Default' and file_type!="image":
            logging.debug("Two Sided [{}]".format(two_sided))
            self.flow["trap_door"].change_two_sided(two_sided)
        else:
            logging.debug("Leaving Two Sided to Default Settings")

    def set_more_options(self):
        quality = self.driver.session_data["test_params"].hpps_quality
        borderless = self.driver.session_data["test_params"].hpps_borderless
        scaling = self.driver.session_data["test_params"].hpps_scaling

        self.flow["more_options"].verify_more_options_screen()
        if quality != 'Default':
            logging.debug("Quality [{}]".format(quality))
            self.flow["more_options"].change_quality(quality)
        else:
            logging.debug("Leaving Quality to Default Settings")
        if scaling != 'Default':
            logging.debug("Scaling [{}]".format(scaling))
            self.flow["more_options"].change_scaling(scaling)
        else:
            logging.debug("Leaving Scaling to Default Settings")
        if self.flow["more_options"].is_photos_tab_selected() == 'true' and borderless != 'Default':
            logging.debug("Borderless [{}]".format(borderless))
            self.flow["more_options"].toggle_borderless(on=borderless=="on")
        else:
            logging.debug("Leaving Borderless to Default Settings")

    @SPL_decorator.print_job_decorator()
    def select_print_and_verify_results_for_trapdoor(self, printer_obj, printer_bonjour_name, jobs=1, cancel_job=False):
        self.select_print_in_trapdoor_to_send_job(printer_obj)
        # Give extra time for print job to start
        time.sleep(2)
        if not cancel_job:
            self.verify_print_result_for_trapdoor(printer_obj, printer_bonjour_name)
        else:
            self.cancel_print_job_in_trapdoor_print_spooler(printer_bonjour_name)

    def select_print_in_trapdoor_to_send_job(self, printer_obj):
        if printer_obj.is_printer_status_ready():
            self.flow["trap_door"].select_print()
        else:
            raise PrinterNotReady("Printer Status was not ready at this time.")

    def verify_print_result_for_trapdoor(self, printer_obj, printer_bonjour_name):
        self.driver.wdvr.open_notifications()
        try:
            self.flow["job_notifications"].select_print_notification_by_printer_name(printer_bonjour_name)
            self.flow["job_notifications"].verify_print_jobs_screen()
            if printer_obj.mech:
                timeout=480
            else:
                timeout=240
            self.flow["job_notifications"].get_printing_results_trap_door(timeout=timeout)
        except (NoSuchElementException, TimeoutException):
            logging.warning("Could not verify job through notifications (Probably because it finished too fast)")

    def cancel_print_job_in_trapdoor_print_spooler(self, printer_bonjour_name):
        self.driver.wdvr.open_notifications()
        self.flow["job_notifications"].select_print_notification_by_printer_name(printer_bonjour_name)
        self.flow["job_notifications"].select_print_job_from_trap_door_print_spooler()
        self.flow["job_notifications"].cancel_selected_jobs()