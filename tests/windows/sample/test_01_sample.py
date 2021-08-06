from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
import pytest

pytest.app_info = "DESKTOP"
class Test_Suite_01_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup

    def test_01_sample(self):
        import pdb 
        pdb.set_trace()