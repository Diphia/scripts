#!/usr/bin/python3
# nessus_caller.py
# diphia@2019
# This script is used to send some commands to nessus and fetch the result

import requests
import json
#import certifi
#import urllib3
import time

nessus_ip='10.73.151.65'
nessus_port='8834'
nessus_username='root'
nessus_password='cmcc#123'

access_key='a655bd9c0d16f00656efbfcd5ad0cd31fefc64b12d2d6778d341277f6988dc5c'
secret_key='0724b4ef60d80bf1c3cee8eac4d3aa3155342846dfcec5009e05e0632346b59b'

url='https://'+nessus_ip+':'+nessus_port

'''
def login():
    token=''
    url_session=url+'/session'
    id_pass={'username':nessus_username,'password':nessus_password}
    response=requests.post(url_session,data=id_pass,verify=False)
    if response.status_code == 200:
        token=json.loads(response.text)['token']
    print('token:'+token)
    return token
'''

def get_scan_list():
    result=''
    url_scans=url+'/scans'
    global header
    header={'X-ApiKeys':'accessKey={access_key};secretKey={secret_key}'.format(access_key=access_key,secret_key=secret_key),
            'Content-type':'application/json',
            'Accept':'text/plain'} 
    response=requests.get(url_scans,headers=header,verify=False)
    if response.status_code == 200:
        result=json.loads(response.text)
    #print(response)
    return result

def get_scan_id(scanname):
    scan_id=0
    scan_list=get_scan_list()['scans']
    if scan_list != '':
        for scan in scan_list:
            if scan['name'] == scanname:
                scan_id=scan['id']
                break
    return scan_id

def scan_launch(iplist):
    url_launch=url+'/scans/{scan_id}/launch'.format(scan_id=get_scan_id('test1'))
    #url_launch=url+'/scans/{scan_id}/launch'.format(scan_id=5)
    print('url='+url_launch)
    data={
            'alt_targets':iplist
    }
    response=requests.post(url_launch,headers=header,data=data,verify=False)
    print(response)
    if response.status_code == 200:
        return True
    else:
        return False

def get_result(scan_id):
    url_result=url+'/scans/{scan_id}'.format(scan_id=scan_id)
    response=requests.get(url_result,headers=header,verify=False)
    if response.status_code == 200:
        vulnerabilities=response['vulnerabilities']
        print(vulnerabilities)
        #print(json.load(response.text)['info'])
        #status=json.load(response.text)['info']['status']

#print(get_scan_list()['scans'])
#print(get_scan_list())
#print(get_scan_id('test1'))
#print(scan_launch(['10.73.151.59']))
get_scan_list()
get_result(5)

