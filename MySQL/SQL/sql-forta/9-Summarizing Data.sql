SELECT AVG(prod_price) AS avg_price FROM Products;

SELECT AVG(prod_price) AS avg_price FROM Products
WHERE vend_id = 'DLL01';

SELECT COUNT(*) AS num_cust FROM Customers;

SELECT COUNT(cust_email) AS num_cust FROM Customers;

SELECT                           MAX(prod_price) as max_price FROM Products;

SELECT MIN(prod_price) as min_price FROM Products;

SELECT SUM(quantity) AS items_ordered FROM OrderItems
WHERE order_num = 20005;

SELECT AVG(DISTINCT prod_price) AS avg_price FROM Products
WHERE vend_id = 'DLL01';

SELECT COUNT(*) AS num_items,
       MIN(prod_price) AS min_price,
       MAX(prod_price) AS max_price,
       AVG(prod_price) AS avg_price,
       AVG(DISTINCT prod_price) AS avg_distinct_price
FROM Products;

-- Challenges
-- 1.
SELECT COUNT(quantity) AS total_sold_items FROM OrderItems;

SELECT COUNT(quantity) AS total FROM OrderItems
WHERE prod_id = 'BR01';

SELECT MAX(prod_price) as max_price FROM Products
WHERE prod_price <= 10;;