#!/usr/bin/python3
# nessus_caller.py
# diphia@2019
# This script is used to send some commands to nessus and fetch the result

import requests
import json
import time

nessus_ip='10.73.151.65'
nessus_port='8834'
nessus_username='root'
nessus_password='cmcc#123'

access_key='a655bd9c0d16f00656efbfcd5ad0cd31fefc64b12d2d6778d341277f6988dc5c'
secret_key='0724b4ef60d80bf1c3cee8eac4d3aa3155342846dfcec5009e05e0632346b59b'

url='https://'+nessus_ip+':'+nessus_port

global header
header={
    'X-ApiKeys':'accessKey={access_key};secretKey={secret_key}'.format(access_key=access_key,secret_key=secret_key),
    }

global header_simu
header_simu={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'X-API-Token':'3A705E74-D87C-4F1F-88EF-F5135FCD45E2',
    }

def get_scan_list():
    result=''
    url_scans=url+'/scans'
    '''
    global header
    header={'X-ApiKeys':'accessKey={access_key};secretKey={secret_key}'.format(access_key=access_key,secret_key=secret_key),
            'Content-type':'application/json',
            'Accept':'text/plain'
            }
            '''
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

def create_scan(template_uuid,scan_name,text_target):
    data={
            'username':'{username}'.format(username=nessus_username),
            'password':'{password}'.format(password=nessus_password),
            }
    session=requests.Session()
    session_login=session.post(url+'/session',headers=header_simu,data=data,verify=False)
    token=str(session_login.text).split(':',1)[1][:-1] # get token
    header_simu['X-Cookie']='token={token}'.format(token=eval(token)) # add fetched token to X-cookie
    header_simu['Sec-Fetch-Site']='same-origin'
    header_simu['Sec-Fetch-Mode']='cors'
    url_scans=url+'/scans'
    data={
            'uuid':'{template_uuid}'.format(template_uuid=template_uuid),
            'credential':{
                "add":{},
                "edit":{},
                "delete":[]
                },
            'settings':{
                'name':'{scan_name}'.format(scan_name=scan_name),
                'enabled':'False',
                'text_target':'{text_target}'.format(text_target=text_target)
                }
            }
    create_scan=session.post(url_scans,headers=header_simu,data=data,verify=False)
    print(create_scan.text)
    print(create_scan)
    #if response.status_code == 200:
        #return response.id
    #else:
        #print(response.status_code)


# As Tenbale disabled some APIs after the upgrade of version 7.0, simulation login is required to launch a speciffic scan.
def scan_launch(scan_id):
    data={
            'username':'{username}'.format(username=nessus_username),
            'password':'{password}'.format(password=nessus_password),
            }
    session=requests.Session()
    session_login=session.post(url+'/session',headers=header_simu,data=data,verify=False)
    token=str(session_login.text).split(':',1)[1][:-1] # get token
    header_simu['X-Cookie']='token={token}'.format(token=eval(token)) # add fetched token to X-cookie
    header_simu['Sec-Fetch-Site']='same-origin'
    header_simu['Sec-Fetch-Mode']='cors'
    launch=session.post(url+'/scans/{scan_id}/launch'.format(scan_id=scan_id),headers=header_simu,verify=False)
    print(launch.status_code)
    if launch.status_code == 200:
        return True
    else:
        return False

def request_status(scan_id):
    url_status=url+'/scans/{scan_id}'.format(scan_id=scan_id)
    response=requests.get(url_status,headers=header,verify=False)
    if response.status_code == 200:
        info=json.loads(response.text)['info']
        #status=info['status']
        print(info)
    else:
        print(response.status_code)

def get_result(scan_id):
    url_result=url+'/scans/{scan_id}'.format(scan_id=scan_id)
    response=requests.get(url_result,headers=header,verify=False)
    if response.status_code == 200:
        vulnerabilities=response['vulnerabilities']
        print(vulnerabilities)
        #print(json.load(response.text)['info'])
        #status=json.load(response.text)['info']['status']



#scan_launch(5)
#request_status(5)
#get_result(5)
create_scan('731a8e52-3ea6-a291-ec0a-d2ff0619c19d7bd788d6be818b65','test8','10.73.151.25')
