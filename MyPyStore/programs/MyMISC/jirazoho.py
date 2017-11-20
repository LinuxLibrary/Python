#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import datetime
TMPFILE = 'jira.csv'
CSVFILE = 'testout.csv'
url = 'https://atlassian.mypyhub.com/sr/jira.issueviews:searchrequest-csv-current-fields/21715/SearchRequest-21715.csv?jqlQuery=project+%3D+%22Inci+Dash%22+AND+created+%3E%3D+-180+AND+updated+%3E%3D+-1d+ORDER+BY+status+ASC%2C+created+ASC%2C+resolved+DESC%2C+Updated+DESC'
username = 'pygeek@mypyhub.com'
password = '$$$$$$'
file = open(TMPFILE, 'w')
data = requests.get(url, auth=(username, password), verify=False).content
file.write(data)
file.close()
outfile = open(CSVFILE, 'w')
dlist = data.split('\n')
if not dlist[-1].startswith('Incident'):
        dlist.pop(-1)
outfile.write(dlist[0])
for line in range(len(dlist)-1):
        format = "%m/%d/%Y %H:%M:%S"
        if line == 0: continue
        datelist = dlist[line].split(',')
        indexes = [index for index in range(len(datelist)) if 'AM' in datelist[index] or 'PM' in datelist[index]]
        if (len(indexes) > 0) and ('AM' in datelist[indexes[0]] or 'PM' in datelist[indexes[0]]):
        	CINDEX = indexes[0]
        	CDATE = datetime.datetime.strptime(datelist[indexes[0]], '%m/%d/%Y %I:%M %p').strftime(format)
        else:
        	CDATE = ''
        if (len(indexes) > 1) and ('AM' in datelist[indexes[1]] or 'PM' in datelist[indexes[1]]):
        	UINDEX = indexes[1]
        	UDATE = datetime.datetime.strptime(datelist[indexes[1]], '%m/%d/%Y %I:%M %p').strftime(format)
        else:
        	UDATE = ''
        if (len(indexes) > 2) and ('AM' in datelist[indexes[2]] or 'PM' in datelist[indexes[2]]):
        	RINDEX = indexes[2]
        	RDATE = datetime.datetime.strptime(datelist[indexes[2]], '%m/%d/%Y %I:%M %p').strftime(format)
        else:
        	RDATE = ''
        if datelist[14]:
        	INDUR = datelist[14].replace('.0','')
        else:
        	INDUR = ''
        if datelist[33]:
        	RESMIN = datelist[33].replace('.0','')
        else:
        	RESMIN = ''
        _line = ','.join(datelist[0:CINDEX]) + ',' + CDATE + ',' + datelist[CINDEX+1] + ',' + UDATE + ',' + ','.join(datelist[UINDEX+1:14]) + ',' + INDUR + ',' + ','.join(datelist[15:RINDEX]) + ',' + RDATE + ',' + RESMIN
        outfile.write('\n' + _line)
outfile.close()