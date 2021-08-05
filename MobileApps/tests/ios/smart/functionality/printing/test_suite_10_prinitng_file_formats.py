import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_10_Printing_File_Formats(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.p = load_printers_session
        cls.home = cls.fc.fd["home"]
        cls.preview = cls.fc.fd["preview"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.file_name = "4pages"
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])
    
    @pytest.mark.parametrize("document_format",["pdf","txt","docx","xlsx"])
    def test_01_verify_printing_different_document_formats(self, document_format):
        """
        C27655278 - PDF
        C27655279 - TXT
        C27655280 - DOC
        C27655282 - XLS
        """    
        self.fc.navigate_to_google_drive_in_files()
        self.fc.select_file_in_google_drive(file_type=document_format, file_name=self.file_name)
        self.preview.verify_preview_screen()
        self.fc.fd["preview"].dismiss_print_preview_coach_mark()
        self.fc.select_print_button_and_verify_print_job(self.p)
    
    @pytest.mark.parametrize("image_format",["jpg","png","bmp","tif"])
    def test_02_verify_printing_different_image_formats(self, image_format):
        """
        C27655274 - JPG
        C27655275 - PNG
        C27655276 - BMP
        C27655277 - TIFF
        """
        if image_format == "jpg":
            file_name = "fish"
        elif image_format == "png":
            file_name = "pikachu"
        elif image_format == "tif":
            file_name = "green_automation"
        elif image_format == "bmp":
            file_name = "test_bmp"
        else:
            file_name = "motorbike"
        self.fc.navigate_to_google_drive_in_files()
        self.fc.select_file_in_google_drive(file_type=image_format, file_name=file_name)
        self.preview.verify_preview_screen()
        self.fc.fd["preview"].dismiss_print_preview_coach_mark()
        self.fc.select_print_button_and_verify_print_job(self.p)