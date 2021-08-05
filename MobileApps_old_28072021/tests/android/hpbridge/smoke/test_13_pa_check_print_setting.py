import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility
pytest.app_info = "hpbridge"


class TestCheckPrintSetting(object):
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

    def test_01_check_printer_setting(self):
        """
        Steps:
            1. Check the "文件打印设置" and “图片打印设置” tab.
        Expected:
            Printer settings should shows match actual.
        :return:
        """
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_my_printer()
        self.pa_my_printer.select_printer(self.printer_name)
        printer = self.api_utility.get_printer_info(self.printer_id)
        self.pa_my_printer.check_print_setting(printer.doc_setting)
        self.pa_my_printer.select_photo_printer_setting()
        self.pa_my_printer.check_print_setting(printer.img_setting)




