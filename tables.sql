CREATE DATABASE APP;

USE APP;


CREATE TABLE Organizers(
o_id INT AUTO_INCREMENT,
o_name VARCHAR(30),
specialty VARCHAR(10),
PRIMARY KEY(o_id)
);

CREATE TABLE Competition(
c_id INT AUTO_INCREMENT,
c_name VARCHAR(50),
c_location VARCHAR(30),
c_date DATETIME,
participantsNo SMALLINT,
PRIMARY KEY(c_id)
);

CREATE TABLE User(
u_id INT AUTO_INCREMENT,
u_name VARCHAR(30),
u_address VARCHAR(30),
entriesNo INT,
PRIMARY KEY(u_id)
);

CREATE TABLE Flower(
f_id INT AUTO_INCREMENT,
u_id INT,
species VARCHAR(30),
size FLOAT,
color VARCHAR(10),
age TINYINT,
PRIMARY KEY(f_id),
FOREIGN KEY(u_id) REFERENCES User(u_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Annuals(
annual_id INT,
cosmos VARCHAR(30),
PRIMARY KEY(annual_id),
FOREIGN KEY(annual_id) REFERENCES competition(c_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Perennials(
perennial_id INT,
perennials VARCHAR(30),
PRIMARY KEY(perennial_id),
FOREIGN KEY(perennial_id) REFERENCES competition(c_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Creates(
o_id INT,
c_id INT,
PRIMARY KEY(o_id,c_id),
FOREIGN KEY(o_id) REFERENCES Organizers(o_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
FOREIGN KEY (c_id) REFERENCES Competition(c_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE Participates(
f_id INT,
c_id INT,
PRIMARY KEY(f_id,c_id),
FOREIGN KEY(f_id) REFERENCES Flower(f_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
FOREIGN KEY(c_id) REFERENCES Competition(c_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE has(
u_id INT,
c_id INT,
PRIMARY KEY(u_id,c_id),
FOREIGN KEY(u_id) REFERENCES User(u_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
FOREIGN KEY(c_id) REFERENCES Competition(c_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE enters(
u_id INT,
f_id INT,
PRIMARY KEY(u_id,f_id),
FOREIGN KEY(u_id) REFERENCES User(u_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
FOREIGN KEY(f_id) REFERENCES Flower(f_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

/*
managing databases 

CREATE DATABASE database;
USE table;
SHOW DATABASES;
SHOW TABLES;
SHOW COLUMNS FROM table;
DROP DATABASE database;

*/

/*managaging tables

INSERT INTO table(column names)VALUES(column values);
UPDATE table SET column1=value1... WHERE condition;
DELETE FROM table WHERE condition;
ALTER TABLE table...
    ADD
    ALTER COLUMN
    RENAME COLUMN name TO name
    DROP COLUMN;
*/

