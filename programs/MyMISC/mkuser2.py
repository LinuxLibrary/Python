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
parser.add_argument("--ctype", dest="cType", default="ftp", required=True, help="FTP connection type (ftp|export)")
parser.add_argument("--atype", dest="aType", required=True, help="FTP account type (hub|fi|rfi|vendor|home|sftp|ftps|images|analytics)")
