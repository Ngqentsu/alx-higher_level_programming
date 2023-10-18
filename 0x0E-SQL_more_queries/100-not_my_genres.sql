-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
SET @dexter_genre_id := (SELECT tv_genres.id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_shows.title = 'Dexter');
SELECT name FROM tv_genres
WHERE tv_genres.id NOT IN (@dexter_genre_id)
ORDER BY tv_genres.name ASC;
