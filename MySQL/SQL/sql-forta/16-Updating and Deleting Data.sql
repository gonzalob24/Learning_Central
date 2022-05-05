-- UPDATE 
UPDATE Customers c
SET cust_name = 'The Fudds',
	cust_email = 'elmer234@fudd.com'
WHERE cust_id = 1000000005;

-- DELETING
DELETE FROM Customers c
WHERE c.cust_id  = 1000000006;

-- does not work -- look into it.
TRUNCATE TABLE Customers;