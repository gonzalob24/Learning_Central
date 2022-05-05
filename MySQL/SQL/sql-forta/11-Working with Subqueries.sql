SELECT order_num FROM OrderItems
WHERE prod_id = 'RGAN01';

SELECT cust_id FROM Orders
WHERE order_num IN ('20007', '20008');

-- combinng both into a subquery. Subqueries are always processed starting with the innermost SELECT statement
-- and working outward
-- this is performing two operations
-- subqueries con only return a single column. If I try to retrieve multiple columns I will get an error.
SELECT cust_id FROM Orders
WHERE order_num IN (SELECT order_num FROM OrderItems
                    WHERE prod_id = 'RGAN01');


SELECT cust_name, cust_contact FROM Customers
WHERE cust_id IN (SELECT cust_id FROM Orders
                  WHERE order_num IN (SELECT order_num FROM OrderItems
                  WHERE prod_id = 'RGAN01'));
  

SELECT COUNT(*) AS orders FROM Orders
WHERE cust_id = 1000000001;

-- Orders is a calcualted field using the COUNT() functions, this is executed onece for every customer in the list
SELECT cust_name, cust_state,
	(SELECT COUNT(*) FROM Orders
     WHERE Orders.cust_id = Customers.cust_id) AS orders
FROM Customers
ORDER BY cust_name;

-- Challengs
-- 1 
SELECT order_num FROM OrderItems
WHERE item_price >= 10;

-- combine the query from above
SELECT cust_id FROM Orders
WHERE order_num IN (SELECT order_num FROM OrderItems
                    WHERE item_price >= 10);

-- 2 date when BRO1 was ordered
SELECT order_num FROM OrderItems
WHERE prod_id = 'BR01';

SELECT cust_id, order_date FROM Orders
WHERE order_num IN (SELECT order_num FROM OrderItems
                    WHERE prod_id = 'BR01')
ORDER BY order_date;

-- 3
SELECT cust_email FROM Customers
WHERE cust_id IN (SELECT cust_id FROM Orders
                  WHERE order_num IN (SELECT order_num FROM OrderItems
                                      WHERE prod_id = 'BR01'));

-- 4 cust_ids with total amount they have ordered
SELECT SUM(quantity*item_price) AS total_ordered FROM OrderItems
GROUP BY order_num;

SELECT cust_id FROM Orders
WHERE order_num IN (SELECT SUM(quantity*item_price) AS total_ordered FROM OrderItems
                    GROUP BY order_num);


SELECT cust_id, (SELECT SUM(quantity*item_price) FROM OrderItems
                 WHERE Orders.order_num = OrderItems.order_num) AS total_ordered
FROM Orders
ORDER BY total_ordered;

-- 5
SELECT prod_id, COUNT(quantity) quant_sold FROM OrderItems
GROUP BY prod_id;

SELECT prod_name, (SELECT SUM(quantity) FROM OrderItems
                   WHERE OrderItems.prod_id = Products.prod_id) AS quant_sold
FROM Products;




-- 
SELECT order_num, item_price FROM OrderItems oi 
WHERE item_price > 10;

SELECT cust_id FROM Orders o 
WHERE order_num IN (SELECT order_num FROM OrderItems oi 
	   				WHERE item_price >= 10);

SELECT order_num FROM OrderItems oi
WHERE prod_id = 'BR01';

SELECT cust_id, order_date FROM Orders o
WHERE order_num IN (SELECT order_num FROM OrderItems oi
					WHERE prod_id = 'BR01')
ORDER BY order_date;

SELECT cust_email FROM Customers c 
WHERE cust_id IN (SELECT cust_id FROM Orders o
				  WHERE o.order_num IN (SELECT order_num FROM OrderItems oi
									  WHERE oi.prod_id = 'BR01'));									  							 
									 
SELECT SUM(quantity*item_price) AS total_ordered FROM OrderItems oi
GROUP BY order_num;		

SELECT cust_id, (SELECT SUM(quantity*item_price) FROM OrderItems oi WHERE oi.order_num = o.order_num) AS total_ordered
FROM Orders o;

SELECT prod_id, SUM(quantity) AS quantity_sold FROM OrderItems oi
GROUP BY prod_id;

SELECT prod_name, (SELECT SUM(quantity) FROM OrderItems oi WHERE oi.prod_id = p.prod_id) AS quantity_sold
FROM Products p;