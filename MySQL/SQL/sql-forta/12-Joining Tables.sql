SELECT p.prod_name, Vendors.vend_name, p.prod_price  FROM Products p, Vendors 
WHERE Vendors.vend_id  = p.vend_id 

-- same as above, inner join is used by default
SELECT vend_name , prod_name, prod_price FROM Vendors v 
JOIN Products p ON v.vend_id = p.vend_id;

-- joining tables, right down the information you need and then figure out how the tables are related
SELECT prod_name, vend_name , prod_price, quantity
FROM OrderItems oi, Products p, Vendors v 
WHERE oi.prod_id = p.prod_id
	AND p.vend_id = v.vend_id
	AND order_num = 20007;


-- recall this query
SELECT cust_name, cust_contact FROM Customers
WHERE cust_id IN (SELECT cust_id FROM Orders
                  WHERE order_num IN (SELECT order_num FROM OrderItems
                  WHERE prod_id = 'RGAN01'));
                  
            
-- using joins
SELECT cust_name, cust_contact FROM Customers c, Orders o, OrderItems oi 
WHERE c.cust_id = o.cust_id 
	AND oi.order_num = o.order_num 
	AND prod_id = 'RGAN01';
	

SELECT cust_name, cust_contact FROM Customers c 
JOIN Orders o ON o.cust_id = c.cust_id 
JOIN OrderItems oi ON oi.order_num = o.order_num 
WHERE prod_id = 'RGAN01';


-- Challenges
-- 1.
SELECT c.cust_name, o.order_num FROM Customers c 
JOIN Orders o ON c.cust_id = o.cust_id
ORDER BY cust_name, order_num;

-- 2. 
SELECT c.cust_name, o.order_num, SUM(oi.quantity*oi.item_price) as order_total FROM Customers c 
JOIN Orders o ON c.cust_id = o.cust_id
JOIN OrderItems oi ON oi.order_num = o.order_num 
GROUP BY o.order_num 
ORDER BY cust_name, order_num;

SELECT cust_name, Orders.order_num, Sum(item_price*quantity) AS OrderTotal
FROM Customers, Orders, OrderItems
WHERE Customers.cust_id = Orders.cust_id
 AND Orders.order_num = OrderItems.order_num
GROUP BY cust_name, Orders.order_num
ORDER BY cust_name, order_num;


-- 3
SELECT cust_id, order_date FROM Orders
WHERE order_num IN (SELECT order_num FROM OrderItems
                    WHERE prod_id = 'BR01')
ORDER BY order_date;

SELECT o.cust_id , o.order_date FROM Orders o 
JOIN OrderItems oi ON oi.order_num = o.order_num 
WHERE oi.prod_id = 'BR01'
ORDER BY order_date;

-- 4
SELECT cust_email FROM Customers
WHERE cust_id IN (SELECT cust_id FROM Orders
                  WHERE order_num IN (SELECT order_num FROM OrderItems
                                      WHERE prod_id = 'BR01'));

SELECT c.cust_email FROM Customers c 
JOIN Orders o ON o.cust_id = c.cust_id 
JOIN OrderItems oi ON oi.order_num = o.order_num 
WHERE prod_id = 'BR01';

-- 5
-- recall GROUP BY must use a real column name not one used to perform aggreagte calculations
SELECT cust_name, SUM(quantity*item_price) AS total_price
FROM Customers c
INNER JOIN Orders o ON o.cust_id = c.cust_id
INNER JOIN OrderItems oi ON oi.order_num = o.order_num 
GROUP BY cust_name
HAVING total_price >= 1000
ORDER BY cust_name;

SELECT cust_name, SUM(item_price*quantity) AS total_price
FROM Customers 
 INNER JOIN Orders ON Customers.cust_id = Orders.cust_id 
 INNER JOIN OrderItems ON Orders.order_num = OrderItems.order_num
GROUP BY cust_name
HAVING SUM(item_price*quantity) >= 1000
ORDER BY cust_name;







