import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_factory import moobe_ows_flow_container_factory
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from SAF.misc import saf_misc
from MobileApps.resources.const.web.const import HPCONNECT as URL
from MobileApps.libs.flows.web.hp_connect.hp_connect import HPConnect
import time
import logging

pytest.app_info = "SMART"


class Test_Suite_02_MOOBE_OWS(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

        cls.stack = request.config.getoption("--stack")
        cls.stack_link = URL.STAGE1_URL if cls.stack == "stage" else URL.PIE_URL
        cls.ssid, cls.password = get_wifi_info(request)
        cls.ows_fc = moobe_ows_flow_container_factory(cls.driver, cls.p, cls.fc.fd["moobe_ows"])
        cls.email = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"]["username"]

    @pytest.fixture(scope="function", autouse=True)
    def execute_ows(self, request):
        self.fc.fd["ios_system"].clear_safari_cache()
        self.driver.wdvr.reset()
        self.fc.setup_moobe_awc_wifi(self.p)
        self.fc.moobe_connect_printer_to_wifi(ssid_name=self.ssid, wifi_password=self.password)
        self.fc.fd["moobe_awc"].select_continue()
        self.fc.fd["moobe_ows"].verify_enjoy_hp_account_benefits()
        self.fc.fd["moobe_ows"].select_sign_up_button()
        self.fc.fd["moobe_ows"].handle_ios_popup()
        self.ows_fc.execute_ows(self.stack, language=1, country=15, align_printer=False,
                                instant_ink_registration=False, hp_connect_registration=True, create_account=False,
                                username="qa.mobiauto@gmail.com", password="mobileapp")

        def hpid_cleanup():
            if "hp_id_hybrid" in self.driver.session_data:
                hpc = HPConnect(ma_misc.load_system_config_file(), stack=self.stack)
                hpc.sign_in_from_home_page(self.driver.session_data["hp_id_hybrid"][0],
                                           self.driver.session_data["hp_id_hybrid"][1])
                hpc.delete_printer(self.p, stack=self.stack, raise_e=False)
            else:
                logging.warning("{} is not in session_data".format("hp_id_hybrid"))
            self.fc.fd["ios_system"].clear_safari_cache()
        request.addfinalizer(hpid_cleanup)

    def test_01_ble_ows_complete(self):
        # Start send link and Moobe Setup Complete
        self.fc.fd["moobe_setup_complete"].verify_print_from_other_devices()
        self.fc.fd["moobe_setup_complete"].select_skip_this_step()
        self.fc.fd["moobe_setup_complete"].select_pop_up_yes_btn()
        self.fc.fd["moobe_setup_complete"].verify_setup_complete_lets_print()
        self.fc.fd["moobe_setup_complete"].select_no_thanks()
        self.fc.fd["moobe_setup_complete"].verify_setup_complete()
        self.fc.fd["moobe_setup_complete"].select_all_done_btn()
        self.fc.fd["home"].verify_home()

    def test_02_verify_print_from_other_devices_ui(self):
        """
        C17019691
        complete MOOBE until the "Print from other devices screen" and verify that page UI
        """
        self.fc.fd["moobe_setup_complete"].verify_print_from_other_devices_ui()

    def test_03_send_link_option(self):
        """
        C17019692
        complete MOOBE until the "Print from other devices screen" and click the send link button and verify popup
        """
        self.fc.fd["moobe_setup_complete"].select_send_link()
        self.fc.fd["share"].verify_share_popup()

    def test_04_send_link_by_text(self):
        """
        C17019693
        complete MOOBE until the "Print from other devices screen" and send link via messages and verify link sent page
        """
        self.fc.fd["moobe_setup_complete"].select_send_link()
        self.fc.fd["share"].verify_share_popup()
        self.fc.fd["share"].select_message()
        self.fc.fd["message"].verify_new_message_screen()
        self.fc.fd["message"].compose_message(self.email)
        self.fc.fd["ios_system"].handle_sim_card_popup()
        self.fc.fd["moobe_setup_complete"].verify_link_sent_screen()

    def test_05_send_link_by_mail(self):
        """
        C17019695
        complete MOOBE until the "Print from other devices screen" and send link via messages and verify link sent page
        """
        self.fc.fd["moobe_setup_complete"].select_send_link()
        self.fc.fd["share"].verify_share_popup()
        self.fc.fd["share"].select_mail()
        self.fc.fd["gmail"].compose_and_send_email(self.email)
        self.fc.fd["moobe_setup_complete"].verify_link_sent_screen()

    def test_06_send_another_link(self):
        """
        C17019696
        complete MOOBE until the "Print from other devices screen" and send link via messages and verify link sent page
        """
        self.fc.fd["moobe_setup_complete"].select_send_link()
        self.fc.fd["share"].verify_share_popup()
        self.fc.fd["share"].select_message()
        self.fc.fd["message"].verify_new_message_screen()
        self.fc.fd["message"].compose_message(self.email)
        self.fc.fd["ios_system"].handle_sim_card_popup()
        self.fc.fd["moobe_setup_complete"].verify_link_sent_screen()
        self.fc.fd["moobe_setup_complete"].select_send_another_link()
        self.fc.fd["share"].select_message()
        self.fc.fd["message"].verify_new_message_screen()
        self.fc.fd["message"].compose_message(self.email)
        self.fc.fd["ios_system"].handle_sim_card_popup()

    def test_07_link_sent_done(self):
        """
        C17019697, C17023763
        complete moobe to the Setup complete --Let's print! page and verify the page
        """
        self.fc.fd["moobe_setup_complete"].select_send_link()
        self.fc.fd["share"].verify_share_popup()
        self.fc.fd["share"].select_message()
        self.fc.fd["message"].verify_new_message_screen()
        self.fc.fd["message"].compose_message(self.email)
        self.fc.fd["ios_system"].handle_sim_card_popup()
        self.fc.fd["moobe_setup_complete"].select_link_sent_done()
        self.fc.fd["moobe_setup_complete"].verify_setup_complete_lets_print()

    def test_08_test_print_page(self):
        """
        C17023780
        complete moobe to the Setup complete --Let's print! page and verify the page
        """
        self.fc.fd["moobe_setup_complete"].select_send_link()
        self.fc.fd["share"].verify_share_popup()
        self.fc.fd["share"].select_message()
        self.fc.fd["message"].verify_new_message_screen()
        self.fc.fd["message"].compose_message(self.email)
        self.fc.fd["ios_system"].handle_sim_card_popup()
        self.fc.fd["moobe_setup_complete"].select_link_sent_done()
        self.fc.fd["moobe_setup_complete"].verify_setup_complete_lets_print()
        self.fc.fd["moobe_setup_complete"].select_print()
        self.fc.fd["moobe_setup_complete"].verify_print_sent_ui()
        self.fc.fd["moobe_setup_complete"].select_continue()
        self.fc.fd["moobe_setup_complete"].verify_setup_complete()

    def test_09_do_not_test_print_page(self):
        """
        C17023781
        complete moobe to the Setup complete --Let's print! page and verify the page
        """
        self.fc.fd["moobe_setup_complete"].select_send_link()
        self.fc.fd["share"].verify_share_popup()
        self.fc.fd["share"].select_message()
        self.fc.fd["message"].verify_new_message_screen()
        self.fc.fd["message"].compose_message(self.email)
        self.fc.fd["ios_system"].handle_sim_card_popup()
        self.fc.fd["moobe_setup_complete"].select_link_sent_done()
        self.fc.fd["moobe_setup_complete"].verify_setup_complete_lets_print()
        self.fc.fd["moobe_setup_complete"].select_no_thanks()
        self.fc.fd["moobe_setup_complete"].verify_setup_complete()

    def test_10_setup_complete_all_done(self):
        """
        C17023782
        complete moobe to the Setup complete --Let's print! page and verify the page
        """
        self.fc.fd["moobe_setup_complete"].select_send_link()
        self.fc.fd["share"].verify_share_popup()
        self.fc.fd["share"].select_message()
        self.fc.fd["message"].verify_new_message_screen()
        self.fc.fd["message"].compose_message(self.email)
        self.fc.fd["ios_system"].handle_sim_card_popup()
        self.fc.fd["moobe_setup_complete"].select_link_sent_done()
        self.fc.fd["moobe_setup_complete"].verify_setup_complete_lets_print()
        self.fc.fd["moobe_setup_complete"].select_print()
        self.fc.fd["moobe_setup_complete"].verify_print_sent_ui()
        self.fc.fd["moobe_setup_complete"].select_continue()
        self.fc.fd["moobe_setup_complete"].verify_setup_complete()
        self.fc.fd["moobe_setup_complete"].select_all_done_btn()
        self.fc.fd["home"].verify_home()


