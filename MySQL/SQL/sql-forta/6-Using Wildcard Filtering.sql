-- searching for specific text somewhere --> use wildcard to match parts of a value
-- LIKE --> wildcard, this is a predicate not an operator
-- % --> match any number of occurrences of any character
-- also matches zero or more characters
SELECT prod_id, prod_name FROM Products
WHERE prod_name LIKE 'fish%';

-- any cahracters before or after bean bag
SELECT prod_id, prod_name FROM Products
WHERE prod_name LIKE '%bean bag%';


-- begin with F and end with Y
SELECT prod_id, prod_name FROM Products
WHERE prod_name LIKE 'F%Y';

-- _ wildcard: its just like the %, but _ matches a single character
SELECT prod_id, prod_name FROM Products
WHERE prod_name LIKE '__ inch teddy bear';

SELECT prod_id, prod_name FROM Products
WHERE prod_name LIKE '%inch teddy bear%';

-- [] a set of characters
-- contacts whose name begins with letter J or M
SELECT cust_contact FROM Customers
WHERE cust_contact LIKE '[J]';

-- CHALLENGES
-- 1. get prod_name and description from Products and return those that have toy
SELECT prod_name, prod_desc FROM Products
WHERE prod_desc LIKE '%toy%';

-- 2. get prod_name and description from Products and return those that DO NOT have toy
SELECT prod_name, prod_desc FROM Products
WHERE NOT prod_desc LIKE '%toy%';

-- 3. get prod_name and description from Products and return those that have toy and carrots in description
SELECT prod_desc, prod_name FROM Products
WHERE prod_desc LIKE '%toy%' AND prod_desc LIKE '%carrots%';

-- 4. get prod_name and description from Products and return where both words toy and carrots appear in the description 
SELECT prod_desc, prod_name FROM Products
WHERE prod_desc LIKE '%toy%carrots%';