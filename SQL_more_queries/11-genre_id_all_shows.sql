-- Select the title of TV shows and genre_id from the specified tables
-- Use a LEFT JOIN to include all records from tv_shows even if there is no matching record in tv_show_genres
-- Join the tables on the show_id column in tv_show_genres and the id column in tv_shows
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id;
