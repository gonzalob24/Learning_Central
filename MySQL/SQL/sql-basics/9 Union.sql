-- combine results from SELECT statements into one result

-- Find a list of employee and branch names
-- Union, haev same number of columns in each select statement
-- have similar data types
-- 
SELECT employee.first_name AS Company_Names FROM employee
UNION
SELECT branch.branch_name FROM branch
UNION
SELECT client_name FROM client;

-- Find a list of al clients and branch suppliers name
SELECT client_name, client.branch_id FROM client
UNION
SELECT supplier_name, branch_supplier.branch_id FROM branch_supplier;

-- Find a list of all money spent or earned by the company
SELECT salary FROM employee
UNION
SELECT total_sales FROM works_with;

