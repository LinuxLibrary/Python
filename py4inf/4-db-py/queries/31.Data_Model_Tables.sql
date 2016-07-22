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


-- # Insert some data into Artist # --
INSERT INTO Artist (name) VALUES ('Led Zepplin');
INSERT INTO Artist (name) VALUES ('AC/DC');

-- # Insert some data into Genre # --
INSERT INTO Genre (name) VALUES ('Rock');
INSERT INTO Genre (name) VALUES ('Metal');

-- # Insert some data into Album # --
INSERT INTO Album (title, artist_id) VALUES ('Who made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);

-- # Insert some data into Track # --
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Black Dog', 5, 297, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Stairway', 5, 482, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('About to Rock', 5, 313, 0, 2, 1);
INSERT INTO Track (title, rating, len, count, album_id, genre_id) VALUES ('Who made Who', 5, 207, 0, 2, 1);

