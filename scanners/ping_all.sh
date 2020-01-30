#!/bin/bash
# ping_all.sh
# diphia@2019
# This script is used to ping the whole network of the given ip address.

if [ $# -ne 1 ]
then
	echo "Usage: ping_all.sh [ip address]"
	echo "Example: ping_all.sh 192.168.1.0"
	exit
fi

ip_addr=$1
ip_addr_prefix=$( echo $ip_addr | cut -d "." -f 1-3)
for ip_addr_postfix in `seq 1 254`
do
	ip_addr_temp="${ip_addr_prefix}.${ip_addr_postfix}"
	#echo "working on ${ip_addr_postfix}"
	ping ${ip_addr_temp} -c 1 | grep "bytes from" | cut -d " " -f 4 | cut -d ":" -f 1

done
