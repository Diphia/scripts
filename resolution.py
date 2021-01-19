import os

SCREEN = 'Virtual1'

RESOLUTIONS = ('3840 2160',
        '2200 1650',
        '1920 1080',
        '1280 920',
        '1280 960',
        '1366 768',
        '1024 768',
        '800 600')

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
