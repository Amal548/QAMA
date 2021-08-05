import pytest
import random
import string
from MobileApps.libs.flows.web.ows.sub_flow.osprey import Osprey
from MobileApps.libs.flows.web.ows.ows_emulator import OWSEmulator

pytest.app_info = "OWS"

class Test_Sample_OWS_Osprey(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, web_session_setup, request):
        self = self.__class__
        self.driver = web_session_setup
        self.driver.set_size("max")
        self.ows_emulator = OWSEmulator(self.driver)
        self.osprey = Osprey(self.driver)
        self.stack = request.config.getoption("--stack")
        
    @pytest.fixture(scope="class", autouse="true")
    def start_flow_using_osprey(self):
        self.driver.navigate(self.ows_emulator.emulator_url[self.stack])
        self.ows_emulator.select_app_or_post_oobe_list_item()
        self.ows_emulator.select_app_type_dropdown_and_choose("Osprey")
        self.ows_emulator.select_start_flow_button()

    def test_01_verify_help_hp_make_better_products(self):
        self.osprey.verify_help_hp_make_better_products_page()

    def test_02_check_no_congratulations_title(self):
        assert self.driver.wdvr.title != "Congratulations, you're are enrolled in HP Instant Ink"

    def test_03_check_continue_button(self):
        self.osprey.verify_option_unselected_in_the_section()
        self.osprey.enter_code_into_postal_code_text_field("12345", clear_text=True)
        self.osprey.select_continue_button()
        self.osprey.check_continue_button_state(check_enabled=False)

    def test_04_in_a_home_section(self):
        self.osprey.select_in_a_home_radio_button()
        self.osprey.verify_radio_button_status("home", checked=True)
        self.osprey.verify_dropdown_list_is_folded("home")
        self.osprey.verify_home_dropdown_toggle_is_displayed()
        self.osprey.verify_each_option_in_dropdown_list_is_selectable("home")

    def test_05_in_a_business_section(self):
        self.osprey.select_in_a_business_radio_button()
        self.osprey.verify_radio_button_status("business", checked=True)
        self.osprey.verify_dropdown_list_is_folded("business")
        self.osprey.verify_business_dropdown_toggle_is_displayed()
        self.osprey.verify_each_option_in_dropdown_list_is_selectable("business")

    def test_06_where_is_printer_located_edit_button(self):
        self.osprey.verify_edit_button_is_not_displayed()

    def test_07_postal_code_with_input_less_than_5_bytes(self):
        self.osprey.enter_code_into_postal_code_text_field("7", clear_text=True)
        self.osprey.verify_no_error_message_displayed()
        self.osprey.check_continue_button_state(check_enabled=True)

    def test_08_postal_code_with_invalid_input(self):
        self.osprey.enter_code_into_postal_code_text_field("1234#*@", clear_text=True)
        self.osprey.verify_no_error_message_displayed()
        self.osprey.check_continue_button_state(check_enabled=True)

    def test_09_postal_code_with_input_more_than_10_bytes(self):
        max_input_length = 10
        fuzzy_input = ''.join(random.choice(string.ascii_uppercase
                                            + string.ascii_lowercase
                                            + string.digits + string.punctuation) for _ in range(max_input_length + 5))
        self.osprey.enter_code_into_postal_code_text_field(fuzzy_input, clear_text=True)
        assert self.osprey.get_value_from_postal_code_text_field() == fuzzy_input[:max_input_length]

    def test_10_empty_page(self):
        osprey_url = self.driver.get_current_url()
        self.osprey.check_any_option()
        self.osprey.enter_code_into_postal_code_text_field("12345", clear_text=True)
        self.osprey.select_continue_button()
        assert osprey_url != self.driver.get_current_url()