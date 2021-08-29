#!/usr/bin/env python3

import os,sys

with open('/Users/diphia/test/filelist', 'r') as f:
    for line in f:
        base_path = "/"+line.split("/")[1]+"/"+line.split("/")[2]
        move_target_path = base_path + "/to_delete/"
        command = "sudo mv " + line.strip() + " " + move_target_path
        #print(command)
        os.system(command)
