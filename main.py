#!/usr/bin/python

import os

for root, dirs, files in os.walk("tops"):
    files.sort()
    for filename in files:
        os.system('sudo ./tops/%s' % filename)
