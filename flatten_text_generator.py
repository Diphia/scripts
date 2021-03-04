#!/usr/bin/env python3

import sys
import yaml
from yaml_flatter import extract

if __name__=="__main__":
    for target in sys.argv[1:]:
        with open(target) as f:
            print('*** '+target.split('/')[-1])
            yaml_dict = yaml.safe_load(f)
            extract(yaml_dict,'')
