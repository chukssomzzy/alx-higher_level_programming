-- creates the database `hbtn_0d_usa` and the table `states` 

-- CREATE db 
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- select db
USE `hbtn_0d_usa`;

-- create table 
CREATE TABLE IF NOT EXISTS `states` (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL
);
