-- Find all employees
SELECT * FROM employee;

-- find all clients
SELECT * FROM client;

-- Find all. employees ordered by salary
SELECT * FROM employee
ORDER BY salary DESC;

-- Find all employees ordered by sex then name
SELECT * FROM employee
ORDER BY sex, first_name, last_name;

-- Find the first 5 employees in the table
SELECT * FROM employee
LIMIT 5;

-- Find the first and last names of all employees
SELECT employee.first_name, employee.last_name FROM employee;

-- Find the forename and surname names fo all employees
-- creates an alias
SELECT employee.first_name AS forename, employee.last_name AS surename FROM employee;

-- Find out all the different genders
-- shows distinct values in a column
SELECT DISTINCT sex FROM employee;

