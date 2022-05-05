CREATE TABLE student (
    student_id INT,
    name VARCHAR(20),
    major VARCHAR(20),
    PRIMARY KEY(student_id)
);

-- get information about the table
DESCRIBE student;

DROP TABLE student;

-- add column
ALTER TABLE student ADD gpa DECIMAL(3, 2);

-- drop a colum
ALTER TABLE student DROP COLUMN gpa;

-- Reading data from table
SELECT * FROM student;

-- Adding data to my table
INSERT INTO student VALUES(1, 'Gonzalo', 'Computer Science');

INSERT INTO student VALUES(2, 'Mery', 'Biology');

-- adding data, specify what valyes I want to isnert even if things are missing 
INSERT INTO student(student_id, name) VALUES(3, 'Alexa');
INSERT INTO student(student_id, name, major) VALUES(4, 'Alison', 'Piano');