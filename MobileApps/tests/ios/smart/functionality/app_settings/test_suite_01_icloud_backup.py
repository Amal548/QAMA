import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*

pytest.app_info = "SMART"

class Test_Suite_01_Back_Up_To_iCloud(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.preview = cls.fc.fd["preview"]
    # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()

    @pytest.fixture(scope="function", autouse="true")
    def fresh_install(self, request):
        self.driver.wdvr.reset()
        self.fc.go_home()

        def clean_up_class():
            self.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    def test_01_verify_backup_icloud_ui(self):
        """
        C1718605 Precondition: iCloud setting turned on
        navigate to app settings -> back up to icloud, verify UI
        """
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_backup_to_icloud_cell()
        self.fc.fd["app_settings"].verify_backup_to_icloud_ui()

    def test_02_verify_icloud_disable_popup(self):
        """
        C17181607 Precondition: preexisting files stored in iCloud and HP smart app
        verify popup after disabling backup to icloud switch
        """
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_backup_to_icloud_cell()
        self.fc.fd["app_settings"].verify_backup_to_icloud_ui()
        self.fc.fd["app_settings"].toggle_switch("backup_icloud_switch", True)
        self.fc.fd["app_settings"].verify_icloud_sync_popup()

    def test_03_do_not_disable_sync(self):
        """
        C17181609 Precondition: preexisting files stored in iCloud and HP smart app
        verify selecting 'Do Not Disable Sync option' does not turn off switch
        """
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_backup_to_icloud_cell()
        self.fc.fd["app_settings"].verify_backup_to_icloud_ui()
        self.fc.fd["app_settings"].toggle_switch("backup_icloud_switch", True)
        self.fc.fd["app_settings"].verify_icloud_sync_popup()
        self.fc.fd["app_settings"].select_do_not_disable_sync()
        self.fc.fd["app_settings"].verify_backup_to_icloud_ui()
        assert self.driver.get_attribute("backup_icloud_switch", "value") == '1'

    def test_04_delete_from_iphone(self):
        """
        C17181610 Precondition: preexisting files stored in iCloud and HP smart app
        verify selecting 'Delete from my iPhone' clears the HP Smart Files
        """
        file_name = self.test_04_delete_from_iphone.__name__
        self.generate_test_image(file_name)
        self.fc.go_to_home_screen()
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_backup_to_icloud_cell()
        self.fc.fd["app_settings"].verify_backup_to_icloud_ui()
        self.fc.fd["app_settings"].toggle_switch("backup_icloud_switch", True)
        self.fc.fd["app_settings"].verify_icloud_sync_popup()
        self.fc.fd["app_settings"].select_delete_documents()
        self.fc.fd["app_settings"].verify_backup_to_icloud_ui()
        self.fc.go_to_home_screen()
        self.fc.go_hp_smart_files_screen_from_home()
        assert self.fc.fd["files"].is_empty_screen() is True

    def test_05_keep_on_iphone(self):
        """
        C17181608 Precondition: preexisting files stored in iCloud and HP smart app
        verify selecting 'Keep on my iPhone' does not delete files
        """
        file_name = self.test_05_keep_on_iphone.__name__
        self.generate_test_image(file_name)
        self.fc.go_to_home_screen()
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_backup_to_icloud_cell()
        self.fc.fd["app_settings"].verify_backup_to_icloud_ui()
        self.fc.fd["app_settings"].toggle_switch("backup_icloud_switch", True)
        self.fc.fd["app_settings"].verify_icloud_sync_popup()
        self.fc.fd["app_settings"].select_keep_documents()
        self.fc.fd["app_settings"].verify_backup_to_icloud_ui()
        self.fc.go_to_home_screen()
        self.fc.go_hp_smart_files_screen_from_home()
        self.fc.fd["files"].verify_file_name_exists("{}.jpg".format(file_name))

    def generate_test_image(self, file_name: str):
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.fd["camera"].verify_camera_btn()
        self.fc.multiple_manual_camera_capture(1)
        self.fc.fd["preview"].select_toolbar_icon(self.fc.fd["preview"].SHARE_AND_SAVE_TEXT)
        self.fc.save_file_to_hp_smart_files_and_go_home(file_name, self.preview.SHARE_SAVE_BTN)
        self.fc.go_hp_smart_files_screen_from_home()
        self.fc.fd["files"].verify_file_name_exists("{}.jpg".format(file_name))


