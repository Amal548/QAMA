from MobileApps.libs.flows.android.hpps.hpps_flow import hppsFlow

class More_Options(hppsFlow):
    """
        More Options - All elements in the Printing more options screen. From both System Ui and Trap Doo.
    """

    # Flow_name - Title of the ui map used in this class
    flow_name = "more_options"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################
    def select_back(self):
        """
        Need to use android back button to move back from More Options
        :return:
        """
        self.driver.back()

    def change_quality(self, quality):
        """
        select quality based on the value given
        works for both Photo and Document tab
        :param quality:
                QUALITY__AUTOMATIC = "quality_automatic_btn"
                QUALITY__BEST = "quality_best_btn"
                QUALITY__DRAFT = "quality_draft_btn"
                QUALITY__NORMAL = "quality_normal_btn"
        :return:
        """
        quality_obj_name = self.check_parameter_in_dict(quality)
        self.driver.click("quality_list_btn")
        self.driver.wait_for_object(quality_obj_name, timeout=3)
        self.driver.click(quality_obj_name)

    def toggle_borderless(self, on=True):
        el = self.driver.find_object("borderless_toggle")

        if (el.get_attribute("checked") == "false" and on) and (el.get_attribute("checked") == "true" and not on):
            el.click()
        return True

    def change_scaling(self, scaling):
        """
        Change the scaling to the value given
        :param scaling:
                SCALING__FILL_PAGE = "scaling_fill_page_btn"
                SCALING__FIT_TO_PAGE = "scaling_fit_to_page_btn"
        :return:
        """
        scaling_obj_name = self.check_parameter_in_dict(scaling)
        self.driver.wait_for_object("scaling_list_btn")
        self.driver.click("scaling_list_btn")
        self.driver.wait_for_object(scaling_obj_name, timeout=3)
        self.driver.click(scaling_obj_name)


    def is_photos_tab_selected(self):
        """
        checks to see if the Photos tab is selected and returns true if so false other wise
        :return:
        """
        return self.driver.find_object('photo_tab_btn', index=0).get_attribute('selected')

########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_more_options_screen(self):
        """
        verify More Options screen is displayed
        :return:
        """
        self.driver.wait_for_object("more_options_title_txt", timeout=15)
