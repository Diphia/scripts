#!/usr/bin/python3
# text2hex.py
# diphia@2020
# This script is used to convert a string to hex

import sys
import binascii

def text2hex(target):
    return binascii.hexlify(bytes(target.encode('utf-8'))).decode('utf-8')

if __name__=="__main__":
    if(len(sys.argv)!=2):
        print("Usage: text2hex [text] ")
        print("Example: text2hex google")
    print(text2hex(sys.argv[1]))


