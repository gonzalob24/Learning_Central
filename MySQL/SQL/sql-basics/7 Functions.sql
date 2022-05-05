-- Find the number of employees
SELECT COUNT(emp_id) AS employee_count FROM employee;

-- How many employees have a supervisor
SELECT COUNT(super_id) FROM employee;

-- Find the number of females born after 1970
SELECT COUNT(emp_id) FROM employee
WHERE sex = 'F' AND birth_date > '1970-01-01';

-- find the average of all employee;s salaries
SELECT AVG(salary) FROM employee
WHERE sex = 'M';

-- Find the sum of all employee salary
SELECT SUM(salary) FROM employee;

-- Find out how many F and M there are
-- GROUP info by sex AGGREGATION
SELECT COUNT(sex), sex FROM employee
GROUP BY sex;

-- Find the total sales of each salesman
SELECT SUM(total_sales), emp_id FROM works_with
GROUP BY emp_id;

-- Find how much money each client spent 
SELECT SUM(total_sales), client_id FROM works_with
GROUP BY client_id;