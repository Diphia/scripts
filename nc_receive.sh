#!/bin/bash
# nc_receive.sh
# diphia@2019
# This script is used to receive a file from target machine via nc 

ip=192.168.50.131
port=333

if [ $# -ne 1 ]
then
	echo "Usage: nc_receive [renamed file name]"
	echo "Example: nc_receive img001.jpg"
	exit
fi

nc -nv ${ip} ${port} > $1
