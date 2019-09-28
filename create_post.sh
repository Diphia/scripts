#!/bin/bash

POST_DIR='/home/diphia/Westfall/content/post'

cp ${POST_DIR}/template.md ${POST_DIR}/$1.md
sed '4d' -i ${POST_DIR}/$1.md
sed '4 ititle: "'$1'"' -i ${POST_DIR}/$1.md
vim ${POST_DIR}/$1.md
