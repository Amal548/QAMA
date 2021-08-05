from couchdb.http import ServerError
from SAF.misc.couch_wrapper import CouchWrapper

class DBUtils(object):
    def __init__(self, couchdb_info):
        self.db_info = couchdb_info
        if self.db_info["url"][-1] == "/":
            self.db_info["url"] = self.db_info["url"][:-1]
        self.package_db_name = "test_package_storage"
        try:
            self.db = CouchWrapper(couchdb_info["url"], self.package_db_name , (couchdb_info["user"], couchdb_info["password"]))
        except ServerError:
            sleep(3)
            self.db = CouchWrapper(couchdb_info["url"], self.package_db_name , (couchdb_info["user"], couchdb_info["password"]))
    
    def upload_build_to_database(self, rec, attachment_path):
        doc_id = self.db.saveRecord(rec)[0]
        file_name = attachment_path.split("/")[-1]
        self.db.addAttachment(doc_id,attachment_path, file_name.replace(" ", "_"))

        return self.db_info["url"] + "/" + self.package_db_name + "/" + doc_id + "/" + file_name.replace(" ", "_")

    def check_build_in_database(self, key_match, view_group, view_name):
        view_list = self.db.getAllViewResults(view_group, view_name)
        for item in view_list.rows:
            key = item.key
            if key == key_match:
                if item.value.get("_attachments", None) is None:
                    print("No attachment is actually in the document!")
                    self.db.deleteRecord(item.value["_id"], dataBase=self.package_db_name)
                else:
                    return self.db_info["url"] + "/" + self.package_db_name + "/" + item.value["_id"] + "/" + list(item.value["_attachments"].keys())[0]
        return False 