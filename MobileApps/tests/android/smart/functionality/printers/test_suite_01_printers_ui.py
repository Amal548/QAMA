from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest


pytest.app_info = "SMART"

class Test_Suite_01_Printers_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]

        # Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]

    def test_01_printer_ui(self):
        """
        Description:
         1. Load Home screen
         2. Click on big "+" or small "+" icon on Home screen

        Expected Results:
         2. Verify below points:
           + Navigation bar: back button, printers title, search icon
           + +Add Printer icon
           + Looking for Wi-Fi Direct Printers? Button
        """
        self.__load_printers_screen()
        self.printers.verify_printers_screen()

    def test_02_search_invalid_printer(self):
        """
        Description:
         1. Load Home screen
         2. Click on Big + button if printer not connected, otherwise clicking small + button
         3. Click on Searching icon on printer lists screen
         4. Enter a invalid printer ip or name

        Expected Result:
         4. There's no printers on the list with keyboard
        """
        self.__search_printer_screen("invalid_name")
        self.printers.verify_search_printers_screen(is_empty=True)

    def test_03_select_printer(self):
        """
        Description:
         1. Load Home screen
         2. Click on big "+" icon if printer not connected, otherwise clicking small + button
         3. Select a target printer on printer list

        Expected Result:
         3. Verify Home screen with printer connected
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_select_network_printer(self.p)
        self.home.verify_loaded_printer()

    @pytest.mark.parametrize("keyword", ["partial_name", "full_name", "ip"])
    def test_04_select_printer_via_searching_by(self, keyword):
        """
        Description:
         1. Load Home screen
         2. Click on big "+" icon if printer not connected, otherwise clicking small + button
         3. Click on Search icon
         4. Enter a valid printer name
         5. Select a target printer on printer list

        Expected Result:
         4. At least one available printer displays on printers list
         5. Verify Home screen with printer connected
        """
        searched_str = {"partial_name": self.printer_name[0:self.printer_name.rfind("[")],
                        "full_name": self.printer_name,
                        "ip": self.printer_ip}
        self.__search_printer_screen(searched_str[keyword])
        number_of_printer = self.printers.count_printers()
        if (keyword == "partial_name" or keyword == "ip") and number_of_printer < 1:
            raise AssertionError("There's no printers on list.")
        elif keyword == "full_name" and number_of_printer != 1:
            raise AssertionError("There's no printers or more than 1 printer on the lists.")
        self.__select_back_btn()
        self.printers.select_printer(self.printer_ip, is_searched=True, keyword=searched_str[keyword])
        self.home.verify_loaded_printer()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_printers_screen(self):
        """
        - Load Home screen.
        - click on big + button if no printer connected before,
          otherwise clicking on small "+" button on Home screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.load_printer_selection()

    def __search_printer_screen(self, key_word):
        """
        - Click on Search icon on Printers screen
        - Verify search screen
        : parameter: keyword
        """
        self.__load_printers_screen()
        self.printers.select_search_icon()
        self.printers.search_printer(key_word = key_word)

    def __select_back_btn(self):
        """
        Click back button until Printers screen popup, maxmium 2 times
        """
        for _ in range(2):
            self.fc.select_back()
            if self.printers.verify_printers_screen(raise_e=False):
                return True
        raise AssertionError("printers screen didn't display after clicking back button 2 times")
