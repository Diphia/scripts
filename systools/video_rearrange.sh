#!/bin/bash
# video_rearrange.sh
# diphia@2020
# This script is used to rearrange the video files, move all in-folder video files to one place

PROCESS_TARGET="/mnt/media/transmission_move_target"
THRESHOLD="100M"

valid_list=`find ${PROCESS_TARGET} +${THRESHOLD}`

for valid_items in ${valid_list}:
do
    echo ${valid_items}
    mv ${valid_items} ${PROCESS_TARGET}
done
