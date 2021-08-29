#!/usr/bin/env python3
# This script is used to flatten a yaml file
import sys
import yaml

def extract(yaml_dict,parent_key):
    for key,value in yaml_dict.items():
        if(type(value) == dict):
            extract(value,parent_key + key + '.')
        else:
            print(parent_key + key)
    return

if __name__=="__main__":
    with open(sys.argv[1]) as f:
        yaml_dict = yaml.safe_load(f)
        extract(yaml_dict,'')
