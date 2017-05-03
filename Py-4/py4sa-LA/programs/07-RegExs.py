#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 03.05.2017
# Purpose : Using Regular Expressions in Python

import re

line = "May  3 03:02:53 dev-r73 sshd[2877]: Failed password for root from 31.330.3.180 port 50388 ssh2"
# For the above line the patterns are explained below
'''
May			- 	[A-Z][a-z]{2}
1/2 spaces after that	-	\s{1,2}
1/2 digits for date	-	\d{1,2}
1 white space		-	\s
Time (03:02:53)		-	\d{2}:\d{2}:\d{2}
1 white space		-	\s
Hostname (word(s))	-	\w*
1 white space		-	\s
sshd			-	Leave it
[2877]			-	\[\d*\]
: Failed password for	-	Leave it
root			-	\w+
from			-	Leave it
31.330.3.180		-	\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
port			-	Leave it
50388			-	\d*
ssh2			-	Leave it
'''

match1 = re.search('[A-Z][a-z]{2}\s{1,2}\d{1,2}\s\d{2}:\d{2}:\d{2}\s\w*\ssshd\[\d*\]: Failed password for \w+ from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d* ssh2', line)

print match1

match2 = re.search('^(.*?)\s(\w+)\ssshd.*?Failed\spass.*?from\s(.*?)\sport.*$', line)
#print match
print match2.groups()

# END
