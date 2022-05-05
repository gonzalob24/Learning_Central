SELECT cust_id, cust_name, cust_contact FROM Customers
WHERE cust_name = (SELECT cust_name FROM Customers
				  WHERE cust_contact = 'Jim Jones');

-- using joins
SELECT c.cust_id, c.cust_name, c.cust_contact  FROM Customers c
JOIN Customers c2 ON c.cust_name = c2.cust_name 
WHERE c2.cust_contact = 'Jim Jones';

SELECT C.*, O.order_num, O.order_date, OI.prod_id, OI.quantity, OI.item_price
FROM Customers AS C, Orders AS O, OrderItems AS OI
WHERE C.cust_id = O.cust_id 
	AND OI.order_num = O.order_num 
	AND prod_id = 'RGAN01';
	

SELECT C.*, O.order_num, O.order_date, OI.prod_id, OI.quantity, OI.item_price
FROM Customers AS C
JOIN Orders O ON C.cust_id = O.cust_id 
JOIN OrderItems OI ON OI.order_num = O.order_num 
WHERE OI.prod_id = 'RGAN01';


SELECT Customers.cust_id, Orders.order_num FROM Customers
JOIN Orders ON Customers.cust_id = Orders.cust_id;

-- left joins include data that is even blank, customers with no orders
SELECT Customers.cust_id, Orders.order_num FROM Customers
LEFT JOIN Orders ON Customers.cust_id = Orders.cust_id;

SELECT Customers.cust_id, Orders.order_num FROM Customers
RIGHT JOIN Orders ON Customers.cust_id = Orders.cust_id;


SELECT Customers.cust_id, COUNT(Orders.order_num) AS num_ord
FROM Customers
JOIN Orders ON Customers.cust_id = Orders.cust_id
GROUP BY Customers.cust_id;

-- will include customers that have not yet placed any orders
SELECT Customers.cust_id, COUNT(Orders.order_num) AS num_ord
FROM Customers
LEFT JOIN Orders ON Customers.cust_id = Orders.cust_id
GROUP BY Customers.cust_id;

-- Challenges
-- 1
SELECT c.cust_name, o.order_num FROM Customers c 
JOIN Orders o ON o.cust_id = c.cust_id
ORDER BY c.cust_name;

SELECT cust_name, order_num
FROM Customers
 JOIN Orders ON Customers.cust_id = Orders.cust_id
ORDER BY cust_name;

-- 2
SELECT c.cust_name, o.order_num FROM Customers c 
LEFT JOIN Orders o ON o.cust_id = c.cust_id
ORDER BY c.cust_name;

-- 3
SELECT p.prod_name, oi.order_num FROM Products p 
LEFT JOIN OrderItems oi ON oi.prod_id = p.prod_id
ORDER BY p.prod_name;

SELECT prod_name, order_num
FROM Products LEFT OUTER JOIN OrderItems
 ON Products.prod_id = OrderItems.prod_id
ORDER BY prod_name;

-- 4
SELECT p.prod_name, COUNT(oi.order_num) AS orders FROM Products p 
LEFT JOIN OrderItems oi ON oi.prod_id = p.prod_id
GROUP BY p.prod_name 
ORDER BY p.prod_name;

SELECT prod_name, COUNT(order_num) AS orders
FROM Products LEFT OUTER JOIN OrderItems
 ON Products.prod_id = OrderItems.prod_id
GROUP BY prod_name
ORDER BY prod_name;

-- 5: Left or Right join depending on where the From starts or join starts
SELECT v.vend_id, COUNT(prod_id) AS availale_products FROM Products p 
RIGHT  JOIN  Vendors v ON v.vend_id = p.vend_id
GROUP BY v.vend_id;

SELECT Vendors.vend_id, COUNT(prod_id)
FROM Vendors
 LEFT OUTER JOIN Products ON Vendors.vend_id = Products.vend_id
GROUP BY Vendors.vend_id;


