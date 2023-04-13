#!/usr/bin/python3
"""Module for loading, adding, and saving arguments to a Python list as JSON"""
from sys import argv

# Importing the necessary functions for loading and saving JSON files
load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

# Try to load the contents of 'add_item.json' or create an empty list
try:
    json_list = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

# Append command-line arguments to the loaded or empty list
for item in argv[1:]:
    json_list.append(item)

# Save the updated list to 'add_item.json' as JSON
save_file(json_list, 'add_item.json')
