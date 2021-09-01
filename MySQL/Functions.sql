-- Counting items: Find the number of employees
SELECT COUNT(emp_id) FROM employee;

SELECT COUNT(super_id) FROM employee;

-- Find the average of all employee's salaries
SELECT AVG(salary) FROM employee;


-- Find the number of female employees born after 1978
SELECT COUNT(emp_id) FROM employee
WHERE sex = 'F' AND birth_date >= '1970-01-01';

-- Find the averge salary of males
SELECT AVG(salary) FROM employee
WHERE sex = 'M';

-- Find the sum of all employees salaries
SELECT SUM(salary) FROM employee;

-- Aggregation: use to display DATABASE
-- Find out how many males and females there AFTER
SELECT COUNT(sex) FROM employee;

-- how many females and males and display sex
SELECT COUNT(sex), sex FROM employee
GROUP BY sex;

-- Find the total sales of each salesman
SELECT SUM(total_sales), emp_id FROM works_with
GROUP BY emp_id;

-- Find how much each client spent
SELECT SUM(total_sales), client_id FROM works_with
GROUP BY client_id;

-- 