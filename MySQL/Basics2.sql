-- capital letter are not required but its convention
-- I can add constraints when creating tables
CREATE TABLE student (
  student_id INT,
  name VARCHAR(20) NOT NULL,
  major VARCHAR(20) UNIQUE,
  PRIMARY KEY(student_id)
);

DESCRIBE student;

DROP TABLE student;

ALTER TABLE student ADD gpa DECIMAL(3, 2);

ALTER TABLE student DROP COLUMN gpa;

-- inserting values
INSERT INTO student VALUES(1, 'Gonzalo Betancourt', 'Computer Science');

INSERT INTO student VALUES(2, 'Maria Carrillo', 'Biology');

INSERT INTO student VALUES(2, NULL, 'Biology');

INSERT INTO student VALUES(2, "Alison Betancourt", 'Biology');



SELECT * FROM student;