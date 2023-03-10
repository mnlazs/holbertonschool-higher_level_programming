-- 0x0E. SQL - More queries, task 7.
-- a script that creates the database hbtn_0d_usa and the table cities
-- 0x0E. SQL - More queries, task 7. Cities table
-- Creates DB `hbtn_0d_usa`
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Creates table `cities` with fields `id`, `state_id`, and `name`.
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id) REFERENCES states(id)
);