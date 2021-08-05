import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc

pytest.app_info = "SMART"

class Test_Suite_01_Image_Export_To_Other_Formats(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.preview = cls.fc.fd["preview"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(stack=cls.stack)

        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    def test_01_verify_share_as_original_functionality(self):
        """
            verify 'Share as Original' functionality - C27655335 
        """ 
        file_name = 'scan_image_from_camera_JPG'
        self.fc.create_and_save_file_using_camera_scan_and_go_home(file_name)
        self.fc.select_a_file_and_go_to_preview_screen(file_name = file_name,file_type='.jpg')
        self.fc.fd["preview"].select_toolbar_icon(self.preview.SHARE_AND_SAVE_BTN)
        # Turning on the share as original button
        self.fc.fd["preview"].toggle_share_as_original_btn()
        assert self.fc.fd["preview"].verify_an_element_and_click(self.preview.FORMAT, click=False) is False
        assert self.fc.fd["preview"].verify_an_element_and_click(self.preview.FILE_SIZE, click=False) is False
        # Turning off the share as original button
        self.fc.fd["preview"].toggle_share_as_original_btn()
        assert self.fc.fd["preview"].verify_an_element_and_click(self.preview.FORMAT, click=False) is not False
        assert self.fc.fd["preview"].verify_an_element_and_click(self.preview.FILE_SIZE, click=False) is not False
        # Turning on the share as original button
        self.fc.fd["preview"].toggle_share_as_original_btn()
        self.fc.fd["preview"].select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.fc.fd["share"].select_save_to_hp_smart()
        self.fc.fd["preview"].select_navigate_back()
        self.fc.fd["home"].select_cancel()
        self.fc.fd["files"].verify_file_name_exists(file_name + "_1.jpg")

    def test_02_verify_image_export_to_pdf(self):
        """
        verify image export to pdf - C27655339
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.save_file_to_hp_smart_files_and_go_home('scan_image_from_camera_PDF',self.preview.SHARE_AND_SAVE_BTN
                                                        , file_type="Basic PDF", go_home=False)
        self.fc.go_hp_smart_files_screen_from_home(select_tile=False)
        self.fc.fd["files"].verify_file_name_exists("scan_image_from_camera_PDF.pdf")

    @pytest.mark.parametrize("image_format",["png","tif","heif"])
    def test_03_verify_export_image_to_other_formats(self, image_format):
        """
        verify image export from PNG to other formats - C27655336
        verify image export from TIF to other formats - C27655337
        verify image export from HEIF to other formats - C27655338
        """
        if image_format == "png":
            file_name = "pikachu"
        elif image_format == "tif":
            file_name = "green_automation"
        else:
            file_name = "motorbike"
        self.fc.navigate_to_google_drive_in_files()
        self.fc.select_file_in_google_drive(file_type=image_format, file_name=file_name)
        self.preview.dismiss_feedback_pop_up()
        self.preview.select_toolbar_icon(self.preview.SHARE_AND_SAVE_BTN)
        file_types = ["JPG", "PNG","PDF", "TIF"]
        file_names = []
        for file_type in file_types:
            file_name = 'format_'+ image_format + "_to_" + file_type
            self.preview.rename_file(file_name)
            self.preview.select_file_type(file_type)
            self.preview.select_navigate_back()
            self.preview.verify_file_type_selected(file_type, raise_e=True)
            self.preview.select_button(self.preview.SHARE_AND_SAVE_BTN)
            self.fc.fd["share"].verify_share_popup()
            self.fc.fd["share"].select_save_to_hp_smart()
            file_names.append(file_name + "." + file_type.lower())
            print(file_names)
            self.preview.select_toolbar_icon(self.preview.SHARE_AND_SAVE_BTN)
        self.fc.go_hp_smart_files_screen_from_home()
        for file_name in file_names:
            # Validate file saved with selected format
            self.fc.fd["files"].verify_file_name_exists(file_name)

