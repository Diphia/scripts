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

ans=sr1(IP(dst=str(ip_address))/ICMP(),timeout=1,verbose=0)

if (ans==None):
    print("No response returned from target")
elif (int(ans[IP].ttl)<=64):
    print(str(ip_address)+" returned TTL="+str(ans[IP].ttl)+", Host is Linux/UNIX")
else:
    print(str(ip_address)+" returned TTL="+str(ans[IP].ttl)+", Host is Windows")
