#!/usr/bin/python3
"""Module for return JSON replesentation of an object (string)"""

import json


def to_json_string(my_obj):
    """
    dumps(): method of the json module return JSON representation of my_obj
    Args:
        my_obj(string): string to get JSON replesentation
    """
    return json.dumps(my_obj)
