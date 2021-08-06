from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_container import Gen2MoobeOWSFlowContainer, FLOW_NAMES
from selenium.common.exceptions import TimeoutException
import logging
import time


#Todo: clean up all flows when it is refactored.
class InfinityMoobeOWSFlow(Gen2MoobeOWSFlowContainer):
    project = "infinity"

    def execute_ows(self, stack, language=1, country=15, align_printer=False, instant_ink_registration=False, hp_connect_registration=True,
                    create_account=True, username=None, password=None):
        self.flow[FLOW_NAMES.MOOBE_OWS].verify_enjoy_hp_account_benefits()
        self.flow[FLOW_NAMES.MOOBE_OWS].select_continue()
        # Register printer to cloud step
        if hp_connect_registration:
            self.ows_hp_id(stack, create_account, username, password)
        # Load cartridges step
        self.load_ink_cartridges_step()
        # Not sure this step for what, still skip for iOS
        # To Android: there is no following steps before alignment
        if self.driver.driver_info["platformName"].lower() == 'ios':
            for _ in range(2):
                self.driver.swipe(direction="right")
            self.flow[FLOW_NAMES.MOOBE_OWS].select_skip_this_step()
            for _ in range(3):
                self.driver.swipe(direction="right")
            self.flow[FLOW_NAMES.MOOBE_OWS].select_skip_this_step()
        # Alignment steps
        self.calibrate_printer_step(is_align=align_printer)

        # Register instant ink cartridge
        self.register_instant_ink_step(is_registration=instant_ink_registration)

        self.flow[FLOW_NAMES.MOOBE_OWS].select_continue_with_setup()

    def load_ink_cartridges_step(self):
        """
        Load ink cartridges
        """
        try:
            # IF this screen display, using udw command for faking pen host of cartridges.
            self.flow[FLOW_NAMES.MOOBE_OWS].verify_set_up_cartridges_screen()
            self.printer.ows_fake_install_setup_cartridges()
            self.flow[FLOW_NAMES.MOOBE_OWS].skip_replace_cartridges_screen()
        except TimeoutException:
            logging.info("Screen for setup cartridges is not displayed")

    def calibrate_printer_step(self, is_align=True):
        """
        Alignment printer
        """
        self.flow[FLOW_NAMES.MOOBE_OWS].verify_print_alignment_screen()
        if is_align:
            self.flow[FLOW_NAMES.MOOBE_OWS].select_align_btn()
            self.flow[FLOW_NAMES.MOOBE_OWS].select_next_btn()
        else:
            self.flow[FLOW_NAMES.MOOBE_OWS].select_skip_this_step()

    def register_instant_ink_step(self, is_registration=True):
        """
        Setup instant ink step
        :param is_setup: True -> setup instant ink. False -> skip it
        """
        try:
            self.flow[FLOW_NAMES.MOOBE_OWS].verify_offer_instant_ink_screen()
            for _ in range(3):
                self.driver.swipe(direction="right")
            if is_registration:
                self.driver.select_continue()
                #Resolve instant ink
            else:
                self.flow[FLOW_NAMES.MOOBE_OWS].select_do_not_enable_ink_saving()
        except TimeoutException:
            logging.info("HP instant ink is not displayed. Skip this step! ")
