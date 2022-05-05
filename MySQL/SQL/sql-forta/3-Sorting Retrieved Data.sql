-- ORDER BY make sure this is my last clause
SELECT prod_name FROM Products
ORDER BY prod_name;

-- sort my using multiple conditions
SELECT prod_id, prod_price, prod_name FROM Products
ORDER BY prod_price, prod_name;

-- Sort by column position based on the SELECT list
SELECT prod_id, prod_price, prod_name FROM Products
ORDER BY 2, 3;

-- sort direction ACS and DESC
SELECT prod_id, prod_price, prod_name FROM Products
ORDER BY prod_price DESC;

-- sort direction using multiple columns
SELECT prod_id, prod_price, prod_name FROM Products
ORDER BY prod_price DESC, prod_name DESC;

SELECT cust_name FROM Customers
ORDER BY cust_name DESC;


-- get cust_id
SELECT cust_id, order_num FROM Orders
ORDER BY cust_id, order_num;

-- get quantity and prcie
SELECT quantity, item_price FROM OrderItems
ORDER BY quantity DESC, item_price DESC;