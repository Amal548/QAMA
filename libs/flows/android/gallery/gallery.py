from MobileApps.libs.flows.android.gallery.gallery_flow import GalleryFlow
from MobileApps.resources.const.android import const

class Gallery(GalleryFlow):
    flow_name="gallery"


########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################

    def open_samsung_gallery(self):
        self.driver.wdvr.start_activity(const.PACKAGE.SAMSUNG_GALLERY, const.LAUNCH_ACTIVITY.SAMSUNG_GALLERY)

    def select_share(self):
        """
        click on the share button
        :return:
        """
        try:
            self.driver.click("share_btn")
        except:
            self.driver.click("samsung_preview_screen")
            self.driver.click("share_btn")

    def select_hpps_share(self):
        """
        click on the Hp Print Service Plugin in the trapdoor flow
        :return:
        """
        value = self.driver.return_str_id_value("trapdoor_hpps_txt",project="hpps",flow="trap_door")
        self.driver.click("_system_txt_place_holder", format_specifier=[value])


    def select_more(self):
        """
        click on the more button
        :return:
        """
        try:
            self.driver.click("more_btn")
        except:
            self.driver.click("samsung_preview_screen")
            self.driver.click("more_btn")

    def select_print(self):
        """
        clicks on the print button in the more options list
        :return:
        """
        self.driver.click("print_btn")
########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################
    def verify_samsung_gallery_screen(self):
        """
        Verify the Samsung Gallery preview screen
        :return:
        """
        self.driver.wait_for_object("samsung_preview_screen")

    def verify_android_share_popup(self):
        """
        verify the android share popup appeared
        :return:
        """
        self.driver.wait_for_object("samsung_share_popup_lv")

    def verify_more_options_list(self):
        """
        verify the more options list appeared
        :return:
        """
        self.driver.wait_for_object("more_options_lv")