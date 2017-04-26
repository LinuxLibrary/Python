#!/usr/bin/python

import requests
import json
import hashlib
import base64
import time
import hmac
import os
import sys
import inspect
import datetime
import csv
import tabulate

#Account Info
AccessId = 'XXXXXXXXXXXXX'
AccessKey = 'xxxxxxxxxxxxx'
Company = 'linux-library'

#Request Info: Get Services
httpVerb ='GET'
resourcePath = '/dashboard/widgets/6363/data'


#Construct URL
url = 'https://'+ Company +'.logicmonitor.com/santaba/rest' + resourcePath

#Get current time in milliseconds
epoch = str(int(time.time() * 1000 ))
#epoch = str(datetime.datetime.now())

#Concatenate Request details
requestVars = httpVerb + epoch + resourcePath

#Construct signature
signature = base64.b64encode(hmac.new(AccessKey,msg=requestVars,digestmod=hashlib.sha256).hexdigest())

#Construct headers
auth = 'LMv1 ' + AccessId + ':' + signature + ':' + epoch
headers = {'Content-Type':'application/json','Authorization':auth}


#Make request
heads = list()
heads.append('Time')
rows = list()
now = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute)
rows.append(now)
info = json.loads(response.content)
rawJson = info['data']['lines']
for _line in rawJson:
        key = str(_line["legend"])
        val = str(_line["data"][0])
        heads.append(key)
        rows.append(val)

csvHeads = ','.join(heads)
csvRows = ','.join(rows)

file = open('wfData.csv', 'w+')
file.write(csvHeads + "\n")
file.write(csvRows)
file.close()

