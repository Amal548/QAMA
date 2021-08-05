import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.google_chrome.google_chrome import GoogleChrome
from selenium.common.exceptions import NoSuchElementException, WebDriverException

import logging


pytest.app_info = "GOOGLE_CHROME"
class Test_Suite_HPPS_Google_Chrome(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup ,load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup

        self.google_chrome = GoogleChrome(self.driver)

        self.sys_config = ma_misc.load_system_config_file()
        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()
        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']
        self.printer_ip = self.printer_info['ip address']


    def test_01_google_chrome_system_ui(self):
        """
            Description:
            Before executing the script, make sure that the phone and printer are connected to same wifi network (eg.rdfishbowl24).
                Step-1: Install and enable HPPS:
                         1) Install HPPS from Play Store.
                         2) Open Android settings.
                         3) Search for Printing settings.
                         4) Remove old print jobs.
                         5) Select HP INC.
                         6) Turn on HP Print service plugin, if turned off.
                         7) Click on 'Ok' to allow the document to pass through he service.
                Step-2: Set HPPS prtocol:
                         1) Click on 'More' button.
                         2) Click on 'Printing Settings'.
                         3) Click on 'Advanced Settings'.
                         4) Select the desired print protocol type.
                         5) Click on 'Back Button'.
                Step-3: Open 'Google Chrome'.
                Step-4: Select 'Search' from top of the screen.
                Step-5: Enter a valid url, if  not default is wiki
                Step-6: Click on 3-dot-menu button from right side of the screen.
                Step-7: Select  share and then select 'Print'.
                Step-8: Open and select printer via System UI.
                         1) Agree and accept terms and conditions if present.
                         2) Accept all access alerts.
                         3) Select 'All printers' from dropdown.
                         4) Select 'Search' from top of the screen.
                         5) Search and select printer by name.
                Step-9:  Select collapse button.
                Step-10: Set System UI printer options, such as 'Copies', 'Color' etc.
                Step-11: Select 'More options'
                Step-12: Set values for more options such as 'Borderless' etc.
                Step-13: Go back to the Printer preview screen.
                Step-14: Select 'Print' and verify the results.
                         1) Select 'Print'.
                         2) Select 'Ok' for document passing.
                         3) Get printing results.
                Step-15: Go to home screen.

            Expected Result:
                Step 3:   Verify Google Chrome home screen.
                Step-6:   Verify 3-dot-menu screen.
                Step-8.2: Verify System UI screen.
                Step-8.3: Verify 'All printers' screen.
                Step-8.5: Verify System UI preview screen with print button.
                Step-9:   Verify System UI print options screen.

        """
        self.google_chrome.open_google_chrome()
        self.google_chrome.verify_google_chrome_home_screen()
        self.google_chrome.select_search_box()
        self.google_chrome.enter_url_and_go_to_website()
        self.google_chrome.select_3_dot_menu()
        self.google_chrome.verify_3_dot_menu_screen()
        self.google_chrome.select_share_from_3_dot_menu_options()
        self.google_chrome.press_print_button_and_redo_share_to_print_if_needed(flow=self.fc.flow["intermediate_flow"])

        self.fc.open_and_select_printer_via_system_ui(self.printer_bonjour_name, timeout=30)
        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.set_printer_options_in_system_ui(file_type=None)
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)

