#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 05.05.2017
# Purpose : Working with JSON in Python

import urllib
import json

url = "https://api.github.com/users/vmsnivas"
request = urllib.urlopen(url)
json_string = request.read()

print json_string


# END
