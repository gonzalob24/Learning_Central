-- capital letter are not required but its convention
CREATE TABLE student (
  student_id INT PRIMARY KEY,
  name VARCHAR(20),
  major VARCHAR(20)
);

DESCRIBE student;

DROP TABLE student;

ALTER TABLE student ADD gpa DECIMAL(3, 2);

ALTER TABLE student DROP COLUMN gpa;

-- inserting values
INSERT INTO student VALUES(1, 'Gonzalo Betancourt', 'Computer Science');

INSERT INTO student VALUES(2, 'Maria Carrillo', 'Biology');

INSERT INTO student(student_id, name) VALUES(3, 'Alexa Torres');

SELECT * FROM student;