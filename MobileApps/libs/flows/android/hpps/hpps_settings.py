from MobileApps.libs.flows.android.hpps.hpps_flow import hppsFlow

class HPPS_Settings(hppsFlow):
    """
        HPPS_Settings - Contains all the elements within the HPPs Settings Page, and all children within.
                        From HP Print Service and System UI(More Options)-
                            About, Paper, Supplies notification, Discovery, Enterprise Options, Advanced Settings
                        From Trap Door and Trap Door(More Options)-
                            About, Paper, Supplies notification, Advanced Settings
    """

    # Flow_name - Title of the ui map used in this class
    flow_name = "hpps_settings"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################
    def select_back_arrow(self):
        """
        selects the back arrow button
        :return:
        """
        self.driver.click("back_arrow_btn")

    def select_about(self):
        """
        Selects the About button
        :return:
        """
        self.driver.click("about_btn")

    def select_paper(self):
        """
        selects the Paper button
        :return:
        """
        self.driver.click("paper_btn")

    def select_supplies_notification(self):
        """
        selects the Supplies Options button
        :return:
        """
        self.driver.click("supplies_notification_btn")

    def select_advanced_settings(self):
        """
        clicks on the advanced settings button
        :return:
        """
        self.driver.click("advanced_settings_btn")

    ####################################################################################################
    #                                           About Page                                             #
    ####################################################################################################

    def get_application_version(self):
        """
        Returns the application version
        :return:
        """
        return self.driver.find_object("app_version_txt").text

    def select_legal_information(self):
        """
        clicks on the Legal information button
        :return:
        """
        self.driver.click("legal_info_btn")

    def select_end_user_license_agreement(self):
        """
        clicks on the eula button
        :return:
        """
        self.driver.click("end_user_license_agreement_btn")

    def select_privacy(self):
        """
        clicks on the privacy button
        :return:
        """
        self.driver.click("privacy_btn")

    ####################################################################################################
    #                                      Advanced Settings Page                                      #
    ####################################################################################################

    def toggle_android_print_rendering_off(self):
        """
        Turns off android print rendering if it is on
        :return:
        """
        el = self.driver.find_object("android_print_rendering_toggle")
        if el.get_attribute("checked") == "true":
            el.click()

    def toggle_android_print_rendering_on(self):
        """
        Turns off android print rendering if it is on
        :return:
        """
        el = self.driver.find_object("android_print_rendering_toggle")
        if el.get_attribute("checked") == "false":
            el.click()

    def select_pclm_compression_type(self, type):
        """
        clicks on the  PCLm compression button and selects the given compression type
        type:
            PCLM__DEFAULT = "default_checkbox"
            PCLM__JPEG = "jpeg_checkbox"
            PCLM__FLATE = "flate_checkbox"
            PCLM__RLE = "rle_checkbox"
        :return:
        """
        self.driver.click("pclm_compression_btn")
        self.driver.wait_for_object("default_checkbox")
        self.driver.click(type)

    def select_print_protocol_type(self, protocol_type):
        """
        clicks on Print Protocol button and selects the type given
        type :
            PROTOCOL__AUTO = "auto_checkbox"
            PROTOCOL__IPP = "ipp_checkbox"
            PROTOCOL__IPPS = "secure_ipp_checkbox"
            PROTOCOL__LEGACY = "legacy_checkbox"
        :return:
        """
        protocol_type_item = self.check_parameter_in_dict(protocol_type)
        self.driver.click("print_protocol_btn")
        self.driver.wait_for_object("print_protocol_popup")
        self.driver.click(protocol_type_item)
       
########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_hpps_settings_screen(self):
        """
        Verify Hp Print Service settings screen
        :return:
        """
        self.driver.wait_for_object("about_btn")

    def verify_about_screen(self):
        """
        verify About screen is loaded
        :return:
        """
        self.driver.wait_for_object("app_version_txt")
        self.driver.wait_for_object("legal_info_btn")
        self.driver.wait_for_object("end_user_license_agreement_btn")

    def verify_advanced_settings_screen(self):
        """
        Verify Advanced Settings screen is loaded
        :return:
        """
        self.driver.wait_for_object("pclm_compression_btn")
        self.driver.wait_for_object("print_protocol_btn")
