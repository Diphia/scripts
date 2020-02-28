#!/usr/bin/python3
# hex2str.py
# diphia@2020
# This script is used to convert hex to string

import sys

def hex2str(target):
    return bytearray.fromhex(target).decode()

if __name__=="__main__":
    print(hex2str(sys.argv[1]))
