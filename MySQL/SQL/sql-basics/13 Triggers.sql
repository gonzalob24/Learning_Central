UPDATE branch
SET mgr_id = 102
WHERE branch_id = 2;

UPDATE employee
SET super_id = 102
WHERE emp_id IN (103, 104, 105);

-- Trigger: a block of SQL code that triggers an action 
-- when something happens, CRUD operation
-- I dont need to create a trigget table but i did for visual purposes
CREATE TABLE trigger_test (
    message VARCHAR(100)
);
-- define trigegr
-- before any new items are inserted
-- for each item that get added insert something to trigger_test table
-- cahnging the delimiter to $$ instead of ;
DELIMITER $$
CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES('added new employee');
    END$$
DELIMITER ;

INSERT INTO employee VALUES(109, 'Oscar', 'Martinez', '1968-02-19', 'M', 69000, 106, 2);

-- access an attribute for that row
--- NEW has access to that row
DELIMITER $$
CREATE
    TRIGGER my_trigger_new BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO trigger_test VALUES(NEW.first_name);
    END$$
DELIMITER ;

INSERT INTO employee VALUES(111, 'Kevin', 'Malone', '1978-02-19', 'M', 89000, 106, 2);

DELIMITER $$
CREATE
    TRIGGER my_trigger_ifelse BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        IF NEW.sex = 'M' THEN
            INSERT INTO trigger_test VALUES('added male employee');
        ELSEIF New.sex = 'F' THEN
            INSERT INTO trigger_test VALUES('added female employee');
        ELSE
            INSERT INTO trigger_test VALUES('added other employee');
        END IF;
    END$$
DELIMITER ;

INSERT INTO employee VALUES(112, 'pam', 'Beesly', '1978-02-19', 'F', 89000, 106, 2);

-- can use with CRUD operations
DELIMITER $$
CREATE
    TRIGGER my_trigger_ifelse AFTER DELETE
    ON employee
    FOR EACH ROW BEGIN
        IF NEW.sex = 'M' THEN
            INSERT INTO trigger_test VALUES('added male employee');
        ELSEIF New.sex = 'F' THEN
            INSERT INTO trigger_test VALUES('added female employee');
        ELSE
            INSERT INTO trigger_test VALUES('added other employee');
        END IF;
    END$$
DELIMITER ;


-- Drop triggers in terminal
DROP TRIGGER name_of_trigger;