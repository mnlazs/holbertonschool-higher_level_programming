-- 0x15. SQL - Introduction, task 15. 
-- script that lists the number of records with the same score in the table 
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;