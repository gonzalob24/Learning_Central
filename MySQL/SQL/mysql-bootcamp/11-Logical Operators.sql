-- NOT EQUAL
SELECT * FROM books b 
WHERE released_year <> '2017';

SELECT * FROM books b 
WHERE released_year != '2017';

-- NOT LIKE
SELECT * FROM books b 
WHERE author_fname NOT LIKE 'D%' OR 'J%';

-- GREATER THAN, > or >=
SELECT * FROM books b 
WHERE stock_quantity > 100;

-- returns true as boolean logic 1 not 0
SELECT 99 > 1;
SELECT 'a' = 'A';

-- LESS THAN. < or <=
SELECT * FROM books b 
WHERE stock_quantity < 100;

-- AND
SELECT * FROM books b 
WHERE released_year > '2010' AND author_lname = 'Eggers';

SELECT * FROM books b 
WHERE released_year > '2010' && author_lname = 'Eggers';


-- OR
SELECT * FROM books b 
WHERE released_year > '2010' OR author_lname = 'Eggers';

-- BETWEEN --> NOT BETWEEN
SELECT * FROM books b 
WHERE stock_quantity BETWEEN '100' AND '150';

SELECT * FROM books b 
WHERE stock_quantity NOT BETWEEN '100' AND '150';


-- CAST
SELECT CAST('2017-04-01' AS DATETIME);


-- IN and NOT IN 
SELECT * FROM books b 
WHERE stock_quantity NOT IN ('100', '154');

-- CASE STATEMENTS
SELECT title, released_year,
	CASE
		WHEN released_year >= 2000 THEN 'Modern Lit'
		ELSE '20th Century Lit'
	END AS GENRE
FROM books b;
	
-- CHALLENGES
SELECT * FROM books b 
WHERE released_year < '1980';

SELECT * FROM books b 
WHERE author_lname = 'Eggers' OR author_lname = 'Chabon';

SELECT * FROM books b 
WHERE author_lname = 'Lahiri' AND released_year > '2000';

SELECT * FROM books b 
WHERE pages BETWEEN '100' AND '200';

SELECT * FROM books b 
WHERE author_lname LIKE 'C%' OR 'S%';

SELECT title, author_lname,
	CASE
		WHEN title LIKE '%stories%' THEN 'Short Story'
		WHEN title IN ('Just Kids', 'A Heartbreaking Work') THEN 'Memoir'
		ELSE 'Novel'
	END AS TYPE
FROM books b;

SELECT author_lname,
	CASE 
		WHEN COUNT(*) = 1 THEN CONCAT(COUNT(*), ' book')
		ELSE CONCAT(COUNT(*), ' books')
	END AS 'COUNT'
FROM books b
GROUP BY author_lname, author_fname;
	



















