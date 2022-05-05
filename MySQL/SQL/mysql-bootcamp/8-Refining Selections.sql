INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES ('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
       ('fake_book', 'Freida', 'Harris', 2001, 287, 428),
       ('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);
       
  
SELECT title FROM books b;

-- DISTINCT: used in conjuction with SELECT to avoid selecting the duplicatesd
SELECT DISTINCT  author_lname FROM books b;
SELECT author_lname FROM books b;


SELECT DISTINCT released_year FROM books b;

SELECT DISTINCT COUNT(CONCAT(author_fname, ' ', author_lname)) FROM books b;

SELECT DISTINCT author_fname, author_lname FROM books b;


-- ORDER BY, ASC by default
SELECT author_lname FROM books b 
ORDER BY author_lname; 

SELECT title FROM books b
ORDER BY title;

SELECT author_lname FROM books b 
ORDER BY author_lname DESC;

SELECT title FROM books b 
ORDER BY title DESC;

SELECT released_year FROM books b 
ORDER BY released_year;

-- ORDER BY 2 refers to the column name in second position
SELECT title, author_fname, author_lname FROM books b 
ORDER BY 2;

SELECT author_fname, author_lname FROM books b 
ORDER BY author_lname, author_fname;

-- LIMIT: limit comes last
SELECT title FROM books b 
LIMIT 3;

	-- specify a starting point in the limit
SELECT  title, released_year FROM books b 
ORDER BY released_year DESC
LIMIT 0,5;

SELECT * FROM books b 
LIMIT 10, 18446744073709551615;

-- LIKE: used to do searching: % are wild cards
	-- % anything before da and anything after da
SELECT title, author_fname FROM books b
WHERE author_fname LIKE '%da%';

SELECT title, author_fname FROM books b
WHERE author_fname LIKE 'da%';

SELECT title FROM books b 
WHERE title LIKE '%the%';

-- ___" 4 underscores in a row means length of 4, 4 digits long
SELECT * FROM books b 
WHERE stock_quantity LIKE '____';

SELECT title FROM books b 
WHERE title LIKE '%\%%';

-- CHALLENGES
SELECT title FROM books b 
WHERE title LIKE '%stories%';

SELECT title, pages FROM books b 
ORDER BY pages DESC
LIMIT 1;

SELECT CONCAT(title, ' - ', released_year) AS summary FROM books b 
ORDER BY released_year DESC 
LIMIT 3;

SELECT title, author_lname FROM books b 
WHERE author_lname LIKE '% %';

SELECT title, released_year, stock_quantity FROM books b 
ORDER BY stock_quantity 
LIMIT 3;

SELECT title, author_lname FROM books b 
ORDER BY author_lname, title;

SELECT CONCAT(UPPER('my favorite author is '), UPPER(author_fname), ' ', UPPER(author_lname), '!')  
AS 'yell' FROM books b
ORDER BY author_lname ;










