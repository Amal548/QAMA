import pytest
import logging
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from ios_settings.src.libs.ios_system_flow_factory import ios_system_flow_factory

pytest.platform = "IOS"

def pytest_addoption(parser):
    ios_argument_group = parser.getgroup('IOS Test Parameters')

    ios_argument_group.addoption("--app-type", action="store", default="adhoc", help="The type of app you would like to run")
    ios_argument_group.addoption("--app-build", action="store", default=None, help="The build version of the app you would like to run")
    ios_argument_group.addoption("--app-version", action="store", default=None, help="Which daily build version you would like to run")


@pytest.fixture(scope="class", autouse=True)
def clear_system_alerts(require_driver_session):
    driver = require_driver_session
    ios_system = ios_system_flow_factory(driver)
    ios_system.dismiss_software_update_if_visible()
    ios_system.select_allow_access_to_photos_popup()
    ios_system.handle_allow_tracking_popup()
