#!/usr/bin/python3
"""creates an Object from a “JSON file"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a given JSON file"""
    with open(filename) as b:
        return json.load(b)
