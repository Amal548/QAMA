from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_container import Gen2MoobeOWSFlowContainer, FLOW_NAMES
from selenium.common.exceptions import TimeoutException
import logging


class VeronaMoobeOWSFlow(Gen2MoobeOWSFlowContainer):
    """
    Tested on Android platform
    """
    project = "verona"

    def __init__(self, driver, printer_obj, ows_flow):
        super(VeronaMoobeOWSFlow, self).__init__(driver, printer_obj, ows_flow)
        self.fp_elements = {"language": [["ui_fl_oobe::st_oobe_list_langs", "model.0"],
                                         ["ui_fl_oobe::st_oobe_list_lang_confirm", "fb_action"]],
                            "country": [["ui_fl_oobe::st_oobe_list_cntry", "model.0"]],
                            "load_paper": ["ui_fl_oobe::st_oobe_load_paper", "fb_action"],
                            "load_cartridges": [["ui_flow_prdsts_error::st_dev_ink_err_ok_action", "fb_msg_ok"]],
                            "instant_ink": [["ui_fl_inksub_oobesetup::st_ii_enrolment_status", "fb_msg_ok"]],
                            "cartridge_error": ["ui_flow_prdsts_error::st_dev_ink_err_ok_action", "fb_msg_ok"],
                            "home_screen": "flow_home::state_home"
                            }

    def load_ink_cartridges_step(self):
        """
        Load ink cartridges steps
        """
        if self.fd[FLOW_NAMES.MOOBE_OWS].verify_setup_cartridges_screen(raise_e=False):
            self.printer.ows_fake_install_setup_cartridges()
            self.fd[FLOW_NAMES.MOOBE_OWS].verify_setup_cartridges_screen(invisible=True, raise_e=True)
            if self.fd[FLOW_NAMES.MOOBE_OWS].skip_something_unexpected_happened_screen():
                self.fd[FLOW_NAMES.MOOBE_OWS].skip_let_try_something_screen()
                self.fd[FLOW_NAMES.MOOBE_OWS].skip_issue_not_identified_screen()
            else:
                self.fd[FLOW_NAMES.MOOBE_OWS].skip_replace_cartridges_screen()
                super(VeronaMoobeOWSFlow, self).load_ink_cartridges_step()

    def calibrate_printer_step(self):
        """
        Print & Scan alignment
        To this printer, all actions for this step are on printer side.
        """
        # Print alignment
        self.fd[FLOW_NAMES.MOOBE_OWS].verify_print_alignment_screen()
        self.printer.set_mech_mode()
        self.click_front_panel_btn(["ui_fl_oobe::st_oobe_align_printer", "fb_action"])
        # Scan alignment
        self.fd[FLOW_NAMES.MOOBE_OWS].verify_scan_printed_page_screen()
        self.click_front_panel_btn(["ui_fl_oobe::st_oobe_calibscan", "fb_action"])
        if self.click_front_panel_btn(["ui_fl_oobe::st_oobe_calibscan_failure", "fb_action"], timeout=30, raise_e=False):
            self.click_front_panel_btn(["ui_fl_oobe::st_oobe_calibscan", "fb_action"])
        try:
            self.fd[FLOW_NAMES.MOOBE_OWS].verify_alignment_finished_screen()
        except TimeoutException:
            logging.info("alignment finished screen never displayed")
        if not self.click_front_panel_btn(["ui_fl_oobe::st_oobe_calibrationsuccessful", "fb_msg_ok"], raise_e=False):
            self.click_front_panel_btn(["ui_fl_oobe::st_oobe_calib_stopped", "fb_msg_ok"])
            self.click_front_panel_btn(["ui_fl_oobe::st_oobe_calib_incomplete", "fb_msg_ok"])
        try:
            self.fd[FLOW_NAMES.MOOBE_OWS].select_continue()
        except TimeoutException:
            logging.info("continue button never displayed")

    def register_instant_ink_step(self, is_registration=True):
        super(VeronaMoobeOWSFlow, self).register_instant_ink_step(is_registration=is_registration)
        if self.driver.driver_info["platformName"].lower() == 'ios':
            self.click_front_panel_btn(["ui_fl_inksub_oobesetup::st_ii_enrolment_status", "fb_msg_ok"])
