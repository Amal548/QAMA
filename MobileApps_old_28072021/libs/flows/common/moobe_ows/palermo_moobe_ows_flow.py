from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_container import Gen2MoobeOWSFlowContainer, FLOW_NAMES


class PalermoMoobeOWSFlow(Gen2MoobeOWSFlowContainer):
    """
    Tested on Android platform with Palemo Fast,
    """
    project = "palermo"

    def __init__(self, driver, printer_obj, ows_flow):
        super(PalermoMoobeOWSFlow, self).__init__(driver, printer_obj, ows_flow)
        self.fp_elements = {"language": [["ui_fl_oobe::st_oobe_list_langs", "model.0"], ["ui_fl_oobe::st_oobe_list_lang_confirm", "fb_confirm"]],
                            "country": [["ui_fl_oobe::st_oobe_list_cntry", "model.0"]],
                            "cartridge_error": ["ui_flow_prdsts_error::st_dev_ink_err_ok_action", "fb_action"],
                            "load_paper": ["ui_fl_oobe::st_loadplain_photopaper", "fb_Done"],
                            "calibration_error":["ui_fl_oobe::st_oobe_calibfailure", "fb_skip"],
                            "home_screen": "flow_home::state_home_folder"
                            }

    def set_language(self, language):
        if language == 1:           # English
            for action in self.fp_elements["language"]:
                self.click_front_panel_btn(action)

    def load_ink_cartridges_step(self):
        """
        Load ink cartridges steps
        """
        if self.fd[FLOW_NAMES.MOOBE_OWS].verify_setup_cartridges_screen(raise_e=False):
            self.printer.ows_fake_install_setup_cartridges()
            if self.verify_front_panel_screen("ui_flow_prdsts_error::st_dev_ink_err_ok_showme_action", timeout=30, raise_e=False):
                self.printer.ows_fake_install_setup_cartridges()
            # Handle for 3 different models of palermo
            self.click_front_panel_btn(self.fp_elements["cartridge_error"], timeout=30, raise_e=False)
            self.fd[FLOW_NAMES.MOOBE_OWS].verify_setup_cartridges_screen(invisible=True, raise_e=True)
            if self.fd[FLOW_NAMES.MOOBE_OWS].skip_something_unexpected_happened_screen():
                self.fd[FLOW_NAMES.MOOBE_OWS].skip_let_try_something_screen()
                self.fd[FLOW_NAMES.MOOBE_OWS].skip_issue_not_identified_screen()
            else:
                self.fd[FLOW_NAMES.MOOBE_OWS].skip_replace_cartridges_screen()

    def load_paper_step(self):
        """
        Load Paper step
        """
        if self.fd[FLOW_NAMES.MOOBE_OWS].verify_load_plain_paper_screen(raise_e=False):
            self.driver.swipe()
            self.fd[FLOW_NAMES.MOOBE_OWS].select_continue()

    def calibrate_printer_step(self):
        """
        Print alignment.
        """
        self.flow[FLOW_NAMES.MOOBE_OWS].verify_begin_calibration_screen()
        self.printer.set_mech_mode()
        # After clicking OK on lad paper, it automatically execute calibrate
        # Handle for 3 different models of palermo
        self.click_front_panel_btn(self.fp_elements["load_paper"], timeout=10)
        self.flow[FLOW_NAMES.MOOBE_OWS].verify_alignment_finished_screen()
        self.click_front_panel_btn(self.fp_elements["calibration_error"], timeout=60, raise_e=False)
        self.fd[FLOW_NAMES.MOOBE_OWS].select_continue()

class PalermoMinusMoobeOWSFlow(PalermoMoobeOWSFlow):
    sub_name = "minus"

    def __init__(self, driver, printer_obj, ows_flow):
        super(PalermoMinusMoobeOWSFlow, self).__init__(driver, printer_obj, ows_flow)
        self.fp_elements = {"language": [["ui_fl_oobe::st_oobe_list_langs", "model.0"], ["ui_fl_oobe::st_oobe_list_lang_confirm", "fb_action"]],
                            "country": [["ui_fl_oobe::st_oobe_list_cntry", "model.0"]],
                            "cartridge_error":["ui_flow_prdsts_error::st_dev_ink_err_ok_action", "fb_msg_ok"],
                            "load_paper":["ui_fl_oobe::st_oobe_load_paper_photo_paper", "fb_action"],
                            "calibration_error":["ui_fl_oobe::st_oobe_calibrationfailed", "fb_option"],
                            "home_screen": "flow_home::state_home"
                            }

