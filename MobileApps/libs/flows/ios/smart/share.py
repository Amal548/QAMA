import time
import logging
import sys
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


def ios_share_flow_factory(driver):
    os_version = driver.driver_info["platformVersion"].split(".")[0]
    for sub_cls in saf_misc.all_subclasses(Share):
        if saf_misc.is_abstract(sub_cls) or not getattr(sub_cls, "flow_name", False):
            continue
        if os_version in sub_cls.__name__:
            return sub_cls(driver)
    logging.warning("Cannot satisfy OS: {}".format(os_version))
    logging.warning("Returning default driver (Note if this doesn't work please overload method with child class)")
    return Share(driver)


class Share(SmartFlow):
    flow_name = "share"

    def select_message(self):
        self.driver.wait_for_object("message_btn").click()

    def select_mail(self):
        """
        Click on Mail on  share screen
        End of flow: New Message screen
        Device: Phone
        """
        self.driver.wait_for_object("mail_btn", timeout=20).click()
        time.sleep(2)

    def dismiss_share_mail(self):
        """
        Dismiss Share Mail
        Steps:
            - Click on Cancel button
            - Click on Delete Draft
        """
        self.driver.click("cancel_btn")
        self.driver.click("delete_draft_btn")

    def select_save_to_hp_smart(self):
        self.driver.wait_for_object("save_to_hp_smart_btn").click()

    def verify_share_popup(self):
        self.driver.wdvr.execute_script("mobile: swipe", {"direction": "up",
                                        'element': self.driver.wait_for_object("share_popup")})
        self.driver.wait_for_object("share_popup")

    def select_shared_albums(self):
        self.driver.wait_for_object("add_to_shared_albums").click()


class Share11(Share):

    def select_shared_albums(self):
        self.driver.wait_for_object("icloud_share").click()

class Share12(Share):
    pass

class Share13(Share):
    pass
class Share14(Share):
    pass
