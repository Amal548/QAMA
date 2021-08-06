from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Message(SmartFlow):
    flow_name = "message"

    def verify_new_message_screen(self, timeout=10):
        self.driver.wait_for_object("new_message_title", timeout=timeout)
        self.driver.wait_for_object("to_textfield", timeout=timeout)
        self.driver.wait_for_object("_shared_cancel", timeout=timeout)
        self.driver.wait_for_object("message_body_textfield", timeout=timeout)

    def compose_message(self, to_input, body_input=''):
        self.driver.send_keys("to_textfield", to_input, press_enter=True)
        if body_input:
            self.driver.send_keys("message_body_textfield", body_input)
        self.driver.wait_for_object("send_btn").click()
