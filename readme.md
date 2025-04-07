Law Automation Tool is widely open source to eloborate the automate process for day to day daily court functionalities and document creation. Also provide the better view of IPC sections and its descriptions as new implemented or ammendment of BNS (Bhartiya Nyaya sanhit) sections clearification and also coparision with IPC.

Installation:
pip install Python3
pip install Caption_Creator
pip install flask_sqlalchemy
pip install flask
pip install reportlab
pip install PIL
pip install django

DB Creation:
CREATE DATABASE 'crud_new1'

BNS Sections Table:
CREATE TABLE bns_sections (
    id bigint DEFAULT NULL,
    IPC_Section varchar(255),
    IPC_Heading varchar(255),
    BNS_Section varchar(255),
    BNS_Heading varchar(255)
);

IPC Sections Table:
CREATE TABLE friends (
    id bigint DEFAULT NULL,
    sectionsCode varchar(255),
    descriptions varchar(255),
    punishments varchar(255)
);

User Login Table:
CREATE TABLE user_login (
    id bigint NOT NULL AUTO_INCREMENT,
    userName varchar(255),
    password varchar(255),
    PRIMARY KEY ('id')
);


LOAD DATA INFILE 'D:\yash\IGNOU_Project\New_Sections_BKP.csv'
INTO TABLE bns_sections
FIELDS TERMINATED BY ','    -- Adjust if your fields are separated by a different character
OPTIONALLY ENCLOSED BY '"'  -- Adjust if your text fields are enclosed by quotes
LINES TERMINATED BY '\n'    -- Adjust if your lines end with a different character (e.g., '\r\n' for Windows)
IGNORE 1 ROWS;
