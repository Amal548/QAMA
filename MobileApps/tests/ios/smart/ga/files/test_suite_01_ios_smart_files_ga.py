import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "SMART"



class Test_suite_01_ios_smart_files_ga(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        cls.fc.go_home(verify_ga=True)

    def test_01_files_max_ga(self):


        self.fc.go_hp_smart_files_screen_from_home()

        self.fc.fd["files"].create_a_folder()
        self.fc.fd["files"].delete_a_folder_by_name()
        self.fc.fd["files"].move_folder_into_this_folder()
        self.fc.fd["files"].select_my_files_back_btn()
        self.fc.fd["files"].my_files_select_search_cancel()
        self.fc.fd["files"].select_my_files_back_btn()
        self.fc.fd["files"].my_files_select_search_cancel()
        self.fc.fd["files"].verify_hp_smart_files_home_screen()
        self.fc.fd["files"].create_a_folder(folder_name="TestFolderRename")
        self.fc.fd["files"].rename_and_delete_folder_moved_folder()
        self.fc.fd["files"].select_my_files_back_btn()
        self.fc.fd["files"].verify_files_screen()
        self.fc.fd["files"].select_and_verify_all_files()
        self.fc.fd["box"].login_cloud_box()
        self.fc.fd["files"].verify_files_screen()
        self.fc.fd["files"].delete_cloud_account_by_name()