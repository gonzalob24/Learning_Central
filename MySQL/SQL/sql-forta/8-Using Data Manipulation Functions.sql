SELECT vend_name, UPPER(vend_name) as vend_name_upcase FROM Vendors
ORDER BY vend_name;

SELECT cust_name, cust_contact FROM Customers
WHERE cust_contact = 'Michael Green';

SELECT cust_name, cust_contact FROM Customers
WHERE SOUNDEX(cust_contact) = SOUNDEX('Michael Green');

SELECT order_num FROM Orders
WHERE EXTRACT(year FROM order_date) = 2020;

SELECT order_num FROM Orders
WHERE YEAR(order_date) = 2020;

-- 1. 
SELECT cust_id, cust_contact AS customer_name, 
       CONCAT(UPPER(LEFT(cust_contact, 2)), UPPER(LEFT(cust_city, 3))) AS user_login
FROM Customers;

-- 2
SELECT order_num, order_date FROM Orders
WHERE YEAR(order_date) = 2020 AND MONTH(order_date) = 1
ORDER BY order_date;

