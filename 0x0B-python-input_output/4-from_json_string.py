#!/usr/bin/python3
"""Module to return object replesented frm JSON string"""

import json


def from_json_string(my_str):
    """
    loads(): Method converts JSON str to python dictionary
    Args:
        my_str(string): json string to be converted to python dictionary
    """
    return json.loads(my_str)
