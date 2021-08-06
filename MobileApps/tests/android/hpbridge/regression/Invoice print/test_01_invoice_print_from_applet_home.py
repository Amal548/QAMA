# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrintQuality

pytest.app_info = "hpbridge"


class TestInvoicePrintFlow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]
        self.print = self.fc.flow["print_flow"]
        self.invoice_print = self.fc.flow["invoice_print"]
        self.print_setting = self.fc.flow["print_setting"]

        # Define variables
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        self.test_invoice = "武汉金拱门"
        self.test_invoice2 = "武汉京东"
        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. The test printer has been enabled webservice and got the welcome page with QR code and Email address 
                displayed on it.
            4. The test printer is not bound with the login Wechat account.
            5. Make sure user added some invoices to "微信卡包->我的票券"
            6. Make sure user hasn't authorized for the "发票打印".
        """
    def test_01_invoice_print_flow_no_printer(self):
        """
        Steps:
            1. Launch the WeChat Applet.
            2. Click the "发票打印" button
            3. Click the "确定" button on below pop up message.
        Expected result:
            Verify the applet home page is displayed normally with no bound printer.
            Verify the "发票打印" button displayed well under the new tab "多功能打印".
            Verify the pop up message "您还未绑定打印机.." is displayed normally on home page.
            Verify the pop up message is disappeared and home page is displayed normally.
        """
        self.wechat.goto_mp()
        self.mphome.check_invoice_print_no_device()
        self.mphome.check_add_printer_filed_no_device()

    def test_02_invoice_print_flow_unselect_invoice(self):
        """
        Steps:
            1. Click the " 添加打印机" button on Applet home page to bind one printer.
            2. Check the home page.
            3. Click the "发票打印" button on home page
            4. Do not select any invoice.
            5. Click the "确定" or "确认"button.
        Expected:
            Verify the new bound printer display normally on home page.
            Verify the "发票打印" button displayed well under the new tab "多功能打印".
            Verify the " 发票列表" page display well.
            Verify the all added invoices in step1 can be displayed correctly in the" 发票列表".
            Verify the item in the invoice list is not selected by default.
            For Ios device: verify the "确定" button is gray with unclickable.
            For Android device: verify the "确认" button is light with clickable.
            For iOS device, the "确定" button is gray with unclickable.
            For Android device, if use doesn't add any invoices，clicking the "确认" button will take the user back to
                home page with the message "暂无可用发票".
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.print.select_invoice_print()
        self.invoice_print.click_confirm_btn()
        self.invoice_print.check_no_invoice_available_prompt()

    def test_03_invoice_print_flow_print_setting(self):
        """
        Steps:
            1. Select and unselect items in the invoice list.
            2. Select one item in the invoice list and then Click the "确定" or "确认"button.
            3.Click the "∨" to expansion the other settings.
            4.Check the UI.
            5.Click the "打印" button on "打印设置" page

        Expected result:
            Verify all the items can be seclected and unselected successfully.
            Verify the "打印设置" page displayed with "∨" button.
            Verify the default settings should be displayed with below.
            For inkjet:份数:1, 彩色: enabled, 纸张尺寸:A4(cannot be changed), 纸张类型:普通纸(cannot be changed),
                质量:一般, 设置为默认值: enabled.
            Verify the selected invoice can be printed out successfully.
            Verify the printed result is consistent with the print Settings.
        """

        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.print.select_invoice_print()
        self.invoice_print.select_invoice(self.test_invoice)
        self.invoice_print.click_confirm_btn()
        self.print_setting.select_collapse_button()
        assert self.print_setting.get_switch_button_status(0)
        assert self.print_setting.get_switch_button_status(1)
        assert self.print_setting.get_default_print_quality() == PrintQuality.NORMAL.value
        self.print_setting.select_print()

    def test_04_invoice_print_multiple_selection(self):
        """
        Steps:
            1. Select more than one item in the invoice list and then click the "确定"or "确认" button

        Expected result:
            Verify it will jumps back to home page and the related prompt message "当前只支持单张发票打印!" will pop up.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.print.select_invoice_print()
        self.invoice_print.select_invoice(self.test_invoice)
        self.invoice_print.select_invoice(self.test_invoice2)
        self.invoice_print.click_confirm_btn()
        self.invoice_print.check_multiple_invoice_selection_prompt()
