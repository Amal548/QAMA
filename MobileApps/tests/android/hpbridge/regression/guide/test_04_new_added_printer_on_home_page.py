import pytest

from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrinterNameOption
pytest.app_info = "hpbridge"


class TestNewAddedPrinterOnHomePage(object):

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
        self.print_setting = self.fc.flow["print_setting"]
        self.print = self.fc.flow["print_flow"]

        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
        """
        # define variables
        self.printer_name = PrinterNameOption.OFFICE.value
        self.api_uitility = APIUtility()
        self.api_uitility.unbind_all_printers()
        self.printer_name_2 = self.api_uitility.bind_default_printer()[0]

    def test_01_new_added_printer(self):
        """
        Steps：
            1.Launch the Applet.
                Bind a printer A and go to the home page.
            2.Bind a printer B and then go to the home page.
            3.Select the picture print or document print till to the print settings page with the printer B.
                Change the printer to printer A on print settings page.
                Click the print button
            4.Back to the home page.
                Check the result.
        Expected:
            1. Verify the printer icon display well on home.
                Verify there is a new in red at the top right corner of the printer A icon.
            2. Verify the new in red disappear at the top right corner of the printer A icon.
                Verify the new in red display at the top right corner of the printer B icon.
            3. Verify the print job can be printed out successfully.
            4. Verify the new in red still display at the top right corner of the printer B icon.
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.verify_printer_exist(self.printer_name_2)
        # bind with API, no new icon
        self.mphome.verify_printer_new_icon(self.printer_name_2, invisible=True)
        self.mphome.close_mp()
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.change_printer_name(self.printer_name)
        self.binding.bind_printer(bound=False)
        self.mphome.verify_printer_exist(self.printer_name)
        self.mphome.verify_printer_new_icon(self.printer_name)
        self.mphome.verify_printer_new_icon(self.printer_name_2, invisible=True)
        self.print.select_picture_print()
        self.print.select_from_album()
        self.print.pick_a_photo()
        self.print_setting.select_printer(self.printer_name_2)
        self.print_setting.select_print()
        # in the print page also can check the home page
        # self.driver.press_key_home()
        # self.wechat.goto_mp()
        self.mphome.verify_printer_exist(self.printer_name)
        self.mphome.verify_printer_new_icon(self.printer_name)
        self.mphome.verify_printer_new_icon(self.printer_name_2, invisible=True)