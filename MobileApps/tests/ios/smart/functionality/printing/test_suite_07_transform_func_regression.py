import logging
from time import sleep

import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview
from SAF.misc import saf_misc

pytest.app_info = "SMART"


class Test_Suite_07_Transform_Func_regression(object):

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

    def test_01_verify_transform_resize_options_func(self):
        """
         verify  resize_options functionality:  C27655206, C27655218, C27655217
        """
        Preview.TF_RESIZE_MOVE_OPTIONS.remove(Preview.TF_RESIZE_MOVE_OPTIONS[0])
        transform_edit_failed = self.apply_and_verify_transform_options(Preview.TF_RESIZE_TXT,
                                                                        Preview.TF_RESIZE_MOVE_OPTIONS)
        assert len(transform_edit_failed) == 0, "Failed to selected following options {}".format(transform_edit_failed)
        logging.info("All transform Resize and Move options applied successfully")
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_02_verify_transform_resize_manual_func(self):
        """
         verify trasform resize manual functionality - C17117643
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.fd["preview"].go_to_print_preview_pan_view(pan_view=False)
        sleep(1)
        preview_img = self.fc.fd["preview"].preview_img_screenshot()
        image_before_edit = self.navigate_to_tfscreen_and_get_pre_edit_img(Preview.TF_RESIZE_TXT,
                                                                           tf_option1=Preview.TF_RESIZE_MOVE_OPTIONS[0])
        sleep(1)
        manual_img = self.fc.fd["preview"].preview_img_screenshot()
        self.driver.swipe(Preview.PREVIEW_IMAGE, direction="left", per_offset=0.55)
        sleep(1)
        move_left_img = self.fc.fd["preview"].preview_img_screenshot()
        self.driver.swipe(Preview.PREVIEW_IMAGE, direction="right", per_offset=0.45)
        sleep(1)
        move_right_img = self.fc.fd["preview"].preview_img_screenshot()
        self.fc.fd["preview"].zoom_preview_image()
        sleep(1)
        zoom_img = self.fc.fd["preview"].preview_img_screenshot()
        self.fc.fd["preview"].select_done()
        sleep(1)
        image_after_edit = self.fc.fd["preview"].preview_img_screenshot()
        self.fc.fd["preview"].select_done()
        sleep(1)
        edited_preview_img = self.fc.fd["preview"].preview_img_screenshot()
        assert saf_misc.img_comp(image_before_edit, image_after_edit) > 0
        assert saf_misc.img_comp(manual_img, move_left_img) > 0
        assert saf_misc.img_comp(move_left_img, move_right_img) > 0
        assert saf_misc.img_comp(move_right_img, zoom_img) > 0
        assert saf_misc.img_comp(preview_img, edited_preview_img) > 0
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_04_verify_resize_cancel_func(self):
        """
         Verify Resize Cancel functionality - C17117644
        """
        image_before_edit = self.navigate_to_tfscreen_and_get_pre_edit_img(Preview.TF_RESIZE_TXT,
                                                                           Preview.TF_RESIZE_MOVE_OPTIONS[1])
        self.fc.fd["preview"].select_cancel()
        sleep(1)
        image_after_cancel = self.fc.fd["preview"].preview_img_screenshot()
        assert saf_misc.img_comp(image_before_edit, image_after_cancel) == 0
        self.fc.fd["preview"].select_cancel()
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)

    def test_05_verify_transform_rotate_options_func(self):
        """
          Verify Transfrom Reize options functionality -
             C25341392, C17153695, C25341391, C25341393
        """
        transform_edit_failed = self.apply_and_verify_transform_options(Preview.TF_ROTATE_TXT,
                                                                        Preview.TF_ROTATE_OPTIONS, 0.1)
        assert len(transform_edit_failed) == 0, "Failed to selected following options {}".format(transform_edit_failed)
        logging.info("All transform Rotate options applied successfully")
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_06_verify_rotate_cancel_func(self):
        """
         Verify Rotate Cancel functionality - C17153696
        """
        image_before_edit = self.navigate_to_tfscreen_and_get_pre_edit_img(Preview.TF_ROTATE_TXT,
                                                                           Preview.TF_ROTATE_OPTIONS[1])
        self.fc.fd["preview"].select_cancel()
        sleep(1)
        image_after_cancel = self.fc.fd["preview"].preview_img_screenshot()
        assert saf_misc.img_comp(image_before_edit, image_after_cancel) == 0
        self.fc.fd["preview"].select_cancel()
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)

    def navigate_to_tfscreen_and_get_pre_edit_img(self, tf_option, tf_option1=None):
        self.fc.fd["preview"].select_transform_options(Preview.TRANSFORM_TXT)
        sleep(1)
        pre_edit_img = self.fc.fd["preview"].preview_img_screenshot()
        self.fc.fd["preview"].select_transform_options(tf_option,
                                                       tf_option_select=tf_option1)
        return pre_edit_img

    def apply_and_verify_transform_options(self, tf_option, tf_sub_options, diff=0.3):
        edit_failed = []
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.fd["preview"].go_to_print_preview_pan_view(pan_view=False)
        for option in tf_sub_options:
            sleep(1)
            preview_img = self.fc.fd["preview"].preview_img_screenshot()
            pre_edit_img = self.navigate_to_tfscreen_and_get_pre_edit_img(tf_option, option)
            self.fc.fd["preview"].select_done()
            sleep(1)
            edited_img = self.fc.fd["preview"].preview_img_screenshot()
            self.fc.fd["preview"].select_done()
            edited_preview_img = self.fc.fd["preview"].preview_img_screenshot()
            if saf_misc.img_comp(pre_edit_img, edited_img) < diff or saf_misc.img_comp(preview_img,
                                                                                       edited_preview_img) < diff:
                edit_failed.append(option)
        return edit_failed
