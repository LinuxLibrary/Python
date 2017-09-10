-- # Reconstruct Data with JOINS # --

SELECT Album.title, Artist.name
FROM Album
JOIN Artist ON Album.artist_id = Artist.id
;

SELECT Album.title, Album.artist_id, Artist.id, Artist.name
FROM Album
JOIN Artist ON Album.artist_id = Artist.id
;

SELECT Track.title, Genre.name
FROM Track
JOIN Genre ON Track.genre_id = Genre.id
;
