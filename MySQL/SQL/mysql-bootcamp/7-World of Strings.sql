-- String functions we can use when selecting strings
-- I can have multiple concats per select
-- CONCAT_WS
SELECT CONCAT(author_fname, ' ', author_lname) FROM books b; 

SELECT CONCAT(author_fname, ' ', author_lname) AS full_name FROM books b; 

SELECT author_fname AS first, author_lname AS last,
CONCAT(author_fname, ' ', author_lname) AS full_name FROM books b; 

SELECT CONCAT_WS('-', title, author_fname, author_lname) AS 'Title - Author' FROM books b;

-- SUBSTRING
SELECT SUBSTRING('Hello World', 1, 4); 

SELECT SUBSTRING('Hello World', 7); 
SELECT SUBSTRING('Hello World', 3); 
SELECT SUBSTRING('Hello World', -3); 

SELECT SUBSTRING(title, 1, 10) FROM books b; 

SELECT CONCAT(SUBSTRING(title, 1, 10), '...') AS short_title FROM books b; 
SELECT CONCAT(SUBSTR(title, 1, 10), '...') AS short_title FROM books b;

-- REPLACE --> replace parts of a string
-- Its case sensitive
SELECT REPLACE('Hello World', 'Hell', '%#@&');
SELECT REPLACE('HellO World', 'o', '*');

SELECT REPLACE(title, 'e', 3) FROM books b;

SELECT CONCAT(SUBSTRING(REPLACE(title, 'e', 3), 1, 10), '...') AS 'custom title' FROM books b; 

-- REVERSE
SELECT REVERSE('Hello World'); 

SELECT REVERSE(author_fname) FROM books b; 

SELECT CONCAT('woof', REVERSE('woof')); 

SELECT CONCAT(author_fname, REVERSE(author_fname)) FROM books b;

-- CHAR LENGTH
SELECT CHAR_LENGTH('Hello World');

SELECT author_lname, CHAR_LENGTH(author_lname) AS lname_length FROM books b; 
SELECT CONCAT(author_lname, ' is ', CHAR_LENGTH(author_lname), ' characters long') FROM books b;

-- UPPER CASE and LOWER CASE
SELECT UPPER('Hellow World'); 
SELECT LOWER('Hellow World'); 

SELECT UPPER(title) FROM books b; 

SELECT CONCAT(UPPER('my favorite book is '), UPPER(title)) FROM books b; 


-- CHALLENGES

SELECT REVERSE(UPPER('Why does my cal look at me with such hatred?'));

SELECT REPLACE(CONCAT('I', ' ', 'like', ' ', 'cats'), ' ', '-');

SELECT REPLACE(CONCAT(title), ' ', '->') AS title FROM books b;
SELECT REPLACE(title, ' ', '->') AS title FROM books b;

SELECT author_lname AS forwards, REVERSE(author_lname) AS backwards FROM books b;

SELECT CONCAT(UPPER(author_fname), ' ', UPPER(author_fname)) as 'full name in caps' FROM books b; 

SELECT CONCAT('The ', title, ' was released in ', released_year) AS blurp FROM books b; 

SELECT title, CHAR_LENGTH(title) AS 'characer count' FROM books b;

SELECT CONCAT(SUBSTRING(title, 1, 10), '...') AS 'short title',
CONCAT(author_lname, ',', author_fname) AS author,
CONCAT(stock_quantity, ' in stock') AS quantity FROM books b;








