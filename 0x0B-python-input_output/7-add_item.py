#!/usr/bin/python3
"""module that add all system args to a list of json file"""

import sys
import os.path


save_to json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.isfile(filename):
    json_file = load_from_json_file(filename)
    json_list = json_file + sys.argv[1:]
    save_to_json_file(json_list, filename)
else:
    save_to_json_file(sys.argv[1:], filename)
