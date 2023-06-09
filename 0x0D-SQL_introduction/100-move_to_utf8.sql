-- Alter Database, Table and Colmn collate attribute

-- db 
USE hbtn_0c_0;

-- Change Database Collate 
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Alter table character set and collate 
ALTER TABLE first_table 
  CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter column 
ALTER TABLE first_table 
  MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
