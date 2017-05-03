#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 03.05.2017
# Purpose : Usage of wrappers in Python

import time
import urllib2

def download_webpage():
	url = 'http://linux-library.blogspot.in'
	response = urllib2.urlopen(url, timeout = 60)
	return response.read()
def elapsed_time():
	t0 = time.time()
	webpage = download_webpage()
	t1 = time.time()
	print "Elapsed time is : %s\n" % (t1 - t0)
print elapsed_time()

def elapsed_time(function_to_time):
	def wrapper():
		t0 = time.time()
		function_to_time()
		t1 = time.time()
		print "Elapsed time is : %s\n" % (t1 - t0)
	return wrapper

@elapsed_time
def download_webpage():
        url = 'http://linux-library.blogspot.in'
        response = urllib2.urlopen(url, timeout = 60)
        return response.read()
download_webpage()

@elapsed_time
def another_function():
        print "Doing something else"
        for i in range(1,1000000):
		pass
another_function()

# END
