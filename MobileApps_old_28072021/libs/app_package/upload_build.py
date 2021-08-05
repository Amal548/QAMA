import sys
import json
from base_class import LocalBuild

if sys.version_info <= (3, 0):
    input = raw_input

couchdb_info = json.loads(input("Couchdb info (in dictionary format): "))
file_path = input("Attachment file path: ")

lb = LocalBuild(couchdb_info)
lb.upload_local_build(file_path)
