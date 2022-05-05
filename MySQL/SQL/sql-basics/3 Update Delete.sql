SELECT * FROM student;

UPDATE student
SET major = 'Soccer'
WHERE major = "undecided";

UPDATE student
SET major = 'Bio'
WHERE major = 'Biology';

UPDATE student
SET major = 'CSI'
WHERE student_id = 1;

-- I can set based on multiple conditions
UPDATE student
SET major = 'Biochemistry'
WHERE major = 'Bio' OR major = 'Piano';

UPDATE student
SET name = 'Itzel', major = 'Piano'
WHERE student_id = 4;

-- this will apply to all rows
UPDATE student
SET major = 'undecided';

--  DELETE all Rows
DELETE FROM student;

DELETE FROM student
WHERE student_id = 1;

DELETE FROM student
WHERE name = 'Mery' OR major = 'Piano';