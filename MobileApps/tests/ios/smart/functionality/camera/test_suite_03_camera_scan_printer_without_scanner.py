import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview
from SAF.misc import saf_misc
import time

pytest.app_info = "SMART"


class Test_Suite_03_Camera_Scan_Printer_Without_Scanner(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.camera = cls.fc.fd["camera"]
        cls.preview_ui = Preview.PREVIEW_UI_ELEMENTS
        cls.preview_ui.remove(Preview.REORDER_BUTTON)
        cls.preview = cls.fc.fd["preview"]

        cls.stack = request.config.getoption("--stack")
        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    @pytest.fixture(scope="function", autouse="true")
    def return_home(self):
        self.fc.go_home(reset=True, stack=self.stack)

    def test_02_verify_enable_access_to_camera(self):
        """
        C15987385   Precondition: fresh install
        1. add a printer and navigate to scan tile then tap on "Don't Allow" on the popup
        2. tap on the link 'Enable Access to Camera' and enable camera option in ios settings and go back to HP Smart
        Expected Results:
            - after verify the enable allow access screen
        :return:
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.camera.select_allow_access_to_camera_on_popup(allow_access=False)
        self.camera.select_popup_option()
        if self.fc.fd["scan"].verify_second_close_btn() is not False:
            self.fc.fd["scan"].select_second_close_btn()
        self.camera.select_enable_access_to_camera_link()
        self.fc.fd["ios_system"].toggle_camera_switch(on=True)
        self.fc.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.fd["home"].verify_home_tile()

    def test_03_verify_manual_capture_print_preview(self):
        """
        C13927417
        1. Select any printer and tap the Scan tile, take a manual picture, and move past adjust boundaries
        Expected results:
            - verify print preview ui and there is no X button when only one scanned item
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_ui_elements()
        self.fc.multiple_manual_camera_capture(1, flash_option=FLASH_MODE.FLASH_AUTO)
        self.fc.fd["preview"].verify_toolbar_icons()
        self.fc.fd["preview"].verify_array_of_elements(self.preview_ui)
        # delete page is hidden
        self.fc.fd["preview"].select_delete_page_icon()
        self.fc.fd["preview"].verify_preview_edit_options()

    def test_04_verify_auto_capture_print_preview(self):
        """
        C14728246
        1. Select any printer and auto capture any image
        Expected results:
            - verify print preview ui
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_ui_elements()
        self.camera.select_auto_option()
        self.camera.capture_multiple_photos_by_auto_mode()
        # switch to manual otherwise image collection view is not clickable
        self.camera.select_manual_option()
        self.camera.select_auto_image_collection_view()
        self.fc.fd["preview"].dismiss_feedback_pop_up()
        self.fc.fd["preview"].verify_toolbar_icons()
        self.fc.fd["preview"].verify_array_of_elements(self.preview_ui)

    def test_05_verify_file_renaming_functionality(self):
        """
        C16017837
        1. Take an image from the camera
        2. Tap on the save icon from toolbar and rename the image and save it to HP smart
        3. tap Home button and go to "files & photos" using bottom pane
        Expected results:
            - after step 3 verify that file is renamed successfully and exists in HP smart Files
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        self.fc.multiple_manual_camera_capture(1, flash_option=FLASH_MODE.FLASH_AUTO)
        file_name = self.test_05_verify_file_renaming_functionality.__name__
        self.fc.save_file_to_hp_smart_files_and_go_home(file_name, self.preview.SHARE_AND_SAVE_BTN)
        self.fc.go_hp_smart_files_screen_from_home()
        self.fc.fd["files"].verify_file_name_exists("{}.jpg".format(file_name))

    def test_06_verify_email_share_functionality(self):
        """
        C16017856   Precondition: make sure to log in any email account
        1. Tap on Scan and select source as camera and perform multiple image capture
        2. On the preview screen, tap on Share and share the scanned images to an email
        Expected results:
            - after step 2 verify that the images are sent to email
        :return:
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        self.camera.select_auto_option()
        self.camera.capture_multiple_photos_by_auto_mode(no_of_images=10, timeout=300)
        self.camera.select_manual_option()
        self.camera.select_auto_image_collection_view()
        self.fc.fd["preview"].select_toolbar_icon(self.preview.SHARE_AND_SAVE_BTN)
        file_name = self.test_06_verify_email_share_functionality.__name__
        self.fc.fd["preview"].rename_file(file_name)
        self.fc.fd["preview"].select_file_type("JPG")
        self.fc.fd["preview"].select_navigate_back()
        self.fc.fd["preview"].select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.fc.fd["share"].select_mail()
        subject = "{}_{}".format("test_06_verify_email_share", self.driver.driver_info["udid"])
        self.fc.fd["gmail"].compose_and_send_email(self.email_address, subject_text=subject)
        msg_id = self.fc.fd["gmail_api"].search_for_messages(q_from=self.email_address,
                                                             q_to=self.email_address, q_unread=True,
                                                             q_subject=subject, timeout=300)
        attachment_names = self.fc.fd["gmail_api"].get_attachments(msg_id[0][u'id'])
        self.fc.fd["gmail_api"].delete_email(msg_id)
        assert all([file_name in str(name) for name in attachment_names]) is True
        assert len(attachment_names) >= 10

    def test_08_verify_share_save_preview_ui(self):
        """
        C17202822
        1. Take a picture and go to preview screen, tap on share/save icon, rename file and save to HP smart
        Expected Results
            - verify share/save preview ui, verify renamed file is saved under HP smart
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_ui_elements()
        self.fc.fd["camera"].select_manual_option()
        self.fc.multiple_manual_camera_capture(1, flash_option=FLASH_MODE.FLASH_AUTO)
        self.fc.fd["preview"].select_toolbar_icon(Preview.SHARE_AND_SAVE_TEXT)
        file_name = self.test_08_verify_share_save_preview_ui.__name__
        self.fc.fd["preview"].rename_file(file_name)
        self.fc.fd["preview"].select_file_type("JPG")
        self.fc.fd["preview"].select_navigate_back()
        self.fc.fd["preview"].select_button(self.preview.SHARE_AND_SAVE_BTN)
        self.fc.fd["share"].select_save_to_hp_smart()
        self.fc.go_hp_smart_files_screen_from_home()
        self.fc.fd["files"].verify_file_name_exists("{}.jpg".format(file_name))

    def test_09_save_functionality_for_multi_page_addition(self):
        """
        C15968008
        1. Add any printer and tap the scan tile
        2. Capture more than 6 images and save them to HP Smart
        3. Go to home screen and tap on "files & photos" icon and navigate to the saved folder
        Expected Results:
            - after step 3 verify the scanned results should be saved as multiple images in one folder
        :return:
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        number_of_images = 6
        self.camera.select_manual_option()
        self.fc.multiple_manual_camera_capture(number_of_images)
        self.fc.fd["preview"].select_toolbar_icon(Preview.SHARE_AND_SAVE_TEXT)
        file_name = self.test_09_save_functionality_for_multi_page_addition.__name__
        self.fc.save_file_to_hp_smart_files_and_go_home(file_name, self.preview.SHARE_AND_SAVE_BTN)
        self.fc.go_hp_smart_files_screen_from_home()
        folder_name = "{}({})".format(file_name, number_of_images)
        self.fc.fd["files"].select_folder_from_list(folder_name)
        self.fc.fd["files"].verify_file_name_exists("{}.jpg".format(file_name))
        for i in range(1, number_of_images):
            self.fc.fd["files"].verify_file_name_exists("{}_{}.jpg".format(file_name, i))

    def test_10_verify_print_functionality(self):
        """
        C14728243
        1. Select any printer and tap the Scan tile
        2. Select source as camera and perform manual image capture and go to print preview
        3. On the preview page, tap on print button
        Expected Results:
            - verify that print is successful
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        self.camera.select_manual_option()
        self.fc.multiple_manual_camera_capture(1, flash_option=FLASH_MODE.FLASH_AUTO)
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_11_verify_page_addition_functionality(self):
        """
        C14728098
        1. Add a printer and tap the scan tile
        2. Select camera as source and take a picture, proceed to print preview
        3. Tap add page icon in print preview and take another picture
        Expected Results:
            - verify that add page is working and pictures have x button
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        number_of_images = 2
        self.camera.select_manual_option()
        self.fc.multiple_manual_camera_capture(number_of_images)
        assert self.fc.fd["preview"].verify_delete_page_x_icon() is not False
        assert self.fc.fd["preview"].get_no_pages_from_preview_label() == number_of_images

    def test_12_verify_zoom_mode(self):
        """
        C15968007
        1. Select a printer, tap on scan tile, take an image, tap on the preview image and cancel out of edit screen
        2. Back in preview screen, expand the preview image
        Expected Results:
            - verify user goes to edit screen after tapping on image preview
            - verify images goes into zoom mode after expanding preview image
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        self.camera.select_manual_option()
        self.fc.multiple_manual_camera_capture(1)
        self.fc.fd["preview"].zoom_preview_image()
        self.fc.fd["preview"].verify_zoomed_mode()

    def test_13_verify_preview_back_button_functionality(self):
        """
        C14728101
        1. Add a printer, tap the scan tile, take picture and go to preview screen
        2. Click the back button and then click the "Yes, Go Home" button
        Expected Results:
            - verify popup after clicking back button and selecting go home will redirect user home
        :return:
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.verify_camera_btn()
        self.camera.select_manual_option()
        self.fc.multiple_manual_camera_capture(1)
        self.fc.fd["preview"].select_navigate_back()
        self.fc.fd["preview"].verify_exit_with_out_saving_popup_options()
        self.fc.fd["preview"].select_yes_go_home_btn()
        self.fc.fd["home"].verify_home()

    def test_14_verify_source_elements_for_printer_without_scanner(self):
        """
        Verify source elements for printer without scanner- C27655114
        1. Install and Open the HP Smart app
        2. Tap on the scan icon on navigation bar
        3. Tap on source
        Expected result: verify that the Source button has 
        - Files & Photos
        - Camera
        """
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.fd["home"].verify_rootbar_scan_icon()
        self.fc.fd["home"].select_scan_icon()
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_popup_option(camera=True)
        self.fc.fd["scan"].select_source_button()
        self.fc.fd["scan"].verify_source_options_for_printer_without_scanner() 
    
    def test_15_verify_source_elements_without_printer(self):
        """
        Verify source elements for printer without scanner- C27655114
        similar testcase as above without adding a printer 
        """
        self.fc.fd["home"].verify_rootbar_scan_icon()
        self.fc.fd["home"].select_scan_icon()
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        self.fc.fd["scan"].select_source_button()
        self.fc.fd["scan"].verify_source_options_for_printer_without_scanner() 