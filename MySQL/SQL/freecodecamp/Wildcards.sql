-- % = any # characters
-- _ = one character

-- Find any clients who are an LLC
SELECT * FROM client
WHERE client_name LIKE '%LLC'; -- ends with

-- Find any branch suppliers whe are in the label business
SELECT * FROM branch_supplier
WHERE supplier_name LIKE '% Label%';

-- Find any employee born in October
SELECT * FROM employee
WHERE birth_date LIKE '%-10%';
SELECT * FROM employee
WHERE birth_date LIKE '____-10%';

-- Find any clients who are schools
SELECT * FROM client
WHERE client_name LIKE '%school%';

