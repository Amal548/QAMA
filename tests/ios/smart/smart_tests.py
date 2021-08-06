from MobileApps.resources.const.ios.const import *

import pytest

test_builder = [

               # "test_inos.py::Test_Class::test_01_home_max_ga",

               # "test_inos.py::Test_Class::test_02_app_settings_max_ga",
               #
               # "test_inos.py::Test_Class::test_03_digital_copy_max_ga",
               #
               #  "test_inos.py::Test_Class::test_04_photos_max_ga",
               #
               #  "test_inos.py::Test_Class::test_05_files_max_ga",
               #
                 "test_inos.py::Test_Class::test_06_scan_max_ga",
               #
               #  "test_inos.py::Test_Class::test_07_scan_by_camera_max_ga",
               #
               #  "test_inos.py::Test_Class::test_08_help_center_max_ga"
                ]

ga_result = "{}/ga/data.json".format(RESULTS.RESULTS_FOLDER)

for test in test_builder:
    result_xml = os.path.join(RESULTS.RESULTS_FOLDER, os.path.basename(test) + '.xml')

    pytest.main(['-s',
                 '-v',
                 '--junitxml', result_xml,
              #  '--app-type', 'ga',
                 '--ga',
                 '--ga-path', ga_result,
                 '--capture=sys', test])
