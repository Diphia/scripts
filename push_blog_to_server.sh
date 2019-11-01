#!/bin/bash
# push_blog_to_server.sh
# diphia@2019
# This script is used to push the local static web pages to the server, the IP address and file location should be set before. After pushing, script will create a log automatically.

remote_username="username"
remote_ip="49.234.63.85"
remote_location="~/"
hugo_location="/home/diphia/Westfall"

if [ ! -f "${hugo_location}/push_history.log" ]
then
	touch ${hugo_location}/push_history.log
	echo "This Logfile is generated by the script [push_blog_to_server]" >> ${hugo_location}/push_history.log
	echo "--------------------------" >> ${hugo_location}/push_history.log
fi

echo " " >> ${hugo_location}/push_history.log
echo " " >> ${hugo_location}/push_history.log
echo "Date:" >> ${hugo_location}/push_history.log

date >> ${hugo_location}/push_history.log
echo " " >> ${hugo_location}/push_history.log

echo "Hugo:" >> ${hugo_location}/push_history.log
cd ${hugo_location}
hugo | sed '1d' >> ${hugo_location}/push_history.log # delete the first line which shows "Building sites ..."
echo " " >> ${hugo_location}/push_history.log

echo "Rsync:" >> ${hugo_location}/push_history.log
rsync -avz -e'ssh -p 22' ${hugo_location}/public ${remote_username}@${remote_ip}:${remote_location} | tail -n 2 >> ${hugo_location}/push_history.log

#echo ${hugo_location}/public ${remote_username}@${remote_ip}:${remote_location}

