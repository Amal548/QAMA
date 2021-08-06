from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest
import logging
from MobileApps.resources.const.android.const import FACEBOOK_ALBUM
import time

pytest.app_info = "SMART"

class Test_Suite_01_GA_Photo(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.photo = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.online_photos = cls.fc.flow[FLOW_NAMES.ONLINE_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]

        #Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress
        cls.instagram_acc = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["instagram_account"][
            "username"]

        cls.instagram_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["instagram_account"][
            "password"]

        cls.fb_username_title = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "fb_username_title"]


    def test_01_ga_photo(self):
        """
        Steps:
        - Launch HP Smart
        - Verify Home screen with big "+" on printer area
        - Click on big "+" button
        - Verify Printer screen
        - Selected target printer on the list (not from search icon)
        - Verify Home Screen with printer connected
        - Click on Photo icon on Navigation bar
        - Verify App Permission screen
        - Click on Allow button on App Permission screen
        - Verify Photo screen
        - Click on Instagram icon
        - Verify Instagram login screen
        - Input username and password
        - Click on Log in button
        - Verify Photo screen with Instagram account logged in success
        - Click on Facebook icon
        - Verify Facebook album screen
        - Select album "Mobile Uploads"
        - Verify Facebook album details screen
        - Long press and select 2 images
        - Verify album details screen with 2 images selected
        - Click on Exit button on the left top of album details
        - Long press and select 11 images
        - Verify album detail screen with 11 images selected
        - Click on Exit button on the left top of album detail screen
        - Click on Back button
        - Verify Facebook album screen
        - Click on Back button
        - Verify Photo screen
        - Click on Instagram
        - Verify Instagram details screen
        - Long press and select 2 images
        - Verify album detail screen with 2 images selected
        - Click on Exit button on the left top of album details screen
        - Click on Back button
        - Verify Photo screen
        - Long press Instagram account
        - Verify Log out screen
        - Click on Log out button
        - Long press Facebook account
        - Verify Log out screen
        - Click Log out screen
        - Close App
        """
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer()
        self.home.select_big_add_icon()
        self.printers.verify_printers_screen()
        self.printers.select_printer(self.printer_ip, is_searched=True, keyword=self.printer_ip)
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()
        self.home.select_nav_photos(is_permission=True)
        self.photo.verify_photos_screen()
        self.photo.select_account_type(acc_type=self.photo.ACC_INSTAGRAM, ga=True)
        time.sleep(10)
        self.online_photos.verify_instagram_login_screen()

        self.online_photos.instagram_login(username=self.instagram_acc, pwd=self.instagram_pwd)
        self.photo.verify_photo_login_acc(acc_type=self.photo.ACC_INSTAGRAM, acc_name=self.instagram_acc, ga=True)
        self.photo.select_account_type(acc_type=self.photo.ACC_FACEBOOK, ga=True)
        time.sleep(30)
        if self.online_photos.verify_fb_login_confirmation_screen(raise_e=False):
            self.online_photos.select_fb_confirmation_continue()
        self.photo.verify_photo_login_acc(acc_type=self.photo.ACC_FACEBOOK, acc_name=self.fb_username_title, ga=True)
        self.photo.select_account_type(acc_type=self.photo.ACC_FACEBOOK, ga=False)
        self.online_photos.verify_online_photos_screen(acc_type=self.online_photos.FACEBOOK_TXT)
        self.online_photos.select_album(FACEBOOK_ALBUM.MOBILE_UPLOADS)
        self.online_photos.verify_album_detail_screen(acc_type=self.online_photos.FACEBOOK_TXT)
        self.online_photos.select_multiple_photos(num=2)
        self.online_photos.verify_multi_selection_screen()
        self.online_photos.select_x_icon()
        self.online_photos.select_multiple_photos(num=11)
        self.online_photos.verify_multi_selection_screen()
        self.online_photos.verify_over_10_selections_screen()
        self.online_photos.select_x_icon()
        self.fc.select_back()
        self.online_photos.verify_online_photos_screen(acc_type=self.online_photos.FACEBOOK_TXT)
        self.fc.select_back()
        self.photo.verify_photos_screen()
        self.photo.select_account_type(acc_type=self.photo.ACC_INSTAGRAM, ga=False)
        self.online_photos.verify_online_photos_screen(acc_type=self.online_photos.INSTAGRAM_TXT)
        self.online_photos.select_multiple_photos(num=2)
        self.online_photos.verify_multi_selection_screen()
        self.online_photos.select_x_icon()
        self.fc.select_back()
        self.photo.verify_photos_screen()
        self.photo.long_press_acc(acc_type=self.photo.ACC_INSTAGRAM)
        self.photo.logout_photo_account(self.photo.ACC_INSTAGRAM)
        self.photo.long_press_acc(acc_type=self.photo.ACC_FACEBOOK)
        self.photo.logout_photo_account(self.photo.ACC_FACEBOOK)