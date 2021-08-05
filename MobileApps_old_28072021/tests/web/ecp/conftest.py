import pytest
from MobileApps.libs.flows.web.ecp.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def ecp_setup(request, web_session_setup):
    """
    This fixture is for Android Jweb set up :
        - Get driver instance
        - Get FlowContainer instance
    :param request:
    :param android_test_setup:
    :return:
    """
    driver = web_session_setup
    fc = FlowContainer(driver)
    return driver, fc