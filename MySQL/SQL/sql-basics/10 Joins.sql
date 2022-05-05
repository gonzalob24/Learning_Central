-- combine rows from two or more tables based on a related column between them

INSERT INTO branch VALUES(4, 'Buffalo', NULL, NULL);

-- Find all branches and their names of the managers
-- JOIN employee table and branch into one table on a specific column
-- referred to as an inner join only managers are included
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
JOIN branch
ON employee.emp_id = branch.mgr_id;

-- LEFT JOIN
-- inlcudes the other results, in this case the employee table
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
LEFT JOIN branch 
ON employee.emp_id = branch.mgr_id;

-- RIGHT JOIN
-- we get all of the rows from the branch table for this example
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
RIGHT JOIN branch 
ON employee.emp_id = branch.mgr_id;