-- Select the genre and count the number of shows 
-- Use a JOIN to link tv_genres with tv_show_genres and tv_shows
-- Group the results by genre
-- Order the results by the number of shows linked in descending order
SELECT tv_genres.name AS genre, count(*) AS number_of_shows
  FROM tv_genres
  JOIN tv_show_genres
  ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
