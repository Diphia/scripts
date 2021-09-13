#!/usr/bin/python3
# strxor.py
# diphia@2020
# This script is used to calculate the string xor

import sys

def strxor(a,b):
    if (len(a) > len(b)):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

if __name__=="__main__":
    if(len(sys.argv)!=3):
        print("Usage: strxor [str a] [str b]")
        print("Example: strxor china japan")
        exit()
    print(strxor(sys.argv[1],sys.argv[2]))
