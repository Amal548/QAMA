from time import sleep

import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview
from SAF.misc import saf_misc

pytest.app_info = "SMART"


class Test_Suite_06_Transform_Functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")

        # Printer variables
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])

    def test_01_verify_transform_settings_func(self):
        """
        Verify Transform screen, Resize and Rotate functionality-
                        C17117642, C25341392
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.fd["preview"].go_to_print_preview_pan_view(pan_view=False)
        preview_before_edit = self.fc.fd["preview"].preview_img_screenshot()
        self.fc.fd["preview"].select_transform_options(Preview.TRANSFORM_TXT)
        transform_img_before_edit = self.fc.fd["preview"].preview_img_screenshot()
        self.fc.fd["preview"].select_transform_options(Preview.TF_RESIZE_TXT,
                                                       tf_option_select=Preview.TF_RESIZE_MOVE_OPTIONS[1])
        self.fc.fd["preview"].select_done()
        image_after_resize_edit = self.fc.fd["preview"].preview_img_screenshot()
        assert saf_misc.img_comp(transform_img_before_edit, image_after_resize_edit) > 0
        self.fc.fd["preview"].select_transform_options(Preview.TF_ROTATE_TXT,
                                                       tf_option_select=Preview.TF_ROTATE_OPTIONS[2])
        self.fc.fd["preview"].select_done()
        image_after_rotate_edit = self.fc.fd["preview"].preview_img_screenshot()
        self.fc.fd["preview"].select_done()
        assert saf_misc.img_comp(transform_img_before_edit, image_after_rotate_edit) > 0
        assert saf_misc.img_comp(image_after_resize_edit, image_after_rotate_edit) > 0
        preview_after_edit = self.fc.fd["preview"].preview_img_screenshot()
        assert saf_misc.img_comp(preview_before_edit, preview_after_edit) > 0

    def test_02_transform_cancel_func(self):
        """
           Verify cancel button functionality on transform screen - C27099488
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.fd["preview"].go_to_print_preview_pan_view(pan_view=False)
        sleep(1)
        preview_before_edit = self.fc.fd["preview"].preview_img_screenshot()
        self.fc.fd["preview"].select_transform_options(Preview.TRANSFORM_TXT)
        sleep(1)
        transform_pre_edit_img = self.fc.fd["preview"].preview_img_screenshot()
        self.fc.fd["preview"].select_transform_options(Preview.TF_RESIZE_TXT,
                                                       tf_option_select=Preview.TF_RESIZE_MOVE_OPTIONS[3])
        self.fc.fd["preview"].select_done()
        sleep(1)
        transform_after_resize = self.fc.fd["preview"].preview_img_screenshot()
        sleep(1)
        assert saf_misc.img_comp(transform_pre_edit_img, transform_after_resize) > 0
        self.fc.fd["preview"].select_transform_options(Preview.TF_ROTATE_TXT,
                                                       tf_option_select=Preview.TF_ROTATE_OPTIONS[2])
        self.fc.fd["preview"].select_done()
        sleep(1)
        transform_after_rotate = self.fc.fd["preview"].preview_img_screenshot()
        sleep(1)
        assert saf_misc.img_comp(transform_after_resize, transform_after_rotate) > 0
        self.fc.fd["preview"].select_cancel()
        sleep(1)
        preview_after_cancel = self.fc.fd["preview"].preview_img_screenshot()
        assert saf_misc.img_comp(preview_before_edit, preview_after_cancel) == 0
