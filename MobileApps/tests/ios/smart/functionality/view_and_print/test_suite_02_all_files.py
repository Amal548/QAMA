import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
import MobileApps.libs.ma_misc.conftest_misc as c_misc

pytest.app_info = "SMART"

class Test_Suite_01_HP_Smart_Files(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")
        cls.sys_config = ma_misc.load_system_config_file()
        try:
            cls.fc.go_home(stack=cls.stack)
            cls.fc.dismiss_tap_here_to_start()
        except Exception:
            attachment_root_path = c_misc.get_attachment_folder()
            c_misc.save_source_and_publish(cls.driver, attachment_root_path)
            c_misc.save_screenshot_and_publish(cls.driver, "{}/screenshot_{}.png".format(attachment_root_path, request.node.name))
            raise

    def test_01_all_files_recents_ui(self):
        """
        C27655028
        """
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].select_allow_access_to_photos_popup()
        self.fc.fd["files"].verify_my_photos_files_screen()
        self.fc.fd["files"].select_all_files_image()
        self.fc.fd["files"].select_save_to_my_iphone(raise_e=False)
        self.fc.fd["files"].select_recent_button()
        self.fc.fd["files"].verify_hp_smart_recent_screen()
        self.fc.fd["files"].verify_browse_button()
        self.fc.fd["files"].verify_recent_button()

    def test_02_browse_icloud_drive_folder(self):
        """
        C27655029- Verify the iCloud Drive screen 
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.dismiss_tap_here_to_start()
        self.fc.fd["home"].select_documents_icon()
        self.fc.fd["photos"].select_allow_access_to_photos_popup()
        self.fc.fd["files"].verify_my_photos_files_screen()
        self.fc.fd["files"].select_all_files_image()
        self.fc.fd["files"].select_save_to_my_iphone(raise_e=False)
        self.fc.fd["files"].select_browse_button()
        self.fc.fd["files"].verify_on_my_iphone()
        self.fc.fd["files"].select_browse_button()
        self.fc.fd["files"].select_icloud_button()
        self.fc.fd["files"].verify_icloud_screen()
        self.fc.fd["files"].verify_icloud_ui_elements_screen()
