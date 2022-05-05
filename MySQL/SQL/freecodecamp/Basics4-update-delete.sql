-- capital letter are not required but its convention
-- I can add constraints when creating tables
CREATE TABLE student (
  student_id INT AUTO_INCREMENT,
  name VARCHAR(20),
  major VARCHAR(20) DEFAULT 'Undecided',
  PRIMARY KEY(student_id)
);

DESCRIBE student;

DROP TABLE student;

ALTER TABLE student ADD gpa DECIMAL(3, 2);

ALTER TABLE student DROP COLUMN gpa;

-- inserting values
INSERT INTO student(name, major) VALUES('Alison Carrillo', 'Computer Science');

INSERT INTO student(name) VALUES('Maria Carrillo');

INSERT INTO student(name, major) VALUES('Alexa Torres', 'Biology');

INSERT INTO student(name, major) VALUES('Alison Betancourt', 'Biology');


-- update information
SELECT * FROM student;
UPDATE student
SET major = 'Bio'
WHERE major = 'Biology';

UPDATE student
SET major = 'Computer Science'
WHERE student_id = 4;

UPDATE student
SET major = 'Biochemistry'
WHERE major = "Bio" OR major = 'Chemistry';

UPDATE student
SET name = 'Tom', major = 'Art'
WHERE student_id = 2;

-- Delete rows from table
DELETE FROM student
WHERE student_id = 4;