# coding: utf-8
import logging
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from time import sleep


class PrintFlow(HPBridgeFlow):
    flow_name = "print_flow"
    # test_device = utlitiy_misc.load_user_device()[1]["device_name"]

    def select_file_print(self):
        """
        Click on the file print category on mini program home page
        :return:
        """
        self.driver.wait_for_object("file_print").click()

    def select_picture_print(self):
        """
        Click on the picture print category on mini program home page
        :return:
        """
        self.driver.wait_for_object("picture_print").click()

    def select_invoice_print(self):
        """
        Click on the invoice print category on mini program home page
        :return:
        """
        self.driver.wait_for_object("invoice_print").click()

    def select_from_chat_history(self):
        """
        Click on the selection from chat history
        :return:
        """
        self.driver.wait_for_object("select_from_chat_history").click()

    def select_from_baidu_disk(self):
        """
        Click on the selection from baidu net disk
        :return:
        """
        self.driver.wait_for_object("select_from_baidu_disk").click()

    def select_from_local_storage(self):
        """
        Click on the selection from local storage
        :return:
        """
        self.driver.wait_for_object("select_from_local_storage").click()

    def click_cancel_btn(self):
        """
        Click on the cancel button
        :return:
        """
        self.driver.wait_for_object("cancel_button").click()

    def select_take_photo(self):
        """
        Click on the take photo button
        :return:
        """
        self.driver.wait_for_object("take_photo").click()

    def take_photo_process(self):
        """
        The flow after select take photo option, since the xpath for shutter button for each device is different,
        so please update the jason file if more mobile devices added
        """
        self.driver.wait_for_object(("click_shutter_" + self.test_device).lower().replace(" ", "_")).click()
        self.driver.wait_for_object(("take_photo_confirm_" + self.test_device).lower().replace(" ", "_")).click()
        self.driver.wait_for_object("complete_btn").click()

    def select_from_album(self):
        """
        Click on the selection from cell phone album.
        """
        self.driver.wait_for_object("select_from_album").click()

    def pick_a_photo(self,  index=0, scope=None):
        """
        The select a photo from album process, select a picture from the album, using index to choose which picture
         will be used
        """
        if scope and scope != "所有图片":
            self.driver.wait_for_object("all_picture_folder").click()
            self.driver.click("picture_folder_spec", format_specifier=scope)
            sleep(1)
        self.driver.wait_for_object("picture_select_list", index=index).click()
        self.driver.click("complete_btn")

    def select_img_from_chat_history(self, index=0):
        """
        Click on the selection from cell chat history, and select a picture from the "文件传输历史" history,
        using index to choose which picture will be used
        :return:
        """
        self.driver.wait_for_object("file_transfer_history").click()
        self.driver.wait_for_object("picture_select_list", index=index).click()
        self.driver.click("select_confirm")

    def select_doc_from_chat_history(self, file_name):
        """
        Click on the selection from cell chat history, and select a document from the "文件传输历史" history,
        using index to choose which picture will be used
        :return:
        """
        self.driver.wait_for_object("file_transfer_history").click()
        self.driver.wait_for_object("test_docs", format_specifier=[file_name]).click()
        self.driver.click("select_confirm")

    def verify_select_options_exist(self, picture_print=True):
        """
        Verify the options for "拍照"/"从手机相册选择"/"从聊天记录选择/从百度网盘选择" and "取消" should be displayed correctly
        after click file print
        :param: picture_print: The default print flow is picture print which set to True, otherwise, it's file print flow
        """
        if picture_print:
            logging.info("Testing the print options in picture print flow")
            self.select_take_photo()
            self.driver.wait_for_object(("click_shutter_" + self.test_device).lower().replace(" ", "_"))
            self.driver.press_key_back()
            self.select_picture_print()
            self.select_from_album()
            self.driver.wait_for_object("all_picture_folder")
            self.driver.press_key_back()
            self.select_picture_print()
            self.select_from_chat_history()
            self.driver.wait_for_object("file_transfer_history")
            self.driver.press_key_back()
            self.select_picture_print()
            self.select_from_baidu_disk()
            self.driver.wait_for_object("baidu_account_txt")
            self.driver.press_key_back()
            self.select_picture_print()
            self.click_cancel_btn()
        else:
            logging.info("Testing the print options in file print flow")
            self.select_from_chat_history()
            self.driver.wait_for_object("file_transfer_history")
            self.driver.press_key_back()
            self.select_file_print()
            self.select_from_baidu_disk()
            self.driver.wait_for_object("baidu_account_txt")
            self.select_file_print()
            self.driver.wait_for_object("select_from_local_storage")
            self.click_cancel_btn()

