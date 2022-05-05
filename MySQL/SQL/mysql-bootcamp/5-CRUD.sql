-- CREATE is used with the INSERT INTO
DROP TABLE cats;

CREATE TABLE cats 
(
	cat_id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(100),
	breed VARCHAR(100),
	age INT,
	PRIMARY KEY (cat_id)
);

INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);
 
 
      
-- READ
      -- * means give me all of the columns in the table
      -- i can specify which columns I want col1, col2, ...
SELECT * FROM cats c;

SELECT name FROM cats c;

SELECT age FROM cats c;

SELECT cat_id FROM cats c;

SELECT name, age FROM cats c;

	-- WHERE clause: used to get specific items from the table based on columns in my query
	-- by default its case INSENSITIVE 

SELECT * FROM cats c 
WHERE age = 4;

SELECT * FROM cats c 
WHERE name = 'Egg';

SELECT cat_id FROM cats c; 

SELECT name, breed FROM cats c;

SELECT name, age FROM cats c 
WHERE breed = 'tabby';

SELECT cat_id, age FROM cats c 
WHERE cat_id = age;

	-- Aliases
SELECT cat_id as id, name as cat_name FROM cats c;

-- UPADTE
UPDATE cats
SET breed = 'Shorthair'
WHERE breed = 'Tabby';

UPDATE cats 
SET age = 14
WHERE name = 'Misty';

	-- SELECT before updating Look at chapter 14 in forta
SELECT * FROM cats c
WHERE c.name = 'Misty';
UPDATE cats
SET age = 20;

UPDATE cats 
SET name = 'Jack'
WHERE name = 'Jackson';

UPDATE cats 
SET breed = 'British Shorthair'
WHERE name = 'Ringo';

UPDATE cats 
SET age = 12
WHERE breed = 'Maine Coon';

-- DELETE
DELETE FROM cats 
WHERE name = 'Egg';

DELETE FROM cats 
WHERE age = 4;

DELETE FROM cats 
WHERE cat_id = age;

DELETE FROM cats;






























- END