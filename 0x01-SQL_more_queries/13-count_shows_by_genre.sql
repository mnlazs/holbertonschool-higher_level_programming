-- 0x0E. SQL - More queries, task 13. No genre 
-- Lists all shows in `hbtn_0d_tvshows` without genre by title, genre.
SELECT genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;