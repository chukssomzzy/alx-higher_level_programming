-- Create user with only read privileges 

-- creates database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

-- create user 
CREATE USER IF NOT EXISTS `user_0d_2`@`localhost` IDENTIFIED BY 'user_0d_2_pwd';

-- grant read access 
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`; 

-- flush privileges 
FLUSH PRIVILEGES;
