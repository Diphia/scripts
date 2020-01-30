#!/bin/bash
# hping_all.sh
# diphia@2019
# This script is used to hping the whole network of the given ip address.

if [ $# -ne 1 ]
then
	echo "Usage: hping_all.sh [ip address]"
	echo "Example: hping_all.sh 192.168.1.0"
	exit
fi

ip_addr=$1
ip_addr_prefix=$( echo $ip_addr | cut -d "." -f 1-3)
for ip_addr_postfix in `seq 1 254`
do
	ip_addr_temp="${ip_addr_prefix}.${ip_addr_postfix}"
	#echo "working on ${ip_addr_postfix}"
	hping3 ${ip_addr_temp} -c 1 | grep "bytes from" | cut -d " " -f 4 | cut -d ":" -f 1
done
