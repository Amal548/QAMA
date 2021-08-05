import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
pytest.app_info = "hpbridge"


class TestUnBindPrinter(object):
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
        self.api_utility = APIUtility()

        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. One or more printers bound to this login WeChat account.
            4. Follow the HP Cloud Print WeChat official account.
        """

        self.api_utility.unbind_all_printers()
        self.printer_name = self.api_utility.bind_default_printer()[0]

    def test_01_unbind_printer(self):
        """
        Steps:
            1.Enter the HP Cloud Print WeChat official account.
            2.Click the Personal Center->My Printers.
            3.Click one printer on Print Device page.
            4.Click "Unbind" button on printer settings screen.
            5.Click the "Unbind" button on confirm unbind printer screen.
            6.Check the Official account and Applet.
        Expected:
            Verify the Printer list screen should be displayed and the unbind printer is not displayed on official account and Applet.
        :return:
        """
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_my_printer()
        self.pa_my_printer.verify_printer_under_account(self.printer_name)
        self.pa_my_printer.unbind_printer(self.printer_name)
        self.pa_home.goto_wechat_from_pa()

        """
        Steps:
            1. Bind the printer which unbind on step1 again.
            2. Unbind the printer on official account.
        Expected:
            1. Check the printer status on applet, current should not be seen on applet.
            2. All UIs on applet should look normally.
        :return:
        """
        self.printer_name = self.api_utility.bind_default_printer()[0]
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_my_printer()
        self.pa_my_printer.verify_printer_under_account(self.printer_name)
        self.pa_my_printer.unbind_printer(self.printer_name)
        self.pa_home.goto_wechat_from_pa()
        self.wechat.goto_mp()
        self.mp.check_add_printer_filed_no_device()

