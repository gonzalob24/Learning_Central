-- using mutliple SELECT statments to get specific data

-- Find names of all employess who have sold over 30,000
-- to a single client
-- now we have all of the ids who sold > 30k
SELECT works_with.emp_id FROM works_with
WHERE works_with.total_sales > 30000;

SELECT employee.first_name, employee.last_name FROM employee
WHERE employee.emp_id IN (
    SELECT works_with.emp_id FROM works_with
    WHERE works_with.total_sales > 30000
);

-- Find all clients who are handled by the branch 
-- that Michael Scott manages
-- assum you know Michaels manager id, emp.id
SELECT client.client_name FROM client
WHERE client.branch_id = (
    SELECT branch.branch_id FROM branch
    WHERE branch.mgr_id = 102
    LIMIT 1 -- make sure I only have one
);

