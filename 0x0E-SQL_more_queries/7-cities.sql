-- CREATES the `hbtn_0d_usa` and the table `cities` 

-- creates db 
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- select database 
USE `hbtn_0d_usa`;

-- create cities table 
CREATE TABLE IF NOT EXISTS `cities` (
  id INT PRIMARY KEY AUTO_INCREMENT,
  state_id INT NOT NULL REFERENCES states(id),
  name VARCHAR(256) NOT NULL
) 
