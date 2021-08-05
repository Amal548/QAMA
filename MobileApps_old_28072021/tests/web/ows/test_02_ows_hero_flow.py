import time
import pytest
import traceback

pytest.app_info = "OWS"

class Test_OWS_Hero_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup, request):
        self = self.__class__
        self.driver, self.emu_platform, self.ows_printer, self.fc = ows_test_setup

    def test_01_test(self, request, subtests):
        pytest.subtests = subtests
        if request.config.getoption("--browser-type") in ["chrome", "edge"] and self.emu_platform in ["IOS", "Android"]:
            pytest.skip()
        steps_to_run = [status["name"] for status in self.ows_printer.oobe_status_list if status["state"] != "completed"]
        steps_to_run.append(False)
        timeout_start=time.time()
        #Want to have a timeout=5 mins after which the while loop should end 
        fail_test=False
        while len(steps_to_run) > 1 and time.time() < timeout_start+300:
            if steps_to_run[1] is False:
                step_name = "end"      
            else:
                step_name = steps_to_run[1]
            with subtests.test(msg="Running OOBE step: " + step_name):
                try:
                    assert self.fc.navigate_ows(self.ows_printer, stop_at=step_name) is True
                except:
                    traceback.print_exc()
                    fail_test = True
                    assert False

            if fail_test:
                raise AssertionError("Test failed (hard) on step: " + step_name)
            steps_to_run = [status["name"] for status in self.ows_printer.oobe_status_list if status["state"] != "completed"]
            steps_to_run.append(False)