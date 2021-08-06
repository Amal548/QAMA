from MobileApps.libs.flows.ios.smart.preview import Preview
import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_03_My_Photos(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.preview = cls.fc.fd["preview"]
        cls.photos = cls.fc.fd["photos"]
        cls.home = cls.fc.fd["home"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home()

    def test_01_verify_my_photos_ui(self):
        """
        C27655031- My Photos- UI
        """
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_my_photos()
        self.photos.verify_my_photos_screen()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT, click=False)
        self.photos.select_navigate_back()
    
    def test_02_my_photos_select_images(self):
        """
        C27655032 - My Photos- Select Image
        """
        self.home.select_documents_icon()
        self.photos.select_allow_access_to_photos_popup(allow_access=True)
        self.photos.select_my_photos()
        self.photos.verify_an_element_and_click(self.photos.RECENT_PHOTOS_TEXT)
        self.photos.verify_select_photos_btn()
        self.photos.verify_photos_screen()
        self.photos.select_multiple_photos(end=4)
        self.photos.verify_multi_selected_photos_screen()
        self.photos.select_next_button()
        self.preview.verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.preview.verify_toolbar_icons()
        self.preview.select_navigate_back()
        self.photos.verify_photos_screen()
        self.photos.select_multiple_photos(end=4)
        self.photos.select_cancel()
        self.photos.verify_photos_screen()

