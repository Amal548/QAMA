import pytest
import datetime
import os
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.ma_misc.excel import Excel
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "SMART"


class Test_Smart_Printer_Discovery(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Initialize and load flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printer = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]
        cls.pd = Excel(os.path.join(pytest.session_result_folder, "printer_discovery/android_smart.xls"))
        cls.pd.load_sheet("Android Smart Printer Discovery")

        # Define variable
        cls.date = str(datetime.datetime.now().strftime('%Y-%m-%d'))

        def clean_up_class():
            cls.pd.save()
            ma_misc.publish_to_junit(os.path.join(pytest.session_result_folder, "printer_discovery/android_smart.xls"))
        request.addfinalizer(clean_up_class)

    def test_android_smart_printer_discovery(self):
        """
        Description:
            - Load Home screen
            - Select target printer in Printer screen
            - Go to My Printer/Printer Information
            - Compare actual printer info(ip, name, and serial no) with the ones from app/printer info
        :param printer: actual printer information
        """
        printers = self.pd.load_printers_info()
        for i in range(5):
            self.pd.write_new_record(["Attemp: {}".format(i + 1), "", ""])
            for printer_info in printers:
                error_msg = ""
                try:
                    self.fc.flow_load_home_screen()
                    self.home.load_printer_selection()
                    self.printer.select_printer(printer_info["ip address"], timeout=60)
                    if self.home.verify_feature_popup(raise_e=False):
                        self.home.select_feature_popup_close()
                    self.home.verify_home_nav()
                    self.home.verify_loaded_printer()
                    self.home.load_printer_info()
                    self.printer_settings.select_printer_setting_opt(self.printer_settings.PRINTER_INFO)
                    from_app = self.printer_settings.get_printer_info()
                    if printer_info["ip address"] != from_app["ip address"] or printer_info["serial number"] != from_app["serial number"]:
                        raise ValueError("Printer Info miss-match:\n\t Expect: {}\n\t Actual: {}".format(printer_info, from_app))
                    test_result = "Pass"
                # Handle for all error:
                except Exception as ex:
                    test_result = "Fail"
                    error_msg = ex.message if getattr(ex, "message", False) else  ex.msg
                self.pd.write_new_record([self.date, "{} ({})".format(printer_info["bonjour name"], printer_info["ip address"]),
                                        test_result, error_msg])
            self.pd.save()