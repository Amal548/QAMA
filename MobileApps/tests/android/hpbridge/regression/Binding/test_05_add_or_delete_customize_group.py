# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility

pytest.app_info = "hpbridge"


class TestAddOrDeleteGroup(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mp_home = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]

        # Define variables
        self.api_utility = APIUtility()
        self.regular_group_name = RandomUtility.generate_digit_letter_strs(5)
        self.long_group_name = RandomUtility.generate_chinese(6)

        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. The test printer has been enabled webservice and got the welcome page with QR code
        """
        self.api_utility.unbind_all_printers()

    def test_01_add_and_delete_group(self):
        """
        Steps:
            1. Scan the QR code to binding the device go to the "绑定打印机" page.
            2. Click the "+" to add custom groups under the "请选择分组" on the binding device page.
            3. Enter the correctly characters and no more than 5 characters in the input box. Click the "完成" button.
            4. Click the "+" to add another custom groups.
            5. Enter the other valid group name and then click the "完成" button.
            6. Long press the new added group name.
            7. Click the "x" button.
            8. Long press the default three groups "客厅" , "卧室" , "书房" name

        Expected result:
            1. Verify the input box should be displayed and user can add custom groups.
            2. Verify the new group should be displayed with highlighted and default selection correctly.
            3. Verify there is a "x" button at the top right corner of the group name.
            4. Verify the current group can be deleted successfully.
            5. Verify there is no "x" button appear at the top right corner of group name.
            6. Verify the default three groups "客厅" , "卧室" , "书房" can not be deleted successfully.
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.add_group(self.regular_group_name)

        self.binding.remove_group(self.regular_group_name)

        self.binding.verify_remove_default_groups()

    def test_02_error_handling_for_adding_custom_groups(self):
        """
        Steps:
            1. Scan the QR code to binding the device go to the "绑定打印机" page.
            2. Click the "+" to add custom groups under the "请选择分组" on the binding device page.
            3. Enter the "various characters" or more than 5 characters in the input box. Click the "完成" button
            4. Enter the correctly characters and no more than 5 characters in the input box. Click the "完成" button.
            5. Click the "+" to add another custom groups. Enter an existing group name and then click the "完成" button.
            6. Continue to add new groups and ensure that there are eight existing groups. Click the "+" to add ninth group.
        Expected results:
            1. Verify the input box should be displayed and user can add custom groups.
            2. Verify the error message "1-5个字符，可输入中文，字母，数字，中划线，空格" should be displayed correctly.
            3. Verify the new group should be added successfully and displayed on the last.
            4. Verify the error message "相同名称不能重复使用" should be displayed correctly.
            5. Verify the error message "只能有8个分组" should be displayed correctly.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.add_group(self.long_group_name)
        self.binding.verify_prompt_message_add_group()
        self.binding.add_more_groups(group_num=5)
        self.binding.click_add_btn()
        self.binding.verify_eight_group_limit_message()


