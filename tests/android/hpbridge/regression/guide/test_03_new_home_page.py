import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrinterNameOption
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
pytest.app_info = "hpbridge"


class TestNewHomePage(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.mp_faq = self.fc.flow["mp_faq"]
        self.binding = self.fc.flow["bind_printer"]
        self.pa_home = self.fc.flow["pa_home"]
        self.pa_my_printer = self.fc.flow["pa_my_printer"]

        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. The test printer has been enabled webservice and got the welcome page with QR code and Email address displayed on it.
            4. The test printer is not bound with the login Wechat account.
        """
        # define variables
        self.printer_name = PrinterNameOption.OFFICE.value
        api_uitility = APIUtility()
        api_uitility.unbind_all_printers()

    def test_01_new_home_page_fields(self):
        """
        Steps：
            1. Search out the WeChat Applet and then launch the Applet.
                Check the all stings and buttons on new home page.
            2. Click all buttons on this page.
        Expected:
            1. Verify the printer home page with no bound printer display correctly.
                Verify the "添加打印机…" "文件打印" "图片打印" "发票打印" "身份证复印" "百度网盘打印" "语音打印" "趣味打印" "网络文章打印" "证件照打印" "添加打印机"
                "惠普耗材积分" and "帮助和支持" icon display well.
                Verify the all stings display correctly.
            2. Verify the related pop up message or page display correctly.
                For "文件打印" "图片打印" "发票打印" "身份证复印" "百度网盘打印" "网络文章打印" "证件照打印" "语音打印" icon, verify the "未绑定设备的温馨提示" will pop up.
                For "趣味打印" icon, verify it jumps to the "我萌纸玩" applet sign in page.
                For "帮助和支持" icon, verify it jumps to the FAQ "微信打印须知" page.
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_add_printer_filed_no_device()
        self.mphome.check_file_print_no_device()
        self.mphome.check_file_print_no_device()
        self.mphome.check_img_print_no_device()
        self.mphome.check_invoice_print_no_device()
        self.mphome.check_id_copy_no_device()
        self.mphome.check_netdisk_print_no_device()
        self.mphome.check_url_print_no_device()
        self.mphome.check_id_photo_no_device()
        self.mphome.check_spice_print_no_device()
        self.mphome.check_voice_print_no_device()
        self.mphome.check_help_support_no_device()

    def test_02_add_and_remove_printer(self):
        """
        Steps；
            1.Click the "添加打印机.." button to 添加打印机 page.
            2.Click the "扫一扫" button and "绑定打印机" button to bound the first printer for the new user.
            3.Enter the Wechat Official Account and then go to unbind the printer.
            4.Launch the Applet and go to the printer home page.
        Expected:
            Verify the printer home page with new bound printer display well.
            Verify there is a red "新" in the upper right corner of the printer icon.
            Verify the printer name display right of the printer icon.
            Verify the unbind the printer operation can be performed successfully.
            Verify there is no bound printer on home page.
        :return:
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.change_printer_name(self.printer_name)
        self.binding.bind_printer(bound=False)
        self.mphome.verify_printer_exist(self.printer_name)
        self.mphome.verify_printer_new_icon(self.printer_name)
        self.driver.press_key_home()
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_my_printer()
        self.pa_my_printer.verify_printer_under_account(self.printer_name)
        self.pa_my_printer.unbind_printer(self.printer_name)
        self.pa_home.goto_wechat_from_pa()
        self.wechat.goto_mp()
        self.mphome.check_add_printer_filed_no_device()

