-- Script that create the database hbtn_0d_usa and table states
-- (in the database hbtn_0d_usa) onMySQL server
-- state description
-- id INT unique, auto generated, cant be null and is primary key
-- name VARCHAR(256) cant be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
