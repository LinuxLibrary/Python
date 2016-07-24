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

