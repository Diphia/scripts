#!/usr/bin/python3
# nessus_scan_launcher.py
# diphia@2019
# This script is used to control the operations of nessus, as Tenable disabled some nessus API after version 7.0, we just need to use a simulation way

import requests
import sys
import io

url='https://10.73.151.65:8834'
username='root'
password='cmcc#123'

def login():
    headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-API-Token':'3A705E74-D87C-4F1F-88EF-F5135FCD45E2',
            }

    data={
        'username':'{username}'.format(username=username),
        'password':'{password}'.format(password=password),
        }

    response=requests.post(url+'/session',data=data,headers=headers,verify=False)
    token=str(response.text).split(':',1)[1][:-1]

    headers_with_token={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'X-API-Token':'3A705E74-D87C-4F1F-88EF-F5135FCD45E2',
            #'X-Cookie':'token={token}'.format(token=token)
            'X-Cookie':'token=ea2143b2e3ae5d15da1998026408d7b0793d88b9150f78a0',
            }

    response_folder=requests.get(url+'/folders',headers=headers_with_token,verify=False)
    #response=session.get(url,headers=headers)

    #print(response.text)
    print('token='+token)
    print(response_folder.text)
    print(response_folder)
    #print(response)
    #print(response_home.text)


login()
