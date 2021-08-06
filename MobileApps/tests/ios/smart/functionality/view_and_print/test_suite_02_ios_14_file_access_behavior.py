import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_02_Ios_14_File_Access_Behavior(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # check for ios 14  
        if cls.driver.platform_version != '14':
            pytest.skip('Skipped because test specific for iOS 14')
        cls.preview = cls.fc.fd["preview"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack)

    def test_01_verify_access_button_my_photos_screen(self):
        """
        C27805646 - Access button on My Photos screen (iOS 14)
        C27805647 - Verify behavior after tapping on Access button (iOS 14)
        """
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].click_select_photos_option()
        self.fc.fd["photos"].select_multiple_photos(end=3)
        self.fc.fd["photos"].select_done()
        self.fc.fd["photos"].select_my_photos()
        self.fc.fd["photos"].select_access_btn()
        self.fc.fd["photos"].verify_allow_photos_access_page()
    
    def test_02_verify_my_photos_with_no_access(self):
        """
        C27808827 - "My Photos" page with no access(iPhone iOS 14)
        C27808826 - Verify "Set Photo Access" redirection on "My Photos" page
        """
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].select_allow_access_to_photos_popup(allow_access=False)
        self.fc.fd["photos"].select_my_photos()
        self.fc.fd["photos"].verify_set_photo_access_btn()
        self.fc.fd["photos"].select_set_photos_access_btn()
        self.fc.fd["ios_system"].verify_hp_smart_title()
    
    def test_03_verify_back_btn_my_photos(self):
        """
        C27808830 - Verify back button on "My Photos" page
        """
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].select_allow_access_to_photos_popup(allow_access=False)
        self.fc.fd["photos"].select_my_photos()
        assert self.fc.fd["photos"].verify_access_btn(raise_e=False) is False
        self.fc.fd["photos"].select_navigate_back()
        self.fc.fd["files"].verify_view_and_print_screen()
    
    def test_04_verify_no_photo_count_visible(self):
        """
        C28159903 - Photos count is not shown for "My Photos" (iOS 14)
        """
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].select_allow_access_to_photos_popup(allow_access=False)
        assert self.fc.fd["photos"].get_photos_count_on_view_and_print_screen() == 0
    
    def test_05_verify_selected_photo_count(self):
        """
        C28159929 - Photos Count is shown for few selected images (iOS 14)
        """
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].click_select_photos_option()
        self.fc.fd["photos"].select_multiple_photos(end=3)
        self.fc.fd["photos"].select_done()
        assert self.fc.fd["photos"].get_photos_count_on_view_and_print_screen() == 3

    def test_06_verify_selected_all_photos_count(self):
        """
        C28159930 - Photos Count is shown for all selected images (iOS 14)
        """
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].select_allow_access_to_photos_popup(allow_access=True)
        assert self.fc.fd["photos"].get_photos_count_on_view_and_print_screen() >= 10
    
    def test_07_verify_my_photos_access_popup(self):
        """
        C28159904 - Behavior by tapping on "My Photos" folder 1-st time (iOS 14)
        """
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].verify_select_photos_btn()
        self.fc.fd["photos"].verify_allow_access_to_photos()
        self.fc.fd["photos"].verify_dont_allow_access_to_photos()
        self.fc.fd["photos"].select_allow_access_to_photos_popup(allow_access=True)
    
    def test_08_verify_select_photos_option_on_popup(self):
        """
        C28159905 - Behavior by tapping "Select Photos" option on pop-up (iOS 14)
        C28159906 - Behavior by tapping "Cancel" button on select image screen (iOS 14)
        """
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].click_select_photos_option() 
        self.fc.fd["photos"].verify_select_photos_page_after_popup()    
        self.fc.fd["photos"].select_cancel()
        self.fc.fd["files"].verify_view_and_print_screen()


        


        


