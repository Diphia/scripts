#!/usr/bin/python3
# str2hex.py
# diphia@2020
# This script is used to convert a string to hex

import sys

def str2hex(target):
    return target.encode('utf-8').hex()

if __name__=="__main__":
    print(str2hex(sys.argv[1]))
