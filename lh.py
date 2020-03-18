#!/usr/bin/python3
# lh.py
# diphia@2020
# This script is used to list the recent modified files in current path and use vim to open it

import os
import re

def get_files():
    files = os.popen('ls -t').read().split('\n')[:-1]
    del_list = []
    for i in range(len(files)):
        if(re.match("^__.*__$",files[i])):
            del_list.append(i)
    for i in del_list:
        files.pop(i)
    return files

if __name__=="__main__":
    files = get_files()
    stroke = 10
    if(len(files) < 10):
        stroke = len(files)
    for i in range(stroke):
        print('(' + str(i) + '): ',end= '')
        print(files[i])
    print('Select a file: ',end = '')
    try:
        selected = input()
    except KeyboardInterrupt:
        exit()
    if(re.match("[0-9]",selected) and int(selected) < 10 and int(selected) >= 0):
        os.system("vim ./"+files[int(selected)])
    else:
        print("invalid input")
