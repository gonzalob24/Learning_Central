-- Make space in db to store data
CREATE DATABASE hello_world_db;

CREATE DATABASE cat_app;

DROP DATABASE testing_db;

DROP DATABASE hello_world_db;

DROP DATABASE cat_app;

-- using the db a bit different here than in the terminal
CREATE DATABASE dog_walking_app;

SELECT database(dog_walking_app); 

USE dog_walking_app;
SELECT * FROM dog_walking_app;


-- create a table
CREATE TABLE tablename
(
	column_name data_type,
	...
);


CREATE TABLE cats (
	name VARCHAR(100),
	age INT
);

CREATE TABLE pastries (
	name VARCHAR(50),
	quantity int
);

-- dropping a table
DROP TABLE cats;