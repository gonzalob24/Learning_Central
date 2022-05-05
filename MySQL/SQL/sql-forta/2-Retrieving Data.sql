-- Find product names
SELECT prod_name FROM products;

-- find multiple column names
SELECT prod_name, prod_price, prod_id FROM products;

-- find all columns
SELECT * FROM Products;

-- Find distinct documents
SELECT DISTINCT vend_id, prod_price FROM Products;

-- Limit results
SELECT prod_name FROM Products
LIMIT 5;

-- using an offset to get the next five rows
-- useful for pagination
SELECT prod_name FROM Products
LIMIT 5 OFFSET 5;

-- all customer ids
SELECT cust_id FROM Customers;

-- unique prod_ids from OrderItems in order
SELECT DISTINCT prod_id FROM OrderItems;