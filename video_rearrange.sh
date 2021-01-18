#!/bin/bash
# video_rearrange.sh
# diphia@2020
# This script is used to rearrange the video files, move all in-folder video files to one place

PROCESS_TARGET="/mnt/media/transmission_move_target"
THRESHOLD="200" # unit is M

# Move Videos to Target
valid_list=`find ${PROCESS_TARGET} -size +${THRESHOLD}M`
for valid_items in ${valid_list}
do
    if [[ `dirname ${valid_items}` != "${PROCESS_TARGET}" ]] # not in target now
    then
        echo "Processing: `echo ${valid_items} | awk -F '/' '{print $NF}'`" 
        mv ${valid_items} ${PROCESS_TARGET}
        if [[ $? == 0 ]]
        then
            echo "`echo ${valid_items} | awk -F '/' '{print $NF}'` Moved"
        else
            echo "Operation Failed"
        fi
    fi
done

# Remove directories
directory_list=`ls -l ${PROCESS_TARGET} | awk '(substr($1,1,1)=="d")&&($9!=".")&&($9!=".."){print $9}'` 
for directory in ${directory_list}
do
    if [[ `du -sm ${PROCESS_TARGET}/${directory} | awk '{print $1}'` -lt ${THRESHOLD} ]]  # judge directory size
    then
        echo "Preparing to remove: ${directory}"
        rm -r ${PROCESS_TARGET}/${directory}
        if [[ $? == 0 ]]
        then
            echo "${directory} Removed"
        else
            echo "Operation Failed"
        fi
    else
        echo "${directory} is larger than ${THRESHOLD}M, you need to check it."
    fi
done
