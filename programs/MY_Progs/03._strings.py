#!/usr/bin/python
# Author : Arjun Shrinivas
# Purpose : Illustration of string match in Python

# Strings declaration

import string

message1 = raw_input("My String1 is : ")
message2 = raw_input("My String2 is : ")

# Main Program
if message1 == message2 :
        print "\n\t\tStrings match !"
        print "\t\t---------------"
        print "Raw value of String1\t--->\t", message1, "\nRaw value of String2\t--->\t", message2, "\n"
        print "Upper of String1\t--->\t", string.upper(message1), "\nUpper of String2\t--->\t", string.upper(message2), "\n"
        print "Init capitalize of String1\t--->\t", string.capitalize(message1), "\nInit capitalize of String2\t--->\t", string.capitalize(message2), "\n"
        print "Init capitalize for everyword of String1\t--->\t", string.capwords(message1), "\nInit capitalize for everyword of String2\t--->\t", string.capwords(messa
ge2), "\n"
        print "Split of String1\t--->\t", string.split(message1), "\nSplit of String2\t--->\t", string.split(message2), "\n"
        print "Join of String1\t--->\t", string.join(message1), "\nJoin of String2\t--->\t", string.join(message2), "\n"
else :
        print "\n\t\tStrings didn't match !"
        print "\t\t----------------------"
        print "Raw value of String1\t--->\t", message1, "\nRaw value of String2\t--->\t", message2, "\n"
        print "Upper of String1\t--->\t", string.upper(message1), "\nUpper of String2\t--->\t", string.upper(message2), "\n"
        print "Init capitalize of String1\t--->\t", string.capitalize(message1), "\nInit capitalize of String2\t--->\t", string.capitalize(message2), "\n"
        print "Init capitalize for everyword of String1\t--->\t", string.capwords(message1), "\nInit capitalize for everyword of String2\t--->\t", string.capwords(messa
ge2), "\n"
        print "Split of String1\t--->\t", string.split(message1), "\nSplit of String2\t--->\t", string.split(message2), "\n"
        print "Join of String1\t--->\t", string.join(message1), "\nJoin of String2\t--->\t", string.join(message2), "\n"
# END
