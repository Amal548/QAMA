import pytest
import random
pytest.app_info = "hpbridge"


class TestHowToPrintInfoPage(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.mp_faq = self.fc.flow["mp_faq"]

    def test_01_check_printers_icon_view(self):
        """
        Steps：
            1. On "FAQ - 如何打印信息页" page.
            2. Click all the printer displayed with icon view.
        Expected:
            1. Verify the printer icon and model name should be displayed correctly.
            2. Verify all the printer icon can be click and go to the corresponding"如何打印信息页" page correctly.
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.select_add_printer()
        self.mphome.goto_print_info_page()
        self.mp_faq.check_printers_in_icon_view()

    def test_02_check_printers_inkjet_list(self):
        """
        Steps:
            1. Click on the list view button in the upper right corner.
            2. Click on the "喷墨打印机".
            3. Click on the "喷墨打印机" again.
            4. Click on the "喷墨打印机" to expand all "喷墨打印机".
                Click on one printer.
        Expected:
            1. Verify all the printer should be displayed with list View correctly. (All printers are classified as inkjet printers and laser printers)
            2. Verify the list below should be automatically expand with all "喷墨打印机" correctly.
            3. Verify the list below should be automatically contraction correctly.
            4. Verify the "如何打印信息页" should be displayed with the printer correctly.
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.select_add_printer()
        self.mphome.goto_print_info_page()
        self.mp_faq.select_list_view()
        self.mp_faq.expand_inkjet_dropdown()
        self.mp_faq.collapse_inkjet_dropdown()
        self.mp_faq.expand_inkjet_dropdown()
        self.mp_faq.check_printers_in_list_view(inkjet=True, index=random.randint(0, 21))

    def test_03_check_printers_lasterjet_list(self):
        """
        Steps:
            1. Click on the list view button in the upper right corner.
            2. Click on the "激光打印机" .
            3. Click on the "激光打印机" again.
            4. Click on the "激光打印机" to expand all "激光打印机".
                Click on one printer.
        Expected:
            1. Verify all the printer should be displayed with list View correctly. (All printers are classified as inkjet printers and laser printers)
            2. Verify the list below should be automatically expand with all "激光打印机" correctly.
            3. Verify the list below should be automatically contraction correctly.
            4. Verify the "如何打印信息页" should be displayed with the printer correctly.

        :return:
        """
        self.wechat.goto_mp()
        self.mphome.select_add_printer()
        self.mphome.goto_print_info_page()
        self.mp_faq.select_list_view()
        self.mp_faq.expand_laserjet_dropdown()
        self.mp_faq.collapse_laserjet_dropdown()
        self.mp_faq.expand_laserjet_dropdown()
        self.mp_faq.check_printers_in_list_view(inkjet=False, index=random.randint(0, 6))

    def test_04_copy_printer_info(self):
        """
        Steps:
            1. Click the "Copy" button on “如何打印信息页” page.
            2. Open the browser and paste the link.
            3. Check the UI.
        Expected:
            1. For step1: The"复制成功，请到浏览器上粘贴并打开该链接" message should be displayed.
            2. For step3: The "惠普打印机京东自营官方旗舰店" JD store page should be displayed.

        :return:
        """
        self.wechat.goto_mp()
        self.mphome.select_add_printer()
        self.mphome.goto_print_info_page()
        self.mp_faq.copy_printer_info()
