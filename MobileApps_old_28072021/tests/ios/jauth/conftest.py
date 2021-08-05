import pytest
from MobileApps.libs.flows.ios.jauth.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def ios_jauth_setup(request, session_setup):
    """
    This fixture is for Ios Jauth set up :
        - Get driver instance
        - Get FlowContainer instance
    :param request:
    :return:
    """
    driver = session_setup
    fc = FlowContainer(driver)
    return driver, fc