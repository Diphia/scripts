#!/bin/bash
# cheat.sh
# diphia@2020
# This script is a shortcut to reach cheatsheets

cheatsheet_loc="/home/diphia/cheatsheet"

cheatsheet_set=${cheatsheet_loc}/$1.cheatsheet

if [[ $# != 2 ]]
then
    if [[ $# == 1 ]]
    then
        cat ${cheatsheet_set}
        exit
    fi
	echo "Usage: cheat [cheatset set] [chapter]"
	echo "Example: cheat [vim] [substitude]"
	exit
fi

chapter=^§.*$2.*  # § sign at the start and include input string

start_line=`grep -n "${chapter}" ${cheatsheet_set} | awk -F ':' '{print $1}'`

for x in ${start_line}
do
    start_line_case=$x
    chapterPassed=0
    end_line=`cat ${cheatsheet_set} | wc -l`+1
    for i in `grep -n "§" ${cheatsheet_set}`
    do
        if [[ ${chapterPassed} == 1 ]]
        then
            end_line=`echo ${i} | awk -F ':' '{print $1}'`
            break
        fi
        if [[ `echo ${i} | awk -F ':' '{print $1}'` == ${start_line_case} ]]
        then
            chapterPassed=1
        fi
    done
    awk -v sl="${start_line_case}" -v dl="${end_line}" 'NR>=sl && NR<dl {print $0}' ${cheatsheet_set} # use -v to define var in awk command
done
