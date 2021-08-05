import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"



class Test_Suite_06_Photo_Edit(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.online_photos = cls.fc.flow[FLOW_NAMES.ONLINE_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]

        # Define variables
        cls.dropbox_username = cls.fc.get_dropbox_acc()["username"]
        cls.dropbox_pwd = cls.fc.get_dropbox_acc()["password"]
        cls.gdrive_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]

        # Cleanup
        def clean_up_class():
            cls.fc.flow_dropbox_logout()
        request.addfinalizer(clean_up_class)

    def test_01_edit_facebook_photos(self, photo_count=5):
        """
        Description: C17023778
         1. Launch Smart app
         2. Select View & Print Navbar Button
         3. Sign into Facebook(if not already signed in)
         4. Select Facebook
         5. Select "Mobile Uploads" album
         6. Select 5 images
         7. Edit each image
        Expected Results:
         1. All preview images have changed
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if self.files_photos.verify_cloud_not_login(self.files_photos.FACEBOOK_TXT, raise_e=False):
            self.files_photos.select_cloud_item(self.files_photos.FACEBOOK_TXT)
            self.online_photos.select_fb_account("QA MobiAuto", raise_e=False)
            if self.online_photos.verify_fb_login_confirmation_screen(raise_e=False):
                self.online_photos.select_fb_confirmation_continue()
        if not self.online_photos.verify_fb_album_screen(raise_e=False):
            self.files_photos.select_cloud_item(self.files_photos.FACEBOOK_TXT)
        self.online_photos.verify_fb_album_screen()
        self.online_photos.select_album("Mobile Uploads")
        self.online_photos.select_multiple_photos(photo_count)
        self.online_photos.select_next()
        self.preview.verify_preview_nav()
        self.preview.verify_multiple_pages(str(photo_count))
        self.__verify_and_edit_all_preview_photos()

    def test_02_load_google_drive_photo(self):
        """
        Description: C17023778
         1. Launch Smart app
         2. Select View & Print Navbar Button
         3. Sign into Google Drive(if not already signed in)
         4. Select Google Drive
         5. Select "testdata_cloud/images/jpg/bow.jpg"
           - google drive doesnt support multiple image selection
        Expected Results:
         1. One image is loaded into preview
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if self.files_photos.verify_cloud_not_login(self.files_photos.GOOGLE_DRIVE_TXT, raise_e=False):
            self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
            self.online_docs.verify_gdrive_choose_account_popup()
            self.online_docs.select_gdrive_gmail_account(self.gdrive_username)
            self.online_docs.allow_gdrive_access(raise_e=False)
        self.files_photos.verify_cloud_added_account(self.files_photos.GOOGLE_DRIVE_TXT, self.gdrive_username)
        self.files_photos.select_cloud_item(self.files_photos.GOOGLE_DRIVE_TXT)
        self.online_docs.verify_online_docs_screen(self.online_docs.GOOGLE_DRIVE_TXT)
        self.online_docs.select_file("testdata_cloud/images/jpg/bow.jpg")
        self.preview.verify_preview_nav()
        self.preview.verify_multiple_pages(str(1))

    def test_03_load_dropbox_photo(self):
        """
        Description: C17023778
         1. Launch Smart app
         2. Select View & Print Navbar Button
         3. Sign into Dropbox(if not already signed in)
         4. Select Dropbox
         5. Select "testdata_cloud/images/jpg/bow.jpg"
           - dropbox doesnt support multiple image selection
        Expected Results:
         1. One image is loaded into preview
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        if self.files_photos.verify_cloud_not_login(self.files_photos.DROPBOX_TXT, raise_e=False):
            self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
            self.fc.flow_dropbox_log_in(self.dropbox_username, self.dropbox_pwd)
        self.files_photos.verify_cloud_added_account(self.files_photos.DROPBOX_TXT, self.dropbox_username)
        self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
        self.online_docs.verify_online_docs_screen(self.online_docs.DROPBOX_TXT)
        self.online_docs.select_file("testdata_cloud/images/jpg/bow.jpg")
        self.preview.verify_preview_nav()
        self.preview.verify_multiple_pages(str(1))

    def __verify_and_edit_all_preview_photos(self):
        """Helper method to loop through and edit all loaded images and verify that they changed"""
        photo_count = self.preview.get_preview_image_count()
        for i in reversed(range(1, photo_count + 1)):  # starts on last image
            self.preview.swipe_to_preview_image_index(i)
            original_img = saf_misc.load_image_from_base64(self.preview.screenshot_img_preview())
            # perform edits
            self.preview.select_preview_image_opts_btn(self.preview.EDIT_BTN, image_index=i)
            self.edit.select_edit_main_option(self.edit.ADJUST)
            self.edit.select_edit_child_option(self.edit.BRIGHTNESS, direction="right", check_end=False, str_id=True)
            self.edit.verify_and_swipe_adjust_slider()
            self.edit.select_edit_done()  # finish brightness edit
            self.edit.select_edit_done()  # finish editing
            # verify image changed
            edited_img = saf_misc.load_image_from_base64(self.preview.screenshot_img_preview())
            assert saf_misc.img_comp(original_img, edited_img) > 0.06, "Preview image should not match original image"
        