#!/usr/bin/env python3
# sshl.py
# diphia@2021
# This script is used to show the saved ssh targets
import platform
from termcolor import colored


user = 'diphia'

# compatible with Linux and macOS
home = '/Users/'+user+'/' if (platform.system()=='Darwin') else '/home/'+user+'/'
ssh_config = home+'.ssh/config'

def read_server():
    server_list = []
    current_server = {}
    with open(ssh_config,'r') as f:
        for line in f:
            if(line == '\n'):
                continue
            if(line.split(' ')[0] == 'Host'):
                server_list.append(current_server)
                current_server = {}
            splited_line = line.strip().split(' ')
            key, value = splited_line[0], splited_line[1]
            if(key == 'Host'):
                if(len(value)>10):
                    value = value[0:7]+'..'
            current_server[key]=value
    server_list.append(current_server)
    del server_list[0]
    return server_list

def print_server(server_list):
    for server in server_list:
        if(server['Port']=='22'):
            server['Port']=''
        else:
            server['Port']=colored(':'+server['Port'],'cyan')
        print(server['Host'].ljust(10)+': '+ server['User']+'@'+server['HostName']+server['Port'])

if __name__=="__main__":
    server_list = read_server()
    print_server(server_list)
