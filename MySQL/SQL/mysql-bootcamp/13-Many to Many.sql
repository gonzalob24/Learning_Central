CREATE DATABASE tvreview_app;

CREATE TABLE reviewers(
	id INT AUTO_INCREMENT PRIMARY KEY, 
	first_name VARCHAR(100),
	last_name VARCHAR(100)
);

CREATE TABLE series(
	id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(100),
	released_year YEAR(4),
	genre VARCHAR(100)
);

CREATE TABLE reviews(
	id INT AUTO_INCREMENT PRIMARY KEY,
	rating DECIMAL(2,1),
	series_id INT,
	reviewer_id INT,
	FOREIGN KEY(series_id) REFERENCES series(id) ON DELETE CASCADE,
	FOREIGN KEY(reviewer_id) REFERENCES reviewers(id) ON DELETE CASCADE
);

-- Series data
INSERT INTO series (title, released_year, genre) VALUES
    ('Archer', 2009, 'Animation'),
    ('Arrested Development', 2003, 'Comedy'),
    ("Bob's Burgers", 2011, 'Animation'),
    ('Bojack Horseman', 2014, 'Animation'),
    ("Breaking Bad", 2008, 'Drama'),
    ('Curb Your Enthusiasm', 2000, 'Comedy'),
    ("Fargo", 2014, 'Drama'),
    ('Freaks and Geeks', 1999, 'Comedy'),
    ('General Hospital', 1963, 'Drama'),
    ('Halt and Catch Fire', 2014, 'Drama'),
    ('Malcolm In The Middle', 2000, 'Comedy'),
    ('Pushing Daisies', 2007, 'Comedy'),
    ('Seinfeld', 1989, 'Comedy'),
    ('Stranger Things', 2016, 'Drama');

-- reviewers data   
INSERT INTO reviewers (first_name, last_name) VALUES
    ('Thomas', 'Stoneman'),
    ('Wyatt', 'Skaggs'),
    ('Kimbra', 'Masters'),
    ('Domingo', 'Cortes'),
    ('Colt', 'Steele'),
    ('Pinkie', 'Petit'),
    ('Marlon', 'Crafford');
 
-- reviews data
INSERT INTO reviews(series_id, reviewer_id, rating) VALUES
    (1,1,8.0),(1,2,7.5),(1,3,8.5),(1,4,7.7),(1,5,8.9),
    (2,1,8.1),(2,4,6.0),(2,3,8.0),(2,6,8.4),(2,5,9.9),
    (3,1,7.0),(3,6,7.5),(3,4,8.0),(3,3,7.1),(3,5,8.0),
    (4,1,7.5),(4,3,7.8),(4,4,8.3),(4,2,7.6),(4,5,8.5),
    (5,1,9.5),(5,3,9.0),(5,4,9.1),(5,2,9.3),(5,5,9.9),
    (6,2,6.5),(6,3,7.8),(6,4,8.8),(6,2,8.4),(6,5,9.1),
    (7,2,9.1),(7,5,9.7),
    (8,4,8.5),(8,2,7.8),(8,6,8.8),(8,5,9.3),
    (9,2,5.5),(9,3,6.8),(9,4,5.8),(9,6,4.3),(9,5,4.5),
    (10,5,9.9),
    (13,3,8.0),(13,4,7.2),
    (14,2,8.5),(14,3,8.9),(14,4,8.9);
     
--
SELECT * FROM reviewers r;

SELECT * FROM reviews;
SELECT * FROM series s;

-- CHALLENGES
-- TV JOINS Challenge
SELECT title, r.rating  FROM series s
JOIN reviews r ON r.series_id = s.id;

-- I can group by id or title
SELECT title, AVG(r.rating) AS avg_rating FROM series s
JOIN reviews r ON r.series_id = s.id
GROUP BY s.id
ORDER BY avg_rating;

SELECT first_name, last_name, r2.rating FROM reviewers r
JOIN reviews r2 ON r2.reviewer_id = r.id;

SELECT * FROM series s
RIGHT JOIN reviews r ON r.series_id = s.id;

-- I can also use ISRATING(r.id)
SELECT title as unreviewed_series FROM series s
LEFT JOIN reviews r ON r.series_id = s.id
WHERE r.id IS NULL;

SELECT s.genre, ROUND(AVG(r.rating), 2) AS avg_rating FROM series s
JOIN reviews r ON r.series_id = s.id
GROUP BY genre
ORDER BY avg_rating;

SELECT first_name, last_name, 
	COUNT(r2.rating) AS 'COUNT', 
	IFNULL(MIN(r2.rating), 0) AS 'MIN', 
	IFNULL(MAX(r2.rating), 0) AS 'MAX', 
	ROUND(IFNULL(AVG(r2.rating), 0), 2) AS 'AVG',
	CASE 
		WHEN COUNT(r2.rating) = 0 THEN 'INACTIVE'
		ELSE 'ACTIVE'
	END as satus
FROM reviewers r
LEFT JOIN reviews r2 ON r2.reviewer_id = r.id
GROUP BY r.id;

SELECT first_name, last_name, 
	COUNT(r2.rating) AS 'COUNT', 
	IFNULL(MIN(r2.rating), 0) AS 'MIN', 
	IFNULL(MAX(r2.rating), 0) AS 'MAX', 
	ROUND(IFNULL(AVG(r2.rating), 0), 2) AS 'AVG',
	IF(COUNT(r2.rating) = 0, 'INACTIVE', 'ACTIVE') AS STATUS
FROM reviewers r
LEFT JOIN reviews r2 ON r2.reviewer_id = r.id
GROUP BY r.id;

-- JOINING all three tables
SELECT title, rating, CONCAT(r2.first_name, ' ', r2.last_name) AS reviewer FROM series s
LEFT JOIN reviews r ON r.series_id = s.id 
RIGHT JOIN reviewers r2 ON r2.id = r.reviewer_id
ORDER BY title;

SELECT title, rating, CONCAT(r2.first_name, ' ', r2.last_name) AS reviewer FROM series s
JOIN reviews r ON r.series_id = s.id 
JOIN reviewers r2 ON r2.id = r.reviewer_id
ORDER BY title;

SELECT IFNULL(title, 'None') AS title, IFNULL(rating, 0) AS rating, CONCAT(r2.first_name, ' ', r2.last_name) AS reviewer FROM series s
LEFT JOIN reviews r ON r.series_id = s.id 
RIGHT JOIN reviewers r2 ON r2.id = r.reviewer_id
ORDER BY title;




