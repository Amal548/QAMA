from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import logging

class NoEmailAccount(Exception):
    pass

class SpecificEmailAccountDoesNotExist(Exception):
    pass

class Gmail(SmartFlow):
    flow_name ="gmail"
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def get_subject(self):
        """
        Get value of subject on Compose Email screen
        :return: subject :str
        """
        self.driver.wait_for_object("subject_tf", timeout=10)
        return self.driver.find_object("subject_tf").text

    def compose_email(self, to_email,from_email="", subject_text="", body_text=""):
        """
        Composes and send an email.

        :param from_email: force the phone to send email from this specific email if not set use the default one
        :param to_email: the address of the account receiving the email
        :param subject_text: Email Header
        :param body_text: Email text body

        END OF FLOW:
        """
        # try:
        #     self.driver.click("popup_ok_btn")
        # except (NoSuchElementException, TimeoutException):
        #     logging.warning("Popup of Gmail is NOT displayed")
        self.driver.wait_for_object("from_tf", timeout=10)
        screen_from_email = self.driver.find_object("from_tf").text
        if screen_from_email == "":
            raise NoEmailAccount("Phone does not have any gmail account associations")
        if from_email != "":
            try:
                self.driver.click("from_picker")
                self.driver.click("from_tf", format_specifier=[from_email])
                screen_from_email = self.driver.find_object("from_tf").text
            except NoSuchElementException:
                logging.warning("There is only one account")
                if screen_from_email != from_email:
                    raise SpecificEmailAccountDoesNotExist(
                        "The specific email you are trying to send from does not exist on this device")

        self.driver.send_keys("to_tf", to_email, check_key_sent=False)
        self.driver.wdvr.press_keycode(66)

        try:
            self.driver.send_keys("subject_tf", subject_text)
        except NoSuchElementException:
            self.check_run_time_permssion()
            self.driver.send_keys("subject_tf", subject_text)
        # Gmail app currently does not let appium send key to the body object
        # if body_text != "":
        #    self.driver.send_keys("compose_email_tf", body_text)

        self.driver.click("send_btn")
        return screen_from_email