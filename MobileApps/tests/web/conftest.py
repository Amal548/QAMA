import os
import uuid
import pytest

pytest.platform = "WEB"

def pytest_addoption(parser):
    web_argument_group = parser.getgroup('Web Test Parameters')
    web_argument_group.addoption("--browser-type", action = "store", default="firefox", help="Chose which type of browser you want to test with")
    web_argument_group.addoption("--platform", action="store", default="ANY", help="Specifiy what platform you want to run on")
    web_argument_group.addoption("--uuid", action="store", default=str(uuid.uuid4()), help="UUID associated with each pytest session (For jenkins)")
    web_argument_group.addoption("--detach", action="store_true", default=False, help="Detaches the browser from the driver, used for leaving browsers open after script")