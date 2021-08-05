import pytest

from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestBaiduPrint(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.binding = self.fc.flow["bind_printer"]
        self.print = self.fc.flow["print_flow"]
        self.baidu_print = self.fc.flow["baidu_print"]
        self.print_setting = self.fc.flow["print_setting"]

        # Define variables

        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. One or more printers bound to this login WeChat account.
            4. The user has bound with Baidu netdisk
        """
        self.test_file = "支持的文档/BobPanda.doc"

    def test_01_baidu_file_print(self):
        """
        Steps:
            2. Click "百度网盘打印"
            3. Select a file to do print
        Expected:
            the file can be print successfully
        :return:
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.baidu_print.select_baidu_print()
        self.baidu_print.select_file(self.test_file)
        self.baidu_print.confirm_file_select(self.test_file)
        self.print_setting.select_print()




