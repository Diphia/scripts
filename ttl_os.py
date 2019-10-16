#!/usr/bin/python3
# ttl_os.py
# diphia@2019
# This script is used to identify the operating system running on the target machine via ttl

from scapy.all import *
import sys

if len(sys.argv)!=2:
    print("Usage")
    sys.exit()

ip_address=sys.argv[1]


