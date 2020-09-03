#!/usr/bin/env python3

import sys
import os.path

"""This gets all the files"""
files = sys.argv
"""this remove the first file from the list because thats the name of the file running"""
files.pop(0)
"""iterates through all the files in the list and checks if its a real file at the same time"""
for file in files:
    if os.path.isfile(file):
        with open(file, 'r') as f:
            data = f.read()
            words = data.split()
            lines = data.split("\n")
            print(f"lines: {len(lines)} words: {len(words)} characters: {len(data)} {file}") 

