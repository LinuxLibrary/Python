#!/usr/bin/python

choice = raw_input('Enjoying the course? (y/n)')
while choice[0] not in ('y' or 'n'):  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")
