# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrinterNameOption
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility

pytest.app_info = "hpbridge"


class TestChangePrinterName(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mp_home = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]

        # Define variables
        self.api_utility = APIUtility()
        self.printer_name = PrinterNameOption.OFFICE.value
        self.special_character_printer_name = RandomUtility.generate_special_chars(10)
        self.valid_printer_name = RandomUtility.generate_digit_letter_strs(10)
        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. The test printer has been enabled webservice and got the welcome page with QR code and Email address displayed on it.
            4. The test printer is not bound with the login Wechat account.
        """
        self.api_utility.unbind_all_printers()

    # Use extend QR code to scan from a image
    def test_01_change_printer_name(self):
        """
        Steps:
            1. Scan the printer QR code by WeChat App or WeChat Applet.
            2. Check the printer binding details page in the Applet.
            3. Check the validation rules for updating printer name section. Input invalid character into the printer
                name section, such as: unsupported special chars, emoticon…


        Expected result:
            1. For online/offline new printer (without binding), a pencil icon is displayed next to the printer's
                model name, and the pencil icon is editable. For reset printer, the pencil icon should not be shown on
                this page. For the already bound printers, the pencil icon should not be shown on this page.
            2. Verify user can update the printer name successfully. Verify user can also quickly specify the printer
                name by clicking the "家庭打印机", "办公打印机"…
            3. Verify a prompt toast "50个字符以内，可输入中文、字母、数字、中划线、空格" should be displayed when user try to
                upate the printer name with unsupported chars/emoticon

        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.change_printer_name(self.printer_name)
        self.binding.verify_printer_name(self.printer_name)
        self.binding.change_printer_name(self.special_character_printer_name)
        self.binding.verify_invalid_character_strings()  # defect QQIOT-2189, test will be passed after defect fixed
        self.binding.verify_binding_printer_btn_status()

    def test_02_change_printer_valid_character(self):
        """
        Steps:
            1. Update the printer name, and then click the "绑定打印机" button.
            2. Check the printer name in Applet printer home page/Public account printer information page….
        Expected result:
            Verify the printer name in Applet printer home page/Public account printer information page are displayed 
            the new one.

        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.click_edit_pencil_icon()
        self.binding.enter_value_into_text_field(self.valid_printer_name)
        self.binding.click_binding_btn()
        self.binding.click_start_print_btn()
        self.mp_home.verify_printer_exist(self.valid_printer_name)