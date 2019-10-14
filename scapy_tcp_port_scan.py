#!/usr/bin/python3
# scapy_tcp_port_scan.py
# diphia@2019
# This script is used to scan the port via tcp

from scapy.all import *
import time
import sys

if len(sys.argv)!=4:
    print("Usage   ./scapy_tcp_port_scan.py [Target IP] [First Port] [Last Port]")
    print("Example   ./scapy_tcp_port_scan.py 1.1.1.1 1 255")
    sys.exit()
    

ip_address=sys.argv[1]
port_start=int(sys.argv[2])
port_end=int(sys.argv[3])

for port in range(port_start,port_end+1):
    a=sr1(IP(dst=ip_address)/TCP(flags="S",dport=port),timeout=1,verbose=0)
    time.sleep(1)
    if(a==None):
        print(str(port)+" -----> Close")
    else:
        if(int(a[TCP].flags)==18):
            print(str(port)+" -----> Open")
        else:
            #print(str(port)+" .... "+str(int(a[TCP].flags)))
            print(str(port)+" -----> Close")

