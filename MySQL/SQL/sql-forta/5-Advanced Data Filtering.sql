-- WHERE with IN and NOT operators
-- can use multiple where clauses with AND , OR
SELECT prod_id, prod_price, prod_name FROM Products
WHERE vend_id = 'DLL01' AND prod_price <= 4
ORDER BY prod_name DESC;

SELECT vend_id, prod_price, prod_name FROM Products
WHERE vend_id = 'DLL01' OR vend_id = 'BRS01'
ORDER BY prod_price;

-- combining both of them
-- make sure to have AND with OR in the correct order
-- this query will return items with price <= 10;
--  ADN before OR
SELECT prod_id, prod_name, prod_price FROM Products
WHERE vend_id = 'DLL01' or vend_id = 'BRS01'
    AND prod_price >= 10;

-- use () to fix the issue
SELECT prod_id, prod_name, prod_price FROM Products
WHERE (vend_id = 'DLL01' or vend_id = 'BRS01')
    AND prod_price >= 10;


-- IN operator IN('', ''...) list of items separated by comma
-- similar behavior as OR but IN is faster when using long lists
SELECT prod_name, prod_price FROM Products
WHERE vend_id IN ('DLL01', 'BRS01')
ORDER BY prod_name;

-- NOT used with some syntax
-- <> has similar behavior
SELECT prod_name FROM Products
WHERE NOT vend_id = 'DLL01'
ORDER BY prod_name;

-- CHALLENGES
-- 1. get vendor name from Vendors return on vendors in California
-- filter by country and state
SELECT vend_name FROM Vendors
WHERE vend_country = 'USA' AND vend_state = 'CA'
ORDER BY vend_state;

-- 2. find all orders where at least 100 of items BR01, 02, 03 were ordered. 
-- show order_num, prod_id, quantity from OrderItems
SELECT order_num, prod_id, quantity From OrderItems
WHERE prod_id IN ('BR01', 'BR02', 'BR03') AND quantity >= 100;

-- 3. get prod_name and prod_price from Products priced between 3 and 6. 
-- use AND and sort by price
SELECT prod_name, prod_price FROM Products
WHERE prod_price >= 3 AND prod_price <= 6
ORDER BY prod_price DESC;