-- SELECT --> tells RDBMS tp select from some table
-- * --> every column wild card 
SELECT * FROM student;

-- just the name
SELECT name FROM student;

-- name and major
SELECT name, major FROM student;

-- other syntax
SELECT student.name, student.major FROM student;

-- order items by column, DESC or ASC
SELECT student.name, student.student_id FROM student
ORDER BY name DESC;

SELECT student.name, student.student_id, student.major FROM student
ORDER BY major, student_id ASC;
-- UPDATE student
-- SET major = 'Biology'
-- WHERE student_id = 4;

SELECT * FROM student
ORDER BY student_id DESC
LIMIT 2;

-- Filtering look more at filtering methods
SELECT * FROM student
WHERE major = 'Biology' OR major = 'Soccer';

SELECT * FROM student
WHERE major <> 'Biology' AND major <> 'Soccer';

--  <, >, <=, >=, =, <> NOT, AND, OR
--  I can cobine these into more complex queries
SELECT * FROM student
WHERE name IN ('Gonzalo', 'Mery');
