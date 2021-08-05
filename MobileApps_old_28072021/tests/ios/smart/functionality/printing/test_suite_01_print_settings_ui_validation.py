import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer, logging
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_01_Print_Settings_UI_Validation(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

        # Printer variables
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(printer_ip=cls.p.get_printer_information()["ip address"])

    def test_01_verify_print_settings_ui_elements(self):
        """
        Verifies ui elements of print preview pan screen  - C17056075
        :return:
        """
        # General Setup
        self.fc.select_a_google_drive_file_and_go_to_print_preview(file_name="2pages")
        self.fc.fd["preview"].verify_printer_name_displayed(self.p.get_printer_information()["bonjour name"])
        if self.fc.fd["preview"].verify_an_element_and_click(Preview.TWO_SIDED, click=False) is False:
            Preview.PRINT_SETTINGS_UI_ELEMENTS.remove(Preview.TWO_SIDED)
            logging.debug("Two Sided option not displayed/applicable to testing printer")
        self.fc.fd["preview"].verify_array_of_elements(Preview.PRINT_SETTINGS_UI_ELEMENTS)

    def test_02_verify_paper_setting_for_ipp_printers(self):
        """
        Verifies only applicable paper size displayed on Paper screen- C16845762
        :return:
        """
        # General Setup
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.fd["preview"].go_to_print_preview_pan_view()
        # Validation
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PAPER)
        assert len(self.fc.fd["preview"].get_options_listed(Preview.PRINT_SETTING_OPTIONS)) >= 1
        self.fc.fd["preview"].select_navigate_back()
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_03_verify_page_range_screen_ui(self):
        """
        Verifies ui elements of page range screen
        verify default selection of pages on page range screen- C16932516, C16932517
        :return:
         """
        # General Setup
        self.fc.select_a_google_drive_file_and_go_to_print_preview(file_name="2pages")
        assert self.fc.fd["preview"].get_option_selected_value(Preview.PAGE_RANGE) == 'All'
        self.fc.fd["preview"].verify_an_element_and_click(Preview.PAGE_RANGE)
        # Validation
        assert set(self.fc.fd["preview"].get_options_listed(Preview.PR_SCREEN_OPTIONS_UI)) == set(
            Preview.PAGE_RANGE_OPTIONS)
        assert self.fc.fd["preview"].verify_pages_selected(Preview.PAGE_RANGE_OPTIONS[0]) is not False
        assert self.fc.fd["preview"].verify_pages_selected(Preview.PAGE_RANGE_OPTIONS[1]) is not False

    def test_04_verify_print_preview_ui(self):
        """
        Verifies print preview ui elements - C25341390
        """
        # General Setup
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.fd["preview"].go_to_print_preview_pan_view(pan_view=False)
        self.fc.fd["preview"].verify_print_preview_ui_elements(self.p.get_printer_information()["bonjour name"])

    def test_05_verify_transform_screen_ui(self):
        """
        Verify Transform, Resize and Rotate screens UI Elements -
                                 C19415079, C17153674, C17117419
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.navigate_to_transform_screen()
        self.fc.fd["preview"].verify_array_of_elements(Preview.TRANSFORM_SCREEN_UI_ELEMENTS)
        self.fc.fd["preview"].verify_array_of_elements([Preview.PREVIEW_IMAGE, Preview.CANCEL_BUTTON, Preview.DONE_BUTTON])
        self.fc.fd["preview"].select_transform_options(Preview.TF_RESIZE_TXT)
        assert set(self.fc.fd["preview"].get_options_listed(Preview.TF_COLLECTION_VIEW)) == set(
            Preview.TF_RESIZE_MOVE_OPTIONS)
        self.fc.fd["preview"].select_cancel()
        self.fc.fd["preview"].select_transform_options(Preview.TF_ROTATE_TXT)
        assert set(self.fc.fd["preview"].get_options_listed(Preview.TF_COLLECTION_VIEW)) == set(
            Preview.TF_ROTATE_OPTIONS)

    def test_06_verify_reorder_screen_ui(self):
        """
        Verify Reorder screens UI Elements - C17023764
        """
        no_of_photos = 2
        self.fc.select_multiple_photos_to_preview(no_of_photos)
        self.fc.fd["preview"].verify_an_element_and_click(Preview.REORDER_BUTTON)
        self.fc.fd["preview"].verify_preview_screen_title(Preview.REORDER_BUTTON)
        self.fc.fd["preview"].verify_array_of_elements([Preview.CANCEL_BUTTON, Preview.DONE_BUTTON])
        assert self.fc.fd["preview"].get_print_page_collection_view_cell() == ['1', '2']
        # assert len(self.fc.fd["preview"].verify_delete_page_x_icon()) == no_of_photos
