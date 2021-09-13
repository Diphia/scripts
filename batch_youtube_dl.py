#!/usr/bin/env python3

import os
import sys

download_list = sys.argv

for url in download_list:
    cmd = "youtube-dl \"" + url + "\""
    os.system(cmd)
