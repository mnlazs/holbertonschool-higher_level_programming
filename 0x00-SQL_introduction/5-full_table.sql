-- 0x05. SQL - Introduction, task 5. print full description
-- script that prints the full description of the table first_table without using DESCRIBE or EXPLAIN
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table' AND TABLE_SCHEMA = 'hbtn_0c_0';
