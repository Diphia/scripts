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
            if(line.find("<!---[source") != -1):
                isMarked = 1
                code_loc = line.split("[")[1].split("]")[0].split(" ")[1]
            if(re.match("^```",line)):
                grave_count += 1
                if(grave_count %2 == 1):
                    current_block_start = linum
                elif(grave_count != 0):
                    current_block_end = linum
                    if(isMarked == 1):
                        current_block={'code_loc':code_loc,'current_start':current_block_start,'current_end':current_block_end}
                        code_blocks.append(current_block)
                        isMarked = 0
                    current_block = []
        print(code_blocks)


if __name__=="__main__":
    if(len(sys.argv)==1):
        print("Usage: update_source [markdown or html file]")
        print("Example: update_source [vim.md]")
    for target in sys.argv[1:]:
        get_code_blocks(target)
