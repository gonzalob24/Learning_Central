DROP TABLE pastries;

CREATE TABLE cats (
	name VARCHAR(50),
	age INT
);

INSERT INTO cats(name, age)
VALUES('Blue', 2);

INSERT INTO cats(name, age)
VALUE('Jetson', 7);

SELECT * FROM cats c;

-- multiple inserts
INSERT INTO cats(name, age)
VALUES ('Charlie', 10),
	   ('Sadie', 3),
	   ('Lazy Bear', 1);
	
	  
CREATE TABLE people (
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	age INT
);

INSERT INTO people (first_name, last_name, age)
VALUES ('Alison', 'Betancourt', 4),
       ('Alexa', 'Torres', 9),
       ('Maria', 'Margarito', 35);


       
--
INSERT INTO cats (name, age)
VALUES ('Butter Jack', '11');


-- age can be null by default even if not specified
INSERT INTO cats (name)
VALUES ('Jessis James');

-- we can specify when a field can't be null

CREATE TABLE cats2 (
	name VARCHAR(100) NOT NULL,
	age INT NOT NULL
);

-- no default value for age and will get an error
INSERT INTO cats2 (name)
VALUES ('Alison');

INSERT INTO cats2 (age) 
VALUES (10);

-- Setting default values
CREATE TABLE cats3 (
	name VARCHAR(100) DEFAULT 'unnamed',
	age INT DEFAULT 99
);

INSERT INTO cats3 (age)
VALUES (10);

INSERT INTO cats3 (name)
VALUES ('Alexa');

-- Combining
CREATE TABLE cats4 (
	name VARCHAR(100) NOT NULL DEFAULT 'unnamed',
	age INT NOT NULL DEFAULT 99,
);

INSERT INTO cats3 ()
VALUES ();

INSERT INTO cats4 ()
VALUES ();

INSERT INTO cats4(name, age)
VALUES ('Quetzal', null);


-- Primary Keys
-- every row must have a unique key to identify the resource

CREATE TABLE unique_cats (
	cat_id INT NOT NULL,
	name VARCHAR(100),
	age INT,
	PRIMARY KEY (cat_id)
);

INSERT INTO unique_cats (cat_id, name, age) 
VALUES (1, 'Fred', 23);

INSERT INTO unique_cats (cat_id, name, age) 
VALUES (2, 'Luis', 2);

-- throws a duplicate key error
INSERT INTO unique_cats (cat_id, name, age) 
VALUES (1, 'James', 4);


-- autogenerate the primary keys to avoid typing what key value we are in
CREATE TABLE unique_cats2 (
	cat_id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(100),
	age INT,
	PRIMARY KEY (cat_id)
);

INSERT INTO unique_cats2 (name, age) 
VALUES ('James', 4);

INSERT INTO unique_cats2 (name, age) 
VALUES ('Siko', 2);


-- practice
CREATE TABLE employees (
	id INT NOT NULL AUTO_INCREMENT,
	last_name VARCHAR(100) NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	middle_name VARCHAR(100),
	age INT NOT NULL,
	current_status VARCHAR(100) NOT NULL DEFAULT 'employed',
	PRIMARY KEY (id)
);

INSERT INTO employees (last_name, first_name, middle_name, age)
VALUES	('Torres', 'Alexa', 'Q', 9),
		('Alison', 'Betancourt', 'I', 4);