-- Relationships:
	-- One to One: 
		-- One customer can have many orders
	-- One to Many:
		-- Most common
		-- One customer can have many orders
	-- Many to Many:
		-- Books can have many authors and authors can have many books

-- ONE TO MANY
	-- Two tables Customers and Orders
	-- Customers can have many orders
	-- orders can have one customer
	
-- Customers: 
	-- first name
	-- last name
	-- email
-- Orders 
	-- Date
	-- price

CREATE DATABASE one_to_many_db;

CREATE TABLE customers (
	cust_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(100),
	last_name VARCHAR(100),
	email VARCHAR(50)
);

-- ON DELETE CASCADE means when deleting a customer also delete the order

CREATE TABLE orders (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
	order_date DATE,
	price DECIMAL(8,2),
	cust_id INT,
	FOREIGN KEY(cust_id) REFERENCES customers(cust_id) ON DELETE CASCADE
);

INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');
       
INSERT INTO orders (order_date, price, cust_id)
VALUES ('2016/02/10', 99.99, 1),
       ('2017/11/11', 35.50, 1),
       ('2014/12/12', 800.67, 2),
       ('2015/01/03', 12.50, 2),
       ('1999/04/11', 450.25, 5);

-- this will give me a Foreign Key constraint
INSERT INTO orders (order_date, price, cust_id)
VALUES ('2013/01/11', 33.76, 98);
      
 --
SELECT * FROM customers c
WHERE  last_name = 'George'; 

SELECT * FROM orders o 
WHERE cust_id = 1; 

SELECT * FROM orders o 
WHERE cust_id = (SELECT cust_id FROM customers c 
				 WHERE cust_id = 1);
				

-- Using JOINS to conjoin data

-- this gives me a cross join, this is not what we want
SELECT * FROM customers c, orders o
WHERE c.cust_id = 1;

-- This is known as an IMPLICIT INNER JOIN
SELECT * FROM customers c, orders o
WHERE c.cust_id = o.cust_id;


-- Explicit INNER JOIN
SELECT * FROM customers c 
JOIN orders o ON o.cust_id = c.cust_id;

SELECT * FROM customers c 
JOIN orders o ON o.cust_id = c.cust_id
ORDER BY price;

SELECT first_name, last_name, SUM(price) FROM customers c 
JOIN orders o ON o.cust_id = c.cust_id
GROUP BY first_name, last_name;

SELECT c.cust_id, c.first_name, c.last_name, SUM(price) AS 'total_spent' FROM customers c 
JOIN orders o ON o.cust_id = c.cust_id
GROUP BY o.cust_id
ORDER BY total_spent DESC;

-- does the order matter no, it only affects how the data looks/presented


-- LEFT JOIN: 
-- Take everything from left table and things that MATCH 
-- this may return NULL VALUES 
-- Why would I need null values: it depends on the use case
SELECT * FROM customers c 
LEFT JOIN orders o ON o.cust_id = c.cust_id;

SELECT first_name, last_name, o.order_date, o.price FROM customers c 
LEFT JOIN orders o ON o.cust_id = c.cust_id;

SELECT c.cust_id, c.first_name, c.last_name,
SUM(price) AS 'total_spent' FROM customers c 
LEFT JOIN orders o ON o.cust_id = c.cust_id
GROUP BY c.cust_id;

SELECT c.cust_id, c.first_name, c.last_name,
IFNULL(SUM(price), 0.00) AS 'total_spent' FROM customers c 
LEFT JOIN orders o ON o.cust_id = c.cust_id
GROUP BY c.cust_id
ORDER BY total_spent;


-- RIGHT JOIN
SELECT c.cust_id, first_name, last_name, o.order_date, o.price FROM customers c 
RIGHT JOIN orders o ON o.cust_id = c.cust_id
ORDER BY price;


-- ON  DELETE CASCADE
SELECT * FROM customers c;
SELECT * FROM orders o;

DELETE FROM customers 
WHERE email = 'george@gmail.com';

-- COMPARE LEFT vs RIGHT JOIN
SELECT * FROM customers c 
LEFT JOIN orders o ON c.cust_id = o.cust_id;

SELECT * FROM orders o
RIGHT JOIN customers c ON c.cust_id = o.cust_id;

-- CHALLENGES

CREATE TABLE students (
	id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(100)
);

CREATE TABLE papers (
	title VARCHAR(100),
	grade INT,
	student_id INT,
	FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
);

INSERT INTO students (first_name) VALUES 
('Caleb'), 
('Samantha'), 
('Raj'), 
('Carlos'), 
('Lisa');
 
INSERT INTO papers (student_id, title, grade ) VALUES
(1, 'My First Book Report', 60),
(1, 'My Second Book Report', 75),
(2, 'Russian Lit Through The Ages', 94),
(2, 'De Montaigne and The Art of The Essay', 98),
(4, 'Borges and Magical Realism', 89);


SELECT first_name, title, grade FROM students s
JOIN papers p ON p.student_id = s.id
ORDER BY grade DESC;

SELECT first_name, title, grade FROM students s 
LEFT JOIN papers p ON p.student_id = s.id;


SELECT first_name, IFNULL(title, 'MISSING') AS title, IFNULL(grade, '0') AS grade FROM students s
LEFT JOIN papers p ON p.student_id = s.id;

SELECT first_name, IFNULL(AVG(grade), 0) AS average,
	CASE 
		WHEN IFNULL(AVG(grade), 0) < 75 THEN 'FAILING'
		ELSE 'PASSING'
	END AS passing_status
FROM students s 
LEFT JOIN papers p ON p.student_id = s.id 
GROUP BY s.id
ORDER BY average DESC;




