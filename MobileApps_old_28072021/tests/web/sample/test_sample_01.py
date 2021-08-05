import os
import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.wprint_test.wprint_test import WPrintTest
from MobileApps.libs.flows.web.ows.ows_printer import EmuPrinter

pytest.app_info = "SAMPLE"

class Test_Suite_Sample_Test_01(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, web_session_setup):
        self = self.__class__
        self.driver = web_session_setup

        self.sys_config = ma_misc.load_system_config_file()

    def test_sample_01(self):
        import pdb 
        pdb.set_trace()
        o = EmuPrinter(self.driver)
        import pdb 
        pdb.set_trace()