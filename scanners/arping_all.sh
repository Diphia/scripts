#!/bin/bash
# arping_all.sh
# diphia@2019
# This script is used to arping all the machines inside the same network

if [ $# -ne 1 ]
then 
	echo "Usage: arping_all.sh [interface]"
	echo "Example: arping_all.sh eth0"
	exit
fi
	
interface=$1
ip_addr_prefix=$(ifconfig ${interface} | grep netmask | cut -d t -f2 | cut -d . -f1-3)
for addr_postfix in `seq 1 254`
do
	ip_addr="${ip_addr_prefix}.${addr_postfix}"
	#echo ${ip_addr}
	arp_return=$(arping -c 1 ${ip_addr})
	arp_return_ip=$(echo ${arp_return} | cut -d"(" -f 2 | cut -d")" -f 1)
	echo ${arp_return_ip}
done
