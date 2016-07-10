#!/usr/bin/python

import re
import urllib
from BeautifulSoup import *

total = 0
url = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html').read()
soup = BeautifulSoup(url)
tags = soup('span')

for line in tags:
	line = str(line)
	val = re.findall('[0-9]+', line)
	total = total + int(val[0])

print "Total: ", total
