#!/usr/bin/python
# Author: Arjun Shrinivas
# Date: 12.04.2017

# This script is used to create subdirectories within ftp customer home directories

######################
## Revision History ##
######################
20170412  AS  Created

######################
## Required Modules ##
######################
import os


###############
## Variables ##
###############
BASE = "/net/u01/ftp"
#A_TYPE = ['fi','test','vendor','hub','rfi','analytics']
C_TYPE = raw_input("Please input account type(s)\nLeave empty if you have single account type: ").split()

## Check for ROOT-USER
if (os.getuid() != 0):
	print "This script must be run as root!"
	os.sys.exit()

## Check directory
if not C_TYPE:
	DIR = raw_input("Please input absolute path of the user: ")
#	print DIR
        if os.path.isdir(DIR):
		SDIRS = raw_input("Please input name(s) of sub-directories to be created: ").split()
                INDIR = os.path.join(DIR,'in')
                UID = str(os.stat(INDIR).st_uid)
                GID = str(os.stat(INDIR).st_gid)
                for SDIR in SDIRS:
                	SDIR = os.path.join(DIR,SDIR)
                        os.mkdir(SDIR)
                        os.system("chmod 770 " + SDIR)
                        os.system("chown " + UID + ":" + GID + " " + SDIR)
                        os.system("nfs4_setfacl -S /root/bin/acl_subdir " + SDIR)
        else:
                print "Account doesn't exists! Please input a valid ftp account and try again"
else:
	print C_TYPE
	BASE_DIR = "/net/u01/ftp"
	ACCOUNT = raw_input("Please input account name: ")
	SDIRS = raw_input("Please input name(s) of sub-directories to be created: ").split()
	for TYPE in C_TYPE:
		DIR = os.path.join(BASE_DIR,TYPE,ACCOUNT)
		if os.path.isdir(DIR):
			INDIR = os.path.join(DIR,'in')
			UID = str(os.stat(INDIR).st_uid)
			GID = str(os.stat(INDIR).st_gid)
			for SDIR in SDIRS:
				SDIR = os.path.join(DIR,SDIR)
				os.mkdir(SDIR)
				os.system("chmod 770 " + SDIR)
				os.system("chown " + UID + ":" + GID + " " + SDIR)
				os.system("nfs4_setfacl -S /root/bin/acl_subdir " + SDIR)
		else:
			print "Account doesn't exists! Please input a valid ftp account and try again"
# END
