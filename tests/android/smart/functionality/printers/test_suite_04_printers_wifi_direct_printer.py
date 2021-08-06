from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SPL.libs.networkcfg.connectionInfo import Adapter
import pytest
import time

pytest.app_info = "SMART"

class Test_Suite_04_Printers_WiFi_Direct_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Skip this test suite for Android 10 and up
        if int(cls.driver.driver_info["platformVersion"].split(".")[0]) > 9:
            pytest.skip("Skip this test suites since it is not supported on Android 10 and up")

        #Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]

        #Define the variable
        cls.p.toggle_wifi_direct(on=True)
        Adapter("wifi1", cls.p.p_con).showPassPhrase= "true"
        cls.wifi_direct_info = cls.p.get_wifi_direct_information()

    def test_01_wifi_direct_printer_ui(self):
        """
        Description:
         1. Load Home screen
         2. Click on big "+" icon on Home screen
         3. Click on Looking for Wi-Fi Direct Printers? Button
         4. Click on Continue button
         5. Allow App Permission

        Expected Result:
         3. Verify Search for printer? Popup screen:
            + Title
            + Continue button
         5. Verify Wi-Fi Direct Printer screen with below point:
            + Title
            + Wi-Fi Direct Printer list
        """
        self.__load_wifi_direct_printers_screen()
        self.printers.dismiss_search_for_printers_popup()
        self.printers.verify_wifi_direct_printers_screen()

    def test_02_search_invalid_wifi_direct_printer(self):
        """
        Description:
         1. Load to Wi-Fi Direct Printers screen
         2. Click on Search icon
         3. Enter a invalid printer name

        Expected Result:
         3. Empty lists with keyword
        """
        self.__search_printer_screen("invalid_name")
        self.printers.verify_search_printers_screen(is_empty=True, is_wifi_direct=True)

    def test_03_search_via_valid_printer_name(self):
        """
        Description:
         1. Load to Wi-Fi Direct Printers screen
         2. Click on Search icon
         3. Enter a valid printer name
        Expected result:
         3. At least one printer display on WiFi printers list
        """
        self.__search_printer_screen(self.wifi_direct_info["name"].split("HP")[1])
        num_of_wifi_direct_printers = self.printers.count_printers(wifi_direct=True)
        assert (num_of_wifi_direct_printers >= 1), "There's no printers on list on the wifi direct printers list."

    def test_04_select_wifi_direct_printer(self):
        """
        Description:
         1. Load to Wi-Fi Direct Printers screen
         2. Select a printer from the Wi-Fi printer list

        Expected result:
         2. Verify Wi-Fi Printer screen with below points:
            + Title
            + Printer's Wi-Fi Direct name
            + Button: Connect to the printer
        """
        self.__select_printer(self.wifi_direct_info["name"])
        self.printers.verify_connect_printers_wifi_direct_screen(is_disconnect=False)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_wifi_direct_printers_screen(self):
        """
        - Load Home screen.
        - click on big + button if no printer connected before,
              otherwise clicking on small "+" button on Home screen
        - click on Looking for Wi-Fi Direct Printers? button
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.load_printer_selection()
        self.printers.select_looking_for_wifi_direct_printers()

    def __search_printer_screen(self, keyword):
        """
        - Load Home screen.
        - click on big + button if no printer connected before,
              otherwise clicking on small "+" button on Home screen
        - click on Looking for Wi-Fi Direct Printers? button
        :param keyword:
        """
        self.__load_wifi_direct_printers_screen()
        self.printers.select_search_icon()
        self.printers.search_printer(key_word=keyword)

    def __select_printer(self, printer_info):
        """
        - Load Home screen.
        - click on big + button if no printer connected before,
              otherwise clicking on small "+" button on Home screen
        - click on Looking for Wi-Fi Direct Printers? button
        :param keyword:
        """
        self.__load_wifi_direct_printers_screen()
        self.printers.verify_wifi_direct_printers_screen()
        self.printers.select_printer(printer_info=printer_info, wifi_direct=True)

    def __type_wifi_direct_printer_pwd(self, pwd):
        """
        - Click connect to the printer button
        - Verify the wireless connect popup screen
        - Type pwd
        :param pwd:
        """
        self.printers.verify_connect_printers_wifi_direct_screen()
        self.printers.select_connect_to_the_printer()
        self.printers.connect_to_wifi_direct_printer(pwd=pwd)
