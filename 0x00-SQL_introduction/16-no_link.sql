-- 0x16 SQL - Introduction, task 16. 
-- script that lists all records of the table 
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
