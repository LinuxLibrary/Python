#!/usr/bin/python

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

fname = raw_input('Enter file name: ')
if (len(fname) < 1) : fname = 'Library.xml'

def lookup(d, tag):
	found = False
	for child in d:
		if found : return child.text
		if child.tag == 'key' and child.text == tag:
			found = True
	return None

stuff = ET.parse(fname)
data = stuff.findall('dict/dict/dict')
print "Dict Count: ", len(data)

for entry in data:
	if ( lookup(entry, 'Track ID') is None ) : continue
	
	name = lookup(entry, 'Name')
	artist = lookup(entry, 'Artist')
	album = lookup(entry, 'Album')
	genre = lookup(entry, 'Genre')
	length = lookup(entry, 'Total Time')
	rating = lookup(entry, 'Rating')
	count = lookup(entry, 'Play Count')
	if name is None or artist is None or album is None or genre is None :
		continue
	
#	print name, artist, album, genre, length, rating, count
	
	cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', (artist, ))
	cur.execute('''SELECT id FROM Artist WHERE name = ( ? )''', (artist, ))
	artist_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', (genre, ))
	cur.execute('''SELECT id FROM Genre WHERE name = ( ? )''', (genre, ))
	genre_id = cur.fetchone()[0]

	cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', (album, artist_id))
	cur.execute('''SELECT id FROM Album WHERE title = ( ? )''', (album, ))
	album_id = cur.fetchone()[0]
	
	cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES ( ?, ?, ?, ?, ?, ? )''', (name, album_id, genre_id, length, rating, count))
	
	conn.commit()

cur.execute('''SELECT Count(*) FROM Artist''')
art_total = cur.fetchone()[0]
cur.execute('''SELECT Count(*) FROM Genre''')
gnr_total = cur.fetchone()[0]
cur.execute('''SELECT Count(*) FROM Album''')
alb_total = cur.fetchone()[0]
cur.execute('''SELECT Count(*) FROM Track''')
trck_total = cur.fetchone()[0]

print "Total Artists: ", art_total, "\n", "Total Genre: ", gnr_total, "\n", "Total Albums: ", alb_total, "\n", "Total Tracks: ", trck_total
