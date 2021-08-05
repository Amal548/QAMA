import pytest
import time
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, WEBVIEW_CONTEXT
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.libs.flows.web.ows.ows_fc_factory import ows_fc_factory
from MobileApps.libs.flows.web.ows.ows_printer import OWSSplPrinter
from MobileApps.resources.const.android.const import WEBVIEW_URL

pytest.app_info = "SMART"


class Test_Suite_04_Complete_Moobe(object):

    @pytest.fixture(scope="class", autouse=True)
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Change to HP+ account for claiming printer in Moobe 
        cls.fc.set_hpid_account("hp+", claimable=True)

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.moobe_awc = cls.fc.flow[FLOW_NAMES.MOOBE_AWC]
        cls.printer_consent = cls.fc.flow[FLOW_NAMES.SMART_PRINTER_CONSENT]
        cls.value_proposition = cls.fc.flow[FLOW_NAMES.INSTANT_INK_VALUE_PROPOSITION]
        cls.moobe_complete = cls.fc.flow[FLOW_NAMES.MOOBE_SETUP_COMPLETE]
        cls.ows_p = OWSSplPrinter(cls.p)
        cls.ows = ows_fc_factory(cls.driver, cls.ows_p, context=WEBVIEW_CONTEXT.SMART)
        cls.yeti = cls.fc.flow[FLOW_NAMES.YETI_FLOW_CONTAINER]

        # Define variables
        cls.ssid, cls.password = get_wifi_info(request)

    def test_01_complete_moobe_with_new_account(self):
        """
        Description:
            - Load Home screen
            - Sign in or create account for hpid
            - Load Printers screen from Home screen
            - Process to select an oobe printer
            - Process an end2end moobe process
                + stage 1: connect printer to wifi
                + stage 2: ows 
                + stage 3: instant ink - skip enrollment
                + stage 4: setup complete
                Stage 2 and 3 are not in the same order of stage based on printer
        Expected Result:
            Moobe process is successful
            - Home screen with this printer.
        """
        # Previous steps before moobe and stage 1 of moobe
        wifi_type = self.fc.get_moobe_connect_wifi_type(self.p)
        is_ble = True if wifi_type == "secure_ble" else False
        is_secure = True if wifi_type == "secure_ble" else False


        self.fc.flow_home_moobe_connect_printer_to_wifi(printer_obj=self.p,
                                                        ssid=self.ssid,
                                                        password=self.password, 
                                                        is_ble=is_ble,
                                                        is_secure=is_secure,
                                                        create_acc=False)
        # Based on printers, checking printer status screen takes different timeout, increate time out to 20
        self.moobe_awc.select_continue()

        # Stage 2: OWS
        # Based on communicating to real printer got getting its information, increase timeout to 20
        self.driver.wait_for_context(WEBVIEW_URL.PRINTER_CONSENT, timeout=20)  
        self.printer_consent.verify_printer_consent_screen() 
        self.printer_consent.click_accept_all()

        # It is for Taccola yeti
        if "taccola" in self.ows_p.project_name and self.p.is_yeti():
            self.yeti.navigate_yeti(profile="taccolabase", biz_model="flex")
        # To other printers
        else:
            self.ows.navigate_ows(self.ows_p)
        
        # Stage 3: Instant ink 
        # Depending on previous screen from ows to instant ink for loading screen with HP+ account
        # Based on observation, timeout=30 covers for all printers
        self.value_proposition.skip_value_proposition_page(timeout=30)

        # To Palermo printers, there is an issue with printing alignment
        # For passing this screen, we have to wait for 3 minutes based on designed. (comment OWS - 64446)
        # Therefore, sleep for 3 minutes for Palermo printer for passing this screen
        if self.ows_p.project_name.split("_")[0] in ["palermo"]:
            time.sleep(180)

        # After value proposition, Taccola Yeti continue ows flow flor liveui 1.0
        if "taccola" in self.ows_p.project_name and self.p.is_yeti():
            self.ows.navigate_ows(self.ows_p)

        # Stage 4 Setup Complete
        self.moobe_complete.verify_setup_complete_screen()
        self.moobe_complete.select_setup_complete_not_now()
        self.moobe_complete.verify_print_other_devices_screen()
        self.moobe_complete.select_not_right_now()

        # Final step, verify at Home screen
        self.home.dismiss_print_anywhere_popup()
        self.home.verify_home_nav()
        self.home.verify_ready_printer_status()
