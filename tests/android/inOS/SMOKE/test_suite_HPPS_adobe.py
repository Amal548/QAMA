import os
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.adobe.adobe import Adobe

pytest.app_info = "ADOBE"
class Test_Suite_HPPS_adobe(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup ,load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup
        self.adobe = Adobe(self.driver)
        self.sys_config = ma_misc.load_system_config_file()
        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()
        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']


    @pytest.mark.parametrize('file', [const.ADOBE.PDF_1, const.TEST_DATA.PDF_3PAGES_WORD_IMAGE, const.TEST_DATA.PDF_5PAGES_EMAIL, const.TEST_DATA.PDF_6PAGES_FORMATTED_DOC])
    def test_01_adobe_system_ui(self, file):
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
                 Step-3: Open 'Adobe Acrobat Reader'.
                 Step-4: Select Search tab from options.
                 Step-5: Select 'Search' from top of the screen.
                 Step-6: Search for the file by name.
                 Step-7: Select file.
                 Step-8: Click on 3-dot-menu button from right side of the desired file name.
                 Step-9: Select 'Print'.
                 Step-10: Open and select printer via System UI.
                         1) Agree and accept terms and conditions if present.
                         2) Accept all access alerts.
                         3) Select 'All printers' from dropdown.
                         4) Select 'Search' from top of the scrren.
                         5) Search and select printer by name.
                 Step-11: Select collapse button.
                 Step-12: Set System UI printer options, such as 'Copies', 'Colour' etc.
                 Step-13: Select 'More options'
                 Step-14: Set values for more options such as 'Borderless' etc.
                 Step-15: Go back to the Printer preview screen.
                 Step-16: Select 'Print' and verify the results.
                         1) Select 'Print'.
                         2) Select 'Ok' for document passing.
                         3) Get printing results.
                 Step-17: Go to home screen.Samsung S7
            Expected Result:
                 Step 3:   Verify 'Adobe Acrobat Reader' home screen.
                 Step-5:   Verify search screen.
                 Step-7:   Verify editor screen.
                 Step-8:   Verify 3-dot-menu screen.
                 Step-8.2: Verify System UI screen.
                 Step-8.3: Verify 'All printers' screen.
                 Step-8.5: Verify System UI preview Samsung S7screen with print button.
                 Step-9:   Verify System UI print options screen.
        """
        self.driver.push_file(ma_misc.get_abs_path(const.TEST_DATA.DOCUMENTS_PDF_FOLDER + "/" + file), const.TEST_DATA.MOBILE_DOWNLOAD + "/documents/pdf/" +file)
        self.adobe.open_adobe_and_search_for_file(file)
        self.adobe.check_search_result_and_redo_the_search_if_needed(file_search=file)
        self.adobe.open_file()
        self.adobe.verify_editor_screen()
        self.adobe.select_3dot_menu()
        self.adobe.verify_3dot_menu_screen()
        self.adobe.select_print()

        self.fc.open_and_select_printer_via_system_ui(self.printer_bonjour_name)

        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.set_printer_options_in_system_ui(file_type="document")
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)

    @pytest.mark.parametrize('file', [const.FILE_LIST.PDF])
    def test_02_adobe_trap_door(self, file):
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
                 Step-3: Open 'Adobe Acrobat Reader'.
                 Step-4: Select 'Search' tab from options.
                 Step-5: Select 'Search' from top of the screen.
                 Step-6: Search for the file by name.
                 Step-7: Select file.
                 Step-8: Click on 'Share' button (from bottom of the screen).
                 Step-9: Select 'HP Print Service' plugin from the trapdoor.
                         1) Agree and accept terms and conditions if present.
                         2) Accept all access alerts.
                         3) Click on 'Search' from top right corner of the screen.
                         4) Select the printer.
                 Step-10: Set values for printer options like 'Color', 'Copies' etc.
                 Step-11: Scroll and select 'More Options' from trapdoor.
                 Step-12: Set values for more options such as 'Scaling', 'Color Mode' etc.
                 Step-13: Go back to the Printer preview screen.
                 Step-14: Select 'Print' and verify the results.
                         1) Select 'Print'.
                         2) Open android notifications from the notification drawer.
                         3) Select the Print notification.
                         4) Get printing results.
                 Step-15: Go to home screen.
            Expected Result:
                 Step-1.3:  Verify Printing screen.
                 Step-1.5:  Verify HP print service screen.
                 Step-2.1:  Verify more options list.
                 Step-2.2:  Verify 'Printing Settings' screen.
                 Step 3:    Verify 'Adobe Acrobat Reader' home screen.
                 Step-5:    Verify search screen.
                 Step-7:    Verify editor screen.
                 Step-9.2:  Verify 'Select Printer' screen.
                 Step-9.4:  Verify Printer Preview screen.
                 Step-13:   Verify printer preview screen.
                 Step-14.3: Verify print job screen.
        """
        self.adobe.open_adobe_and_search_for_file(file)
        self.adobe.check_search_result_and_redo_the_search_if_needed(file_search=file)
        self.adobe.open_file()
        self.adobe.verify_editor_screen()
        self.adobe.select_share_copy()
        self.fc.flow["intermediate_flow"].select_app(self.driver.return_str_id_value("trapdoor_hpps_txt", project="hpps", flow="trap_door"))

        self.fc.open_and_select_printer_via_trapdoor(self.printer_bonjour_name)
        self.fc.set_printer_options_in_trap_door(file_type="document")
        self.fc.flow["trap_door"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["trap_door"].verify_printer_preview_screen()
        self.fc.select_print_and_verify_results_for_trapdoor(self.p, self.printer_bonjour_name)