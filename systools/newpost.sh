#!/bin/bash
# new_post.sh
# Diphia@2019
# This script is used to create a new post for Hugo from a template, it will automatically change the post title 

POST_DIR='/home/diphia/Westfall/content/post'

if [ $# -ne 1 ]
then
	echo "Usage: newpost [new post name]"
	echo "Example: newpost [Linux_Shell_Script]"
	exit
fi

if [ ! -f "${POST_DIR}/$1.md" ]
then
    cp ${POST_DIR}/template.md ${POST_DIR}/$1.md
    sed '4d' -i ${POST_DIR}/$1.md
    sed '4 ititle: "'$1'"' -i ${POST_DIR}/$1.md
    vim ${POST_DIR}/$1.md
else
    echo "File exist"
    exit
fi
