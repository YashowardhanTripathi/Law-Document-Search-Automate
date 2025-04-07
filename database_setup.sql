-- Create the database
CREATE DATABASE crud_new1;

-- Use the database
USE crud_new1;

-- Create bns_sections table
CREATE TABLE bns_sections (
    id BIGINT DEFAULT NULL,
    IPC_Section VARCHAR(255),
    IPC_Heading VARCHAR(255),
    BNS_Section VARCHAR(255),
    BNS_Heading VARCHAR(255)
);

-- Create friends (IPC Sections) table
CREATE TABLE friends (
    id BIGINT DEFAULT NULL,
    sectionsCode VARCHAR(255),
    descriptions VARCHAR(255),
    punishments VARCHAR(255)
);

-- Create user_login table
CREATE TABLE user_login (
    id BIGINT NOT NULL AUTO_INCREMENT,
    userName VARCHAR(255),
    password VARCHAR(255),
    PRIMARY KEY (id)
);

-- Load data into bns_sections table
LOAD DATA INFILE 'D:/yash/IGNOU_Project/New_Sections_BKP.csv'
INTO TABLE bns_sections
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;