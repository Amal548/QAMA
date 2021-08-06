import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_03_Verification_Image_Export_To_Pdf(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.preview = cls.fc.fd["preview"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        #Navigate to home
        cls.fc.go_home(button_index=1, stack=cls.stack)
        
        def clean_up_function():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_function)

    def test_01_verify_image_export_to_different_size(self):
        """
        verify image export with Actual size - C27655346
        verify image export to Large size - C27655347
        verify image export with Medium size - C27655348
        verify image export to pdf with Small size - C27655349
        """
        self.fc.create_and_save_file_using_camera_scan_and_go_home(file_name="test_file")
        self.fc.select_a_file_and_go_to_preview_screen(file_type="jpg", file_name="test_file.")

        file_size_list = ["small", "medium", "large", "actual"]
        file_names = []
        
        for file_size in file_size_list:
            if file_size == "small":
                scale = self.preview.FILE_SIZE_SMALL
            elif file_size == "meduim":
                scale = self.preview.FILE_SIZE_MEDIUM
            elif file_size == "actual":
                scale = self.preview.FILE_SIZE_ACTUAL
            else:
                scale = self.preview.FILE_SIZE_LARGE
            # export image to pdf   
            self.preview.select_toolbar_icon(self.preview.SHARE_AND_SAVE_BTN)
            self.preview.rename_file("test_file_" + file_size)
            file_names.append("test_file_" + file_size + ".pdf")
            self.preview.select_file_type("PDF")
            self.preview.select_navigate_back()
            self.preview.verify_file_type_selected("PDF", raise_e=True)
            self.preview.verify_an_element_and_click(self.preview.FILE_SIZE, click=True)
            self.preview.verify_an_element_and_click(scale, click=True)
            self.fc.fd["preview"].select_navigate_back()
            self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
            self.fc.fd["share"].verify_share_popup()
            self.fc.fd["share"].select_save_to_hp_smart()
        self.preview.select_navigate_back()
        self.fc.fd["home"].select_cancel()
        self.fc.go_hp_smart_files_screen_from_home()
        for file_name in file_names:
            # Validate file saved with selected format
            self.fc.fd["files"].verify_file_name_exists(file_name)