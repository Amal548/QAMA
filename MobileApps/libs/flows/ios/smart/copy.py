
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Copy(SmartFlow):
    flow_name = "copy"

    START_BLACK_BTN = "start_black_button"
    START_COLOR_BTN = "start_color_button"
    ADD_PAGES_BTN = "add_pages_button"
    COPY_PREVIEW_EXIT_POPUP = "copy_preview_exit_popup"

    COPY_PREVIEW_ELEMENTS = [
        START_BLACK_BTN,
        START_COLOR_BTN,
        ADD_PAGES_BTN,
    ]


########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows
#                                                                                                                      #
########################################################################################################################

    def select_object_size(self, object_size):
        """
            selects the object size for digital copy: we have 6 available options defined in const file
        :param object_size:
        :return:
        """
        ga_dynamic_key_value = self.get_text_from_str_id(object_size)
        self.driver.ga_container.insert_ga_key("digital_copy_paper_size_type", ga_dynamic_key_value)

        self.driver.click("object_size_btn")
        self.driver.click(object_size)


    def select_flash_button(self):
        """
         clicks the flash button to change the flash mode: ga is dynamic,
            developers need to set the variables to know current flash mode
        :return:
        """
        ga_dynamic_key_value = "ON"
        self.driver.ga_container.insert_ga_key("digital_copy_flash_mode", ga_dynamic_key_value)

        self.driver.click("flash_button")

    def select_capture_button(self):
        """
            clicks the capture button to capture the object:
            capture the ga for copy type and also input size from object size selection:
        :return:
        """
        self.driver.click("capture_button")

    def select_add_more_pages(self):
        """
            it will click the small plus button on right corner of preview
            so we will add more copies to same JOB:
            GA added:
        :return:
        """
        self.driver.click("add_pages_button")

    def select_number_of_copies(self, change_copies=1):
        """
            selects the number of copies from small tray table:
        :return:
        """
        ga_dynamic_key_value = change_copies
        self.driver.ga_container.insert_ga_key("digital_copy_number_of_copies", ga_dynamic_key_value)

        self.driver.click("copies_tray_button")
        self.driver.scroll("copies_table", format_specifier=[change_copies],check_end=False,click_obj=True)

    # TODO: taking time to select, try to minimize execution time, so commented temporarily
    # tile_switches = self.driver.find_object("chane_copies_val_2", multiple=True)
    # logging.info("Number of UIAELEMENTS: {}".format(len(tile_switches)))
    # print("1")
    # for tile_switch in tile_switches:
    #     switch_name = tile_switch.get_attribute("name")
    #     tile_switch_value = tile_switch.get_attribute("value")
    #     if tile_switch_value == change_copies:
    #         logging.info("Enabling [{}]. Clicking toggle!".format(switch_name))
    #         tile_switch.click()
    #         break
    # self.driver.scroll(str(change_copies), scroll_object="copies_table")

    def select_resize_in_digital_copy(self, resize):
        """
            selects the resize option: from available:: defined in const file
        :return:
        """
        self.driver.click("resize_tray_button")
        ga_dynamic_key_value = self.driver.find_object(resize).get_attribute("value")

        self.driver.ga_container.insert_ga_key("digital_copy_resize", ga_dynamic_key_value)
        self.driver.click(resize)

    def select_start_color(self):
        """
        clicks the start color button: it adds the GA for three things
            1) no of copies 2) resize type 3) color or black
        :return:
        """
        self.driver.click("start_color_button")

    def select_start_black(self):
        """
        clicks the start black button: it adds the GA for three things
            1) no of copies 2) resize type 3) color or black
        :return:
        """
        self.driver.click("start_black_button")

    def select_enable_access_to_camera_link_text(self):
        """
        clicks on enable access to camera button on the camera not allowed screen, to go manual settings page
        :return:
        """
        self.driver.click("enable_access_to_camera_link_txt")

    def enable_camera_access_toggle_in_settings(self):
        """
        clicks the toggle on in settings page to enable access to camera:
        :return:
        """
        self.driver.click("toggle_on_camera_access_system_ui")

    def select_settings(self):
        """
        clicks the settings button to go back to hp smart app from manual settings page:
            some times we may require in future:
        :return:
        """
        self.driver.click("settings_button")

    def select_x_to_close(self):
        """
            clicks the X button on copy screen to close current and go back to home with out taking capture
        :return:
        """
        self.driver.click("x_btn_on_copy")

    def select_auto_capture(self):
        """
        Select Auto option on camera screen to capture automatically: we have manual and auto button
        """
        self.driver.click("auto_btn")


########################################################################################################################
#                                                                                                                      #
#                                                  Verification Flows
#                                                                                                                      #
########################################################################################################################

    def verify_copy_screen(self):
        """
        Verifies the copy screen with flash button:
        :return:
        """

        self.driver.wait_for_object("capture_button")

    def verify_copy_preview_screen(self):
        """
        verifies the preview screen after capture:
        :return:
        """
        self.driver.wait_for_object("Digital_copy_preview_title")

    def verify_enable_access_to_camera_screen(self):
        """
        Verify the camera not allowed screen: will find the enable access to camera link to go manual settings page
        :return:
        """
        self.driver.wait_for_object("enable_access_to_camera_link_txt")
    
    def verify_copy_preview_screen_exit_popup(self):
        self.driver.wait_for_object("copy_preview_exit_popup")

########################################################################################################################
#                                                                                                                      #
#                                                  Functionality Related sets
#                                                                                                                      #
########################################################################################################################
