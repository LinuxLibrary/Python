#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 20th Mar 2017

###############################
## Code revision information ##
###############################

# 20170323 		AS		Created mkuser.py



######################
## REQUIRED MODULES ##
######################

import os
import commands
import time
import re
import string
import random
from datetime import datetime

###############
## Variables ##
###############

TEST = True
U_CODE = ""
U_TYPE = ""
C_TYPE = "ftp"
USER_NAME = ""
USER_CHECK = ""
PASSWORD = ""
DESC = ""
DIR = "/u01"
FTP_RANGE_LOW = 30000
FTP_RANGE_HIGH = 39999
FTP_PASSWD = "/u01/ncftpd/etc/passwd.db"
FTP_SHELL = "none"
MAXLEN = 10
GID = 500
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



############
## GETOPS ##
############

# Get U_CODE FROM STDIN
os.system("clear")
print "\t==================================\n"
print "\t", CURDATE, "\n"
print "\tMake User Script for SPS customers\n"
while TEST:
	print " \t------ Internet FTP, RFC 959 ------"
	print "\t[H]ub \t\t\t(Hub tree - retailers/buyers)"
	print "\t[F]I Vendor \t\t(FI tree - DC3)"
	print "\t[R]etail Pro Vendor\t(RFI tree)"
	print "\t[V]endor \t\t(DC4 - most new)"
	print "\t[I]mages \t\t(Lamps Plus vendors)"
	print "\t[A]nalytics \t\t(Analytics)"
	print "\n\t-------- Secure protocols --------"
	print "\t[S]FTP \t\t\t(SSH file transfer protocol, RFC 4251-4256)"
	print "\tFTP/SS[L] \t\t(FTP with SSL/TLS extensions, RFC 2228, 4217)\n"
	U_CODE = raw_input("Select account type: ").lower()
	print "\nUser Code : %s" %(U_CODE)
	if (U_CODE == "h" or U_CODE == "v" or U_CODE == "f" or U_CODE == "r" or U_CODE == "u" or U_CODE == "i" or U_CODE == "a"):
		TEST = False
		if (U_CODE == "h"): U_TYPE = "hub"
		if (U_CODE == "f"): U_TYPE = "fi"
		if (U_CODE == "r"): U_TYPE = "rfi"
		if (U_CODE == "v" or U_CODE == "i"): U_TYPE = "vendor"
		if (U_CODE == "u"): U_TYPE = "home"
		if (U_CODE == "s"): U_TYPE = "sftp"
		if (U_CODE == "l"): U_TYPE = "ftps"
		if (U_CODE == "i"): U_CODE = "images"
		if (U_CODE == "a"): U_TYPE = "analytics"
		if (U_CODE == "home"): DIR = ""
		if (U_CODE == "home"): C_TYPE = "export"
	elif (U_CODE == "s" or U_CODE == "l"):
		RETVAL = commands.getstatusoutput("ssh -t FTP_CONTROL /root/bin/mksftpuser.bash")[0]
		print RETVAL
		# Don't need to do the rest if mksftpuser.bash failed.
		if (RETVAL == 256): os._exit(RETVAL)
		PATH_NAME = raw_input("\nEnter path: ")
		time.sleep(25)
		os.system("nfs4_setfacl -R -S /root/bin/acl_base $path_name/in")
		os.system("nfs4_setfacl -R -S /root/bin/acl_base $path_name/out")
		os.system("nfs4_setfacl -R -S /root/bin/acl_base $path_name/testin")
		os.system("nfs4_setfacl -R -S /root/bin/acl_base $path_name/testout")
		exit()
	else:
		print "Invalid Option!\n"

TEST = True
while TEST:
	USER_NAME = raw_input("\nEnter user name. Note, all usernames are converted to lowercase: ").lower()
	print USER_NAME
	if (USER_NAME == "" or len(USER_NAME) > MAXLEN):
		print "Usernames must begin with [a-z] and have max of %d chars.\n" % (MAXLEN)
	else:
		if (C_TYPE == "ftp" or C_TYPE == "export"):
			try:
				USER_CHECK = subprocess.check_output(["sudo","/u01/ncftpd/sbin/ncftpd_passwd","-f",FTP_PASSWD,"-q",USER_NAME]).strip()
			except:
				RETVAL = 256
			if USER_CHECK:
				print "User already exists!\n"
			elif (RETVAL == 256):
				TEST = False
			else:
				print "ERROR: ncftpd_passwd returned %d!\n This script cannot continue!\n" % (RETVAL)
				os._exit()
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
				else:
					TEST = False

TEST = True
while TEST:
	DESC = raw_input("\nEnter a description: ")
	print DESC
	SEARCH = re.search(r"([a-zA-Z_0-9]+)",DESC)
	if SEARCH:
		TEST = False
	else:
		print "Invalid description!\n"

H_DIR = "%s/%s/%s/%s" % (DIR,C_TYPE,U_TYPE,USER_NAME)
PASSWORD = password()

DIRCHECK = os.path.isdir(H_DIR)
if (DIRCHECK == True):
	print "Directory %s already exists!\n" % (H_DIR)
else:
	if (C_TYPE == "ftp"):
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
		if (U_CODE == "images"):
			try:
				os.makedirs(os.path.join(H_DIR, 'images'))
			except:
				print "Unable to create %s/images" 
		elif (C_TYPE == "export"):
			try:
				os.makedirs(H_DIR)
			except:
				print "Unable to create %s" % (H_DIR)

UIDS = list()
COUNTS = dict()

if (C_TYPE == "ftp" or C_TYPE == "export"):
	PASSWD = commands.getstatusoutput("sudo /u01/ncftpd/sbin/ncftpd_passwd -f /u01/ncftpd/etc/passwd.db -x")[1]
	for LINE in PASSWD:
		COLS = LINE.split(':')
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
	try:
		subprocess.check_output(["chmod","-R","0700",H_DIR])
	except:
		print "Unable to change permissions on %s" % (H_DIR)
	try:
		subprocess.check_output(["chown","-R",UID,H_DIR])
	except:
		print "Unable to change owner on %s" % (H_DIR)
	try:
		subprocess.check_output(["chgrp","-R",GID,H_DIR])
	except:
		print "Unable to change group on %s" % (H_DIR)
	NFS4_DIR = H_DIR
	NFS4_DIR = NFS4_DIR.replace('u01', 'net/nfs4')
	FTP_ENTRY = [USER_NAME,PASSWORD,UID,GID,DESC,H_DIR,FTP_SHELL]
	FTP_ENTRY = ':'.join(FTP_ENTRY)
	subprocess.check_output(["nfs4_setfacl","-R","-S","/root/bin/acl_base",NFS4_DIR])
	try:
		subprocess.check_output(["sudo","/u01/ncftpd/sbin/ncftpd_passwd","-f",FTP_PASSWD,"-c","-a",FTP_ENTRY])
	except:
		print "Unable to create user : %s" % (USER_NAME)
	print "-----------------------------------------"
	print "Username : %s" % (USER_NAME)
	print "Password : %s" % (PASSWORD)
	print "Description : %s" % (DESC)
	print "-----------------------------------------"
