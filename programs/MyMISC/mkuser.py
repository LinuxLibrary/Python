#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 20th Mar 2017

###############################
## Code revision information ##
###############################

# 20170320 		AS		Created mkuser.py



######################
## REQUIRED MODULES ##
######################

import os
import commands
import time
import re
from datetime import datetime

###############
## Variables ##
###############

TEST = True
U_CODE = ""
U_TYPE = ""
C_TYPE = "ftp"
USERNAME = ""
PASSWORD = ""
DESCRIPTION = ""
DIR = "/u01"
FTP_RANGE_LOW = 30000
FTP_RANGE_HIGH = 39999
FTP_PASSWD = "/u01/ncftpd/etc/passwd.db"
FTP_SHELL = None
MAXLEN = 10
GID = 500
FTP_CONTROL = "ftp20"
CURDATE = datetime.now()
RETVAL = None

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
			RETVAL = commands.getstatusoutput("sudo /u01/ncftpd/sbin/ncftpd_passwd -f FTP_PASSWD -q USER_NAME >/dev/null 2>/dev/null")[0]
			if (RETVAL == 0):
				print "User already exists!\n"
			elif (RETVAL == 256):
				TEST = False
			else:
				print "ERROR: ncftpd_passwd returned RETVAL!\n This script cannot continue!\n"
				os._exit(RETVAL)
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
print H_DIR	
