#!/usr/bin/python

DEFAULT_DIR = "/Users/maksie/Documents/Wallpapers/Anime"

import random
import sys
import os

path = ''
choice = ''
#if arg supplied choose arg else choose default dir for path
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = DEFAULT_DIR
#get all files from path if they aren't called .DS_Store (default file placed in mac folders)
files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and not x == '.DS_Store'] 
choice = random.choice(files)
os.system("osascript -e 'tell application \"System Events\" to set picture of every desktop to ("'"{}"'" as POSIX file as alias)'".format(os.path.join(path, choice)))
