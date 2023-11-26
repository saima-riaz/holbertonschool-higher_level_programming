-- Select genre names for the show Dexter
-- Join tables to link genres, show genres, and shows
-- Filter for the show Dexter
-- Group results by genre name
-- Order results in ascending order by genre name
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY tv_genres.name
ORDER BY tv_genres.name ASC;
