import os
import json
import logging
import argparse
import httplib2

from apiclient.discovery import build
from datetime import datetime, timedelta, date
from MobileApps.libs.ma_misc import ma_misc


from google.oauth2 import service_account
from google.auth.transport.requests import Request

class BadFilterException(Exception):
    pass

class GAComparison():
    SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
    DAT_FILE = ma_misc.get_abs_path("scripts/ga_api/analyticsreporting.dat")
    DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
    # Path to client_secrets.json file.
    # TO GET CLIENT JSON GO TO https://console.developers.google.com/apis/credentials?project=helical-client-128323
    CLIENT_SECRETS_PATH = (ma_misc.get_abs_path('scripts/ga_api/client_secret.json')) # Path to client_secrets.json file.
    # qamobileapps@gmail.com View ID
    # ID GO TO https://ga-dev-tools.appspot.com/account-explorer/ to obtain View ID
    ID_BY_OS = {"ios" : '81103606', 'android': '106657797'}

    def __init__(self, platform, view_id=None, query_filters=None):
        """Initializes GA_Comparison object.

         need to install api lib:
            su pip install --upgrade google-api-python-client

        view_id = String of the id associated to the Google Analysis project
                (the small gray number under the project name in the Views section:
                Analytics Accounts -> Properties & Apps -> View)
        query_filters: Json object that contain the search query filters [use all for best results]
                {   mobile_device_model: string value of the model device ["iPhone" for all iPhones or "Nexus 5X", "Nexus 5" ],
                    "operating_system_version": string value of the os version on the device,
                    "app_version": string value of the app version, might need to remove .ipa or .apk,
                    "city":string value of the city location the test was run in (or phone believes its in),
                }
        create_master = Collects all the data given the query filters before the tests has run to reduce test failures

        Initializes the analyticsreporting service object.
        analytics an authorized analyticsreporting service object.
        """


        if view_id is None:
            view_id = self.ID_BY_OS[platform.lower()]
        self.filters = None
        if query_filters is not None:
            self.load_filter(query_filters)


        credentials = service_account.Credentials.from_service_account_file(self.CLIENT_SECRETS_PATH)
        scoped_credentials = credentials.with_scopes(self.SCOPES)
        http = scoped_credentials.authorize(http=httplib2.Http())
        # Build the service object.
        self.analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=self.DISCOVERY_URI)
        self.view_id = view_id

    def load_filter(self, input_filter):
        #Common Filters
        #ga:mobileDeviceModel
        #ga:city
        #ga:appVersion
        #ga:operatingSystemVersion
        #ga:hour
        #ga:minute
        filters=[]
        for key, value in input_filter.iteritems():
            if type(key) is tuple and len(key) == 2:
                operator = key[1].upper()
                actual_key = key[0]
            else:
                operator = "EXACT"
                actual_key = key

            filters.append({
                        'filters': [
                            {
                                "dimensionName": actual_key,
                                "operator": operator,
                                "expressions":[value]
                            }
                        ]
                        })
        self.filters = filters


    def queue_ga_data(self, start_date=str(date.today()), end_date=str(date.today()), category=None):
        #These are the current metrics. If additional metrics is needed please raise an issue
        master_dict = {}
        metric_dict = {
                       "screen":["ga:screenviews"],
                       "event": ["ga:totalEvents"],
                       "event_without_label": ["ga:totalEvents"],
                       "timer": ["ga:avgUserTimingValue", "ga:UserTimingSample"],
                       "ecommerce": ["ga:itemRevenue", "ga:itemQuantity"]
                      }

        dimension_dict= {
                        "screen": ["ga:screenName"],
                        "event": ["ga:eventCategory", "ga:eventAction", "ga:eventLabel"],
                        "event_without_label": ["ga:eventCategory", "ga:eventAction"],
                        "timer": ["ga:userTimingCategory","ga:userTimingVariable"],
                        "ecommerce": ["ga:productName","ga:productSku", "ga:productCategoryHierarchy", "ga:productBrand", "ga:productCouponCode"]
                        }

        for key, value in metric_dict.iteritems():
            if category is not None:
                if key != category:
                    continue
            body={
                'reportRequests': [
                {
                    'viewId': self.view_id,
                    'dateRanges': [{'start_date': start_date, 'endDate': end_date}],
                    'metrics': [],
                    'dimensions': [],
                    'pageSize': 300
                }]}
            
            for item in metric_dict[key]:
                body["reportRequests"][0]["metrics"].append({'expression': item})
            for item in dimension_dict[key]:
                body["reportRequests"][0]["dimensions"].append({"name": item})

            if self.filters is not None:
                body['reportRequests'][0]['dimensionFilterClauses'] = self.filters

            master_dict = self.__parse_data(key,self.analytics.reports().batchGet(body=body).execute(), master_dict)

        master_dict["_info"] = str(date.today())
        return master_dict

    def compare_ga_data(self, web_test_result_dict, ga_test_result_dict, timer_validation_delta=20):
        """
        Compares the results from Ga website to the test results depending on the key name
        :param web_test_result_dict: data from Ga website
        :param ga_test_result_dict:  data from test result
        :return: True or False
        """
        total_result = True
        ga_test_result_data = {k.lower():v for k,v in ga_test_result_dict["data"].items()} 
        web_test_result_dict = {k.lower():v for k,v in web_test_result_dict.items()}
        ga_skip_key_list = ga_test_result_dict.get("skip", [])
    

        for key, value in ga_test_result_data.iteritems():
            key = key.lower()
            logging.info("\nComparing key: " + key + "\n")
        
            if web_test_result_dict.get(key, None) is None:
                logging.error("\n Failed: " + key + " does not exist in result pulled from the web")
                total_result = False
                continue

            if key in ga_skip_key_list:
                logging.info("\n Skipping: " + key)
                logging.info("Web data: " + str(web_test_result_dict[key]))
                logging.info("Json data: " + str(ga_test_result_data[key]))

            if ga_test_result_data[key]["type"] == "timers":
                web_count = web_test_result_dict[key]["avg_time"]
                test_count = ga_test_result_data[key]["avg_time"]
                difference = abs(test_count-web_count)
                description = "[TESTING Time for : {}] \n " \
                         "\t Average Time From Google Analytics : {}\n" \
                         "\t Average Time From Test Results : {}\n" \
                         "[RESULT : {}]".format(key, test_count, web_count, difference )
                if difference > timer_validation_delta:
                    total_result = False
                    logging.info(description)
                    logging.error("\n Failed: " + key + " time difference greater then validation time delta")

            elif ga_test_result_data[key]["type"] in ["event", "screen", "ecommerce"]:
                web_count = web_test_result_dict[key]["count"]
                test_count = ga_test_result_data[key]["count"]
                if web_count == test_count:
                    logging.debug("\n Key: " + key + "\nPassed: " + str(web_count) + " == " + str(test_count) + "\n")
                else:
                    logging.error("\n Key: " + key + "\nFailed: " + str(web_count) + " !=" + str(test_count) + "\n")
                    total_result = False

         
        if total_result:
            logging.info("\nGA result: " + "PASS\n")
        else:
            logging.info("\nGA result: " + "FAILED\n")
            logging.debug("\n Web Data: " + str(web_test_result_dict))
            logging.debug("\n Json Data: " + str(ga_test_result_dict))
            logging.debug("\n Filters: " + str(self.filters))
        return total_result
    
    def build_filter_from_info(self, info_dict):
        known_keys= ["start_time", "end_time", "country", "device_model", "city", "app_version", "os_version"]

        start_date = str(date.today())
        end_date = str(date.today())
        filter_dict = {}        

        for key, value in info_dict.iteritems():
            if key == "start_time" or key == "end_time":
                time_list = value.split("-")
                if len(time_list) >= 3:
                    if key == "start_time":
                        start_date = "-".join(time_list[:3])
                    else:
                        end_date = "-".join(time_list[:3])
                else:
                    raise BadFilterException("Bad time string: " + str(value))


                if len(time_list) == 4:
                    datetime_obj = datetime.strptime(value, "%Y-%m-%d-%H")
                    if key == "start_time":
                        operator = "NUMERIC_GREATER_THAN"
                        datetime_obj = datetime_obj - timedelta(hours=1)
                    else:
                        operator = "NUMERIC_LESS_THAN"
                        datetime_obj = datetime_obj + timedelta(hours=1)

                    filter_dict[("ga:dateHour", operator)] = datetime_obj.strftime("%Y%m%d%H")

                elif len(time_list) == 5:
                    datetime_obj = datetime.strptime(value, "%Y-%m-%d-%H-%M")

                    if key == "start_time":
                        operator = "NUMERIC_GREATER_THAN"
                        datetime_obj = datetime_obj - timedelta(minutes=1)
                    else:
                        operator = "NUMERIC_LESS_THAN"
                        datetime_obj = datetime_obj + timedelta(minutes=1)

                    filter_dict[("ga:dateHourMinute",operator)] =datetime_obj.strftime("%Y%m%d%H%M")
              


            elif key == "country":
                filter_dict["ga:country"] =  value

            elif key == "device_model":
                filter_dict["ga:mobileDeviceModel"] =value

            elif key == "city":
                filter_dict["ga:city"] =  value

            elif key == "app_version":
                filter_dict["ga:appVersion"] = value

            elif key == "os_version":
                filter_dict["ga:operatingSystemVersion"] =  value
        self.load_filter(filter_dict)
        return start_date, end_date


    def validate_ga(self, ga_json_file):
        with open(ga_json_file, "r") as fh:
            ga_data = json.loads(fh.read())

        start_date, end_date = self.build_filter_from_info(ga_data["info"])
        web_data = self.queue_ga_data(start_date=start_date, end_date=end_date)
        return self.compare_ga_data(web_data, ga_data)

    def __parse_data(self, event_type, response, base_dict):
        for report in response.get('reports', []):

            rows = report.get('data', {}).get('rows', [])
            if event_type == "timer":
                for row in rows:
                    dimensions = row.get('dimensions', [])
                    metrics = row.get('metrics', [])[0]["values"]
                    key = unicode((unicode(dimensions[0]),"TIMER",unicode(dimensions[1]))).lower()
                    value = {"count": int(metrics[1]),
                             "avg_time": float(metrics[0]),
                             "type": event_type}

                    base_dict[key] = value
            elif event_type == "ecommerce":
                for row in rows:
                    key = unicode(tuple(row.get('dimensions', [])))
                    count = int(row.get("metrics", [])[0]["values"][1])
                    total = float(row.get('metrics', [])[0]["values"][0])
                    if base_dict.get(key, None) is not None:
                        base_dict[key]["count"] += count
                        base_dict[key]["total"] += total
                    base_dict[key] = {"count": count, "type": event_type, "total": total}
            else:
                for row in rows:
                    dimensions = row.get('dimensions', [])
                    if len(dimensions) == 3:
                        category = unicode(dimensions[0])
                        action = unicode(dimensions[1])
                        label = unicode(dimensions[2])
                        dimensions = (category, action, label)
                        event_type = "event"
                    elif len(dimensions) == 2:
                        category = unicode(dimensions[0])
                        action = unicode(dimensions[1])
                        dimensions = (category, action, 'not set')
                        event_type = "event"

                    elif len(dimensions) == 1:
                        dimensions = dimensions[0]
                        event_type = "screen"

                    count = row.get('metrics', [])[0]['values'][0]
                    base_dict[unicode(dimensions).lower()] = {"count" : int(count),
                                                     "type": event_type}

        return base_dict

if __name__ == "__main__":
    #For list of operator visit https://developers.google.com/analytics/devguides/reporting/core/v4/rest/v4/reports/batchGet#DimensionFilter
    obj = GAComparison("ios")
    #obj.validate_ga("data.json")
    a = obj.queue_ga_data(start_date="2018-09-01", end_date="2018-11-20", category="ecommerce")

    #fh = open("app_settings_test1_iphone8_11.0.3_ga_data_2018-11-09 08^%15^%32.524340.json", "r")
    #data = json.loads(fh.read())
    #fh.close()
    #obj.compare_ga_data(a, data)
