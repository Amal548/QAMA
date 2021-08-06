from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import FACEBOOK_ALBUM
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE
import logging
import pytest

pytest.app_info = "SMART"


class Test_Suite_01_Facebook(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.online_photos = cls.fc.flow[FLOW_NAMES.ONLINE_PHOTOS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.fb_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.CLOUD_ACCOUNT))["facebook"]["account_01"][
            "username"]
        cls.fb_password = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.CLOUD_ACCOUNT))["facebook"]["account_01"][
            "password"]

    def test_01_facebook_login(self):
        """
        Descriptions:
            1. Reset app as first time launch
            2. Load Home screen
            3. Click on Photos icon
            4. Click on Facebook btn
            5. Click on Continue as QA button (or any btn which accept this verification)

        Expected Result:
            Verify:
                3. Photos screen
                4. Verified FB account display
                5. Photos screen with logged in FB account
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_cloud_not_login(self.files_photos.FACEBOOK_TXT)
        self.files_photos.select_cloud_item(self.files_photos.FACEBOOK_TXT)
        self.online_photos.select_fb_account("QA MobiAuto", raise_e=False)
        if self.online_photos.verify_fb_login_confirmation_screen(raise_e=False):
            self.online_photos.select_fb_confirmation_continue()
        elif self.online_photos.verify_fb_login_screen(raise_e=False):
            self.online_photos.login_to_fb(self.fb_username, self.fb_password)
        if self.online_photos.verify_fb_album_screen(raise_e=False):
            self.driver.press_key_back()
        self.files_photos.verify_cloud_added_account(self.files_photos.FACEBOOK_TXT, "QA MobiAuto")

    def test_02_facebook_select_over_10_photos(self):
        """
        Descriptions:
            1. Load Fb screen (if it is not logged in to any account, log in it)
            2. Select an album
            3. Select over 10 photos

        Expected Result:
            Verify:
                3. Facebook screen with only 10 selections and Next button
        """
        self.__load_facebook_album_detail_screen()
        self.online_photos.select_multiple_photos(11)
        self.online_photos.verify_over_10_selections_screen()

    @pytest.mark.parametrize("number_photos", ["one_photo", "multiple_photo"])
    def test_03_facebook_share_gmail(self, number_photos):
        """
        Descriptions:
            1. Load Fb screen (if it is not logged in to any account, log in it)
            2. Select one/multiple photo in one album
            3. Process a Share via Gmail at Landing Page

        Expected Result:
            Verify:
                3. Sharing via Gmail is successful
        """
        self.__load_facebook_album_detail_screen()
        if number_photos == "one_photo":
            self.online_photos.select_single_photo()
        else:
            self.online_photos.select_multiple_photos(3)
            self.online_photos.select_next()
        self.preview.verify_preview_nav(is_edit=True)
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.fc.flow_preview_share_via_gmail(self.email_address,
                                                  "{}".format("{}_{}".format(self.test_03_facebook_share_gmail.__name__, number_photos)),
                                             from_email=self.email_address)

    @pytest.mark.parametrize("number_photos", ["one_photo", "multiple_photo"])
    def test_04_facebook_print(self, number_photos):
        """
        Descriptions:
            1. Load Fb screen (if it is not logged in to any account, log in it)
            2. Select one/multiple in one album
            3. Process a printing job at Landing Page

        Expected Result:
            Verify:
                3. Printing is successful (check printer and app)
        """
        self.__load_facebook_album_detail_screen(is_printer=True)
        jobs = 1
        if number_photos == "one_photo":
            self.online_photos.select_single_photo()
        else:
            self.online_photos.select_multiple_photos(2)
            self.online_photos.select_next()
            jobs = 2
        self.fc.flow_preview_make_printing_job(self.p, jobs=jobs)

    @pytest.mark.parametrize("back_btn", ["mobile", "app"])
    def test_05_facebook_back_from(self, back_btn):
        """
        Description:
          1. Load to Photos screen with logged in FB account
          2. Select any a album
          3. Click on Back button on FB album detail's screen
          4. Click on Back button on FB album screen
             Or Click on Back button from mobile device

        Expected Result:
          4. Verify view & print screen with FB account login
        """
        self.__load_facebook_album_detail_screen()
        self.fc.select_back()
        self.online_photos.verify_fb_album_screen()
        if back_btn == "mobile":
            self.driver.press_key_back()
        else:
            self.fc.select_back()
        self.files_photos.verify_cloud_added_account(self.files_photos.FACEBOOK_TXT, "QA MobiAuto")

    def test_06_facebook_logged_out(self):
        """
        Description:
            1. Load to Photos screen with logged in FB account
            2. Long press "Facebook"
            3. Click on Log out
        Expected Result:
            Verify for following steps:
                2. Verify Facebook Log out screen
                3. Verify Photos screen without Facebook logged in
        :return:
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.load_logout_popup(self.files_photos.FACEBOOK_TXT)
        self.files_photos.logout_cloud_item(self.files_photos.FACEBOOK_TXT)
        self.files_photos.verify_cloud_not_login(self.files_photos.FACEBOOK_TXT)

    # -----------------         PRIVATE FUNCTIONS       ---------------------------------
    def __load_facebook_album_detail_screen(self, is_printer=False):
        """
        From Home screen:
            - Select target printer
            - Click on photos icon
            - Login to Facebook account if it is not logged in.
            - Click on Facebook button
            - Select an album
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        if is_printer:
            self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_cloud_item(self.files_photos.FACEBOOK_TXT)
        self.online_photos.select_fb_account("QA MobiAuto", raise_e=False)
        if self.online_photos.verify_fb_login_confirmation_screen(raise_e=False):
            self.online_photos.select_fb_confirmation_continue()
        if not self.online_photos.verify_fb_album_screen(raise_e=False) and self.files_photos.verify_files_photos_screen(raise_e=False):
            self.files_photos.select_cloud_item(self.files_photos.FACEBOOK_TXT)
        self.online_photos.verify_fb_album_screen()
        self.online_photos.select_album(FACEBOOK_ALBUM.MOBILE_UPLOADS)