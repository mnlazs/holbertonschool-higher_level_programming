-- 0x0E. SQL - More queries, task 7.
-- a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Creates table `states` with fields `id` and `name`.
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE NOT NULL AUTO_INCREMENT FOREIGN KEY,
       name VARCHAR(256) NOT NULL
); 