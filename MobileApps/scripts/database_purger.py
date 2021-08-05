from SAF.misc.couch_wrapper import CouchWrapper

couchdb_info = {"url": "https://saldb06.vcs.rd.hpicorp.net/", "user":"service", "password":"service"}
db = CouchWrapper(couchdb_info["url"], "spl_printer_lock_records" , (couchdb_info["user"], couchdb_info["password"]))
view_list = db.getAllViewResults("moobe_printer", "printerListBySerial")
for item in view_list.rows:
    db.deleteRecord(item["id"], dataBase="spl_printer_lock_records")