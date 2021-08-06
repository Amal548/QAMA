import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility
pytest.app_info = "hpbridge"


class TestChangePrinterName(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.pa_home = self.fc.flow["pa_home"]
        self.pa_my_printer = self.fc.flow["pa_my_printer"]
        self.mp = self.fc.flow["mp_home"]

        # Define variables
        self.new_name = RandomUtility.generate_digit_letter_strs(15)
        self.api_utility = APIUtility()

        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. One or more printers bound to this login WeChat account.
            4. Follow the HP Cloud Print WeChat official account.
        """

        self.api_utility.unbind_all_printers()
        self.printer_name, self.printer_id = self.api_utility.bind_default_printer()

    def test_01_change_bound_printer_name(self):
        """
        Steps:
            1.Enter the HP Cloud Print WeChat official account.
            2.Click the Personal Center->My Printers.
            3.Click one printer on Print Device page.
            4.Click "change name" button on printer settings screen.
            5.set a new name and click the "save" button
            6.back to Wechat applet and check the printer name
        Expected:
            Verify the Printer's name can be change successfully
        :return:
        """
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_my_printer()
        self.pa_my_printer.verify_printer_under_account(self.printer_name)
        self.pa_my_printer.select_printer(self.printer_name)
        self.pa_my_printer.change_printer_name(self.new_name)
        self.pa_home.goto_wechat_from_pa()
        self.wechat.goto_mp()
        self.mp.verify_printer_exist(self.new_name)





