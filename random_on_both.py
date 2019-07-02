#!/usr/bin/python

DEFAULT_DIR = "/Users/maksie/Documents/Wallpapers/Anime"

import random
import sys
import os

path = ''
choice = ''

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = DEFAULT_DIR

files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and not x == '.DS_Store']
for i in range(1,3):
    choice = random.choice(files)
    full_path = os.path.join(path, choice)
    os.system("osascript -e 'tell application \"System Events\" to set picture of desktop {} to ("'"{}"'" as POSIX file as alias)'".format(i, full_path))

