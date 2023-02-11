-- 0x0E. SQL - More queries, task 13. No genre 
-- Lists all shows in `hbtn_0d_tvshows` without genre by title, genre.
SELECT tv_genres.name AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_show_genres
LEFT JOIN tv_genres
ON tv_genres.id = genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC;