from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from SPL.libs.networkcfg.connectionInfo import Adapter
import pytest

pytest.app_info = "SMART"

class Test_Suite_05_Printer_Info(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]

        # turn off Wifi Direct
        cls.p.toggle_wifi_direct(on=False)

    def test_01_printer_info(self):
        """
        Description:
            1/ Load Home screen 
            2/ Connect to target printer
            3/Click on Printer Settinload_printergs tile on Home screen
            4/ Click on Printer Information on My Printer screen
            5/ Get all information about printer on screen. Then, compare with the information from printer

        Expected Result:
            5/ They should match.
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_select_network_printer(self.p)
        self.home.load_printer_info()
        self.printer_settings.verify_my_printer(self.p.get_printer_information()["bonjour name"])
        self.printer_settings.select_printer_setting_opt(self.printer_settings.PRINTER_INFO)

        # Check Printer information on App with information on printer
        is_equal = {"status": True, "message": ""}
        info_from_app = self.printer_settings.get_printer_info()
        info_from_printer = self.p.get_printer_information()
        if not self.__verify_info(info_from_app, info_from_printer):
            is_equal["status"] = False
            is_equal["message"] = "From App: {}\n  From Printer: {}".format(info_from_app, info_from_printer)
        if not is_equal["status"]:
            raise InfoMismatchException("There are incorrect info in Printer Info: \n  {}".format(is_equal["message"]))

    def test_02_printer_network_info(self):
        """
        Descriptions:
            1/ Press Back key of mobile device. If current screen is not My Printer, then implement step 1 to step 3 of test 01.
            2/ Click on Network Information on My Printer screen
            3/ Get all information about printer's network oin app. Then, compare them with the information from printer
        Expected Result:
            3/ They should match.
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_select_network_printer(self.p)
        self.home.load_printer_info()
        self.printer_settings.verify_my_printer(self.p.get_printer_information()["bonjour name"])
        self.printer_settings.select_printer_setting_opt(self.printer_settings.NETWORK_INFO)

        # Compare Wireless Information
        is_equal = {"status": True, "message": ""}
        info_from_app = self.printer_settings.get_wireless_info()
        info_from_printer = self.p.get_wireless_network_information()
        if not self.__verify_info(info_from_app, info_from_printer):
            is_equal["status"] = False
            is_equal["message"] = "Wireless Info:\n From App: {}\n  From Printer: {}".format(info_from_app, info_from_printer)
        if not is_equal["status"]:
            raise InfoMismatchException("There are incorrect info in:\n{}".format(is_equal["message"]))

    # **************************************************************
    #                     PRIVATE FUNCTIONS                        *
    # **************************************************************

    def __verify_info(self, from_app, from_printer):
        """
        Verify all information of printer on App with the one on printer
        :param from_app: list of information that is gotten from App
        :param from_printer: list of information that is gotten from Printer
        :return: True if is equal. Otherwise, False
        """
        is_equal = True
        for key in from_app:
            if key == "state":
                if from_app[key].lower() != from_printer[key].lower():
                    is_equal = False
                    break
            else:
                if from_app[key] != from_printer[key]:
                    is_equal = False
                    break
        return is_equal

class InfoMismatchException(Exception):
    pass
