import pytest
from MobileApps.libs.flows.android.jweb.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def android_jweb_setup(request, android_test_setup):
    """
    This fixture is for Android Jweb set up :
        - Get driver instance
        - Get FlowContainer instance
    :param request:
    :param android_test_setup:
    :return:
    """
    driver = android_test_setup
    fc = FlowContainer(driver)
    return driver, fc