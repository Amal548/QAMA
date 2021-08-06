import os
import json
import pytest
import logging
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc

def pytest_addoption(parser):
    android_ga_argument_group = parser.getgroup('Android Smart GA Test Parameters')
    android_ga_argument_group.addoption("--ga-path", action="store", default=None, help="path of GA result in json")


@pytest.fixture(scope="class", autouse=True)
def android_smart_save_ga_result(request):
    """
    Save ga_result to a customize path. If customize_path is None, using default path
        /results/<platformName>/<deviceName_udid>/ga/result.json
    If the file is existed, then result will merge with it.
    :return:
    """
    def ga_suite_teardown():
        driver = request.cls.driver
        path = request.config.getoption("--ga-path") if request.config.getoption(
            "--ga-path") else "{}ga/result.json".format(pytest.test_result_folder)
        if request.config.getoption("--ga"):
            ma_misc.create_dir(path[:path.rfind("/")])
            if not os.path.exists(path):
                with open(path, 'w') as outfile:
                    json.dump({"data":{}}, outfile, indent=4)
            temp = saf_misc.load_json(path)["data"]
            ga_result = driver.ga_container.ga_data
            for id in temp:
                if id in ga_result["data"]:
                    ga_result["data"][id]["count"] += temp[id]["count"]
                else:
                    ga_result["data"][id] = temp[id]
            with open(path, 'w') as outfile:
                json.dump(ga_result, outfile, indent=4)

            ma_misc.publish_to_junit(path)

    request.addfinalizer(ga_suite_teardown)

    

    
