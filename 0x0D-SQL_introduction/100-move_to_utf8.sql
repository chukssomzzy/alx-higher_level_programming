-- Alter Database, Table and Colmn collate attribute
-- db 
USE hbtn_0c_0;
-- Change Database Collate 
ALTER DATABASE hbtn_0c_0
    CHARACTER SET UTF8MB4
    COLLATE UTF8MB4_UNICODE_CI;
-- Alter table character set and collate 
ALTER TABLE first_table 
  CONVERT TO CHARACTER SET UTF8MB4 COLLATE UTF8MB4_UNICODE_CI;
