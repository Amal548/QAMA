from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
import requests


class MPFAQ(HPBridgeFlow):
    flow_name = "mp_faq"

    # below are all supported printers on FAQ page
    inkjet_printers = ["HP DeskJet IA 3776/3777/3778/3779 All-in-One",
                       "HP DeskJet 2621/2622/2623/2628 All-in-One",
                       "HP DeskJet IA 2676/2677/2678 All-in-One",
                       "HP DeskJet IA 3636/3638",
                       "HP DeskJet IA 5078/5088 All-in-One",
                       "HP DeskJet IA 5278 All-in-One",
                       "HP DeskJet Ink Advantage 3838 All-in-One",
                       "HP DeskJet Ink Advantage Ultra 4729 All-in-One",
                       "HP ENVY Photo 6220/6222 All-in-One",
                       "HP Ink Tank 410/411/418/419",
                       "HP OfficeJet Pro 8010/8012 All-in-One",
                       "HP OfficeJet Pro 8020/8028 All-in-One",
                       "HP OfficeJet Pro 8710",
                       "HP OfficeJet Pro 9010/9018/9019 All-in-One",
                       "HP OfficeJet Pro 9020/9026/9028 All-in-One",
                       "HP Officejet Pro 6960",
                       "HP Officejet Pro 6970",
                       "HP Smart Tank Wireless 511/516/518/519 All-in-One",
                       "HP Smart Tank Wireless 531/538 All-in-One",
                       "HP Smart Tank Wireless 616/618/619 All-in-One",
                       "HP TangoX",
                       "HP Tango"]

    laserjet_printers = ["HP LaserJet Pro M104w All-in-One",
                         "HP LaserJet Pro MFP M132nw All-in-One",
                         "HP LaserJet Pro MFP M132snw All-in-One",
                         "HP LaserJet Pro MFP M226dw",
                         "HP LaserJet Pro MFP M227fdw",
                         "HP LaserJet Ultra M106w All-in-One",
                         "HP LaserJet Ultra MFP M230fdw"]

    jd_link = "https://mall.jd.com"

    def check_printers_in_icon_view(self):
        """
        In applet "如何打印信息页" page, check all the list printers and click each printer, verify
        erify all the printer icon can be click and go to the corresponding"如何打印信息页" page correctly.
        :return:
        """
        self.driver.wait_for_object("icon_view_list")
        printers = self.driver.find_object("icon_view_list", multiple=True)
        assert len(printers) == len(self.inkjet_printers) + len(self.laserjet_printers)

        all_printers = self.inkjet_printers[0:10]
        all_printers.extend(self.laserjet_printers)
        all_printers.extend(self.inkjet_printers[10:])

        for printer_model in all_printers:
            if not self.check_element_in_screen("printer_spec", format_specifier=[printer_model]):
                self.swipe_to_element_shown("printer_spec", format_specifier=[printer_model])
            self.driver.click("printer_spec", format_specifier=[printer_model])
            self.driver.wait_for_object("step1")
            assert self.driver.get_text("printer_model") == printer_model
            self.driver.click("top_arrow_back_btn")

    def select_icon_view(self):
        """
        Click icon view button and change the printer list to icon view list
        :return:
        """
        self.driver.click("icon_view_button")
        self.driver.wait_for_object("icon_view_list")

    def select_list_view(self):
        """
        Click list view button and change the printer list to list view list
        :return:
        """
        self.driver.click("list_view_button")
        self.driver.wait_for_object("inkjet_dropdown")

    def expand_inkjet_dropdown(self):
        """
        Click inkjet drop down button and verify the list has been expanded
        :return:
        """
        self.driver.click("inkjet_dropdown")
        self.driver.wait_for_object("list_view_list")

    def collapse_inkjet_dropdown(self):
        """
        Click inkjet drop down button and verify the list has been expanded
        :return:
        """
        self.driver.click("inkjet_dropdown")
        self.driver.wait_for_object("list_view_list", invisible=True)

    def expand_laserjet_dropdown(self):
        """
        Click inkjet drop down button and verify the list has been expanded
        :return:
        """
        self.driver.click("laserjet_dropdown")
        self.driver.wait_for_object("list_view_list")

    def collapse_laserjet_dropdown(self):
        """
        Click inkjet drop down button and verify the list has been expanded
        :return:
        """
        self.driver.click("laserjet_dropdown")
        self.driver.wait_for_object("list_view_list", invisible=True)

    def check_printers_in_list_view(self, index=None, inkjet=True):
        """
        Check the printers in the ink jet list, verify all the printer icon can be click and go to
        the corresponding "如何打印信息页" page correctly.
        :param index: if it is None, check all the printers, otherwise
        check the indicated printer with the given index
        :return:
        """
        printer_list = self.inkjet_printers if inkjet else self.laserjet_printers
        if index is None:
            for printer_model in printer_list:
                if not self.check_element_in_screen("printer_spec", format_specifier=[printer_model]):
                    self.swipe_to_element_shown("printer_spec", format_specifier=[printer_model])
                self.driver.click("printer_spec", format_specifier=[printer_model])
                self.driver.wait_for_object("step1")
                assert self.driver.get_text("printer_model") == printer_model
                self.driver.click("top_arrow_back_btn")
        elif type(index) is int:
            if not self.check_element_in_screen("printer_spec", format_specifier=[printer_list[index]]):
                self.swipe_to_element_shown("printer_spec", format_specifier=[printer_list[index]])
            self.driver.click("printer_spec", format_specifier=[printer_list[index]])
            self.driver.wait_for_object("step1")
            assert self.driver.get_text("printer_model") == printer_list[index]
            self.driver.click("top_arrow_back_btn")
        else:
            raise KeyError("Index should be None or number")

    def copy_printer_info(self):
        """
        in the icon view, and click the "Copy" button on “如何打印信息页” page.
        verify the"复制成功，请到浏览器上粘贴并打开该链接" message should be displayed.
        if we open it by browser.the "惠普打印机京东自营官方旗舰店" JD store page should be displayed.
        in this method, we use assert it is a JD link
        :return:
        """
        if not self.check_element_in_screen("copy_btn"):
            self.swipe_to_element_shown("copy_btn")
        self.driver.click("copy_btn")
        # self.driver.wait_for_object("copy_success_msg")
        assert self.jd_link in self.driver.wdvr.get_clipboard_text()

    def click_search_button(self):
        """
        in the printer info page printers view page, click the search button and goto search page
        :return:
        """
        self.driver.click("search_button")
        self.driver.wait_for_object("input_box")

    def verify_search_results(self, search_str):
        """
        Search the given string and check the results
        :param search_str:
        :return:
        """
        all_printers = self.inkjet_printers + self.laserjet_printers
        self.driver.send_keys("input_box", search_str)
        results = []
        for item in all_printers:
            if search_str in item:
                results.append(item)

        if len(results) == 0:
            self.driver.wait_for_object("no_results_msg1")
            self.driver.wait_for_object("no_results_msg2")
        else:
            for printer in results:
                self.driver.wait_for_object("search_result_spec", format_specifier=[printer])
