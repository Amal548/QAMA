import logging
import time
from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Home(SmartFlow):
    flow_name = "home"

    ACTIVITY_BTN = "activity_btn"
    INBOX_BTN = "inbox_btn"
    ACCOUNT_BTN = "account_btn"
    SIGN_IN_BTN = "signin_btn"
    SUPPLIES_BTN = "supplies_btn"
    SHORTCUTS_BTN = "shortcuts_btn"
    WELCOME_TO_HP_SMART_INBOX = "welcome_to_your_hp_inbox"
    NO_PRINT_ACTIVITY_TITLE = "no_printer_activity_title"
    MOBILE_FAX_BTN = "mobile_fax_btn"
    TOGGLE_MENU = "toggle_menu"
    VIEW_NOTIFICATIONS_TITLE = "view_notifications_title"
    VIEW_NOTIFICATIONS_LINK = "view_notifications_link"
    ACTIVITY_TABS = [MOBILE_FAX_BTN, SUPPLIES_BTN, ACCOUNT_BTN, SHORTCUTS_BTN]

    ########################################################################################################################
    #                                                                                                                      #
    #                                              ACTION  FLOWS                                                           #
    #                                                                                                                      #
    ########################################################################################################################

    def select_get_started_by_adding_a_printer(self, handle_popup=True):
        """
        clicks  add printer sign on home page
        :return:
        """
        if self.verify_add_your_first_printer(raise_e=False) is not False:
            self.select_add_your_first_printer()
        else:
            self.select_printer_plus_button_from_topbar()
        # iOS 13 bluetooth security update
        if handle_popup:
            if self.verify_bluetooth_popup(raise_e=False):
                self.handle_bluetooth_popup()
            # Handle Bluetooth setup pop-up when bluetooth is off
            if self.verify_close(raise_e=False) is not False:
                self.select_close()
                logging.info("Bluetooth is off")

    def select_printer_plus_button_from_topbar(self):
        """
        clicks the small + symbol on the top bar of home page:
            its located right most corner on the home page. but it will display after a printer selection atleast once
        :return:
        """
        self.driver.click("add_new_printer_from_top_bar")

    def select_notification_bell(self):
        """

        :return:
        """
        self.driver.click("notification_bell_btn")

    def long_press_on_printer(self):
        """
        it clicks long press on the printer in carousel to bring printer menu live:
            printer menu has options: printer details:
                                      forget this printer:
        :return:
        """
        self.driver.wait_for_object("estimate_cartridge_levels_text_btn", timeout=20)
        self.driver.long_press("estimate_cartridge_levels_text_btn")

    def select_personalize_btn(self):
        """
        selects the Personalize button
        """
        self.driver.scroll("personalize_btn", click_obj=True)

    def verify_tile_displayed(self, tile_name):
        return self.driver.scroll(tile_name, direction="down", scroll_object="tile_collection_view", raise_e=False)

    def select_tile_by_name(self, tile_name):
        """
        clicks on the given tile name:
            tile_name is a shared_obj locator available in shared_obj ui map:

        for GA, we assuming that we are at HOME screen and performed verify_home(ga=True)
        """
        ga_dynamic_key_value = self.driver.return_str_id_value(tile_name)
        self.driver.ga_container.insert_ga_key("home_tile_name_clicked_one", ga_dynamic_key_value)

        try:
            self.driver.scroll(tile_name, direction="down", scroll_object="tile_collection_view")
        except NoSuchElementException:
            logging.warning("the tile was not enabled, which we would like to click")

        name = self.driver.return_str_id_value(tile_name)
        visible = self.driver.find_object(tile_name).get_attribute("visible")
        if visible:
            try:
                self.driver.click("tile_title", format_specifier=[name])
                # iPhone6+ OS:12.4.1 never finds the element using xpath for some odd reason
            except NoSuchElementException:
                self.driver.wait_for_object(tile_name).click()
        else:
            self.driver.swipe()

    def select_different_printer(self):
        """
        From Home screen, go to Printers screen via:
            - Click on Printer button on navigation bar of Home screen
            - CLick on 'Select a Different Printer' button
        End of flow: Printers screen
        """
        self.driver.click("select_printer_btn")

    def select_printer_info(self):
        """
        From Home screen, go to Printers screen via:
            - Click on Printer button on navigation bar of Home screen
            - CLick on 'See my Printer Information' button
        End of flow: Printer Information
        """
        self.driver.click("printer_info_btn")

    def select_carousel(self):
        self.driver.click("device_carousel_collection_view")

    def select_printer_information_from_menu(self):
        """
        From Home screen, go to Printers screen via:
            - Click on Printer button on navigation bar of Home screen
            - CLick on 'See My Printer Information' button
        End of flow: Printers screen
        """

        self.driver.click("printer_information_btn")

    def select_forget_printer_from_menu(self):
        """

        :return:
        """
        self.driver.click("forget_this_printer_btn")
    
    def select_hide_printer_from_menu(self):
        """

        :return:
        """
        self.driver.click("hide_printer_btn")

    def select_forget_printer_cancel_btn(self):
        """

        :return:
        """
        self.driver.click("forget_printer_cancel_btn")

    def select_photos(self):
        self.driver.click("photos_btn")

    def select_forget_printer_forget_btn(self):
        self.driver.click("forget_printer_forget_btn")

    def select_hide_printer_confirmation_btn(self):
        self.driver.click("hide_printer_confirmation_btn")

    def click_on_printer_icon(self):
        """
        clicks on the printer icon in the Printer Overview to open/close the printer options menu
        :return:
        """
        self.driver.scroll("printer_image", direction="up", click_obj=True)
        # self.driver.click("printer_image")

    def select_notifications(self):
        """
        Click on Notifications button on Home navigation bar

        End of flows: Notifications screen

        """
        self.driver.click("notification_bell_btn")

    def select_my_printer(self):
        self.driver.click("more_btn")

    def swipe_carousel(self, direction="left"):
        self.driver.swipe("device_carousel_collection_view", direction=direction)

    ####################################################################################################################
    #                                              BOTTOM ACTION BAR                                                   #
    ####################################################################################################################
    def select_home_icon(self):
        """
        Click on 'Home' icon on bottom action bar
        """
        self.verify_rootbar_home_icon().click()

    def select_documents_icon(self):
        """
        Click on 'View and Print' icon on bottom action bar
        """
        self.verify_rootbar_documents_icon().click()

    def select_scan_icon(self):
        """
        Click on 'Scan' icon on bottom action bar
        """
        self.verify_rootbar_scan_icon().click()

    def select_app_settings(self):
        """
        Click on 'Settings' icon on bottom action bar
        """
        self.verify_rootbar_app_settings().click()

    def select_account_icon(self):
        """
        Click on 'Account' icon on bottom action bar
        """
        self.verify_rootbar_account_icon().click()

    def dismiss_tap_account_coachmark(self):
        time.sleep(2)
        if self.driver.wait_for_object("tap_account_coachmark", displayed=False, raise_e=False) is not False:
            self.driver.click_by_coordinates(area='bl')

    def handle_location_pop(self):
        if self.verify_allow_while_using_app(raise_e=False) is not False:
            self.handle_location_popup()
            logging.info("Location pop-up displayed")

    def select_sign_in_icon(self):	
        self.driver.click("signin_btn")	

    def select_create_account_icon(self):	
        self.driver.click("create_account_icon")	

    def select_settings_icon(self):
        self.driver.click("settings_opt")
    
    ########################################################################################################################
    #                                                                                                                      #
    #                                              VERIFICATION  FLOWS                                                     #
    #                                                                                                                      #
    ########################################################################################################################

    def verify_printer_menu_screen(self, raise_e=True):
        """
            verifies the small printer menu daillog as a screen after long press on printer:
                verifying using printer table view (small box)
        :return:
        """
        self.driver.wait_for_object("printer_menu_table_view", interval=5, raise_e=raise_e)

    def verify_empty_carousel(self):
        self.verify_add_your_first_printer()

    def verify_notification_bell(self):
        """
        verifies the notification bell
        :return:
        """
        self.driver.wait_for_object("notification_bell_btn")

    def verify_hp_smart_nav_bar(self):
        self.driver.wait_for_object("top_navigation_bar_name")

    def verify_loaded_printer(self, printer_name, raise_e=True):
        """
        Verify that a printer is loaded via:
            - Left side: printer name
            - Right side: Estimated Cartridge Levels displays or Get Support button
        """
        self.verify_printer_name(printer_name)
        if not self.driver.wait_for_object("estimate_cartridge_levels_text_btn", raise_e=False):
            self.driver.wait_for_object("get_support_btn", raise_e=raise_e)

    def verify_printer_name(self, printer_name, raise_e=True):
        return self.driver.wait_for_object("printer_name_txt", format_specifier=[printer_name], raise_e=raise_e)

    def verify_printer_information_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("estimate_cartridge_levels_text_btn", timeout=20)

    def verify_forget_printer_popup(self):
        """

        :return:
        """
        self.driver.wait_for_object("forget_printer_forget_btn")
    
    def verify_hide_printer_popup(self):
        """

        :return:
        """
        self.driver.wait_for_object("hide_this_printer_popup")

    def verify_forget_printer_cancel_popup(self):
        """

        :return:
        """
        self.driver.wait_for_object("forget_printer_cancel_btn")

    def verify_estimated_cartridge_levels(self):
        """
        verifies the estimated cartridge levels text
        :return:
        """
        self.driver.wait_for_object("estimated_cartridge_level", timeout=20)

    # FIXME: feature is deprecated. use verify_printer_name to verify printer name on carousel dynamically
    def get_printer_name_from_top_nav_bar(self):
        """
        Verifies the name of the selected printer in the top nav bar
        :param name:
        :return:
        """
        if self.driver.wait_for_object("printer_name_txt", timeout=5, raise_e=False) is not False:
            printer_name = self.driver.wait_for_object("printer_name_txt", timeout=5, raise_e=False)
            return str(printer_name.get_attribute("value")).strip()

    def get_printer_name_from_device_carousel(self, printer_cell="DeviceCarouselInfo-1"):
        printer_name = None
        if self.driver.wait_for_object("device_name_in_carousel", format_specifier=[printer_cell],
                                       raise_e=False) is not False:
            printer_name = self.driver.get_attribute("device_name_in_carousel", attribute='value',
                                                     format_specifier=[printer_cell])
        return printer_name

    def verify_printer_not_connected_popup(self):
        """
        verifies that the printer not connected popup is displayed after clicking a grayed out tile
        :return:
        """
        self.driver.wait_for_object("printer_not_connected_txt")

    def verify_notifications_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("notifications_title")

    def verify_home_tile(self, raise_e=False):
        # close promotion banner pop-up
        if self.driver.wait_for_object("promotion_banner_pop_up", timeout=5, raise_e=False) is not False:
            self.driver.click("promotion_banner_pop_up")
            if self.driver.wait_for_object("_shared_cancel", timeout=3, raise_e=False) is not False:
                self.driver.click("_shared_cancel")
            else:
                self.driver.click("_shared_back_arrow_btn")
        if self.driver.wait_for_object("_Shared_no_thanks_btn", timeout=3, raise_e=False) is not False:
            self.driver.click("_Shared_no_thanks_btn")
        self.close_smart_task_awareness_popup()
        self.close_print_anywhere_pop_up()

        return self.driver.wait_for_object("tile_collection_view", raise_e=raise_e)

    def verify_tap_here_to_start(self, raise_e=False):
        """
        WAC popup on home screen
        """
        return self.driver.wait_for_object("tap_here_to_start", raise_e=raise_e)

    def verify_home(self, raise_e=True):
        """
        Verifies home screen via:
        1. Tile collection
        2. Bottom navigation bar: home icon is active
        """
        self.allow_notifications_popup(timeout=10, raise_e=False)
        if self.verify_tap_account_coachmark_popup(raise_e=False):
            self.dismiss_tap_account_coachmark()
        self.driver.wait_for_object("tile_collection_view", raise_e=False)
        if self.verify_rootbar_home_icon(raise_e=False) is not False:
            return self.verify_rootbar_home_icon().get_attribute("value") == '1'
        else:
            if raise_e:
                raise NoSuchElementException("Home not Displayed")
            else:
                return False

    def verify_add_your_first_printer(self, raise_e=True):
        """
        Add Your First printer card
        """
        return self.driver.find_object("add_your_first_printer", raise_e=raise_e)

    def verify_add_printer_on_carousel(self):
        """
        Add printer card for when a printer exists on carousel
        """
        self.driver.wait_for_object("add_printer_img_txt")

    def select_add_your_first_printer(self):
        self.verify_add_your_first_printer().click()

    def verify_printer_added(self):
        return self.driver.wait_for_object("printer_image", timeout=5, raise_e=False)

    # GA tiles showing and tile count
    def check_tile_show_and_count(self):

        counted_tile_list = []

        tiles = self.get_all_tiles()
        for tile in tiles:
            name = tile.text
            if name is None:
                continue
            if name in counted_tile_list:
                continue

            logging.debug("Tile Name: {}".format(name))
            self.driver.scroll("tile_title", format_specifier=[name], direction="down",
                               scroll_object="tile_collection_view")

            if name == "Personalize":
                excluded_tile = name
                logging.debug("List Size: {}".format(excluded_tile))
            else:
                scrubbed_name = name.replace(" ", "-")
                # scrubbed_name = scrubbed_name.replace("\n", "")
                self.driver.ga_container.insert_ga_key("home_tile_name", scrubbed_name)
                self.driver.wait_for_object("tile_title", format_specifier=[name], timeout=30, interval=1)
                counted_tile_list.append(name)

        logging.debug("List Size: {}".format(len(counted_tile_list)))
        self.driver.ga_container.insert_ga_key("home_tile_count", len(counted_tile_list))
        self.driver.wait_for_object("tile_collection_view")
        self.driver.scroll("device_info_section", direction="up")

    def get_all_tiles(self):
        return self.driver.find_object("tile_frame", multiple=True,
                                       root_obj=self.driver.find_object("tile_collection_view"))

    # TODO: this method need to refactor more when method used in execution
    def select_printer_from_carousel(self, printer_name):

        self.driver.wait_for_object("tile_collection_view")

        self.driver.scroll("device_info_section", direction="up")
        # self.driver.swipe("tile_collection_view", "up") # TODO: keep swipe if device carousel changes again

        timeout = time.time() + 120
        direction = 'left'
        last_tested_printer = ''
        carousel_cv = self.driver.find_object("device_carousel_collection_view")

        while time.time() < timeout:
            self.driver.wait_for_object("printer_name_txt")
            pn = self.driver.find_object("printer_name_txt")
            current_printer = pn.get_attribute("value")
            if last_tested_printer == current_printer:
                direction = 'left' if direction == 'right' else 'right'

            if printer_name in current_printer:
                logging.info("Found Printer on carousel")
                break

            self.driver.swipe(carousel_cv, direction="left") if direction == 'left' \
                else self.driver.swipe(carousel_cv, direction="right")

    def available_printers_in_carousel(self, printer_name=''):

        self.driver.wait_for_object("tile_collection_view")
        self.driver.scroll("device_info_section", direction="up")
        self.driver.wait_for_object("device_carousel_collection_view")

        required_printer = printer_name

        timeout = time.time() + 180
        while time.time() < timeout:
            r_objects = self.driver.find_object('device_carousel_collection_view', multiple=True)
            for obj in r_objects:

                found = False
                current_printer_name = self.driver.find_object("printer_name_txt").get_attribute('value')

                if current_printer_name == required_printer:
                    obj.click()
                    found = True

                if not found:
                    self.driver.swipe(swipe_object="device_carousel_collection_view", check_end=False)
                else:
                    break

    def verify_smart_task_awareness_popup(self, timeout=5, raise_e=False):
        return self.driver.wait_for_object("smart_task_awareness_popup", timeout=timeout, raise_e=raise_e)

    def close_smart_task_awareness_popup(self):
        # TODO: remove this location & notificaiton popup once AIOI-11099 & 10937 is resolved
        self.allow_notifications_popup(raise_e=False)
        if self.verify_allow_while_using_app(raise_e=False) is not False:
            self.handle_location_popup()
        if self.verify_smart_task_awareness_popup():
            self.driver.click("smart_task_pop_up_close_btn")
        else:
            logging.info("smart task awareness popup not displayed")

    def close_print_anywhere_pop_up(self):
        self.allow_notifications_popup(raise_e=False)
        if self.driver.wait_for_object("print_anywhere_anytime_popup", timeout=3, raise_e=False) is not False:
            self.driver.click("print_anywhere_anytime_pop_up_close_btn")
            logging.info("Print anywhere popup displayed")

    def select_tap_here_to_start(self, timeout=60):
        self.driver.wait_for_object("tap_here_to_start", timeout=timeout).click()

    def remove_printer_by_forget_printer_option(self):
        self.driver.long_press("second_printer_img")
        self.verify_printer_menu_screen()
        self.select_forget_printer_from_menu()
        self.verify_forget_printer_popup()
        self.select_forget_printer_forget_btn()

    def remove_printer(self):
        self.driver.wait_for_object("printer_image")
        self.driver.long_press("printer_image")
        self.verify_printer_menu_screen()
        self.select_forget_printer_from_menu()
        self.verify_forget_printer_popup()
        self.select_forget_printer_forget_btn()
    
    def hide_printer(self):
        if self.verify_printer_menu_screen(raise_e=False) is False:
            self.driver.wait_for_object("printer_image")
            self.driver.long_press("printer_image")
            self.verify_printer_menu_screen()
        self.select_hide_printer_from_menu()
        self.verify_hide_printer_popup()
        self.select_hide_printer_confirmation_btn()

    def verify_feature_unavailable_popup(self, message: str):
        """
        :param message: ui map obj key for the popup error message
        """
        self.driver.wait_for_object("feature_unavailable")
        self.driver.wait_for_object("_shared_str_ok")
        self.driver.wait_for_object(message)

    def verify_limited_access_popup(self):
        self.driver.wait_for_object("limited_access")
        self.driver.wait_for_object("limited_access_no_printer")
        self.driver.wait_for_object("_shared_continue_btn")
        self.driver.wait_for_object("_shared_cancel")

    def verify_printer_dropdown_options(self):
        self.driver.long_press("printer_image")
        self.verify_printer_menu_screen()
        self.driver.wait_for_object("forget_this_printer_btn")
        self.driver.wait_for_object("printer_information_btn")

    def verify_tap_account_coachmark_popup(self, raise_e=True):
        return self.driver.wait_for_object("tap_account_coachmark", displayed=False, raise_e=raise_e)

    def verify_print_anywhere_popup(self):
        self.driver.wait_for_object("print_anywhere_anytime_popup")
    
    def verify_create_account_icon(self, raise_e=True):
        return self.driver.wait_for_object('create_account_icon', raise_e=raise_e)

    def verify_sign_in_icon(self, raise_e=True):
        return self.driver.wait_for_object("signin_btn", raise_e=raise_e)

    ###################################################################################
    #                               PHOTOMYNE                                         #
    ###################################################################################
    def verify_photomyne_popup(self):
        self.driver.wait_for_object("_Shared_no_thanks_btn")
        self.driver.wait_for_object("_shared_close")
        self.driver.wait_for_object("try_photomyne")
        self.driver.wait_for_object("photomyne_consent")

    def select_try_photomyne(self):
        self.driver.click("try_photomyne")

    def select_no_thanks(self):
        self.driver.click("_Shared_no_thanks_btn")

    def verify_notification_screen(self):
        """
        Verify notification screen
        """
        self.driver.wait_for_object("notification_title")
        self.driver.wait_for_object("activity_btn")
        self.driver.wait_for_object("inbox_btn")
