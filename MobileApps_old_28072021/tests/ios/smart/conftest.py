import pytest
import logging
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *




@pytest.fixture(scope="function", autouse=True)
def ios_smart_get_app_log(request):
    fc = request.cls.fc
    driver = request.cls.driver
    def get_app_log():
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_ios_app_log_and_publish(fc, driver, attachment_root_path, request.node.name)  
    request.addfinalizer(get_app_log)
