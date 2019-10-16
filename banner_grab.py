#!/usr/bin/python3
# banner_grab.py
# diphia@2019
# This script is used to grab the banner information of a speciffic port range of server

import socket
import select
import sys

if (len(sys.argv)!=4):
    print("Usage:")
    sys.exit()

ip_address=sys.argv[1]
port_start=int(sys.argv[2])
port_end=int(sys.argv[3])

for port in range(port_start,port_end+1):
    try:
        grabber=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        grabber.connect((ip_address,port))
        ready=select.select([grabber],[],[],1) # waiting for grabber to be available
        if (ready[0]):
            print("TCP Port "+str(port)+" - "+str(grabber.recv(4096)))
            grabber.close()
    except:
        print("TCP Port "+str(port)+" - no banner information")
        pass
