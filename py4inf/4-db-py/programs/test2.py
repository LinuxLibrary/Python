#!/usr/bin/python

import sqlite3

name = raw_input("Please input name: ")
conn = sqlite3.connect('test.db')
cur = conn.cursor()

cur.execute('''SELECT name FROM Users WHERE name = ?''', (name, ))
row = cur.fetchone()

print row
