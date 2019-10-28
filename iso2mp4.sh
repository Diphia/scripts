#!/bin/bash
# iso2mp4.sh
# diphia@2019
# This script is used to convert the ISO format file to mp4 automatically, ffmpeg packages are required for transcoding

filename_prefix=$(echo $1 | cut -d "." -f 1)
#echo ${filename_prefix}
if [ ! -d "/mnt/${filename_prefix}" ]
then
	sudo mkdir /mnt/${filename_prefix}/
fi

sudo mount -o ro $1 /mnt/${filename_prefix}
