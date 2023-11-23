-- create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user if not exists
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'users_0d_2_pwd';
-- Grant SELECT privilege on the specific database
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
