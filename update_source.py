#!/usr/bin/python3
# update_source.py
# diphia@2020
# This script is used to update cited code in Markdown and HTML file
# Mark in articles should be inserted like "<!---[source ~/scripts/update_source.py]--->"

import sys
import re

def get_code_blocks(target_doc):
    linum = 0
    grave_count = 0
    current_block = []
    code_blocks = []
    isMarked = 0
    with open(target_doc,'r') as f:
        for line in f:
            linum += 1
            #if(line.find("<!---[source") != -1):
            if(re.match("^<\!---\[source",line)):
                isMarked = 1
                try:
                    code_loc = re.search('(?<=\<!---\[source\s).+(?=])',line).group()
                except:
                    code_loc = ''
            if(re.match("^```",line)):
                grave_count += 1
                if(grave_count %2 == 1):
                    try:
                        current_code_type = re.search('(?<=^```).*',line).group()
                    except:
                        current_code_type = ''
                    current_block_start = linum
                elif(grave_count != 0):
                    current_block_end = linum
                    if(isMarked == 1):
                        current_block={'code_loc':code_loc,'current_start':current_block_start,'current_end':current_block_end,'current_code_type':current_code_type}
                        code_blocks.append(current_block)
                        isMarked = 0
                    current_block = []
        return code_blocks

def update_code_blocks(code_blocks):
    for code_block in code_blocks:
        print(code_block)


if __name__=="__main__":
    if(len(sys.argv)==1):
        print("Usage: update_source [markdown or html file]")
        print("Example: update_source [vim.md]")
    for target in sys.argv[1:]:
        code_blocks = get_code_blocks(target)
        update_code_blocks()
