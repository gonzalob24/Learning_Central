-- constraints controll how we insert data
-- NOT NULL, always have a name
-- UNIQUE
-- setting default values: DEFAULT 'value'
-- AUTO_INCREMENT: dont have to add id 
CREATE TABLE student (
    student_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) DEFAUlT 'undecided',
    PRIMARY KEY(student_id) 
);

INSERT INTO student VALUES(1, 'Gonzalo', 'Computer Science');
INSERT INTO student VALUES(2, 'Mery', 'Biology');
INSERT INTO student(student_id, name) VALUES(3, 'Alexa');
INSERT INTO student(student_id, name, major) VALUES(4, 'Alison', 'Piano');
INSERT INTO student(student_id, name) VALUES(1, 'Gonzalo');
-- INSERT INTO student(student_id, name, major) VALUES(5, 'Jack', 'Piano');

INSERT INTO student(name, major) VALUES('Gonzalo', 'CS');

DROP TABLE student;