#!/usr/bin/python3
# set_resolution.py
# diphia@2020
# This script is used to set screen resolution with xrandr and cvt

import os

SCREEN = 'Virtual1'

RESOLUTIONS = ('3840 2160',
        '2200 1650',
        '1920 1080',
        '1280 920',
        '1280 960')

if __name__=="__main__":
    print('Select a resolution below:')
    for i in range(len(RESOLUTIONS)):
        print(str(i)+': '+RESOLUTIONS[i])
    print('Type the number: ')
    selected = input()
    cvt_output = os.popen('cvt '+RESOLUTIONS[int(selected)]).read().split('\n')[1][9:]
    res_name = cvt_output.split(' ')[0][1:-1]
    os.system('xrandr --newmode '+cvt_output)
    os.system('xrandr --addmode '+SCREEN+' '+res_name)
    os.system('xrandr --output '+SCREEN+' --mode '+res_name)


