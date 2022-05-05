-- Aggregat Functio;ns: Op;erate on a set of rows to calculate and return a single VALUES 

-- * counts every row
SELECT COUNT(*) FROM books b; 
-- count distinct author first names
SELECT COUNT(DISTINCT author_fname) FROM books b; 

-- how many unique authors
SELECT COUNT(DISTINCT author_lname, author_fname) FROM books b;

-- How many titles contain "the"
SELECT COUNT(title) FROM books b 
WHERE title LIKE '%the%';

-- GROUP BY: Summarizes or aggregates identical data into single rows
SELECT author_lname, COUNT(*) AS books FROM books b 
GROUP BY author_lname
ORDER BY books;

SELECT author_lname FROM books b
GROUP BY author_lname;

-- MIN and MAX
SELECT MIN(released_year) FROM books b;

SELECT MAX(released_year) FROM books b;

SELECT * FROM books b
WHERE pages = (SELECT MAX(pages) FROM books b);

SELECT pages, title FROM books b 
ORDER BY pages DESC 
LIMIT 1;

SELECT author_fname, author_lname, MIN(released_year) FROM books b 
GROUP BY author_lname, author_fname;

SELECT author_fname, author_lname, MAX(pages) FROM books b
GROUP BY author_lname, author_fname;

-- SUM
SELECT SUM(pages) FROM books b;

SELECT author_fname, author_lname, SUM(pages) FROM books b
GROUP BY author_lname, author_fname;

-- Avg Function
SELECT author_fname, author_lname, AVG(pages) FROM books b
GROUP BY author_lname , author_fname;

SELECT released_year, AVG(stock_quantity) FROM books b
GROUP BY released_year;

SELECT author_fname, author_lname, AVG(pages) FROM books b
GROUP BY author_lname, author_fname;

-- CHALLENGES
SELECT COUNT(*) FROM books b;

SELECT released_year, COUNT(*) FROM books b
GROUP BY released_year;

SELECT SUM(stock_quantity) FROM books b;

SELECT author_fname, author_lname, AVG(released_year) FROM books b
GROUP BY author_lname, author_fname;

SELECT CONCAT(author_fname, ' ', author_lname) AS full_name, pages FROM books b
WHERE pages = (SELECT MAX(pages) FROM books);

SELECT released_year AS 'year', COUNT(*) AS 'books', AVG(pages) AS 'avg pages' FROM books b
GROUP BY released_year
ORDER BY released_year ASC;


