SELECT cust_name, cust_contact, cust_email FROM Customers
WHERE cust_state IN ('IL','IN','MI');

SELECT cust_name, cust_contact, cust_email FROM Customers
WHERE cust_name = 'Fun4All';

SELECT cust_name, cust_contact, cust_email FROM Customers
WHERE cust_state IN ('IL','IN','MI') OR cust_name = 'Fun4All';

-- combining these into one
SELECT cust_name , cust_contact, cust_email FROM Customers
WHERE cust_state IN ('IL','IN','MI')
UNION 
SELECT cust_name, cust_contact, cust_email FROM Customers
WHERE cust_name = 'Fun4All';

-- this will include even duplicates
SELECT cust_name , cust_contact, cust_email FROM Customers
WHERE cust_state IN ('IL','IN','MI')
UNION ALL
SELECT cust_name, cust_contact, cust_email FROM Customers
WHERE cust_name = 'Fun4All'
ORDER BY cust_name, cust_email;

-- challenges
-- 1
SELECT oi.prod_id, oi.quantity FROM OrderItems oi 
WHERE quantity = 100
UNION 
SELECT oi.prod_id, oi.quantity FROM OrderItems oi
WHERE oi.prod_id LIKE 'BNBG%'
ORDER BY prod_id;

SELECT prod_id, quantity FROM OrderItems
WHERE quantity = 100
UNION
SELECT prod_id, quantity FROM OrderItems
WHERE prod_id LIKE 'BNBG%'
ORDER BY prod_id;

-- 2 using a single select statment
SELECT prod_id, quantity FROM OrderItems
WHERE quantity = 100
	OR prod_id LIKE 'BNBG%'
ORDER BY prod_id;

-- 3
SELECT prod_name FROM Products
UNION
SELECT cust_name FROM Customers
ORDER BY prod_name;









