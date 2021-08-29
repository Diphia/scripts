#!/usr/bin/env python3

import sys
import re

def get_indent(line, i=0):
    if(line[i] == " "):
        return 1 + get_indent(line,i+1)
    else:
        return 0

def get_yaml_path(f, linum):
    print(f[linum])

if __name__=="__main__":
    with open(sys.argv[1]) as f:
        get_yaml_path(f, sys.argv[2])
#    print(get_indent(" xxxxx "))
