import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

pytest.app_info = "SMART"


class Test_suite_01_ios_smart_photos_ga(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup):
        cls = cls.__class__

        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        cls.fc.go_home(verify_ga=True)

    def test_01_photos_max_ga(self):
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].select_allow_access_to_photos_popup()
        self.fc.fd["files"].verify_my_photos_files_screen()
        self.fc.fd["files"].select_my_photos_button_on_files_screen()
        self.fc.fd["photos"].verify_my_photos_screen()
        self.fc.fd["photos"].select_all_photos()
        self.fc.fd["photos"].verify_all_photos_screen()
        self.fc.fd["photos"].select_all_photos_option_select()
        self.fc.fd["photos"].select_multiple_photos()
        self.fc.fd["photos"].verify_multi_selected_photos_screen()
        self.fc.fd["photos"].select_cancel()
        self.fc.fd["photos"].verify_all_photos_screen()
        self.fc.fd["photos"].select_back_button()
        self.fc.fd["photos"].verify_my_photos_screen()
        self.fc.fd["photos"].select_back_button()
        self.fc.fd["files"].verify_my_photos_files_screen()

    def test_02_facebook_max_ga(self):
        self.fc.go_hp_smart_files_screen_from_home()
        self.fc.fd["files"].select_facebook_on_files_screen()
        self.fc.fd["files"].select_allow_access_to_facebook_popup()
        self.fc.fd["facebook"].handle_facebook_is_already_login()
        self.fc.fd["facebook"].verify_facebook_photos_albums_screen()
        self.fc.fd["facebook"].select_time_line_album()
        self.fc.fd["facebook"].verify_photos_album()
        self.fc.fd["facebook"].select_multiple_photos_select_option()
        self.fc.fd["photos"].select_multiple_photos()
        self.fc.fd["facebook"].verify_multiple_selected_photos_screen()
        self.fc.fd["facebook"].select_cancel()
        self.fc.fd["facebook"].select_back()
        self.fc.fd["facebook"].verify_facebook_photos_screen()
        self.fc.fd["facebook"].select_back()
        self.driver.swipe(direction="up")
        self.fc.fd["files"].verify_files_screen()
        self.fc.fd["files"].select_edit()
        self.fc.fd["files"].verify_x_button_on_files_screen()
        self.fc.fd["files"].select_x_button_to_delete()
        self.fc.fd["files"].verify_facebook_account_deleted_popup()
        self.fc.fd["files"].select_remove_on_popup()
        self.fc.fd["files"].verify_files_screen()







