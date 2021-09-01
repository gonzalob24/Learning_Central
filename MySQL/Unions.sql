-- Combine results of multiple select statements

-- Find a list of employee and branch names
SELECT first_name FROM employee;

-- Find all branch names
SELECT branch_name from branch;

-- How do I combine these two statements
-- number of columns must have the same number
-- data types have to be the same
SELECT first_name FROM employee
UNION 
SELECT branch_name FROM branch
UNION
SELECT client_name from client;

-- Find a list of all clients and branch suppliers names
-- both tables have the same client name 
SELECT client_name, branch_id FROM client
UNION
SELECT supplier_name, branch_id FROM branch_supplier;

-- Find a list of all money spent or earned by the company
SELECT salary FROM employee
UNION
SELECT total_sales FROM works_with;