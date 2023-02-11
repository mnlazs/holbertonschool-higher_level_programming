-- 0x0E. SQL - More queries, task 12
-- script that lists all shows contained in hbtn_0d_tvshows 
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_show.title, tv_show_genres.genre_id;