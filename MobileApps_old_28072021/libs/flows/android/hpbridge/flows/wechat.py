from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow, Stacks
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from time import sleep


class WeChat(HPBridgeFlow):
    flow_name = "wechat"

    def goto_pa(self):
        """
        from WeChat home page, go to HP Bridge public account device list page
        :return:
        """
        stack = utlitiy_misc.load_stack_info()
        if stack["stack"] == Stacks.DEV:
            mp_locator = "dev_public_account"
        else:
            mp_locator = "stage_public_account"
        self.launch_wechat()
        self.driver.wait_for_object("address_book_button")
        self.driver.click("address_book_button")
        self.driver.click("public_account_button")
        self.driver.click(mp_locator)

    def scan_qrcode_to_mp(self, public_account_qr_code=False):
        """
        Launch HP Bridge mini program by sacn the printer QR code
        :param:public_account_qr_code - Extend printer QR code(default) or Public QR code(set to True)
        """
        if not self.driver.find_object("qrcode_chat_page", raise_e=False):
            self.driver.press_key_home()
            self.launch_wechat()
            self.driver.wait_for_object("address_book_button")
            self.driver.click("qrcode_owner")
        self.driver.click("qrcode_list", index=-1)
        self.driver.long_press("full_screen")
        if not public_account_qr_code:
            self.driver.click("qrcode_recognize")
            self.driver.wait_for_object("mp_loading_icon", raise_e=False)
            self.driver.wait_for_object("mp_loading_icon", timeout=15, invisible=True)
        else:
            self.driver.wait_for_object("public_account_qrcode_recognize").click()

    def back_from_qrcode(self):
        """
        Go back to Wechat home page from chat window with a QR code opened
        :return:
        """
        self.driver.click("full_screen")
        self.driver.press_key_back()

    def goto_mp(self):
        """
        According to the stack parameter, launch the corresponding HP Bridge mini program
        from WeChat "my mini programs list"
        :param stack: which program going to launch
        :return:
        """
        stack = utlitiy_misc.load_stack_info()
        if stack["stack"] == Stacks.DEV:
            mp_locator = "mp_icon_dev"
        else:
            mp_locator = "mp_icon_stage"
        self.launch_wechat()
        self.driver.wait_for_object("address_book_button")
        self.driver.swipe(direction="up", per_offset=0.7)
        self.driver.wait_for_object(mp_locator)
        self.driver.click(mp_locator)
        sleep(5)

    def send_qrcode(self, qrcode_index=0, pa_qrcode=False, stage_pa_qr=True):
        """
        According the index select a qrcode from the WeChat album, and send it to "文件传输助手"
        :param qrcode_index:
        :param:pa_qrcode, public account QR code
        :param: stage_pa_qr: stage public qr code or Dev public qr code
        """
        self.launch_wechat()
        self.driver.wait_for_object("address_book_button")
        self.driver.click("qrcode_owner")
        self.driver.click("more_func")
        self.driver.click("wechat_album")
        self.driver.click("all_folder")
        if not pa_qrcode:
            self.driver.click("qrcode_folder")
            self.driver.click("img_list", index=qrcode_index)
        else:
            self.driver.click("pa_qrcode")
            if stage_pa_qr:
                self.driver.click("img_list", index=0)
            else:
                self.driver.click("img_list", index=1)
        self.driver.click("send_btn")
        self.driver.wait_for_object("qrcode_list")

    def scan_qr_code(self):
        """
        Click on Wechat home page, then click on more option menu and select scan to scan a QR code
        :return:
        """
        self.launch_wechat()
        self.driver.wait_for_object("wechat_button").click()
        self.driver.click("more_option_icon")
        self.driver.click("scan_option")
        self.driver.wait_for_object("mp_loading_icon", raise_e=False)
        self.driver.wait_for_object("mp_loading_icon", invisible=True)

