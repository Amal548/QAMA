from MobileApps.libs.flows.ios.smart.copy import Copy
import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*
pytest.app_info = "SMART"

class Test_Suite_01_Verify_Copy_Functionality(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.preview = cls.fc.fd["preview"]
        cls.copy = cls.fc.fd["copy"]
        cls.camera = cls.fc.fd["camera"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.COPY_ELEMENTS = Copy.COPY_PREVIEW_ELEMENTS
        cls.fc.go_home()
    
    def test_01_pop_up_for_allowing_access_to_camera_dont_allow(self):
        """
        C27655119 - Pop up for allowing access to camera (Don't Allow button)
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=False)
        self.copy.select_x_to_close()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_home()
        self.home.select_tile_by_name(HOME_TILES.TILE_COPY)
        self.camera.select_enable_access_to_camera_link()
        # set access in ios settings
        self.fc.fd["ios_system"].toggle_camera_switch(on=True)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.dismiss_tap_here_to_start()
        self.home.verify_home()
        self.home.select_tile_by_name(HOME_TILES.TILE_COPY)
        self.camera.verify_camera_screen()
    
    def test_02_copy_pop_up_when_printer_not_connected(self):
        """
        C27655118 - Copy- Pop up when printer is not connected
        """
        self.fc.go_to_home_screen()
        self.fc.remove_default_paired_printer()
        self.home.select_tile_by_name(HOME_TILES.TILE_COPY)
        self.home.select_ok()
        self.home.verify_home()
    
    def test_03_verify_pop_up_for_allowing_access_to_camera_ok_btn(self):
        """
        C27655129 - Pop up for allowing access to camera(OK button)
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_ui_elements_for_copy_functionality()
    
    def test_04_verify_copy_camera_screen_functionality(self):
        """
        C27655122 - Copy - Camera screen UI
        C27655130 - Copy - Camera screen functionality
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        # verify X button
        self.copy.select_x_to_close()
        self.home.close_smart_task_awareness_popup() 
        self.home.verify_home()
        self.home.select_tile_by_name(HOME_TILES.TILE_COPY)   
        #check for flash modes
        modes = [attr for attr in dir(FLASH_MODE) if not attr.startswith("__")]
        for mode in modes:
            self.camera.select_flash_mode(getattr(FLASH_MODE, mode))
            self.camera.verify_flash_mode_state(getattr(FLASH_MODE, mode))
        # check for object size options
        obj_sizes = [attr for attr in dir(OBJECT_SIZE) if not attr.startswith("__")]
        for size in obj_sizes:
            self.copy.select_object_size(getattr(OBJECT_SIZE, size))
        
    def test_05_verify_copy_preview_screen_functionality(self):
        """
        C27655121 - Copy- Preview screen
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        self.copy.verify_copy_preview_screen()
        self.copy.verify_array_of_elements(self.COPY_ELEMENTS)
        #verify number of copies functionality
        self.copy.select_number_of_copies(4)
        # Check for print RESIZE  options
        sizes = [attr for attr in dir(RESIZE) if not attr.startswith("__")]
        for size in sizes:
            self.copy.select_resize_in_digital_copy(getattr(RESIZE, size))
    
    def test_06_verify_pop_up_for_leaving_the_preview_screen(self):
        """
        C27655124 - Pop up for leaving the Preview screen
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        self.copy.select_navigate_back()
        self.copy.verify_copy_preview_screen_exit_popup()
        self.copy.select_no_option()
        self.copy.verify_copy_preview_screen()
        self.copy.select_navigate_back()
        self.copy.verify_copy_preview_screen_exit_popup()
        self.copy.select_yes()
        self.camera.verify_camera_screen()
    
    def test_07_verify_add_copy_functionality(self):
        """
        C27655126 - Copy - Add a copy
        """
        self.navigate_to_copy_screen()
        self.camera.select_allow_access_to_camera_on_popup(allow_access=True)
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        # Add copy
        self.copy.select_add_more_pages()
        self.camera.verify_camera_screen()
        self.copy.select_capture_button()
        total_pages = self.preview.get_no_pages_from_preview_label()
        assert total_pages == 2
        self.copy.select_start_black()
    
    def navigate_to_copy_screen(self):
        self.fc.go_to_home_screen()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.dismiss_tap_here_to_start()
        self.home.select_tile_by_name(HOME_TILES.TILE_COPY)        