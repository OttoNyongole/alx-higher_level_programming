#!/usr/bin/python3
"""Module to write an object to text file using json replesentation"""

import json

def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj(dict): object to be converted to a JSON object
        filename(file pointer): pointer to json file
    """
    with open(filename, encoding="utf-8", 'w') as file:
        file.write(json.dumps(my_obj))
