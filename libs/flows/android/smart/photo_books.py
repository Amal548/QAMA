from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import logging

class PhotoBooks(SmartFlow):
    flow_name="photo_books"
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_no_thanks(self):
        """
        Click on No Thanks button on Create Photo Books screen
        """
        self.driver.click("no_thanks_btn")

    def select_get_my_photo_book(self):
        """
        Click on Get My Photo Book button on Create Photo Books screen
        """
        self.driver.click("get_my_photo_book_btn")

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_create_photo_books_screen(self):
        """
        Verify Create Photo Books screen with:
           + Title
           + Get my Photo Book button
           + No Thanks button
        """
        self.driver.wait_for_object("create_photo_books_title")
        self.driver.wait_for_object("get_my_photo_book_btn")
        self.driver.wait_for_object("no_thanks_btn")