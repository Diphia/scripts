#!/bin/bash
# transmission_move_downloaded.sh
# diphia@2020
# This script is used to automatically move the downloaded files (by Transmission) to a speciffic directory

TARGET_DIR="/mnt/media/transmission_move_target"
NETRC="/home/diphia/.netrc"
PORT="9092"

done_list=`transmission-remove ${PORT} -N ${NETRC} -l | grep Done`
echo ${done_list}

