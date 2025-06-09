# Домашнее задание к лекции «Продвинутая выборка данных»

Задание 1.

заполняем таблицы данныи:

    INSERT INTO Genre (id, title) VALUES 
    (1, 'Rap'),
    (2, 'Hip-hop'),
    (3, 'Alternative Rock/Indie'),
    (4, 'Pop');

    INSERT INTO Artist (id, name) VALUES
    (1, 'Doppiez'),
    (2, 'Hollyflame'),
    (3, 'Weekey'),
    (4, 'SQWOZ BAB'),
    (5, 'ЛЁНЯ'),
    (6, 'Бонд с кнопкой'),
    (7, 'opium'),
    (8, 'SASHA MARNI'),
    (9, 'WHITE GALLOWS'),
    (10, 'Rozalia'),
    (11, 'MAUR'),
    (12, 'BARGAEV'),
    (13, 'nessqchai'),
    (14, 'MIKAYA'),
    (15, 'My Own Shadow'), 
    (16, 'The Band Name');

    INSERT INTO Genre_Artist (genre, artist) VALUES
    (1, 1), -- Rap - Doppiez
    (1, 2), -- Rap - Hollyflame
    (1, 3), -- Rap - Weekey
    (1, 4), -- Rap - SQWOZ BAB
    (1, 5), -- Rap - ЛЁНЯ
    (1, 11),-- Rap - MAUR
    (1, 12),-- Rap - BARGAEV
    (1, 14),-- Rap - MIKAYA
    (1, 15),-- Rap - My Own Shadow
    (3, 6), -- Alternative Rock/Indie - Бонд с кнопкой
    (3, 7), -- Alternative Rock/Indie - opium
    (3, 9), -- Alternative Rock/Indie - WHITE GALLOWS
    (3, 10),-- Alternative Rock/Indie - Rozalia
    (3, 16),-- Alternative Rock/Indie - The Band Name
    (2, 13),-- Hip-hop - nessqchai
    (2, 15),-- Hip-hop - My Own Shadow
    (4, 8); -- Pop - SASHA MARNI

    INSERT INTO Album (id, title, year) VALUES
    (1, 'Тени прошлого', 2024),
    (2, 'Городской дым', 2024),
    (3, 'Между строк', 2024),
    (4, 'Best of 2020', 2020),
    (5, 'My Sound', 2019),
    (6, 'Solo Tracks', 2023); 

    INSERT INTO Track (id, title, duration, album) VALUES
    (1, 'Третий лишний', 240, 1),
    (2, 'Врал', 220, 1),
    (3, 'Не стерпится, не слюбится', 210, 1),
    (4, 'Горе от ума', 230, 1),
    (5, 'Tokyo', 220, 2),
    (6, 'Кухни', 210, 2),
    (7, 'Говорила', 220, 2),
    (8, 'Вольная', 220, 2),
    (9, 'Голая', 230, 2),
    (10, 'Если это не любовь?', 250, 3),
    (11, 'Давай накуримся', 210, 3),
    (12, 'Два Типа', 220, 3),
    (13, '1v9', 200, 3),
    (14, 'Люби', 210, 3),
    (15, 'My Way', 180, 5),
    (16, 'Мой мир', 190, 4),
    (17, 'One Last Song', 210, 6), 
    (18, 'Fast Exit', 180, 5);

    INSERT INTO Artist_Album (artist, album) values
    (14, 1), -- MIKAYA - "Тени прошлого"
    (5, 1), -- ЛЁНЯ - "Тени прошлого"
    (1, 1), -- Doppiez - "Тени прошлого"
    (4, 2), -- SQWOZ BAB - "Городской дым"
    (6, 2), -- Бонд с кнопкой - "Городской дым"
    (7, 2), -- opium - "Городской дым"
    (8, 3), -- SASHA MARNI - "Между строк"
    (3, 3), -- Weekey - "Между строк"
    (13, 3),-- nessqchai - "Между строк"
    (16, 4),-- The Band Name - "Best of 2020"
    (15, 5),-- My Own Shadow - "My Sound"
    (8, 6); -- SASHA MARNI - "Solo Tracks"

    INSERT INTO Collection (id, title, year) VALUES
    (1, 'Top of the rap', 2024),
    (2, 'Underground Mixtape', 2024),
    (3, 'Chill Vibes', 2024),
    (4, 'Best of 2024', 2024),
    (5, 'Hits from 2018-2020', 2019);

    INSERT INTO Track_Collection (track, collection) VALUES
    (1, 1),  -- "Третий лишний" в "Top of the rap"
    (2, 1),  -- "Врал" в "Top of the rap"
    (3, 1),  -- "Не стерпится, не слюбится" в "Top of the rap"
    (4, 1),  -- "Горе от ума" в "Top of the rap"
    (5, 1),  -- "Tokyo" в "Top of the rap"
    (7, 1),  -- "Говорила" в "Top of the rap"
    (11, 1), -- "Давай накуримся" в "Top of the rap"
    (1, 2),  -- "Третий лишний" в "Underground Mixtape"
    (6, 2),  -- "Кухни" в "Underground Mixtape"
    (8, 2),  -- "Вольная" в "Underground Mixtape"
    (9, 2),  -- "Голая" в "Underground Mixtape"
    (12, 2), -- "Два Типа" в "Underground Mixtape"
    (13, 2), -- "1v9" в "Underground Mixtape"
    (4, 3),  -- "Горе от ума" в "Chill Vibes"
    (5, 3),  -- "Tokyo" в "Chill Vibes"
    (8, 3),  -- "Вольная" в "Chill Vibes"
    (9, 3),  -- "Голая" в "Chill Vibes"
    (10, 3), -- "Если это не любовь?" в "Chill Vibes"
    (14, 3), -- "Люби" в "Chill Vibes"
    (2, 4),  -- "Врал" в "Best of 2024"
    (3, 4),  -- "Не стерпится, не слюбится" в "Best of 2024"
    (5, 4),  -- "Tokyo" в "Best of 2024"
    (7, 4),  -- "Говорила" в "Best of 2024"
    (10, 4), -- "Если это не любовь?" в "Best of 2024"
    (12, 4), -- "Два Типа" в "Best of 2024"
    (3, 4),  -- Дополнительно добавили Hollyflame в Best of 2024
    (15, 5), -- "My Way" в "Hits from 2018-2020"
    (16, 5), -- "Мой мир" в "Hits from 2018-2020"
    (18, 5); -- "Fast Exit" в "Hits from 2018-2020"

