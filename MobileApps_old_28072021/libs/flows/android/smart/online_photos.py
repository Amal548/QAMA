from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import package_utils
from time import sleep


class OnlinePhotos(SmartFlow):
    flow_name = "online_photos"
    FACEBOOK_TXT = "facebook_txt"
    INSTAGRAM_TXT = "instagram_txt"
    GOOGLE_PHOTOS_TXT = "google_photos_txt"

    # *********************************************************************************
    #                                GENERAL FLOWS                                    *
    # *********************************************************************************

    # ---------------------     ACTION FLOWS       ------------------------------------
    def select_album(self, album):
        """
        Select a Facebook album
        :param album: album's name
        """
        self.driver.scroll("album_name", direction="down", format_specifier=[album], timeout=30, check_end=False).click()

    def select_single_photo(self, index = 0):
        """
        Select a photo by tapping on the thumbnail - index
        End of flow: Landing Page
        """
        self.driver.wait_for_object("photo_thumbnail", timeout=10)
        sleep(5)   # completely loading thumbnails - solve Instagram's issue
        self.driver.click("photo_thumbnail", index=index)

    def select_multiple_photos(self, num):
        """
        Select multiple photos by:
            - Long press at first photos.
            - Continue selecting multiple photos until reaching num
        Note: Be used to select single photo by this way.
        :param num: number of selected photos
        End of flow: number of photos are selected
        """
        self.driver.wait_for_object("photo_thumbnail", timeout=10)
        sleep(5)  # completely loading thumbnails - solve Instagram's issue
        if num > 0:
            self.driver.long_press(self.driver.find_object("photo_thumbnail", index=0))
            photos = self.driver.find_object("photo_thumbnail", multiple=True)
            for index in range(1, num):
                photos[index].click()

    def select_next(self):
        """
        Click on Next button that is on multiple selection screen of photos
        End of flow: Landing Page
        """
        self.driver.click("next_btn")

    def get_number_selection(self):
        """
        Get number of selected photos
        :return: number of selected photos
        """
        return self.driver.find_object("selected_num_txt").text

    def select_x_icon(self):
        """
        Click on X icon on multiple selection screen
        End of flow: Online Photos screen
        """
        self.driver.click("exit_icon_btn")


    # ---------------------     VERIFICATION FLOWS       ------------------------------
    def verify_online_photos_screen(self, acc_type):
        """
        Verify Online Photos album screen
            - title
            - list of albums/thumbnails
        :param acc_type: type of acc (Facebook or Instagram). Use class variable:
                            - FACEBOOK_TXT
                            - INSTAGRAM_TXT
                            - GOOGLE_PHOTOS_TXT
        """
        self.driver.wait_for_object(acc_type)
        if acc_type == self.FACEBOOK_TXT or acc_type == self.GOOGLE_PHOTOS_TXT:
            self.driver.wait_for_object("album_list", timeout=10)
        elif acc_type == self.INSTAGRAM_TXT:
            self.driver.wait_for_object("photo_thumbnail", timeout=10)
        else:
            raise NoSuchElementException("Current screen is not {} screen".format(self.get_text_from_str_id(acc_type)))

    def verify_multi_selection_screen(self):
        """
        Verify Multi-Selection screen of a Online Photos via:
            - Exit icon button
            - Number of selection text
            - Next button
        """
        self.driver.wait_for_object("exit_icon_btn")
        self.driver.wait_for_object("selected_num_txt")
        self.driver.wait_for_object("next_btn")

    def verify_over_10_selections_screen(self):
        """
        Verify Muli-Selection screen with more than 10 photos via:
            - Exit icon button
            - 10 text
            - Next button
        """
        self.driver.wait_for_object("over_10_photos_exit_icon_btn")
        self.driver.wait_for_object("next_btn")
        if self.driver.find_object("selected_num_txt").text != "10":
            raise NoSuchElementException("Number of selection is not equal to 10 photos!")

    def verify_album_detail_screen(self, acc_type):
        """
        Verify Album screen of an Online Photos
        :param acc_type: type of acc (Facebook or Instagram). Use class variable:
                            - FACEBOOK_TXT
                            - INSTAGRAM_TXT
                            - GOOGLE_PHOTOS_TXT
        """
        self.driver.wait_for_object(acc_type)
        self.driver.wait_for_object("photo_thumbnail")

    # *********************************************************************************
    #                                FACEBOOK FLOWS                                   *
    # *********************************************************************************
    def select_fb_account(self, account_name, raise_e=True):
        """
        Click on account name of FB
        """
        return self.driver.click("fb_account_name", format_specifier=[account_name], raise_e=raise_e)

    def select_fb_confirmation_continue(self):
        """
        Click Continue button on confirmation screen
        """
        self.driver.click("fb_confirmation_continue_btn", change_check={"wait_obj": "fb_confirmation_continue_btn", "invisible": True})

    def login_to_fb(self, username, password):
        """
        Login to Facebook with username and password
        """
        self.driver.wait_for_object("fb_login_username_tf").send_keys(username)
        self.driver.wait_for_object("fb_login_password_tf").send_keys(password)
        sleep(1)
        self.driver.click("fb_login_btn", change_check={"wait_obj": "fb_login_btn", "invisible": True})
        self.driver.wait_for_object("fb_login_continue_btn").click()

    def verify_fb_login_confirmation_screen(self, raise_e=True):
        """
        Verify facebook login confirmation screen
        """
        return self.driver.wait_for_object("fb_login_title", timeout=20, raise_e=raise_e) is not False \
               and self.driver.wait_for_object("fb_confirmation_continue_btn", raise_e=raise_e) is not False

    def verify_fb_login_screen(self, raise_e=True):
        """
        Verify facebook login screen
        """
        return self.driver.wait_for_object("fb_login_username_tf", raise_e=raise_e) is not False \
            and self.driver.wait_for_object("fb_login_password_tf", raise_e=raise_e) is not False

    def verify_fb_album_screen(self, raise_e=True):
        """
        Verify current screen is fb's album
        """
        return self.driver.wait_for_object("facebook_txt", raise_e=raise_e) is not False and \
                self.driver.wait_for_object("album_name", raise_e=raise_e) is not False

    # *********************************************************************************
    #                                GOOGLE PHOTOS FLOWS                              *
    # *********************************************************************************
    def google_photos_login(self, username):
        """
        - Choose an account on Choose Account popup
        - Allow access
        :param username: username
        """
        self.driver.wait_for_object("google_photos_choose_account_popup", timeout=10)
        self.driver.click("google_photos_choose_acc_txt", format_specifier=[username])
        self.driver.wait_for_object("google_photos_access_allow_btn")
        self.driver.click("google_photos_access_allow_btn")