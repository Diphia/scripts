#!/usr/bin/python3
# scapy_tcp_port_scan_full_connection.py
# diphia@2019
# This script is used to scan the port via tcp and it will establish full connection to the target machine

from scapy.all import *

dest="10.73.151.6"
port=1080

SYN=IP(dst=dest)/TCP(dport=port,flags='S')

print("----- SENT(FIRST) -----")
SYN.display()

print("\n\n ----- RECEIVED(FIRST) -----")
response=sr1(SYN,timeout=1,verbose=0)
response.display()

if(int(response[TCP].flags)==18):
    print("\n\n ----- SENT(SECOND) -----")
    A=IP(dst=dest)/TCP(dport=port,flags='A',ack=(response[TCP].seq+1))
    A.display()
    print("\n\n ----- RECEIVED(SECOND) -----")
    response2=sr1(A,timeout=1,verbose=0)
    response2.display()
else:
    print("SYN ACK not returned")
