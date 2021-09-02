INSERT INTO branch values(4, 'Buffalo', NULL, NULL);

-- JOIN brnach and employee tables on emp_id and mgr_id being equal
-- Find all branches and the names of their managers
SELECT emp_id, first_name, branch_name FROM employee
JOIN branch
ON emp_id = mgr_id;

-- left join all of the employees get included, means include all of the rows from the left table
SELECT emp_id, first_name, branch_name FROM employee
LEFT JOIN branch
ON emp_id = mgr_id;

-- include all of the rows from the right table
SELECT emp_id, first_name, branch_name FROM employee
RIGHT JOIN branch
ON emp_id = mgr_id;