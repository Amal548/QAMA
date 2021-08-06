import pytest
import datetime
import os
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.common.printer_discovery.printer_discovery import PrinterDiscovery
from SAF.misc.excel import Excel
from MobileApps.libs.ma_misc import ma_misc
from selenium.common.exceptions import NoSuchElementException, TimeoutException

pytest.app_info = "SMART"


class Test_Smart_Printer_Discovery(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup

        # Initialize and load flows
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.flow["home"]
        cls.printer = cls.fc.flow["printers"]
        cls.pd = PrinterDiscovery()
        cls.excel = Excel(os.path.join(pytest.session_result_folder, "printer_discovery/ios_smart.xls"))
        if not cls.excel.load_sheet("iOS Smart Printer Discovery", raise_e=False):
            cls.excel.add_sheet("iOS Smart Printer Discovery")

        # Define variable
        cls.date = str(datetime.datetime.now().strftime('%Y-%m-%d'))

        def clean_up_class():
            cls.excel.save()
            ma_misc.publish_to_junit(os.path.join(pytest.session_result_folder, "printer_discovery/ios_smart.xls"))
        request.addfinalizer(clean_up_class)

    def test_asmart_printer_discovery(self):
        """
        Description:
            - Load Home screen
            - Select target printer in Printer screen
            - Go to Printer Settings/Printer Information
            - Compare actual printer info(ip, name, and serial no) with the ones from app/printer info
        :param printer: actual printer information
        """
        printers = self.pd.load_printers_info()
        for i in range(5):
            self.excel.write_new_record(["Attemp: {}".format(i + 1), "", ""])
            for printer_info in printers:
                error_msg = ""
                try:
                    self.fc.go_home()
                    self.home.select_get_started_by_adding_a_printer()
                    self.printer.verify_printers_nav()
                    self.printer.select_printer_from_printer_list(printer_info["ip address"], timeout=30)
                    self.home.verify_home(ga=False)
                    self.home.verify_loaded_printer()
                    test_result = "Pass"
                # Handle for all error:
                except (NoSuchElementException, TimeoutException) as ex:
                    test_result = "Fail"
                    error_msg = ex.msg
                self.excel.write_new_record([self.date, "{} ({})".format(printer_info["bonjour name"], printer_info["ip address"]),
                                             test_result, error_msg])
            self.excel.save()