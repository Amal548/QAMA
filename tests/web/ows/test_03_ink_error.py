import pytest

pytest.app_info = "OWS"

class Test_03_ink_error(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup, request):
        self = self.__class__
        self.driver, self.emu_platform, self.ows_printer, self.fc=ows_test_setup
         
    def test_01_navigate_to_ink_step(self, request):
        if request.config.getoption("--browser-type") in ["chrome", "edge"] and self.emu_platform in ["IOS", "Android"]:
            pytest.skip()
        self.fc.navigate_ows(self.ows_printer, stop_at="insertInk")

    def test_02_send_error_state(self, request):
        self.ows_printer.toggle_ledm_status("insert_ink_dropbox", option_value="failed")
        self.fc.flow["load_ink"].verify_spinner_modal()
        self.ows_printer.send_product_status(request.config.getoption("--emu-error"))

    def test_03_verify_error_modal(self):
        self.fc.flow["load_ink"].verify_error_modal()

    def test_04_verify_error_modal_hide(self):
        self.fc.flow["load_ink"].click_error_modal_learn_more_btn()
        self.fc.flow["load_ink"].verify_error_modal(invisible=True)
        self.fc.flow["load_ink"].verify_collapsed_error_body(invisible=False)

    def test_05_verify_error_modal_show(self):
        self.fc.flow["load_ink"].click_collapsed_error_body()
        self.fc.flow["load_ink"].verify_error_modal(invisible=False)
        self.fc.flow["load_ink"].verify_collapsed_error_body(invisible=True)

    def test_06_recover_error_state(self):
        self.ows_printer.send_product_status("noAlerts")
        self.ows_printer.insert_ink()
        self.fc.flow["load_ink"].ink_click_continue()

    def test_07_complete_flow(self):
        self.fc.navigate_ows(self.ows_printer)