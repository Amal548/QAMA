from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from time import sleep


class BaiduPrint(HPBridgeFlow):
    flow_name = "baidu_print"

    def select_baidu_print(self):
        """
        click "百度网盘打印" in home page
        :return:
        """
        self.driver.click("baidu_netdisk_print")

    def select_file(self, file_path):
        """
        Select the file from the file list, sometimes, the file will outside the current screen,
        we need to swipe the screen and check the file exist or not in current screen.
        :param file_path: the file name can be a path or just the name
        :return:
        """
        file = str(file_path).split("/")
        for path in file:
            self.swipe_to_element_shown("item_spec", format_specifier=[path])
            self.driver.click("item_spec", format_specifier=[path])
            sleep(1)

    def check_file_selected(self, file_name):
        """
        check the file, if it is selected, return true, else re turn false
        :param file_name:
        :return:
        """
        current_file = self.driver.wait_for_object("item_spec", format_specifier=[file_name])
        file_checked = self.driver.get_attribute("file_checkbox", "checked", root_obj=current_file)
        if file_checked == "true":
            return True
        else:
            return False

    def confirm_file_select(self, file_name):
        """
        Verify the file/image checkbox is checked and click "确定" button
        :return:
        """
        if not self.check_file_selected(str(file_name).split("/")[-1]):
            raise Exception("The file checkbox is not selected")
        self.driver.click("confirm_button")


