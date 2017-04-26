#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 25.04.2017


# This script is used to create subdirectories within ftp customer home directories

######################
## Revision History ##
######################
20170425  AS  Created

######################
## Required Modules ##
######################
import os
import argparse

######################
## ARGUMENT PARSING ##
######################

parser = argparse.ArgumentParser(description="Create sub-directories for FTP users")
parser.add_argument("--aType", dest="aType", required=False, help="Input account type(s) enclosed in quotes and seperated by white space")
parser.add_argument("--user", dest="user", required=False, help="Input FTP User name")
parser.add_argument("--abPath", dest="abPath", required=False, help="Input absolute path of the FTP user Home Directory")
parser.add_argument("--sDirs", dest="sDirs", required=True, help="Input sub-directories enclosed in quotes and seperated by white space")
args = parser.parse_args()

###############
## VARIABLES ##
###############
BASE_DIR = "/net/u01/ftp"
C_TYPE = args.aType
SDIRS = args.sDirs
ACCOUNT = args.user

## Check for ROOT-USER
if (os.getuid() != 0):
        print "This script must be run as root!"
        os.sys.exit()

###############
## FUNCTIONS ##
###############

def create_dirs():
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

###############
## MAIN CODE ##
###############

if not C_TYPE:
	DIR = args.abPath
	DIR = DIR.lstrip('/')
	dList = DIR.split('/')
	if "net" not in dList:
		dList.insert(0, "net")
		DIR = "/" + '/'.join(dList)
	else:
		DIR = "/" + DIR
	create_dirs()
else:
	for TYPE in C_TYPE:
		DIR = os.path.join(BASE_DIR,TYPE,ACCOUNT)
		create_dirs()

# END
