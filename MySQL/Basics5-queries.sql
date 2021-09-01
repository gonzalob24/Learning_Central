-- select every column or I can specify a column from a table
SELECT * FROM student;

-- select just the names
SELECT name FROM student;

-- select namd and major
SELECT name, major FROM student;

-- I can append table.COLUMN
SELECT student.name, student.major FROM student;

-- I can order them by name ascending or descending
SELECT student.name, student.major
FROM student
ORDER BY name DESC;

-- order by different sub columns
SELECT student.name, student.major
FROM student
ORDER BY major, student_id;

-- select a certain number of queries
SELECT * FROM student
LIMIT 2;

-- in order
SELECT * FROM student
ORDER BY student_id DESC
LIMIT 2;

-- filter
SELECT * FROM student
WHERE major = 'Computer Science';

-- certain columns where major = something
SELECT name, major FROM student
WHERE major = 'Computer Science' OR name = 'Alison';

-- <, > , <=, >=, =, <>, AND, OR
SELECT * FROM student
WHERE student_id <= 2 and name <> 'Gonzalo Betancourt';

-- IN keyword
SELECT * FROM student
WHERE name IN ('Tom', 'Gonzalo') AND student_id >= 2;