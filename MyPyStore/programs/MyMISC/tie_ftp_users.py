#!/usr/bin/python

from operator import itemgetter
import commands
import csv

PASSWD = commands.getstatusoutput("cat /root/PyScripts/passwd")[1]
P_LIST = PASSWD.split('\n')
COUNT = len(P_LIST)
U_LIST = list()
U_LIST.sort()

PCSV_FILE_W = open("/root/PyScripts/tempUsers.csv",'w')
for _line in P_LIST:
	U_LINE = _line.split(':')
	USER_ID = U_LINE[2]
	U_LIST.append(int(USER_ID))
	USER_NAME = U_LINE[0]
	COMPANY_NAME = U_LINE[4]
	HOME_DIR = U_LINE[5]
	CSV_ROW = USER_ID + ',' + USER_NAME + ',' + COMPANY_NAME + ',' + HOME_DIR
	PCSV_FILE_W.write(CSV_ROW + "\n")
PCSV_FILE_W.close()
