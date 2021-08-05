import logging
import time
from selenium.common.exceptions import *
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.instant_ink.mobile_flow_container import MobileFlowContainer

class MissingCredentialException(Exception):
    pass


class FLOW_NAMES():
    MOOBE_OWS = "moobe_ows"
    HPID = "hp_id_hybrid"
    INSTANT_INK_MOBILE = "instant_ink_mobile"


def return_firmware_type(printer_obj):
    if printer_obj.p_obj.isSOL:
        return "sol"
    else:
        return "sirius"


class BaseMoobeOWSFlowContainer(object):
    def __init__(self, driver, printer_obj, ows_flow):
        self.driver = driver
        self.printer = printer_obj
        self.system_config= ma_misc.load_system_config_file()
        self.fd = {FLOW_NAMES.MOOBE_OWS: ows_flow,
                   FLOW_NAMES.HPID: HPID(driver=driver),
                   FLOW_NAMES.INSTANT_INK_MOBILE: MobileFlowContainer(driver=driver)}

        self.fp_elements = {}

    @property
    def flow(self):
        return self.fd

    def click_front_panel_btn(self, fp_element, timeout=10, raise_e=True):
        """
        Click on button on front panel of printer
        :param fp_element: front panel element
        :type fp_element: list [screen_id, button_id]
        """
        logging.debug("Select button on front panel of printer : {}".format(fp_element))
        if self.verify_front_panel_screen(fp_element[0], timeout=timeout, raise_e=False):
            return self.printer.fp.pressWidget(widgetId=fp_element[1], actionType="select", waitSeconds=2)
        if raise_e:
            raise TimeoutException("{} screen does not display".format(fp_element[0]))
        else:
            logging.warning("{} screen does not display".format(fp_element[0]))
            return False

    def verify_front_panel_screen(self, screenID, timeout=30, raise_e=True):
        logging.debug("Verify front panel screen by: {}".format(screenID))
        timeout = time.time() + timeout
        while time.time() < timeout:
            if self.printer.fp.elementValuesGet("//ScreenId") == screenID:
                return True
        if raise_e:
            raise TimeoutException("{} screen does not display".format(screenID))
        else:
            logging.warning("{} screen does not display".format(screenID))
            return False

    def set_language(self, language):
        if language == 1:           # English
            for action in self.fp_elements["language"]:
                self.click_front_panel_btn(action)

    def set_country(self, country):
        if country == 15:       # USA
            for action in self.fp_elements["country"]:
                self.click_front_panel_btn(action)

    def language_country_step(self, language=1, country=15):
        """
        Set language and country step.
        Note: To app, this screen is not displayed for some printers on Android side.
              Work on this screen from app if it displayed.
              Only work on printer side.
        :param language:
        :param country:
        :return:
        """
        self.flow[FLOW_NAMES.MOOBE_OWS].skip_country_language_screen()
        self.set_language(language)
        self.set_country(country)

    def load_paper_step(self):
        """
        Load Paper step
        """
        if self.fd[FLOW_NAMES.MOOBE_OWS].verify_load_plain_paper_screen(raise_e=False):
            self.click_front_panel_btn(self.fp_elements["load_paper"])
            self.driver.swipe()
            self.fd[FLOW_NAMES.MOOBE_OWS].select_continue()

    def load_ink_cartridges_step(self):
        """
        Load ink cartridges
        Note: There is no app flow, only printer flow
        :return:
        """
        try:
            for fp_element in self.fp_elements["load_cartridges"]:
                self.click_front_panel_btn(fp_element)
        except TimeoutException:
            logging.info("Screen for loading ink cartridge from printer is not displayed")

    def register_instant_ink_step(self, is_registration=True):
        """
        Setup instant ink step
        :param is_setup: True -> setup instant ink. False -> skip it
        """
        if is_registration:
            raise NotImplemented("Implement it")
        else:
            self.fd[FLOW_NAMES.MOOBE_OWS].skip_register_instant_ink_screen()

    def ows_hp_id(self, stack, create_account=True, username=None, password=None):
        if create_account:
            if not self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_up(raise_e=False):
                self.fd[FLOW_NAMES.HPID].click_create_account_link()
            self.driver.session_data[FLOW_NAMES.HPID] = self.fd[FLOW_NAMES.HPID].create_account()
        else:
            if username is None:
                raise MissingCredentialException("Credential username is not set")
            if password is None:
                raise MissingCredentialException("Credential password is not set")
            if self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_up(raise_e=False):
                self.driver.swipe(per_offset=.5)
                self.fd[FLOW_NAMES.HPID].click_sign_in_link_from_create_account()
            self.flow[FLOW_NAMES.HPID].login(username, password)
            self.driver.session_data[FLOW_NAMES.HPID] = (username, password)
        system_cfg = ma_misc.load_system_config_file()
        if system_cfg["printer_power_config"]["type"] != "manual":
            self.printer.db_object.update_HPID_creds(self.printer.serial, stack,
                                                     self.driver.session_data[FLOW_NAMES.HPID][0],
                                                     self.driver.session_data[FLOW_NAMES.HPID][1])

    #Needs fixing
    def calibrate_printer_step(self):
        self.printer.fp.pressWidget("fb_option")
        self.printer.fp.pressWidget("fb_option")
        if "Used Cartridges" in self.printer.fp._screenInfoXml():
            self.printer.fp.pressWidget("fb_msg_ok")
        if "st_oobe_load_paper_photo_paper" in self.printer.fp._screenInfoXml():
            self.printer.fp.pressWidget("fb_action")

    def clean_up_printer(self, ssid, password):
        """
        Use to clean up printer if test fails. Make sure printer to be set up completely for other tests.
        """
        if self.printer.is_oobe_mode():
            self.printer.exit_oobe()
        if self.fp_elements and \
                self.verify_front_panel_screen(self.fp_elements["home_screen"], timeout=10, raise_e=False):
            self.click_front_panel_btn(self.fp_elements["cartridge_error"], timeout=30, raise_e=False)
        self.printer.connect_to_wifi(ssid, password)


class Gen1MoobeOWSFlowContainer(BaseMoobeOWSFlowContainer):
    firmware="sirius"

    def execute_ows(self, p_object, stack, instant_ink_registration=False, hp_connect_registration=True, create_account=True, username=None, password=None):
        self.flow["moobe_ows"].verify_hp_instant_ink_screen()

        if not instant_ink_registration:
            self.flow[FLOW_NAMES.MOOBE_OWS].select_get_ink_at_regular_price()
            self.flow[FLOW_NAMES.MOOBE_OWS].select_continue()
        else:       
            self.driver.swipe()
            self.driver.swipe()
            self.flow[FLOW_NAMES.MOOBE_OWS].select_continue()
            self.flow["instant_ink_mobile"].instant_ink_flow(p_object, stack)


class Gen2MoobeOWSFlowContainer(BaseMoobeOWSFlowContainer):
    firmware = "sol"

    def execute_ows(self, stack, language=1, country=15, align_printer=False, instant_ink_registration=False,
                    hp_connect_registration=True, create_account=True, username=None, password=None):
        self.language_country_step(language, country)
        if hp_connect_registration:
            self.ows_hp_id(stack, create_account, username, password)
        self.load_ink_cartridges_step()
        self.load_paper_step()
        self.calibrate_printer_step()
        self.register_instant_ink_step(instant_ink_registration)

