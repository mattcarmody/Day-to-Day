#! python3
# leveler.py - Flattens out the files in a tree.

import pyperclip, os, random

# Ask for input.
path = input('Give me a path (or press enter to paste from clipboard.)')

# If no input, paste from clipboard.
if path == '':
    path = pyperclip.paste()
# If path is still empty, we have a problem.
    if path == '':
        print('I need something to work with.')

# Walk through files, moving them to the base directory.
for foldername, subdirectories, filenames in os.walk(path):
    for filename in filenames:
        try:
            os.rename(os.path.join(foldername, filename), os.path.join(path, filename))
# If there's an error, it's probably a duplicate name. Rename with random prefix.
        except OSError:
            print('Trying to rename file... ' + filename)
            new = 'ZqZ' + str(random.randrange(1, 1000)) + filename
            os.rename(os.path.join(foldername, filename), os.path.join(path, new))
