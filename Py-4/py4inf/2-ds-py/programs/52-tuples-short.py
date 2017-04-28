#!/usr/bin/python
# This is a short version of using the reverse sorting using tuples.
# It works same like the previous program but the difference is just we are using a different logic to shorten the program.

c = {'a':10, 'b':1, 'c':22}
# print sorted( [ (v,k) for k, v in c.items() ] )
fout =  sorted( [ (v,k) for k, v in c.items() ] )
print fout
