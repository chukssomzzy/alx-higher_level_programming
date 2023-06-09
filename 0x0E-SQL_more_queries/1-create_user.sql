-- create a super user 

-- user  
CREATE USER IF NOT EXISTS `user_0d_1`@`localhost` IDENTIFIED BY 'user_0d_1_pwd';

-- GRANT priviledges 
GRANT ALL PRIVILEGES ON *.* TO `user_0d_1`@`localhost` WITH GRANT OPTION;
