#!/usr/bin/python3
# scapy_tcp_scan.py
# diphia@2019
# This script is used to scan the network of given ip address, based on scapy module

from scapy.all import *
import sys

dport=80

if len(sys.argv)!=2:
    print("Usage   ./scapy_tcp_scan.py ip_address")
    print("Example   ./scapy_tcp_scan.py 1.1.1.0")
    sys.exit()

ip_address=str(sys.argv[1])
ip_address_prefix=ip_address.split('.')[0]+"."+ip_address.split('.')[1]+"."+ip_address.split('.')[2]
#print(ip_address)


for ip_address_postfix in range(1,255):
    ip_address_temp=str(ip_address_prefix+"."+str(ip_address_postfix))
    print('processing {ip_address_temp}'.format(ip_address_temp=ip_address_temp))
    packet_to_send=IP(dst=ip_address_temp)/TCP(dport=dport,flags='A')
    response=sr1(packet_to_send,timeout=0.1,verbose=0)
    try:
        if int(response[TCP].flags)==4:
            print(ip_address_temp)
    except:
        pass

