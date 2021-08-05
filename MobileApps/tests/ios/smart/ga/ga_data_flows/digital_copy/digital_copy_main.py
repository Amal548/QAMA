

from MobileApps.resources.const.ios.const import *



import pytest

test_builder = ["test_suite_digital_copy.py::Test_Class::test_01_digital_copy_data_flow1",
                "test_suite_digital_copy.py::Test_Class::test_02_digital_copy_data_flow2",
                "test_suite_digital_copy.py::Test_Class::test_03_digital_copy_data_flow3"]

for test in test_builder:
    result_xml = os.path.join(RESULTS.RESULTS_FOLDER, os.path.basename(test) + '.xml')

    pytest.main(['-s', '-v',
                 '--junitxml', result_xml,
                 '--app-type', 'ga',
                 '--app-build', '6.0',
                 '--app-version', '751',
                 '--ga',
                 '--capture=sys', test])