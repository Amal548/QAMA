import pytest

pytest.app_info = "OWS"

class Test_04_calibration_error(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup, request):
        self = self.__class__
        self.driver, self.emu_platform, self.ows_printer, self.fc=ows_test_setup

    def test_01_navigate_to_ink_step(self, request):
        if request.config.getoption("--browser-type") in ["chrome", "edge"] and self.emu_platform in ["IOS", "Android"]:
            pytest.skip()
        self.fc.navigate_ows(self.ows_printer, stop_at="insertInk")

    def test_02_send_error_state_ink(self, request):
        self.ows_printer.toggle_ledm_status("insert_ink_dropbox", option_value="failed")
        self.fc.flow["load_ink"].verify_spinner_modal()
        self.ows_printer.send_product_status("cartridgeFailure")

    def test_03_verify_error_modal(self):
        self.fc.flow["load_ink"].verify_error_modal()

    def test_04_recover_error_state(self):
        self.ows_printer.send_product_status("noAlerts")
        self.ows_printer.insert_ink()
        self.fc.flow["load_ink"].ink_click_continue()

    def test_05_navigate_to_calibrate(self):
        self.fc.navigate_ows(self.ows_printer, stop_at="calibration")

    def test_06_send_error_state_calibration(self, request):
        self.ows_printer.toggle_ledm_status("calibration_dropbox", option_value="failed")
        self.ows_printer.click_get_oobe_status_btn()
        self.fc.flow["calibration"].verify_spinner_modal()
        self.ows_printer.send_product_status(request.config.getoption("--emu-error"))

    def test_07_verify_error_page(self):
        self.fc.flow["calibration"].verify_failure_screen()

    def test_08_recover_error_state(self):
        self.ows_printer.send_product_status("noAlerts")
        self.ows_printer.calibrate_printer()

    def test_08_complete_ows(self):
        self.fc.navigate_ows(self.ows_printer)