Задание 2.

1. Название и продолжительность самого длительного трека.

        SELECT title, duration FROM Track ORDER BY duration DESC LIMIT 1;

2. Название треков, продолжительность которых не менее 3,5 минут.

        SELECT title, duration FROM Track WHERE duration >= 210 ORDER BY duration;

3. Названия сборников, вышедших в период с 2018 по 2020 год включительно.

        SELECT title, year FROM Collection WHERE year BETWEEN 2018 AND 2020;

4. Исполнители, чьё имя состоит из одного слова.

        SELECT name FROM Artist WHERE name NOT LIKE '% %';

5. Название треков, которые содержат слово «мой» или «my».

        SELECT title FROM Track WHERE title ILIKE '%мой%' OR title ILIKE '%my%';

Итог:

    SELECT title, duration FROM Track ORDER BY duration DESC LIMIT 1;
    SELECT title, duration FROM Track WHERE duration >= 210 ORDER BY duration;
    SELECT title, year FROM Collection WHERE year BETWEEN 2018 AND 2020;
    SELECT name FROM Artist WHERE name NOT LIKE '% %';
    SELECT title FROM Track WHERE title ILIKE '%мой%' OR title ILIKE '%my%';

Задание 3.

1. Количество исполнителей в каждом жанре.

        SELECT g.title AS genre, COUNT(ga.artist) AS artist_count
        FROM Genre g
        LEFT JOIN Genre_Artist ga ON g.id = ga.genre
        GROUP BY g.title;

2. Количество треков, вошедших в альбомы 2019–2020 годов.

        SELECT COUNT(*) AS track_count
        FROM Track t
        LEFT JOIN Album a ON t.album = a.id
        WHERE a.year BETWEEN 2019 AND 2020;

3. Средняя продолжительность треков по каждому альбому.

        SELECT a.title AS album, AVG(t.duration) AS avg_duration
        FROM Track t
        JOIN Album a ON t.album = a.id
        GROUP BY a.title
        ORDER BY avg_duration;

4. Все исполнители, которые не выпустили альбомы в 2020 году.

        SELECT ar.name
        FROM Artist ar
        WHERE ar.id NOT IN (
        SELECT artist
        FROM Artist_Album aa
        JOIN Album al ON aa.album = al.id
        WHERE al.year = 2020);

5. Названия сборников, в которых присутствует конкретный исполнитель.

        SELECT DISTINCT c.title AS collection
        FROM Collection c
        JOIN Track_Collection tc ON c.id = tc.collection
        JOIN Track t ON tc.track = t.id
        JOIN Album a ON t.album = a.id
        JOIN Artist_Album aa ON a.id = aa.album
        JOIN Artist ar ON aa.artist = ar.id
        WHERE ar.name = 'Doppiez';

Задание 4.

1. Названия альбомов, в которых присутствуют исполнители более чем одного жанра.

        SELECT a.title AS album
        FROM Album a
        JOIN Artist_Album aa ON a.id = aa.album
        JOIN Genre_Artist ga ON aa.artist = ga.artist
        GROUP BY a.title
        HAVING COUNT(DISTINCT ga.genre) > 1;

2. Наименования треков, которые не входят в сборники.

        SELECT t.title
        FROM Track t
        LEFT JOIN Track_Collection tc ON t.id = tc.track
        WHERE tc.track IS NULL;

3. Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.

        SELECT ar.name
        FROM Artist ar
        JOIN Artist_Album aa ON ar.id = aa.artist
        JOIN Track t ON aa.album = t.album
        WHERE t.duration = (SELECT MIN(duration) FROM Track);

4. Названия альбомов, содержащих наименьшее количество треков.

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
