import os
import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.google_sheets.google_sheets import GoogleSheets
from selenium.common.exceptions import NoSuchElementException


pytest.app_info = "GOOGLE_SHEETS"
# Sometimes HPPS plugin does not render excel files.
class Test_Suite_HPPS_google_sheets(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup ,load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup

        self.google_sheets = GoogleSheets(self.driver)
        self.sys_config = ma_misc.load_system_config_file()
        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()
        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']
        self.printer_ip = self.printer_info['ip address']

    @pytest.mark.parametrize('file', os.environ.get("FILE_SELECTION_TYPE", const.GOOGLE_SHEETS.XLS_1).split(','))
    def test_01_google_sheets_system_ui(self, file):
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
                Step-3: Open 'Google Sheets'.
                Step-4: Select 'Search' from top of the screen.
                Step-5: Search for the file by name.
                Step-6: Click on 3-dot-menu button from right side of the desired file name.
                Step-7: Select 'Print'.
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
                Step 3:   Verify Google Sheets home screen.
                Step-4:   Verify search screen.
                Step-5:   Verify search result screen.
                Step-6:   Verify 3-dot-menu screen.
                Step-8.2: Verify System UI screen.
                Step-8.3: Verify 'All printers' screen.
                Step-8.5: Verify System UI preview screen with print button.
                Step-9:   Verify System UI print options screen.

        """

        self.google_sheets.open_google_sheets()
        self.google_sheets.verify_google_sheets_home()
        self.google_sheets.select_search()
        self.google_sheets.verify_search_screen()
        self.google_sheets.search_for_file_by_name(file)
        self.google_sheets.check_search_result_and_redo_the_search_if_needed(file_search=file)
        self.google_sheets.select_3dot_menu()
        self.google_sheets.verify_3dot_menu_screen()
        self.google_sheets.verify_print_menu()
        self.google_sheets.select_print()

        self.fc.open_and_select_printer_via_system_ui(self.printer_bonjour_name)
        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.set_printer_options_in_system_ui(file_type="document")
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)
