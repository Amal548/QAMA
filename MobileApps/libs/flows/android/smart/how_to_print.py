from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from MobileApps.resources.const.android.const import PACKAGE
from selenium.common.exceptions import NoSuchElementException

class HowToPrint(SmartFlow):
    flow_name = "how_to_print"

    GOOGLE_DRIVE = "google_drive"
    DROPBOX = "dropbox"
    GMAIL = "gmail"
    GOOGLE_PHOTOS = "google_photos"
    MICROSOFT_OFFICE = "microsoft_office"
    GOOGLE_CHROME = "google_chrome"
    FACEBOOK_PHOTOS = "facebook_photos"
    GOOGLE_DRIVE_TUTOR = "google_drive_tutor_txt"
    DROPBOX_TUTOR = "dropbox_tutor_txt"
    GMAIL_TUTOR = "gmail_tutor_txt"
    GOOGLE_PHOTOS_TUTOR = "google_photos_tutor_txt"
    MICROSOFT_OFFICE_TUTOR = "microsoft_office_tutor_txt"
    GOOGLE_CHROME_TUTOR = "google_chrome_tutor_txt"
    FACEBOOK_PHOTOS_TUTOR = "facebook_tutor_txt"

    #*********************************************************************************
    #                               ACTION FLOWS                                     *
    #*********************************************************************************
    def select_how_to_print_option(self, option):
        """
        Click on option of How to Print to expand/collapse its print tutor text

        End of flow: How to Print
        :param option: option of How to Print. It is class variable:
                GOOGLE_DRIVE
                DROPBOX
                GMAIL
                GOOGLE_PHOTOS
                MICROSOFT_OFFICE
                GOOGLE_CHROME
                FACEBOOK_PHOTOS
        """
        # Start at top of screen
        self.driver.scroll("google_drive", direction="up", timeout=20)
        self.driver.scroll(option, timeout=20, check_end=False).click()

    def select_open(self):
        """
        Click on Open button

        End of flow: corresponding screen based on option
        """
        self.driver.scroll("open_btn", timeout=10, check_end=False)
        self.driver.click("open_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_how_to_print_screen(self, raise_e=True):
        """
        Verify current screen is How to Print screen via:
            - Title
            - Instruction text
        """
        return self.driver.wait_for_object("title", timeout=10, raise_e=raise_e) is not False \
               and self.driver.wait_for_object("instruction_txt", timeout=10, raise_e=raise_e) is not False

    def verify_how_to_print_options(self):
        """
        Verify that 7 following options are on How to Print screen:
            + Google Drive
            + Dropbox
            + Gmail
            + Google Photos
            + Microsoft Office
            + Google Chrome
            + Facebook Photos
        """
        self.driver.wait_for_object("google_drive")
        self.driver.wait_for_object("dropbox")
        self.driver.wait_for_object("gmail")
        self.driver.wait_for_object("google_photos")
        self.driver.wait_for_object("microsoft_office")
        self.driver.wait_for_object("google_chrome")
        self.driver.wait_for_object("facebook_photos")

    def verify_how_to_print_tutor(self, invisible=False):
        """
        Verify tutor text of an option in How to Print
        :param invisible: invisible or not
        """
        self.driver.wait_for_object("tutor_details_txt", invisible=invisible, timeout=10)
        if not invisible:
            # Some last tutor at bottom.
            self.driver.scroll("open_btn", timeout=10, check_end=False)

    def verify_opened_third_party_app_screen(self, option):
        """
        Verify current screen is third party app screen which is corresponding to option
        :param option: one of following class constant
            + Google Drive
            + Dropbox
            + Gmail
            + Google Photos
            + Microsoft Office
            + Google Chrome
            + Facebook Photos
        """
        corresponding_screens = {self.GOOGLE_DRIVE: PACKAGE.GOOGLE_DRIVE,
                                 self.DROPBOX: PACKAGE.DROPBOX,
                                 self.GMAIL: PACKAGE.GMAIL,
                                 self.GOOGLE_PHOTOS: PACKAGE.GOOGLE_PHOTOS,
                                 self.MICROSOFT_OFFICE: PACKAGE.MICROSOFT_WORD,
                                 self.GOOGLE_CHROME: PACKAGE.GOOGLE_CHROME,
                                 self.FACEBOOK_PHOTOS: PACKAGE.FACEBOOK}
        if self.driver.get_current_app_activity()[0] != corresponding_screens[option]:
            raise NoSuchElementException("{} is not launched".format(option))