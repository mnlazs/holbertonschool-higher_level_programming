-- 0x0E. SQL - More queries, task 14.
-- Lists all shows in `hbtn_0d_tvshows` without genre by title
SELECT genres.name
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
INNER JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name;