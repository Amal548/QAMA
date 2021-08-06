import re
from SAF.misc.couch_wrapper import CouchWrapper

class lst_db(object):
    def __init__(self, db,  db_info):
        self.db = CouchWrapper(db_info["url"], db , (db_info["user"], db_info["password"]))

    def get_record_list(self):
        db_rec = self.db.getAllViewResults("get_info", "rec_list")
        rec_list = {}
        for row in db_rec.rows:
            rec_list[row.key] = row.value
        return rec_list

    def get_record(self, rec_id, os_type):
        db_rec = self.db.getViewResultByKey("get_info", "rec_by_id", startKey=[os_type, rec_id], endKey=[os_type, rec_id])
        if len(db_rec.rows) != 1:
            print "More or less than one record with key: " + rec_id + " " + os_type
            sys.exit()
        else:
            return db_rec.rows[0]["value"]

    def save_record(self, data):
        self.db.saveRecord(data, doc_id = data["_id"])




if __name__=="__main__":
    match = 0
    mismatch = 0
    corrupt_data = 0
    db = lst_db("ma_app_strings_aio_ios", {"url": "https://saldb06.vcs.rd.hpicorp.net/", "user":"service", "password":"service"})
    db2 = lst_db("lst_records", {"url": "https://saldb06.vcs.rd.hpicorp.net/", "user":"service", "password":"service"})

    rec = db.db.getAllViewResults("ios_aio", "ios_aio_all")
    allRec = db2.db.getAllViewResults("get_info", "rec_by_id")
    for r_rec in allRec:
        if r_rec.key[0] == "ios":
            curRec = r_rec

    for row in rec.rows:
        app_str = {}
        spec_str = {}
        #print row["key"]
        if curRec["value"]["result_str_dict"].get(row["key"], None) is not None:
            if row["value"].get("str_APP", None) is None or row["value"].get("str_SPECIFICATION", None) is None:
                corrupt_data += 1
                continue
            for key, value in row["value"]["str_APP"].iteritems():
                if key == "filename":
                    continue
                actual_key = key.split("_")[1]
                if "-" in actual_key and "zh" not in actual_key:
                    if "en" in actual_key:
                        continue
                    actual_key = actual_key.split("-")[0]
                if value != "" and value != "<empty>":
                    app_str[actual_key] = value.encode("utf-8").decode("string_escape").decode("utf-8").strip()
            for key, value in row["value"]["str_SPECIFICATION"].iteritems():
                if key == "filename":
                    continue
                actual_key = key.split("_")[1]
                if "-" in actual_key and "zh" not in actual_key:
                    if "en" in actual_key:
                        continue
                    actual_key = actual_key.split("-")[0]
                if value != "" and value != "<empty>":
                    if type(value) == list:
                        value = value[0]
                    spec_str[actual_key] = re.sub(r'[\r\n\t]+', r'', value).replace(u"\\\u2019", u"\u2019").encode("utf-8").decode("string_escape").decode("utf-8").strip()

            if app_str.get("ar", None) is not None: del app_str["ar"]
            if app_str.get("he", None) is not None: del app_str["he"]
            if spec_str.get("ar", None) is not None: del spec_str["ar"]
            if spec_str.get("he", None) is not None: del spec_str["he"]

            if curRec["value"]["apk_str_dict"].get(row["key"], {}).get("pt-BR", None) is not None: 
                curRec["value"]["apk_str_dict"].get(row["key"], {})["pt"] = curRec["value"]["apk_str_dict"].get(row["key"], {}).get("pt-BR", None)
                del curRec["value"]["apk_str_dict"].get(row["key"], {})["pt-BR"]

            if curRec["value"]["spec_str_dict"].get(row["key"], {}).get("pt-BR", None) is not None: 
                curRec["value"]["spec_str_dict"].get(row["key"], {})["pt"] = curRec["value"]["spec_str_dict"].get(row["key"], {}).get("pt-BR", None)
                del curRec["value"]["spec_str_dict"].get(row["key"], {})["pt-BR"]

            if app_str == curRec["value"]["apk_str_dict"].get(row["key"], {}) and spec_str == curRec["value"]["spec_str_dict"].get(row["key"], {}):
                curResult = curRec["value"]["result_str_dict"][row["key"]]["result"]
                curReason = curRec["value"]["result_str_dict"][row["key"]]["reason"]
                if row["value"]["status"].lower() == "failed":
                    cr_id = row["value"]["comments"].split('\n')[0].split("]")[0].split("AIOA")[-1].replace("]", "")
                    try:
                        cr_id = int(cr_id)
                    except ValueError:
                        cr_id = None
                    if cr_id is not None:
                        curRec["value"]["result_str_dict"][row["key"]]["cr"] = cr_id

                    curResult = "failed"
                    curReason = "[0][failed]" + row["value"]["comments"].split('\n')[0].split("] ")[-1]
                    #print curRec["value"]["result_str_dict"][row["key"]]
                elif row["value"]["status"].lower() == "n/a" or row["value"]["status"].lower() == "removed":
                    if curResult != "removed":
                        curReason = curReason.replace("[" + curResult + "]", "[removed]")    
                        curResult = "removed"
                elif row["value"]["status"].lower() == "passed":
                    if curResult != "passed":
                        curReason = curReason.replace("[" + curResult + "]", "[passed]")                       
                        curResult = "passed"
                elif row["value"]["status"].lower() == "not test":
                    if curResult != "not test":
                        curReason = curReason.replace("[" + curResult + "]", "[not test]")                       
                        curResult = "not test"

                curRec["value"]["result_str_dict"][row["key"]]["reviewed"] = True 
                curRec["value"]["result_str_dict"][row["key"]]["reason"] = curReason
                curRec["value"]["result_str_dict"][row["key"]]["result"] = curResult
            else:
                continue

                #import pdb 
                #pdb.set_trace()
                #print app_str
                #print curRec["value"]["apk_str_dict"].get(row["key"], {})
                #print spec_str 
                #print curRec["value"]["spec_str_dict"].get(row["key"], {})
                #import pdb
                #pdb.set_trace()

    db2.save_record(curRec["value"])