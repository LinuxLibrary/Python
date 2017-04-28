#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 21.04.2017

###############################
## Code revision information ##
###############################

# 20170421              AS              Created mkuser2.py



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

parser = argparse.ArgumentParser(description='FTP Account Creation')
parser.add_argument("--ctype", dest="cType", default="ftp", required=True, help="FTP connection type (ftp|export) For SFTP/FTPS use export & PLEASE INPUT DIR NAME")
parser.add_argument("--dir", dest="dName", required=False, help="DIR Name for export connection users")
parser.add_argument("--atype", dest="aType", required=True, help="FTP account type (hub|fi|rfi|vendor|home|sftp|ftps|images|analytics)")
parser.add_argument("--user", dest="uName", required=True, help="FTP User Name")
parser.add_argument("--desc", dest="desc", required=True, help="Company name enclosed in quotes")
args = parser.parse_args()

###############
## Variables ##
###############

USER_CHECK = ""
PASSWORD = ""
DIR = "/u01/ftp"
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


os.system("clear")
print "\t==================================\n"
print "\t", CURDATE, "\n"
print "\tMake User Script for SPS customers\n"

if (args.cType == "export"):
	RETVAL = commands.getstatusoutput("ssh -t FTP_CONTROL /root/bin/mksftpuser.bash")[0]
	if (RETVAL == 256): sys.exit(RETVAL)
	time.sleep(25)
	os.system("nfs4_setfacl -R -S /root/bin/acl_base " + args.dName + "/in")
	os.system("nfs4_setfacl -R -S /root/bin/acl_base " + args.dName + "/out")
	os.system("nfs4_setfacl -R -S /root/bin/acl_base " + args.dName + "/testin")
	os.system("nfs4_setfacl -R -S /root/bin/acl_base " + args.dName + "/testout")
	sys.exit()

if (args.uName == "" or len(args.uName) > MAXLEN):
	print "Usernames must begin with [a-z] and have max of %d chars.\n" % (MAXLEN)
else:
	if (args.cType == "ftp" or args.cType == "export"):
		PDBFILE = commands.getstatusoutput("sudo /u01/ncftpd/sbin/ncftpd_passwd -f /u01/ncftpd/etc/passwd.db -x")[1]
		ENTRIES = PDBFILE.split('\n')
		CHECK_USERS = list()
		for ENTRY in ENTRIES:
			USER = ENTRY.split(':')[0]
	        	CHECK_USERS.append(USER)
		if args.uName in CHECK_USERS:
			print "User already exists!"
	else:
		try:
			PWFILE = open("/etc/passwd")
		except:
			print "Unable to open passwd file!"
		while PWFILE:
			USER = subprocess.Popen(["grep",USER_NAME,"/etc/passwd"],stdout=subprocess.PIPE)
			out, err = USER.communicate()
			if out:
				print "User %s already exists" % (USER_NAME)

SEARCH = re.search(r"([a-zA-Z_0-9]+)",args.desc)
if not SEARCH:
	print "Invalid description!\n"

H_DIR = "%s/%s/%s" % (DIR, args.aType, args.uName)
PASSWORD = password()

# Create subdirectories for user
DIRCHECK = os.path.isdir(H_DIR)
if (DIRCHECK == True):
	print "Directory %s already exists!\n" % (H_DIR)
else:
	if (args.cType == "ftp"):
		try:
			os.makedirs(os.path.join(H_DIR, 'in'))
		except:
			print "Unable to create %s/in" % (H_DIR)
		try:
			os.makedirs(os.path.join(H_DIR, 'out'))
		except:
			print "Unable to create %s/out" % (H_DIR)
		try:
			os.makedirs(os.path.join(H_DIR, 'testin'))
		except:
			print "Unable to create %s/testin" %(H_DIR)
		try:
			os.makedirs(os.path.join(H_DIR, 'testout'))
		except:
			print "Unable to create %s/testout" % (H_DIR)
		if (args.aType == "images"):
			try:
				os.makedirs(os.path.join(H_DIR, 'images'))
			except:
				print "Unable to create %s/images" % (H_DIR)
		elif (args.cType == "export"):
			try:
				os.makedirs(H_DIR)
			except:
				print "Unable to create %s" % (H_DIR)

# Create UID and change Directory permissions
UIDS = list()
COUNTS = dict()

if (args.cType == "ftp" or args.cType == "export"):
	PASSWD = commands.getstatusoutput("sudo /u01/ncftpd/sbin/ncftpd_passwd -f /u01/ncftpd/etc/passwd.db -x")[1]
	COLS = PASSWD.split(':')
	UIDS.append(COLS[2])
	UIDS = [int(NUM) for NUM in UIDS]
	UIDS.sort()
	for UID in UIDS:
		if UID not in COUNTS:
			COUNTS[UID] = 1
		else:
			COUNTS[UID] = COUNTS[UID] + 1
	for UID in range(FTP_RANGE_LOW,FTP_RANGE_HIGH+1):
		if UID not in UIDS: break
		if (UID == FTP_RANGE_HIGH):
			print "Out of UIDs in range %d - %d" % (FTP_RANGE_LOW,FTP_RANGE_HIGH)
		break
	UID = str(UID)
	GID = str(GID)
	os.system("chmod -R 0770 " + H_DIR)
	os.system("chown -R " + UID + " " + H_DIR)
	os.system("chgrp -R " + GID + " " + H_DIR)
	NFS4_DIR = H_DIR
	NFS4_DIR = NFS4_DIR.replace('u01', 'net/nfs4')
	NFS4_LIST = NFS4_DIR.split('/')
	PATH = "/"
	for i in NFS4_LIST:
		PATH = os.path.join(PATH,i)
		if not os.path.isdir(PATH):
			os.mkdir(PATH)
	FTP_ENTRY = [args.uName,PASSWORD,str(UID),str(GID),args.desc,H_DIR,FTP_SHELL]
	FTP_ENTRY = ':'.join(FTP_ENTRY)
	os.system("nfs4_setfacl -R -S /root/bin/acl_base " + NFS4_DIR)
	try:
		os.system("sudo /u01/ncftpd/sbin/ncftpd_passwd -f " + FTP_PASSWD + " -c -a " + FTP_ENTRY)
	except:
		print "Unable to create user: %s" % (args.uName)

	# Print Username, Password and Description
	print "-----------------------------------------"
	print "Username : %s" % (args.uName)
	print "Password : %s" % (PASSWORD)
	print "Description : %s" % (args.desc)
	print "-----------------------------------------"

