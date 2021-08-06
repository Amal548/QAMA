import pytest
from MobileApps.libs.flows.ios.jweb.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def ios_jweb_setup(request, session_setup):
    """
    This fixture is for Ios Jarvis set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest Ios Reference app
    :param request:
    :param android_test_setup:
    :return:
    """
    driver = session_setup
    fc = FlowContainer(driver)
    return driver, fc