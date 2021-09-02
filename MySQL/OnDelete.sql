-- ON DELETE: something that we can do when rows are deleted.AUTO_INCREMENT. mgr_id is not essential for branch table
-- CASCADE : deletes rows in multiple tables

CREATE TABLE branch (
  branch_id INT,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,

  PRIMARY KEY(branch_id),

  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

DELETE FROM employee 
WHERE emp_id = 102;

SELECT * FROM branch;

SELECT * FROM employee;

-- CASCADE
-- branch id in this table is crucial b/c its a primary KEY, PR cant be NULL
CREATE TABLE branch_supplier(
  branch_id INT,
  supplier_name VARCHAR(40),
  supplier_type VARCHAR(40),

  PRIMARY KEY(branch_id, supplier_name),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);

DELETE FROM branch
WHERE branch_id = 2;

SELECT * FROM branch_supplier;