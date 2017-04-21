#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 20.04.2017

###############################
## Code revision information ##
###############################

# 20170420              AS              Created mkuser2.py



######################
## REQUIRED MODULES ##
######################

import os
import commands
import time
import re
import string
import random
import subprocess
import argparse
from datetime import datetime

######################
## ARGUMENT PARSING ##
######################

parser = argparser.ArgumentParser(description='FTP Account Creation')
parser.add_argument("--ctype", dest="cType", default="ftp", required=True, help="FTP connection type (ftp|export) For SFTP/FTPS use export & PLEASE INPUT DIR NAME")
parser.add_argument("--dir", dest="dir", required=False, help="DIR Name for export connection users")
parser.add_argument("--atype", dest="aType", required=True, help="FTP account type (hub|fi|rfi|vendor|home|sftp|ftps|images|analytics)")
parser.add_argument("--user", dest="uName", required=True, help="FTP User Name")
parser.add_argument("--desc", dest="desc", required=True, help="Company name enclosed in quotes")
args = parser.parse_args()

###############
## Variables ##
###############

USER_NAME = ""
USER_CHECK = ""
PASSWORD = ""
DIR = "/u01"
FTP_RANGE_LOW = 30000
FTP_RANGE_HIGH = 39999
FTP_PASSWD = "/u01/ncftpd/etc/passwd.db"
FTP_SHELL = "none"
MAXLEN = 10
GID = "500"
FTP_CONTROL = "ftp20"
CURDATE = datetime.now()
RETVAL = None

###############
## FUNCTIONS ##
###############

def password():
        MYPUNCTUATION = '!?.%_!?*#'
        STRINGTOT = string.ascii_uppercase + string.ascii_lowercase + string.digits + MYPUNCTUATION
        STRINGS = [random.choice(STRINGTOT) for CHAR in range(13)]
        PASS = ''.join(STRINGS)
        return PASS


