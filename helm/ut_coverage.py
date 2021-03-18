#!/usr/bin/env python3
import sys
import re
import os

def include_extracter(content):
    variable = content.split(" ")[0].strip("\"")
    indent_match = re.match('.*indent\s([0-9]*)', content)
    indent_level = int(indent_match.group(1)) if indent_match else 0
    return indent_level,variable

def main_yaml_process(filepath):
    used_variables = [filepath]
    linum = 0
    with open(filepath) as f:
        for line in f:
            linum += 1
            m = re.match('.*{{\s*include\s(.*)\s.*}}.*', line)
            if(m):
                indent_level, variable = include_extracter(m.group(1))
                used_variables.append([linum, indent_level, variable])
    return used_variables

if __name__=="__main__":
#    templates_path = sys.argv[1] + "templates/"
    #yaml_files = list(filter(lambda f:True if (re.match('.*.yaml$',f)) else False ,os.listdir(templates_path)))
#    for yaml_file in yaml_files:
        #print(main_yaml_process(templates_path + yaml_file))
