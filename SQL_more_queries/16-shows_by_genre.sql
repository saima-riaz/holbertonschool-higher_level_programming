-- Select the title of shows and genre name from tv_shows, tv_genres, and tv_show_genres
-- Use a LEFT JOIN to include all records from tv_shows even if there is no matching record in tv_show_genres
-- Join the tables on the show_id column in tv_show_genres and the id column in tv_shows
-- Use another LEFT JOIN to include shows without a genre
-- Join tv_genres on genre_id in tv_show_genres and id in tv_genres
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
