#!/bin/bash
# new_post.sh
# Diphia@2019
# This script is used to create a new post for Hugo from a template, it will automatically change the post title 

POST_DIR='/home/diphia/Westfall/content/post'

cp ${POST_DIR}/template.md ${POST_DIR}/$1.md
sed '4d' -i ${POST_DIR}/$1.md
sed '4 ititle: "'$1'"' -i ${POST_DIR}/$1.md
vim ${POST_DIR}/$1.md
