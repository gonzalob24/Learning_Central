-- create table
-- cant define the other primary keys as foreign keys becuase they dont exists yet.
CREATE TABLE employee (
  emp_id INT,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  birth_date DATE,
  sex VARCHAR(1),
  salary INT,
  super_id INT,
  branch_id INT,

  PRIMARY KEY(emp_id)
);

CREATE TABLE branch (
  branch_id INT,
  branch_name VARCHAR(40),
  mgr_id INT,
  mgr_start_date DATE,

  PRIMARY KEY(branch_id),

  FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;

CREATE TABLE client (
  client_id INT,
  client_name VARCHAR(40),
  branch_id INT,

  PRIMARY KEY(client_id),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);

CREATE TABLE works_with(
  emp_id INT,
  client_id INT,
  total_sales INT,
  
  PRIMARY KEY(emp_id, client_id),
  FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE,
  FOREIGN KEY(emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE
);

CREATE TABLE branch_supplier(
  branch_id INT,
  supplier_name VARCHAR(40),
  supplier_type VARCHAR(40),

  PRIMARY KEY(branch_id, supplier_name),
  FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);