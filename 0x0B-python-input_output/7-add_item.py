#!/usr/bin/python3

"""Load serialized data, deserialize the data, sholve them into a
list and dump them into a file"""
import sys
import json
if __name__ != "__main__":
    exit()
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, filename)
