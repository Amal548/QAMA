from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import GOOGLE_PHOTOS
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
import pytest

pytest.app_info = "SMART"


class Test_Suite_02_My_Photos(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]

    @pytest.mark.parametrize("album", ["jpg", "jpeg", "jpeg_undersized", "jpeg_oversized"])
    def test_01_my_photos_share_gmail(self, album):
        """
        Descriptions:
            1.Load Photos screen via tiles or icon
            2. Click on My Photos
            3. Select first photo in album which name is corresponding image type
            4. Make a share via gmail

        Expected Result:
            Verify:
                3.Landing Page:
                         - Edit button
                4. At Landing Page for sharing tab,
                         - file name text box is not display
                         - Share button display
                    Then, Share gmail successul
        """
        self.__load_my_photos_screen(from_tile=False)
        self.local_photos.select_album_photo_by_index(album_name=album)
        self.preview.verify_preview_nav(is_edit=True)
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.fc.flow_preview_share_via_gmail(self.email_address,
                                            "{}_{}".format(self.test_01_my_photos_share_gmail.__name__, album),
                                             from_email=self.email_address)

    @pytest.mark.parametrize("album", ["jpg", "jpeg", "jpeg_undersized", "jpeg_oversized"])
    def test_02_my_photos_print(self, album):
        """
        Descriptions:
            1.Load Photos screen via tiles or icon
            2. Click on My Photos
            3. Select first photo in album which name is corresponding image type
            4. Make a printing job

        Expected Result:
            Verify:
                3.Landing Page:
                    - Edit button
                4. Printing job should be successful
        """
        self.__load_my_photos_screen(is_printer=True, from_tile=True)
        self.local_photos.select_album_photo_by_index(album_name=album)
        if "novelli" in self.p.p_obj.projectName:
            self.preview.verify_print_size_screen()
            self.preview.select_print_size_btn(self.preview.PRINT_SIZE_4x6_STANDARD)
        self.fc.flow_preview_make_printing_job(self.p)

    @pytest.mark.parametrize("album", ["jpeg_corrupted", "bmp", "gif", "webp"])
    def test_03_my_photos_select_unsupported_photo(self, album):
        """
        Descriptions:
            1.Load Photos screen via tiles or icon
            2. Click on My Photos
            3. Select first photo in album which name is corresponding image type

        Expected Result:
            Verify:
                3. Verify Select a Photo screen
        """
        self.__load_my_photos_screen(from_tile=True)
        self.local_photos.select_album_photo_by_index(album_name=album)
        self.local_photos.verify_select_photo_screen()

    @pytest.mark.parametrize("back_btn", ["mobile", "app"])
    def test_04_my_photos_back_key(self, back_btn):
        """
        Description:
            1. Load Photos screen from Home
            2. Click on My Photos button
            3. Click Back key (app/mobile device)
        Expected Result:
            3. Photos screen
        """
        self.__load_my_photos_screen(from_tile=False)
        self.__select_back(back_btn)
        self.files_photos.verify_files_photos_screen()

    def test_05_my_photos_select_a_photo_cancel_btn(self):
        """
        Description:
            1. Load Photos screen from Home
            2. Click on My Photos button
            3. Click any album to Select a Photo screen
            4. Click on X button on Select a photo screen

        Expected Result:
            4. Verify Select a photo screen with album lists
        """
        self.__load_my_photos_screen(from_tile=True)
        self.local_photos.select_album(album_name="jpg")
        self.local_photos.select_cancel_btn()
        self.local_photos.verify_select_photo_screen()

    @pytest.mark.parametrize("back_btn", ["mobile", "app"])
    def test_06_preview_from_my_photos_back_btn(self, back_btn):
        """
        Description:
            1. Load Photos screen from Home
            2. Click on My Photos
            3. Select any supported image to go to Landing Page
            4. At Preview screen, click on back (app/mobile device)
        Expected Result:
            4. Files & Photos screen
        """
        # Make sure, not affect by previous test as this one no need to connect to printers
        self.fc.reset_app()
        self.__load_my_photos_screen(from_tile=False)
        self.local_photos.select_album_photo_by_index(album_name=GOOGLE_PHOTOS.JPEG)
        self.preview.verify_preview_nav(is_edit=True)
        self.__select_back(back_btn)
        self.files_photos.verify_files_photos_screen()

    # -----------------         PRIVATE FUNCTIONS       ---------------------------------
    def __load_my_photos_screen(self, is_printer=False, from_tile = True):
        """
        From Home screen:
            - Select target printer if is_printer = True
            - Click on Print Photos tile for photos icon
            - Click on MY Photos button
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        if is_printer:
            self.fc.flow_home_select_network_printer(self.p)
        if from_tile:
            self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        else:
            self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)

    def __select_back(self, back_btn):
        """
        Click on Back button from mobile back key or back button on Scan screen
        :param mobile_back: True: mobile back key, False: back btn on Scan screen
        """
        if back_btn == "mobile":
            self.driver.press_key_back()
        else:
            self.fc.select_back()
