#!/usr/bin/python3
# nessus_scan_launcher.py
# diphia@2019
# This script is used to launch a scan in Nessus, as Tenable disabled some nessus APIs after version their upgrade to 7.0, a simulation way is required 

import requests
import sys
import io

url='https://10.73.151.65:8834'
username='root'
password='cmcc#123'

def launch():
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-API-Token':'3A705E74-D87C-4F1F-88EF-F5135FCD45E2',
            }
    data={
        'username':'{username}'.format(username=username),
        'password':'{password}'.format(password=password),
        }
    session=requests.Session()
    session_login=session.post(url+'/session',headers=headers,data=data,verify=False)
    token=str(session_login.text).split(':',1)[1][:-1] # get token
    headers['X-Cookie']='token={token}'.format(token=eval(token)) # add fetched token to X-cookie
    headers['Sec-Fetch-Site']='same-origin'
    headers['Sec-Fetch-Mode']='cors'
    launch=session.post(url+'/scans/10/launch',headers=headers,verify=False)
    print(launch.status_code)
    print(launch.text)
    #print(folders.text)



launch()
