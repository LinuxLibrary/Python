#!/usr/bin/python

import urllib

user = raw_input('Enter your Github Login name: ')
passwd = raw_input('Enter your password: ')
url = 'https://api.github.com/user/repos/v3/authorize?'

query_args = { "grant_type":"password",
	"username":user,
	"password":passwd
}

encoded_args = urllib.urlencode(query_args)

repolist_url = url+urllib.urlopen(encoded_args)

print repolist_url
