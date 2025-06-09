
SELECT title, duration FROM Track ORDER BY duration DESC LIMIT 1;
SELECT title, duration FROM Track WHERE duration >= 210 ORDER BY duration;
SELECT title, year FROM Collection WHERE year BETWEEN 2018 AND 2020;
SELECT name FROM Artist WHERE name NOT LIKE '% %';
SELECT title FROM Track WHERE title ILIKE '%мой%' OR title ILIKE '%my%';



SELECT g.title AS genre, COUNT(ga.artist) AS artist_count
FROM Genre g
LEFT JOIN Genre_Artist ga ON g.id = ga.genre
GROUP BY g.title;

SELECT COUNT(*) AS track_count
FROM Track t
LEFT JOIN Album a ON t.album = a.id
WHERE a.year BETWEEN 2019 AND 2020;

SELECT a.title AS album, AVG(t.duration) AS avg_duration
FROM Track t
JOIN Album a ON t.album = a.id
GROUP BY a.title
ORDER BY avg_duration;

SELECT ar.name
FROM Artist ar
WHERE ar.id NOT IN (
SELECT artist
FROM Artist_Album aa
JOIN Album al ON aa.album = al.id
WHERE al.year = 2020);

SELECT DISTINCT c.title AS collection
FROM Collection c
JOIN Track_Collection tc ON c.id = tc.collection
JOIN Track t ON tc.track = t.id
JOIN Album a ON t.album = a.id
JOIN Artist_Album aa ON a.id = aa.album
JOIN Artist ar ON aa.artist = ar.id
WHERE ar.name = 'Doppiez';



SELECT a.title AS album
FROM Album a
JOIN Artist_Album aa ON a.id = aa.album
JOIN Genre_Artist ga ON aa.artist = ga.artist
GROUP BY a.title
HAVING COUNT(DISTINCT ga.genre) > 1;

SELECT t.title
FROM Track t
LEFT JOIN Track_Collection tc ON t.id = tc.track
WHERE tc.track IS NULL;

SELECT ar.name
FROM Artist ar
JOIN Artist_Album aa ON ar.id = aa.artist
JOIN Track t ON aa.album = t.album
WHERE t.duration = (SELECT MIN(duration) FROM Track);

SELECT a.title
FROM Album a
JOIN Track t ON a.id = t.album
GROUP BY a.title
HAVING COUNT(t.id) = (
    SELECT COUNT(t.id)
    FROM Track t
    GROUP BY t.album
    ORDER BY COUNT(t.id)
    LIMIT 1);
