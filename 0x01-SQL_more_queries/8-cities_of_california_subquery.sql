-- 0x0E. SQL - More queries, task 8.
--  script that lists all the cities of California
SELECT id, name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;