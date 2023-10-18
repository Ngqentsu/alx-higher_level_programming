-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
USE hbtn_0d_tvshows;
SELECT name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
