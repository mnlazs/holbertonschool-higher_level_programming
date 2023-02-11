-- 0x0E. SQL - More queries, task 7.
-- a script that creates the database hbtn_0d_usa and the table cities
SELECT id, name
FROM cities
WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;