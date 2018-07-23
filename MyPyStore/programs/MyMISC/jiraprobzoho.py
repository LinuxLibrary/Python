#!/usr/bin/env python

import csv
import sys
import pytz
import codecs
import tzlocal
import commands
reload(sys)
sys.setdefaultencoding("utf-8")
import json
from datetime import *

JCURL='curl -b /tmp/jcookie.txt --cookie-jar  /tmp/jcookie.txt -s '
AccessID ='''pygeek@mypyhub.com'''
AccessKey = '''$$$$$$'''
Query = '''project%20%3D%20"Problem%20Management"%20and%20updated%20>%20-10d'''

CMD="%s  -u '%s:%s' 'https://atlassian.mypyhub.com/rest/api/2/search?jql=%s'" %(JCURL,AccessID, AccessKey, Query)
CURLOUT = commands.getoutput(CMD)
JSONDATA = json.loads(CURLOUT)
ISSUES = JSONDATA["issues"]

def CTIME(MTIME):
        try:
             local_timezone = tzlocal.get_localzone()
             DATE = MTIME.split('.')[0].replace('T',' ')
             DATE = datetime.strptime(DATE, "%Y-%m-%d %H:%M:%S")
             local_time = DATE.replace(tzinfo=pytz.utc).astimezone(local_timezone)
             UTCDATE =  local_time.strftime('%Y-%m-%d %H:%M:%S')
             return UTCDATE
        except:
             return None
FILE = open("Prob.csv","w")
HEADER = ["Project Name","Issue key","Custom field (Severity)","Custom field (Environment)","Summary","Custom field (Platform Component)","Issue Type","Status","Assignee","Reporter","Creator","Created","Resolved","Updated","Description","Custom field (Team Resolved By)","Custom field (Customer Captain)"]
CSVWRT = csv.writer(FILE,codecs.getwriter("utf-8")(sys.stdout),delimiter=',',quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
CSVWRT.writerow(HEADER)
for PROB in range(0,len(ISSUES)):
        ISSUELIST = []
        ISSUELIST.append(ISSUES[PROB]["fields"]["project"]["name"])
        ISSUELIST.append(ISSUES[PROB]["key"])
        ISSUELIST.append(ISSUES[PROB]["fields"]["customfield_16003"]["value"])
        ISSUELIST.append(ISSUES[PROB]["fields"]["customfield_16002"]["value"])
        ISSUELIST.append(ISSUES[PROB]["fields"]["summary"])
        try:
                ISSUELIST.append(ISSUES[PROB]["fields"]["customfield_19003"]["value"] + "-" + ISSUES[PROB]["fields"]["customfield_19003"]["child"]["value"])
        except:
                ISSUELIST.append(ISSUES[PROB]["fields"]["customfield_19003"]["value"])
        ISSUELIST.append(ISSUES[PROB]["fields"]["issuetype"]["name"])
        ISSUELIST.append(ISSUES[PROB]["fields"]["status"]["name"])
        try:
                ISSUELIST.append(ISSUES[PROB]["fields"]["assignee"]["name"])
        except:
                ISSUELIST.append("")
        ISSUELIST.append(ISSUES[PROB]["fields"]["reporter"]["name"])
        ISSUELIST.append(ISSUES[PROB]["fields"]["creator"]["name"])
        ISSUELIST.append(CTIME(ISSUES[PROB]["fields"]["created"]))
        try:
                ISSUELIST.append(CTIME(ISSUES[PROB]["fields"]["resolutiondate"]))
        except:
                ISSUELIST.append("")
        try:
                ISSUELIST.append(CTIME(ISSUES[PROB]["fields"]["updated"]))
        except:
                ISSUELIST.append("")
        ISSUELIST.append(ISSUES[PROB]["fields"]["description"])
        try:
                ISSUELIST.append(ISSUES[PROB]["fields"]["customfield_17507"]["value"])
        except:
                ISSUELIST.append("")
        try:
                ISSUELIST.append(ISSUES[PROB]["fields"]["customfield_31131"]["name"])
        except:
                ISSUELIST.append("")
        CSVWRT.writerow(ISSUELIST)
FILE.close()