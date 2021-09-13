#!/usr/bin/python3
# hex2text.py
# diphia@2020
# This script is used to convert hex to string

import sys

def hex2text(target):
    return bytearray.fromhex(target).decode()

if __name__=="__main__":
    if(len(sys.argv)!=2):
        print("Usage: hex2text [hex_string] ")
        print("Example: hex2text 676f6f676c65")
    print(hex2text(sys.argv[1]))
