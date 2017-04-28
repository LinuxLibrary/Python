-- # Create Artist table with 2 columns id, name # --
CREATE TABLE Artist (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	name TEXT
);

-- # Create Genre table with 2 columns id, name # --
CREATE TABLE Genre (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT
);

-- # Create Album table with 3 columns id, artist_id, title # --
CREATE TABLE Album (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id INTEGER,
	title TEXT
);

-- # Create Track table with 7 columns id, title, album_id, genre_id, len, rating and count # --
CREATE TABLE Track (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT,
	album_id INTEGER,
	genre_id INTEGER,
	len INTEGER,
	rating INTEGER,
	count INTEGER
);
