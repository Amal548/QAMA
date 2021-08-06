import os
import sys
import time
import copy
import json
import traceback
import langcodes
from pprint import pprint
from SAF.misc.excel import Excel
#from googletrans import Translator
from SAF.driver import driver_factory
from MobileApps.libs.ma_misc.str_id_localization import StringProcessor

if not os.path.isfile("./data.json"):
    sp = StringProcessor("android", None)
    data = sp.android_build_dict_from_xml("/work")
else:
    fh = open("data.json", "r", encoding="utf-8")
    data = json.load(fh)
    fh.close()
total = 0
data_copy = copy.deepcopy(data)
lang_dict = {
    "zh-rCN": "zh",
    "zh-rTW": "zh",

}
failed_dict={}

info_dict = {"server": {"url": "intsrv1u.sdg.rd.hpicorp.net",
                        "port": "4444"},
                     "dc":{"platform": "WINDOWS",
                           }}
driver = driver_factory.web_driver_factory("firefox", info_dict)
print("Driver started")
driver.wdvr.get("https://translate.google.com/")
driver.wdvr.maximize_window()
time.sleep(5)
def process_dl(dl):
    if "no" in dl:
        return dl.replace("no", "nb")
    else:
        return dl

def get_lang(driver, _str):
    txt_area = driver.wdvr.find_element_by_css_selector("textarea")
    try:
        driver.wdvr.find_element_by_css_selector("button[data-language-code='auto']")
        code_locator = "button[data-language-code='auto']"
    except:
        code_locator = "div.sl-sugg-button-container div[role='button']"

    while "detect language" not in driver.wdvr.find_element_by_css_selector(code_locator).text.lower():
        try:
            textarea = driver.wdvr.find_element_by_css_selector("textarea")
            textarea.clear()
            textarea.click()
            try:
                driver.wdvr.find_element_by_css_selector("button[aria-label='Clear source text']").click()
            except:
                driver.wdvr.find_element_by_css_selector("button[aria-label='Clear text']").click()
        except:
            driver.wdvr.get("https://translate.google.com/")
            time.sleep(2)
            txt_area = driver.wdvr.find_element_by_css_selector("textarea")
            print("detect lang loop")
    txt_area.send_keys(_str[:50])
    time.sleep(2)
    while True:
        detect_lang = driver.wdvr.find_element_by_css_selector(code_locator).text.lower()
        if "detected" not in detect_lang:
            textarea = driver.wdvr.find_element_by_css_selector("textarea")
            textarea.clear()
            textarea.click()
            textarea.send_keys(_str[:50])
            time.sleep(2)
            continue
        else:
            return langcodes.find(detect_lang.split(" - detected")[0]).language

def write_to_excel(str_id, lang):
    excel = Excel("./test.xlsx")
    newsheet = excel.add_sheet("result", raise_e=False)
    if newsheet:
        excel.write_new_record(["str id", "str en", "str localized", "spec lang", "google detect lang", "manual review result"])
    else:
        excel.load_sheet("result")
    str_en = lang["english_str"]
    str_localized = lang["localized_str"]
    spec_lang = lang["spec_lang"]
    detected_lang = lang["detected_lang"]
    excel.write_new_record([str_id, str_en, str_localized, spec_lang, detected_lang])
    excel.save()

def write_json(data):
    fh = open("./data.json", "w+", encoding="utf-8")
    fh.write(json.dumps(data_copy))
    fh.close()

while data_copy != {}:
    data = copy.deepcopy(data_copy)
    try:
        for key, value in data.items():
            for lang, _str in value.items():
                if _str == "":
                    continue
                dl = get_lang(driver, _str)
                if lang_dict.get(lang, lang) not in process_dl(dl) and dl != "en":
                    write_to_excel(key, {"spec_lang": lang, "detected_lang": dl, "english_str": value.get("en", ""), "localized_str": _str})
                total += 1
                try:
                    del data_copy[key][lang]
                    write_json(data_copy)
                except KeyError:
                    pass
                print("Passed: Key: " + key + " Lang: " + lang + " DL: " + dl + " Str: " + _str)
            try:
                del data_copy[key]
                write_json(data_copy)
            except KeyError:
                pass
    except:
        traceback.print_exc()
driver.close()
