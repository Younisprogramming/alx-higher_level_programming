#!/usr/bin/python3
"""adds all arguments to a Python list,
and then save them to a file"""
import sys

if __name__ == "__main__":
    save_to = __import__('5-save_to_json_file').save_to_json_file
    load_from = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to(items, "add_item.json")
