-- % = any # of character, _ = one characer

-- Find any clients who are LLC
-- LIKE used with wild cards LIKE 'match_patter_here'
-- % any characters before pattern
SELECT * FROM client
WHERE client_name LIKE '%LLC';

-- Find any brancg suppliers who are in the label business
SELECT * FROM branch_supplier
WHERE supplier_name LIKE '% Label%';

-- Find any employee born in october
SELECT * FROM employee
WHERE birth_date LIKE '____-10%';

-- Find any clients who are schools
SELECT * FROM client
WHERE client_name LIKE '%school%';

