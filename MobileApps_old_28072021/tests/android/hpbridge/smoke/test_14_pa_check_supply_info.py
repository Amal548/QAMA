import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility
pytest.app_info = "hpbridge"


class TestSupplyInfo(object):
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
        self.test_printer = "Muscatel 6960"

        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. One or more printers bound to this login WeChat account.
            4. Follow the HP Cloud Print WeChat official account.
        """

        self.api_utility.unbind_all_printers()
        self.printer_name, self.printer_id = self.api_utility.bind_default_printer(self.test_printer)

    def test_01_check_supply_info(self):
        """
        Steps:
            2. Check the "估计墨盒量" tab.
            3. Click the "Shopping Cart" icon on the right.
        Expected:
            "估计墨盒量" tab should match actual printer status.("您的打印机状态出现问题，暂不支持耗材信息读取，请从电脑端或打印机控制面板获取更多信息" message should shows up if printer is offline or in reset status.)
            Purchase Supply page should shows up. And corresponding ink type shows up successful.
        :return:
        """
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_my_printer()
        self.pa_my_printer.select_printer(self.printer_name)
        self.pa_my_printer.select_supply_info()
        supply_info = self.api_utility.get_supply_info(self.printer_id)
        self.pa_my_printer.check_supply_info(supply_info)




