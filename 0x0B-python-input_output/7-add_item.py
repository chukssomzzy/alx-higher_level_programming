#!/usr/bin/python3

"""Load serialized data, deserialize the data, sholve them into a
list and dump them into a file"""
import sys
import json
if __name__ != "__main__":
    exit()
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

list_arg = []

for arg in sys.argv[1:]:
    list_arg.append(arg)

filename = "add_item.json"
file_list = []

try:
    file_list = load_from_json_file(filename)
    for obj in file_list:
        list_arg.append(obj)
except ValueError as e:
    print("[{}] {}".format(e.__class__.__name__, e))
except FileNotFoundError as e:
    fp = open(filename, "w", encoding="utf-8")
    fp.close()

save_to_json_file(list_arg, filename)
