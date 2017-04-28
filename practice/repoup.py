#!/usr/bin/python

import urllib, json, re

user = raw_input('Please input your GitHub login name: ')
passwd = raw_input('Please input your password: ')

url = ''
fname = 'repos.txt'
fh = open(fname).read()

jdat = json.loads(str(fh))
acct = list()
repos = list()
hurl = list()
gurl = list()
git_prefix = 'git+ssh://'
git_suffix = '.git'
for line in jdat:
	account = str(line["owner"]["login"])
	if account in acct : continue
	acct.append(account)

for line in jdat:
	reponame = str(line["name"])
	if reponame in repos : continue
	repos.append(reponame)

	html_url = str(line["html_url"])
	hurl.append(html_url)
	purl = str(re.findall('git\S*', html_url)[0])
	git_url = git_prefix+purl+git_suffix
	gurl.append(git_url)
	print git_url

'''
	print "========================"
	print "Account: ", account
	print "Repository name: ", reponame
	print "HTML URL: ", html_url 
	print "========================"
'''

print acct
print repos
print hurl
print gurl
