#!/bin/bash
# transmission_move_downloaded.sh
# diphia@2020
# This script is used to automatically move the downloaded files (by Transmission) to a speciffic directory

TARGET_DIR="/mnt/media/transmission_move_target"
NETRC="/home/diphia/.netrc"
PORT="9092"

done_list=`transmission-remote ${PORT} -N ${NETRC} -l | grep Done`
done_id_list=`echo "${done_list}" | awk '$1!="ID"{print $1}'`
echo ${done_id_list}

if [[ -z "${done_id_list}" ]]
then
    echo "No items to operate"
    exit
fi

for id in ${done_id_list}
do
    echo "Processing : ${id}"
    transmission-remote ${PORT} -N ${NETRC} -t ${id} --move ${TARGET_DIR}
    transmission-remote ${PORT} -N ${NETRC} -t ${id} --remove 
done
