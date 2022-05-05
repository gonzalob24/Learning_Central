-- WHERE is specifying search criteria
-- use right after the table name

-- simple equality test
SELECT prod_name, prod_price FROM Products
WHERE prod_price = 3.49;

-- Another simple example
SELECT prod_name, prod_price FROM Products
WHERE prod_price < 10;

-- check for non matches using a string delimiter
-- <> or !=
SELECT vend_id, prod_name FROM Products
WHERE vend_id <> 'DLL01';


-- range filtering
SELECT prod_name, prod_price FROM Products
WHERE prod_price BETWEEN 5 AND 10;

-- check for Null values
SELECT cust_name FROM Customers
WHERE cust_email IS NULL;

-- CHALLENGES --
--
--
-- 1. get prod_id and name from Products where price is 9,49
SELECT prod_price, prod_name FROM Products
WHERE prod_price = 9.49;

-- 2. where price is >=9
SELECT prod_price, prod_name FROM Products
WHERE prod_price >= 9;

-- 3. Get unique list ofg order numbers from OrderItems that contain 100 or more of any item
SELECT DISTINCT order_num FROM OrderItems
WHERE quantity >= 100;

-- 4. get prod_name, prod_price from Products for prices between 3, 6
-- sort by price
SELECT prod_name, prod_price FROM Products
WHERE prod_price BETWEEN 3 AND 6
ORDER BY prod_price;