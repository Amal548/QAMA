import os
import json
import uuid
import time
import argparse
import untangle
import subprocess

class SuiteFailedException(Exception):
    pass

class MissingRequiredProperty(Exception):
    pass

schema_version = "1"
data_env = "RealData"
performance = False
required_property = ["suite_test_platform", "suite_test_stack", "suite_test_client", "suite_test_category"]
parser = argparse.ArgumentParser(description='Convert Junit XML to Dashboard json')
parser.add_argument('-f', dest='file_name', action='store', help='The XML file path')

args = parser.parse_args()
json_data = {"event": {}}
data = untangle.parse(args.file_name)
hook_file_path = "/qama/framework/bin/report_results"

json_data["event"]["host"] = data.testsuites.testsuite["hostname"]
json_data["event"]["timestamp"] = data.testsuites.testsuite["timestamp"]
json_data["event"]["schema_version"] = schema_version
json_data["event"]["suite_test_env"] = data_env
json_data["event"]["suite_test_owner"] = "QAMA Mobile/Web Test Automation"

for _property in data.testsuites.testsuite.properties.property:
    if _property["name"] == "performance":
        performance = _property["value"] == "True"
        continue
    json_data["event"][_property["name"]] = _property["value"]

if not set(required_property).issubset(set(json_data["event"])):
    raise MissingRequiredProperty("Missing these required property: " + str(set(required_property).difference(json_data["event"])))

pass_percentage = 1 - int(data.testsuites.testsuite["failures"]) / int(data.testsuites.testsuite["tests"])
if not performance:
    json_data["event"]["suite_test_result"] = "success" if pass_percentage == 1 else "failed"
    json_data["event"]["suite_test_percentage_of_success"] = str(pass_percentage * 100) + "%"

elif performance and pass_percentage != 1:
    raise SuiteFailedException("Failed performance run does not capture data")

if performance:
    testcase_data = {"performance":{}}
else:
    testcase_data = {}
    
for testcase in data.testsuites.testsuite.testcase:
    testcase_data["suite_test_name"] = testcase["classname"]
    testcase_data["suite_test_script_name"] = testcase["file"]
    if performance:
        system_error = testcase.system_err.cdata.split("\n")
        for line in system_error:
            if "[Performance]" in line:
                p_data = line.split("-")[1]
                t_lst = p_data.split(":")
                testcase_data["performance"][t_lst[0]] = t_lst[1]
json_data["event"].update(testcase_data)

fh = open(str(uuid.uuid4()) + ".json", "w+", encoding="utf-8")
fh.write(json.dumps(json_data))
file_path = os.path.realpath(fh.name)
fh.close()

os.system(hook_file_path + " " + file_path)
os.remove(file_path)