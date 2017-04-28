#!/usr/bin/python

file = raw_input("Enter file name: ")
fh = open(file)
#text = fh.read()
mails = dict()

for line in fh:
	if not line.startswith('From '): continue
	line = line.rstrip()
	line = line.split()
	mail = line[1]
	mails[mail] = mails.get(mail,0) + 1

bigmail = None
bigcount = None
for mail,count in mails.items():
	if bigcount is None or count > bigcount:
		bigmail = mail
		bigcount = count
#print mails
print bigmail, bigcount
