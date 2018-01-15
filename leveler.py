#! /usr/bin/python3
# leveler.py - Flattens out the files in a tree. Doesn't delete subdirectories.

import os
import pyperclip
import random
import sys

path = input("Give me a path (or press enter to paste from clipboard.)")

# If no input, paste from clipboard.
if path == "":
    path = pyperclip.paste()
    # If nothing on clipboard, terminate.
    if path == '':
        print("There doesn't seem to be anything on the clipboard.")
        sys.exit()

# Walk through files, moving them to the base directory.
# TODO: skip files in base directory, they're being 'renamed'
for foldername, subdirectories, filenames in os.walk(path):
    for filename in filenames:
        try:
            os.rename(os.path.join(foldername, filename), os.path.join(path, filename))
            print("Renamed " + filename)
# If there's an error, it's probably a duplicate name. Rename with random prefix.
        except OSError:
            print("Trying to rename file... " + filename)
            new = "ZqZ" + str(random.randrange(1, 1000)) + filename
            os.rename(os.path.join(foldername, filename), os.path.join(path, new))
print("Done.")
