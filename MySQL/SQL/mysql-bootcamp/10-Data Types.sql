-- Working with data types

-- http://webdev.slides.com/coltsteele/mysql-99-102
-- Use CHAR when storing fixed legnth text
-- otherwise use VARCHAR 

CREATE DATABASE newtesting;

CREATE TABLE dogs (
	name CHAR(5),
	breed VARCHAR(10)
);

INSERT INTO dogs (name, breed)
VALUES ('bob', 'beagle'),
	   ('robby', 'corgi'),
	   ('Jane', 'Retriever');

SELECT * FROM dogs;

-- INT

-- DECIMAL(max_number_of_digits, digits_after_decimal)
	-- DECIMAL(5, 2) --> 999.22

CREATE TABLE items (
	price DECIMAL(5,2)
);

INSERT INTO items(price)
VALUES (7);

INSERT INTO items(price)
VALUES (34.88); 

INSERT INTO items(price)
VALUES (1.9999);

INSERT INTO items(price)
VALUES (798);

SELECT * FROM items i;

-- FLOAT (~7) (4 bytes) / DOUBLE (~15) (8 bytes)
	-- are not precise after a certain amount of digits
	-- Always try and use decimals unless precision does not matter

CREATE TABLE stuff (price FLOAT);

INSERT INTO stuff (price)
VALUES (88.45);

INSERT INTO stuff (price)
VALUES (88.7745);

INSERT INTO stuff (price)
VALUES (8877.45);

INSERT INTO stuff (price)
VALUES (88.77665544);

SELECT * FROM stuff;

-- DATES and TIMES
	-- DATE --> no time 'yyy-mm-dd'
	-- TIME --> no date 'hh:mm:ss'
	-- DATETIME --> date and time 'yyy-mm-dd hh:mm:ss'

CREATE TABLE people (
	name VARCHAR(100),
	bdate DATE,
	btime TIME,
	bdatetime DATETIME);


INSERT INTO people (name, bdate, btime, bdatetime)
VALUES ('Jack', '1983-11-11', '10:07:35', '1983-11-11 10:07:35');

INSERT INTO people (name, bdate, btime, bdatetime)
VALUES ('Padma', '1943-1-1', '11:20:18', '1943-1-1 11:20:18');


-- CURDATE, CURTIME, NOW

INSERT INTO people (name, bdate, btime, bdatetime) 
VALUES ('Toaster', CURDATE(), CURTIME(), NOW());

SELECT * FROM people;


-- Formatting DATES : Check the docs for additional DATE_FORMATS
SELECT name, bdate, DAY(bdate), DAYNAME(bdate), 
DAYOFWEEK(bdate), DAYOFYEAR(bdate)  FROM people;

SELECT name, bdatetime, DAY(bdatetime),
DAYNAME(bdatetime), DAYOFWEEK(bdatetime), DAYOFYEAR(bdatetime),
HOUR(bdatetime) FROM people;

SELECT DATE_FORMAT(bdatetime, '%W') FROM people p; 

SELECT DATE_FORMAT(bdatetime, '%m/%d/%Y') FROM people p; 


-- DATE Math
SELECT name, bdate, DATEDIFF(NOW(), bdate) FROM people p; 

SELECT bdatetime, DATE_ADD(bdatetime, INTERVAL 1 MONTH) FROM people p;

-- TIMESTAMPS
CREATE TABLE comments(
	content VARCHAR(100),
	created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO comments(content)
VALUES ('lol I found this funny'),
	   ('It was not funny at all');

SELECT * FROM comments;

-- I can use NOW or CURRENT_TIMESTAMP
CREATE TABLE comments2(
	content VARCHAR(100),
	created_at TIMESTAMP DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO comments2(content)
VALUES ('lol I found this funny too'),
	   ('It was not funny at all!!');

SELECT * FROM comments2;

UPDATE comments2
SET content = 'Ok maybe it was a bit funny...'
WHERE content = 'lol I found this funny too';

SELECT * FROM comments2;


-- USE CHAR when storign fixed length strings
-- 

CREAT TABLE inventory(
	item_name VARCHAR(100),
	price DECIMAL(8, 2),
	quantity INT
);

-- DATETIME vs TIMESTAMP:
	-- DATETIME has a longer range, TIMESTAMP takes up less space
	-- TIMESTAMP is used for things like meta-data about when something is created
	-- or updated.

SELECT DATE_FORMAT(CURDATE(), '%m/%d/%Y');
SELECT DATE_FORMAT(NOW(), '%M %D at %h:%i');
