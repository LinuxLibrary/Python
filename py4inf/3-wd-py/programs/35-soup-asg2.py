#!/usr/bin/python

import re, urllib
from BeautifulSoup import *

url = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Fikret.html').read()
soup = BeautifulSoup(url)
tags = soup('a')

for tag in tags:
	print tag
