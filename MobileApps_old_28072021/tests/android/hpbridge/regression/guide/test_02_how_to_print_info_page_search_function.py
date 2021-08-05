import pytest
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility
pytest.app_info = "hpbridge"


class TestHowToPrintInfoPageSearch(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.mp_faq = self.fc.flow["mp_faq"]

    def test_01_test_search_function(self):
        """
        Steps：
            1. User is on "Bind printer detail step guide" page
            2. Click on the search button in the upper right corner.
            3. Enter the effective search criteria and then search.
            4. Enter the invalid search criteria and then search.
        Expected:
            1. Verify all the printers should be displayed with icon View correctly. (The icon view displayed as default)
            2. Verify the search page should be displayed correctly.
            3. Verify the qualified printer should be searched out correctly.
            4. Verify there no printer to display and should be display a big "sad" symbol.
                The message is shown as: 没有找到相关的打印机请尝试输入其它关键字
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.select_add_printer()
        self.mphome.goto_print_info_page()
        self.mp_faq.click_search_button()
        self.mp_faq.verify_search_results("622")
        self.mp_faq.verify_search_results("asdfghjkl")
        self.mp_faq.verify_search_results(RandomUtility.generate_digit_strs(3))
