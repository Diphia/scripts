#!/usr/bin/env python3

import sys
import re
import os

def include_extracter(line):
    content = re.match(".*{{-*\s*include\s(.*)\s.*}}.*" ,line).group(1)
    variable = content.split(" ")[0].strip("\"")
    indent_match = re.match('.*indent\s([0-9]*)', content)
    indent_level = int(indent_match.group(1)) if indent_match else 0
    return indent_level,variable

def fetch_include_content(indent_level, variable):
    templates_path = chart + 'templates/'
    tpl_files = list(filter(lambda f:True if (re.match('.*.tpl$',f)) else False ,os.listdir(templates_path)))
    for tpl_file in tpl_files:
        result = []
        result_string = ""
        flag = 0
        indent_string = ""
        for i in range(indent_level):
            indent_string+=" "
        with open(templates_path+tpl_file) as f:
            for line in f:
                if(re.match('.*define \"'+variable+'\" .*', line)):
                    flag = 1
                    continue
                if(flag >= 1 and re.match('.* if .*', line)):
                    flag += 1
                if(re.match(".*{{.*end.*}}.*", line)):
                   if(flag == 1):
                       break
                   else:
                       flag -= 1
                if(flag >= 1):
                    if(re.match(".*{{-*\s*include\s(.*)\s.*}}",line)):
                        new_indent_level, new_variable = include_extracter(line)
                        result.append(fetch_include_content(new_indent_level+indent_level, new_variable))
                    else:
                        result.append(line)
        if(result == []):
            continue
        else:
            for line in result:
                result_string += indent_string + line
            return result_string

def process_execute(line):
    if(re.match(".*{{-*\s*include\s(.*)\s.*}}.*", line)): # include block
        indent_level, variable = include_extracter(line)
        return re.sub("{{.*}}", fetch_include_content(indent_level, variable), line)
    elif(re.match("^\t*\s*{{.*}}\t*\s*$", line)): # execute block as full line
        return ""
    elif(re.match("^.*{{.*}}.*$", line)): # execute block as value
        return re.sub("{{.*}}", "replaced_value", line)
    else:
        return line

def format_yaml(f):
    data = f.readlines()
    return list(map(process_execute,data))

if __name__=="__main__":
    chart = '/home/diphia/temp/ut_coverage/aic-vdu-cprt/'
    with open(sys.argv[1]) as f:
        for line in format_yaml(f):
            print(line,end="")
    #with open('/tmp/test', 'w') as f_w:
        #f_w.writelines(to_write)

    #print(fetch_include_content(2,'common.custom_extensions.global.labels'))
