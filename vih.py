#!/usr/bin/python3
# vih.py
# diphia@2020
# This script is used to quick open the latest modified files by vim

import os
import re

VIMINFO = '/home/diphia/.viminfo'

def get_blocks(target_doc):
    flag = 0
    block = []
    with open(target_doc,'r',errors = 'ignore') as f:
        for line in f:
            if (flag == 0):
                if(re.match("^# File marks",line)):
                    flag = 1
            else:
                if(re.match("^'[0-9].*",line)):
                    block.append(line)
                if(len(block) == 10):
                    return block

def truncate_path(block):
    paths = []
    for line in block:
        paths.append(line.split('  ')[3].strip())
    return paths

if __name__=="__main__":
    block = get_blocks(VIMINFO)
    paths = truncate_path(block)
    for i in range(len(paths)):
        print('(' + str(i)+'): ',end = '')
        print(paths[i])
    print('Select a file: ',end = '')
    try:
        selected = input()
    except KeyboardInterrupt:
        exit()
    if(re.match("[0-9]",selected) and int(selected) < 10 and int(selected) >= 0):
        os.system("vim "+paths[int(selected)])
    else:
        print("invalid input")
