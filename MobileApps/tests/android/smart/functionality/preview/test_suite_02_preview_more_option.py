from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.resources.const.android.const import PACKAGE
pytest.app_info = "SMART"


class Test_Suite_02_Preview_More_Option(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.digital_copy = cls.fc.flow[FLOW_NAMES.DIGITAL_COPY]

    def test_01_more_option_from_scanner(self):
        """
        Description:
        1. Load to Hom screen
        2. Click on Add icon to access printers list
        3. Select a target printer
        4. Click on Printer Scan on Home screen
        5. Click on Scan button
        6. Click on More Option icon on Preview screen

        Expected Results:
        6. Verify More Option screen with:
           + Print Help
           + Print Format displays
        """
        self.__load_preview_screen()
        self.preview.select_more_option()
        self.preview.verify_more_option(print_format_invisible=False)

    @pytest.mark.parametrize("print_as_type", ["jpg", "pdf"])
    def test_02_more_option_print_format(self, print_as_type):
        """
        Description:
        1. Load to Hom screen
        2. Click on Add icon to access printers list
        3. Select a target printer
        4. Click on Scan tile on Home screen
        5. Click on Scan button
        6. Click on More Option screen
        7. Click on Print Format
        8. Click on Print as JPG (print_as_type = "jpg"):
        Or
           Click on Print as PDF (print_as_type = "pdf"):

      Expected Results:
        7. Verify Print Format screen with:
           + Print Format title
           + Print as JPG item
           + Print as PDF item
        8. Make sure app go back to Preview screen
        :param print_as_type:
        """
        self.__load_preview_screen()
        self.preview.select_option_print_format()
        self.preview.verify_print_format_screen()
        if print_as_type == "jpg":
            self.preview.select_print_as_jpg_btn()
        else:
            self.preview.select_print_as_pdf_btn()
        self.preview.verify_preview_nav()

    def test_03_more_option_from_photos(self):
        """
        Description:
        1. Load to Hom screen
        2. Click on View & Print on Home screen if from_source = "from_photo"
        3. Click on My Photo on View & Print screen
        4. Select a photo
        5. Click on More Option icon on Preview screen

        Expected Results:
        5. Verify More Option screen with:
           + Print Help
           + Print Format disappears (from_photo)
        """
        self.__load_preview_screen(from_scanner=False)
        self.preview.select_more_option()
        self.preview.verify_more_option(print_format_invisible=True)

    def test_04_print_help(self):
        """
        Description:
        1. Load to Hom screen
        2. Click on View & Print
        3. Click on My Photos
        4. Select a photo to Preview screen
        5. Click on More Option icon
        6. Click on Print Help item
        7. Check 2 boxes
        8. Check the 3rd boxes, and click on OK button

      Expected Results:
        6. Verify Print Help screen with:
           + 3 checkboxs
           + Title
        7. OK button isn't clickable
        8. Verify Preview screen
        """
        self.__load_preview_screen(from_scanner=False)
        self.preview.select_option_print_help()
        self.preview.verify_print_help_screen()
        self.preview.toggle_cb_on_print_help(self.preview.PRINT_PLUGIN_CB)
        self.preview.toggle_cb_on_print_help(self.preview.PRINTING_SETTINGS_CB)
        self.preview.verify_ok_button(is_enabled=False)
        self.preview.toggle_cb_on_print_help(self.preview.PRINTER_SELECT_CB)
        self.preview.verify_ok_button(is_enabled=True)
        self.preview.select_print_help_ok_btn()
        self.preview.verify_preview_nav()

    @pytest.mark.parametrize("link_name", ["open_google_play", "open_print_settings"])
    def test_05_print_help_link_verify(self, link_name):
        """
        Description:
        1. Load to Hom screen
        2. Click on View & Print
        3. Click on My Photos
        4. Select a photo to Preview screen
        5. Click on More Option icon
        6. Click on Print Help item
        7. Click on Links on Print Help screen:
           + Open Printing Settings link
           + Google Play link
      Expected Results:
        7. Verify the link we clicked
        :param link_name:
        """
        self.__load_preview_screen(from_scanner=False)
        self.preview.select_option_print_help()
        if link_name == "open_google_play":
            self.preview.select_link_on_print_help(self.preview.OPEN_GOOGLE_PLAY)
            self.digital_copy.verify_google_play_link()
        else:
            self.preview.select_link_on_print_help(self.preview.OPEN_PRINT_SETTINGS)
            assert (self.driver.get_current_app_activity()[0] == PACKAGE.SETTINGS), "Android Settings is not launching"

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_preview_screen(self, from_scanner=True):
        """
        1. Load App to Home screen
        2. Connect a target printer
        3. Click on Scan from Home screen
        4. Click on Scan button
        """
        self.fc.flow_load_home_screen()
        if from_scanner:
            self.fc.flow_home_scan_single_page(self.p, from_tile=True)
        else:
            self.fc.flow_home_load_photo_screen(self.p, from_tile=True)
            self.local_photos.select_album_photo_by_index(album_name="jpg")
            if "novelli" in self.p.p_obj.projectName:
                self.preview.verify_print_size_screen()
                self.preview.select_print_size_btn(self.preview.PRINT_SIZE_4x6_STANDARD)
        self.preview.verify_preview_nav()