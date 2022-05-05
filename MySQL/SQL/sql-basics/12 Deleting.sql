-- If i delete Michael what will happen to the manager id
-- in the branch table the manager id will be set to NULL
-- ON DELETE SET NULL --> value is set to null
--      when to use: mgt_id is not essential for branch table
-- ON DELETE CASCADE --> the row get deleted
--      when to use: branch suppplier branch id can't be null 
--      as it is used as a composite key

DELETE FROM employee
WHERE employee.emp_id = 102;

INSERT INTO employee VALUES(102, 'Michael', 'Scott', '1964-03-15', 'M', 75000, 100, 2);