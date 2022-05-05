
SELECT COUNT(*) AS num_prods FROM Products
WHERE vend_id = 'DLL01';

-- grouping is used to instruct the DBMS to sort the data and group it by vend_id
-- so num_prods is calcualted once per vend_id
SELECT vend_id, COUNT(*) AS num_prods FROM Products
GROUP BY vend_id;

-- filter groups
SELECT cust_id, COUNT(*) AS orders FROM Orders
GROUP BY cust_id
HAVING COUNT(*) = 1; 

SELECT vend_id, COUNT(*) AS num_prods FROM Products
WHERE prod_price >= 4
GROUP BY vend_id
HAVING COUNT(*) >= 2;

SELECT order_num, COUNT(*) AS items FROM OrderItems
GROUP BY order_num
HAVING COUNT(*) >= 3
ORDER BY order_num, order_num;

-- Challenges
-- 1
SELECT order_num, COUNT(*) AS order_lines FROM OrderItems
GROUP BY order_num
ORDER BY order_lines;

SELECT order_num, quantity  FROM OrderItems oi;

SELECT DISTINCT order_num FROM OrderItems oi
WHERE quantity >= 100;

SELECT DISTINCT order_num  FROM OrderItems oi;
SELECT order_num FROM OrderItems oi
GROUP BY order_num;

SELECT order_num FROM OrderItems oi
GROUP BY order_num
HAVING SUM(quantity) >= 100;

SELECT vend_id, MIN(prod_price) AS cheapest_item FROM Products
GROUP BY prod_id
ORDER BY cheapest_item;

-- recall GROUP BY must use a real column name not one used to perform aggreagte calculations
SELECT order_num, SUM(quantity*item_price) AS best_customers FROM OrderItems
GROUP BY order_num
HAVING SUM(quantity*item_price) >= 1000
ORDER BY order_num;
