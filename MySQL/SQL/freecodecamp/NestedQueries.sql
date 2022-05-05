-- using multiple select statements

-- Find names of all employees who have sold over 30k to a single client
-- shwo first name and last name from employee table where result of the second query is in the first table
SELECT first_name, last_name FROM employee
WHERE emp_id IN (
  SELECT emp_id FROM works_with
  WHERE total_sales > 30000
);


-- Find names of all employees who have sold over 50,000
 

-- Find all clients who are handled by the branch that Michael Scott manages
-- Assume you know Michael's ID
SELECT client.client_name FROM client
WHERE client.branch_id = (
  SELECT branch.branch_id FROM branch
  WHERE branch.mgr_id = 102
  LIMIT 1
);

 -- Find all clients who are handles by the branch that Michael Scott manages
 -- Assume you DONT'T know Michael's ID
 


-- Find the names of employees who work with clients handled by the scranton branch


-- Find the names of all clients who have spent more than 100,000 dollars
