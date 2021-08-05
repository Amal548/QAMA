from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow

class LocalPhotos(SmartFlow):
    flow_name = "local_photos"

    ACC_FACEBOOK = ["facebook_account", "facebook_account_with_ga"]
    ACC_INSTAGRAM = ["instagram_account", "instagram_account_with_ga"]

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def select_album(self, album_name):
        """
        At Select Photo screen:
            - Click on target album by name
        Note: -> Album should have some photos. (4 or 5 is good)
        :param album_name: album's name
        """
        self.verify_select_photo_screen()
        if not self.driver.scroll("photo_album_title", format_specifier=[album_name], scroll_object="photos_lv", timeout=60, check_end=False, click_obj=True, raise_e=False):
            self.driver.scroll("photo_album_title", direction="up", format_specifier=[album_name],scroll_object="photos_lv", timeout=60, check_end=False, click_obj=True)

    def select_album_photo_by_index(self, album_name, photo_index=1):
        """
        At Select Photo screen:
            - Click on target album by name
            - Select its photo by index number
        Note: At screen of target album, photo_index only apply all elements at first list.
              -> Album should have some photos. (4 or 5 is good)
              PHOTO THUMBNAIL STARTS INDEX AT 1
        End of flow: Landing Page or Select Photo screen based on types of photo
                        + supported type such as png,jpg,...: Landing Page
                        + unsupported type: stay at Select Photos screen
        :param album_name: album's name
        :param photo_index: index number of photo
        """
        self.verify_select_photo_screen()
        if not self.driver.scroll("photo_album_title", format_specifier=[album_name], scroll_object="photos_lv",timeout=90, check_end=False, raise_e=False):
            self.driver.scroll("photo_album_title", direction="up", format_specifier=[album_name],scroll_object="photos_lv", timeout=90, check_end=False)
        self.driver.click("photo_album_title", format_specifier=[album_name])
        self.driver.click("photo_thumbnail", index=photo_index)

    def select_cancel_btn(self):
        """
        Click on X button on Select a photo screen
        """
        self.driver.click("close_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_select_photo_screen(self):
        """
        Verify that current screen is 'Select a Photos' via:
            - It's title
        """
        self.driver.wait_for_object("select_photo_title")
