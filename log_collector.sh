#!/bin/bash

time_stamp=$(date +%Y%m%d)
dir_name="${time_stamp}""_log"
#mkdir ${dir_name}

dmesg > ${dir_name}/dmesg_${time_stamp}.log 
last > ${dir_name}/last_${time_stamp}.log
lastb > ${dir_name}/lastb_${time_stamp}.log
cp /root/.bash_history ${dir_name}/root_bash_history_${time_stamp}.log 
cp /var/log/message ${dir_name}/message_${time_stamp}.log >> /dev/null 2>&1
cp /var/log/cron ${dir_name}/cron_${time_stamp}.log >> /dev/null 2>&1
cp /var/log/cups ${dir_name}/cups_${time_stamp}.log >> /dev/null 2>&1
cp /var/log/secure ${dir_name}/secure_${time_stamp}.log >> /dev/null 2>&1
cp /var/log/syslog ${dir_name}/syslog_${time_stamp}.log >> /dev/null 2>&1
cp /var/log/auth.log ${dir_name}/auth.log_${time_stamp}.log >> /dev/null 2>&1

echo -e "all logs collected:\n"
tar cvf ${dir_name}.tar ${dir_name}
echo -e "\n${dir_name}.tar created"
