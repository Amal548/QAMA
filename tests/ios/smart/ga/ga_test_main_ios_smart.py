from MobileApps.resources.const.ios.const import *
import pytest
import os

test_builder = {

                "APP_SETTINGS": "./app_settings/test_suite_01_app_settings_ga.py::Test_Class::test_01_app_settings_max_ga",

                "CAMERA":"./camera/test_suite_01_scan_from_camera_ga.py::Test_Class::test_02_scan_by_camera_print_edit_max_ga",

                "DIGITAL_COPY":"./digital_copy/test_suite_01_digital_copy_ga.py::Test_Class::test_01_digital_copy_max_ga",

                "FILES": "./files/test_suite_01_files_ga.py::Test_Class::test_01_files_max_ga",

                "HELP_CENTER":"./help_center/test_suite_01_help_center_ga.py::Test_Class::test_01_help_center_max_ga",

                 "HOME":"./home/test_suite_01_home_ga.py::Test_Class::test_01_home_max_ga",

                "PHOTOS": "./photos/test_suite_01_photos_ga.py::Test_Class::test_01_photos_max_ga",

                "SCAN":"./scan/test_suite_01_scan_from_printer_ga.py::Test_Class::test_02_scan_edit_ga_coverage_flow_1",


            }
test_flow = os.environ.get("TEST_FLOW", "CAMERA").split(',')


ga_result = "{}/ga/data.json".format(RESULTS.RESULTS_FOLDER)

for test in test_flow:
    test_case_name = test_builder[test]
    print (test_case_name)

    ga_result = test.split('::')[-1]
    result_xml = os.path.join(RESULTS.RESULTS_FOLDER, test.split('::')[-1] + '.xml')

    pytest.main(['-s',
                 '-v',
                 '--junitxml', result_xml,
                 #'--app-type', 'ga',
                 '--ga',
                 '--ga-path', ga_result,
                 '--capture=sys', test_case_name])